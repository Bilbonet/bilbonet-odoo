# Copyright 2024 bilbonet.net - Jesus Ramiro
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.onchange("product_id")
    def product_id_change(self):
        """
        Inherit this method to bring
        more discount fields to the saleorder lines
        """
        res = super(SaleOrderLine, self).product_id_change()
        if res != None and self.product_id and self.order_id.partner_id:
            self._get_product_discounts()
        return res

    @api.onchange("product_uom", "product_uom_qty")
    def product_uom_change(self):
        """
        Inherit this method to bring
        more discount fields to the saleorder lines
        """
        if self.product_uom_qty and self.product_id:
            self._get_product_discounts()
        return super(SaleOrderLine, self).product_uom_change()

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
