# Copyright 2024 - Bilbonet <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models
from odoo.osv.expression import AND


class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    delivery_zone_id = fields.Many2one(
        comodel_name="partner.delivery.zone",
        string="Delivery Zone",
        index=True,
        store=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
    )

    @api.depends("company_id", "picking_type_id", "state", "delivery_zone_id")
    def _compute_allowed_picking_ids(self):
        allowed_picking_states = ["waiting", "confirmed", "assigned"]

        for batch in self:
            if not batch.delivery_zone_id:
                return super()._compute_allowed_picking_ids()
            else:
                domain_states = list(allowed_picking_states)
                if batch.state == "draft":
                    domain_states.append("draft")
                domain = [
                    ("company_id", "=", batch.company_id.id),
                    ("state", "in", domain_states),
                ]
                if not batch.is_wave:
                    domain = AND([domain, [("immediate_transfer", "=", False)]])
                if batch.picking_type_id:
                    domain += [("picking_type_id", "=", batch.picking_type_id.id)]

                domain += [("delivery_zone_id", "=", batch.delivery_zone_id.id)]
                batch.allowed_picking_ids = self.env["stock.picking"].search(domain)
