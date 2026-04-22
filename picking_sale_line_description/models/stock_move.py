# Copyright 2026 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    sale_line_description = fields.Text(
        string="Sale Line Description",
        related="sale_line_id.name",
        readonly=True,
    )
