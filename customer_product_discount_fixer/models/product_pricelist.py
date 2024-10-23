# Copyright 2024 bilbonet.net - Jesus Ramiro
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class Pricelist(models.Model):
    _inherit = "product.pricelist"

    discount_policy = fields.Selection(
        selection_add=[
            ("none", "Do not apply any calculations with discounts"),
        ],
        ondelete={"none": "set default"},
    )
