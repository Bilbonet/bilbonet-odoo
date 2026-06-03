# Copyright 2026 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import Form, tagged

from odoo.addons.sale_commission_oca.tests.test_sale_commission import (
    TestSaleCommission,
)


@tagged("post_install", "-at_install")
class TestProductCategorySaleCommission(TestSaleCommission):
    def _create_product_category_sale_order(self, product=None):
        sale_order_form = Form(self.sale_order_model)
        sale_order_form.partner_id = self.partner
        with sale_order_form.order_line.new() as line_form:
            line_form.product_id = product or self.product
            line_form.product_uom_qty = 1
        return sale_order_form.save()

    def _create_product_category_agent(
        self, category=None, agent=None, commission=None
    ):
        return self.env["product.category.agent"].create(
            {
                "category_id": (category or self.product.categ_id).id,
                "agent_id": (agent or self.agent_monthly).id,
                "commission_id": (commission or self.agent_monthly.commission_id).id,
            }
        )

    def test_product_category_agent_is_added_to_sale_order_line(self):
        self._create_product_category_agent()

        sale_order = self._create_product_category_sale_order()

        self.assertEqual(sale_order.order_line.agent_ids.agent_id, self.agent_monthly)

    def test_product_category_agent_is_not_duplicated(self):
        self._create_product_category_agent()
        self.partner.agent_ids = [(6, 0, self.agent_monthly.ids)]

        sale_order = self._create_product_category_sale_order()

        self.assertEqual(len(sale_order.order_line.agent_ids), 1)
        self.assertEqual(sale_order.order_line.agent_ids.agent_id, self.agent_monthly)

    def test_product_category_agent_depends_on_sale_line_product(self):
        category = self.env["product.category"].create(
            {"name": "Product Manager Category"}
        )
        product = self.product.copy({"name": "Product Manager Product"})
        product.categ_id = category
        self._create_product_category_agent(category=category)

        sale_order = self._create_product_category_sale_order(product=product)

        self.assertEqual(sale_order.order_line.agent_ids.agent_id, self.agent_monthly)
