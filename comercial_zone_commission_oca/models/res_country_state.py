# Copyright 2026 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResCountryState(models.Model):
    _inherit = "res.country.state"

    commercial_zone_id = fields.Many2one(
        comodel_name="commercial.zone",
        string="Commercial Zone",
        ondelete="restrict",
        index=True,
    )
