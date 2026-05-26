# Copyright 2026 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import Form, tagged

from odoo.addons.sale_commission_oca.tests.test_sale_commission import (
    TestSaleCommission,
)


@tagged("post_install", "-at_install")
class TestCommercialZoneSaleCommission(TestSaleCommission):
    def _create_sale_order(self):
        sale_order_form = Form(self.sale_order_model)
        sale_order_form.partner_id = self.partner
        with sale_order_form.order_line.new() as line_form:
            line_form.product_id = self.product
            line_form.product_uom_qty = 1
        return sale_order_form.save()

    def _create_commercial_zone(self):
        return self.env["commercial.zone"].create(
            {
                "name": "Test Commercial Zone",
                "agent_ids": [
                    (
                        0,
                        0,
                        {
                            "agent_id": self.agent_monthly.id,
                            "commission_id": self.agent_monthly.commission_id.id,
                        },
                    )
                ],
            }
        )

    def test_zone_agent_is_added_to_sale_order_line(self):
        zone = self._create_commercial_zone()
        self.partner.commercial_zone_id = zone

        sale_order = self._create_sale_order()

        self.assertEqual(sale_order.order_line.agent_ids.agent_id, self.agent_monthly)

    def test_commercial_zone_agent_is_not_duplicated(self):
        zone = self._create_commercial_zone()
        self.partner.commercial_zone_id = zone
        self.partner.agent_ids = [(6, 0, self.agent_monthly.ids)]

        sale_order = self._create_sale_order()

        self.assertEqual(len(sale_order.order_line.agent_ids), 1)
        self.assertEqual(sale_order.order_line.agent_ids.agent_id, self.agent_monthly)
