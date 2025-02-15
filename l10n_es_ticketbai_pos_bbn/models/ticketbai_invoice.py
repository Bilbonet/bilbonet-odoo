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
        Cancel and recreates invoices that are in an error state and have a POS order ID.

        Process of cancel is set by the inherited function, due to this we
        can't t cancel here or call the function before recreate the pos invoice.
        """
        for record in self.sudo().filtered(
            lambda x: x.state == TicketBaiInvoiceState.error.value and x.pos_order_id
        ):
            if TicketBaiSchema.TicketBai.value == record.schema and record.pos_order_id:
                record.pos_order_id._tbai_build_invoice()

        return super().cancel_and_recreate()
