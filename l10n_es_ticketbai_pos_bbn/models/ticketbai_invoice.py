# Copyright 2025 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import logging

from odoo import api, fields, models

from odoo.addons.l10n_es_ticketbai_api.models.ticketbai_invoice import (
    TicketBaiInvoiceState,
)
from odoo.addons.l10n_es_ticketbai_api.ticketbai.xml_schema import TicketBaiSchema

_logger = logging.getLogger(__name__)
TBAI_REJECTED_MAX_RETRIES = 5


class TicketBAIInvoice(models.Model):
    _inherit = "tbai.invoice"

    is_duplicated = fields.Boolean(
        string="Duplicated",
        compute="_compute_is_duplicated",
        help="This field is used to mark the POS invoice name as duplicated",
    )

    @api.depends("name", "state")
    def _compute_is_duplicated(self):
        for record in self:
            record.is_duplicated = False
            if record.pos_order_id and record.state == "error":
                # Get the last response and check if the response code is "005"
                last_response = record.tbai_response_ids.sorted('id', reverse=True)[:1]
                record.is_duplicated = any(
                    msg.code == "005" for msg in last_response.tbai_response_message_ids
                )

    def renumber_pos_invoice(self):
        """
        Renumber the POS invoice if it is duplicated.
        """
        self.ensure_one()
        if self.is_duplicated:
            pos_order = self.name + "R"
            self.pos_order_id.write({"l10n_es_unique_id": pos_order})
            self.name = pos_order
            self.cancel_and_recreate()

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
