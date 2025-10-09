# Copyright 2024 bilbonet.net - Jesus Ramiro
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.depends("product_id", "product_uom", "product_uom_qty", "order_id.partner_id")
    def _compute_discount(self):
        """
        Override Odoo's discount computation to include custom discount logic
        """
        # First, call the parent computation for standard discount logic
        result = super()._compute_discount()

        # Then apply our custom discount logic
        for line in self:
            if line.product_id and line.product_uom_qty and line.order_id.partner_id:
                line._get_product_discounts()

        return result

    def _get_product_discounts(self):
        partner_id = self.order_id.partner_id
        discounts = partner_id.get_product_discounts(
            self.product_id, self.product_uom_qty, self.date_order
        )
        if discounts:
            self.update(
                {
                    "discount": discounts.discount,
                    "discount2": discounts.discount2,
                    "discount3": discounts.discount3,
                    "discounting_type": discounts.discounting_type,
                }
            )
