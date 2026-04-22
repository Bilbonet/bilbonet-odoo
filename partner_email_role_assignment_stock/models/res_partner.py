# Copyright 2026 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    used_address_picking = fields.Boolean(
        string="Used like mail for picking",
    )
    mail_addresses_picking = fields.One2many(
        comodel_name="res.partner",
        inverse_name="parent_id",
        string="Mails for pickings",
        domain=[("used_address_picking", "=", True)],
    )

    def write(self, vals):
        partners = super().write(vals)
        if "used_address_picking" in vals and "name" not in vals:
            for partner in self:
                partner.write({"name": partner.name})
                partner._get_name()
        return partners

    def _get_name(self):
        """Display picking email contacts by their email address instead of name."""
        name = super()._get_name()
        if self.email and self.used_address_picking:
            name = self.email
        return name
