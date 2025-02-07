# Copyright 2025 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import logging

from odoo import api, models

from odoo.addons.l10n_es_ticketbai_api.models.ticketbai_invoice import (
    RefundCode,
    RefundType,
    SiNoType,
    TicketBaiInvoiceState,
)
from odoo.addons.l10n_es_ticketbai_api.ticketbai.xml_schema import TicketBaiSchema
from odoo.addons.l10n_es_ticketbai_api.models.ticketbai_response import (
    TicketBaiCancellationResponseCode as CancellationResponseCode,
    TicketBaiInvoiceResponseCode as InvoiceResponseCode,
    TicketBaiResponseState as ResponseState,
)

_logger = logging.getLogger(__name__)
TBAI_REJECTED_MAX_RETRIES = 5


class TicketBAIInvoice(models.Model):
    _inherit = "tbai.invoice"

    def cancel_and_recreate(self):
        """
        Cancels and recreates invoices that are in an error state and have a POS order ID.

        Process of cancel is set by the inherited function, due to this we
        can't t cancel here or call the function before recreate the pos invoice.
        """
        for record in self.sudo().filtered(
            lambda x: x.state == TicketBaiInvoiceState.error.value and x.pos_order_id
        ):
            if TicketBaiSchema.TicketBai.value == record.schema and record.pos_order_id:
                record.pos_order_id._tbai_build_invoice()

        return super().cancel_and_recreate()

    @api.model
    def send_pending_invoices(self):
        """
        We replaced the function to modify the behavior with TicketBAI responses:
            Mark pending invoices as error, except in the following:
            - TicketBai (Invoice)
                - 005: Invoice already registered -> mark as sent.
            - AnulaTicketBai (Cancellation)
                - 011: Invoice already registered -> mark as sent.

        In these cases the state is better error, because that situation
        requires a check from the responsible person to evaluate which would
        be the best solution.
        Maybe there are problems repeating numbers in the aplication, and the
        invoice actually not registered in the taxes agency.
        """

        next_pending_invoice = self.get_next_pending_invoice()
        retry_later = False
        rejected_retries = 0
        while (
            next_pending_invoice
            and not retry_later
            and rejected_retries < TBAI_REJECTED_MAX_RETRIES
        ):
            try:
                with self.env.cr.savepoint():
                    tbai_response = next_pending_invoice.send()
                    if ResponseState.RECEIVED.value == tbai_response.state:
                        next_pending_invoice.mark_as_sent()
                    elif ResponseState.REJECTED.value == tbai_response.state:
                        # Reestablish the company pointer to the last invoice built and
                        # successfully sent.
                        # Mark pending invoices as error, except in the following:
                        # - TicketBai (Invoice)
                        #   - 006: service not available. Retry later.
                        # - AnulaTicketBai (Cancellation)
                        #   - 012: service not available. Retry later.
                        error = True
                        # TicketBAI Response warning and error codes
                        response_codes = list(
                            set(tbai_response.tbai_response_message_ids.mapped("code"))
                        )
                        if (
                            TicketBaiSchema.TicketBai.value
                            == next_pending_invoice.schema
                        ):
                            if (
                                InvoiceResponseCode.SERVICE_NOT_AVAILABLE.value
                                in response_codes
                            ):
                                retry_later = True
                                error = False
                        elif (
                            TicketBaiSchema.AnulaTicketBai.value
                            == next_pending_invoice.schema
                        ):
                            if (
                                CancellationResponseCode.SERVICE_NOT_AVAILABLE.value
                                in response_codes
                            ):
                                retry_later = True
                                error = False
                        if error:
                            self.mark_chain_as_error(next_pending_invoice)
                            rejected_retries += 1
                    elif ResponseState.REQUEST_ERROR.value == tbai_response.state:
                        # In case of multi-company it would be delaying
                        # independently from the company and tax agency,
                        # maybe only one of them is out of service.
                        # For now delay for all companies and all tax agencies.
                        retry_later = True
                    elif ResponseState.BUILD_ERROR.value == tbai_response.state:
                        retry_later = True
                    if not retry_later:
                        next_pending_invoice = self.get_next_pending_invoice()
            except Exception:
                _logger.exception(
                    "Communication failed with TicketBAI server.", exc_info=True
                )
                retry_later = True
