# Copyright 2026 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    commercial_zone_id = fields.Many2one(
        comodel_name="commercial.zone",
        string="Commercial Zone",
        ondelete="restrict",
        index=True,
    )

    def _commercial_fields(self):
        fields_to_sync = super()._commercial_fields()
        fields_to_sync.append("commercial_zone_id")
        return fields_to_sync
