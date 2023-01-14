# Copyright (C) 2022 Jesus Remiro <bilbonet@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class AccounInvoiceLineDescriptionExtend(models.TransientModel):
    _name = "account.invoice.line.description.extend"
    _description = "Account Invoice line description extend"

    @api.model
    def _default_product_id(self):
        line_id = self.env.context.get("active_id")
        return self.env["account.move.line"].browse(line_id).product_id.id

    @api.model
    def _default_ex_descript(self):
        line_id = self.env.context.get("active_id")
        return self.env["account.move.line"].browse(line_id).ex_descript

    account_move_line_id = fields.Many2one(
        comodel_name="account.move.line",
        string="Account invoice line",
        default=lambda self: self.env.context.get("active_id"),
    )
    product_id = fields.Many2one(
        comodel_name="product.product",
        string="Product",
        default=_default_product_id,
    )
    ex_descript = fields.Html(
        string='Extended Description',
        default=_default_ex_descript,
    )

    def action_save_description(self):
        self.ensure_one()
        self.account_move_line_id.ex_descript = self.ex_descript
    