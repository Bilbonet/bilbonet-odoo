# Copyright (C) 2023 Jesus Remiro <bilbonet@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    used_address_sale = fields.Boolean(
        string="Used like mail for sale",
    )
    used_address_invoice = fields.Boolean(
        string="Used like mail for invoice",
    )
    mail_addresses_sale = fields.One2many(
        comodel_name="res.partner",
        inverse_name="parent_id",
        string="Mails for sale",
        domain=[("used_address_sale", "=", True)],
    )
    mail_addresses_invoice = fields.One2many(
        comodel_name="res.partner",
        inverse_name="parent_id",
        string="Mails for invoice",
        domain=[("used_address_invoice", "=", True)],
    )

    def write(self, vals):
        partners = super().write(vals)
        if (
            "used_address_sale" in vals
            or "used_address_invoice" in vals
            and "name" not in vals
        ):
            for partner in self:
                partner.write(
                    {
                        "name": partner.name,
                    }
                )
                partner._get_name()
        return partners

    def _get_name(self):
        """Display role-based email contacts by their email address instead of name."""
        name = super()._get_name()
        if self.email and (self.used_address_sale or self.used_address_invoice):
            name = self.email
        return name
