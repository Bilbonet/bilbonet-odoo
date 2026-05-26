# Copyright 2026 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import Form, tagged

from odoo.addons.sale_commission_oca.tests.test_sale_commission import (
    TestSaleCommission,
)


@tagged("post_install", "-at_install")
class TestCommercialZoneSaleCommission(TestSaleCommission):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.country = cls.env["res.country"].create(
            {
                "name": "Commercial Zone Test Country",
                "code": "XZ",
            }
        )
        cls.state = cls.env["res.country.state"].create(
            {
                "name": "Commercial Zone Test State",
                "code": "CZS",
                "country_id": cls.country.id,
            }
        )

    def _create_commercial_zone_sale_order(self):
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

        sale_order = self._create_commercial_zone_sale_order()

        self.assertEqual(sale_order.order_line.agent_ids.agent_id, self.agent_monthly)

    def test_commercial_zone_agent_is_not_duplicated(self):
        zone = self._create_commercial_zone()
        self.partner.commercial_zone_id = zone
        self.partner.agent_ids = [(6, 0, self.agent_monthly.ids)]

        sale_order = self._create_commercial_zone_sale_order()

        self.assertEqual(len(sale_order.order_line.agent_ids), 1)
        self.assertEqual(sale_order.order_line.agent_ids.agent_id, self.agent_monthly)

    def test_partner_commercial_zone_is_set_from_state_on_create(self):
        zone = self._create_commercial_zone()
        self.state.commercial_zone_id = zone

        partner = self.res_partner_model.create(
            {
                "name": "Commercial Zone Partner",
                "country_id": self.country.id,
                "state_id": self.state.id,
            }
        )

        self.assertEqual(partner.commercial_zone_id, zone)

    def test_explicit_partner_commercial_zone_wins_on_create(self):
        state_zone = self._create_commercial_zone()
        explicit_zone = self.env["commercial.zone"].create(
            {"name": "Explicit Commercial Zone"}
        )
        self.state.commercial_zone_id = state_zone

        partner = self.res_partner_model.create(
            {
                "name": "Explicit Commercial Zone Partner",
                "country_id": self.country.id,
                "state_id": self.state.id,
                "commercial_zone_id": explicit_zone.id,
            }
        )

        self.assertEqual(partner.commercial_zone_id, explicit_zone)

    def test_partner_commercial_zone_is_set_from_state_on_write(self):
        zone = self._create_commercial_zone()
        self.state.commercial_zone_id = zone
        partner = self.res_partner_model.create(
            {
                "name": "Commercial Zone Partner",
                "country_id": self.country.id,
            }
        )

        partner.write({"state_id": self.state.id})

        self.assertEqual(partner.commercial_zone_id, zone)

    def test_partner_commercial_zone_is_set_from_state_on_form(self):
        zone = self._create_commercial_zone()
        self.state.commercial_zone_id = zone

        partner_form = Form(self.res_partner_model)
        partner_form.name = "Commercial Zone Form Partner"
        partner_form.country_id = self.country
        partner_form.state_id = self.state

        self.assertEqual(partner_form.commercial_zone_id, zone)

    def test_manual_partner_commercial_zone_can_be_changed(self):
        state_zone = self._create_commercial_zone()
        manual_zone = self.env["commercial.zone"].create(
            {"name": "Manual Commercial Zone"}
        )
        self.state.commercial_zone_id = state_zone
        partner = self.res_partner_model.create(
            {
                "name": "Manual Commercial Zone Partner",
                "country_id": self.country.id,
                "state_id": self.state.id,
            }
        )

        partner.write({"commercial_zone_id": manual_zone.id})

        self.assertEqual(partner.commercial_zone_id, manual_zone)

    def test_explicit_partner_commercial_zone_wins_on_write(self):
        state_zone = self._create_commercial_zone()
        explicit_zone = self.env["commercial.zone"].create(
            {"name": "Explicit Write Commercial Zone"}
        )
        self.state.commercial_zone_id = state_zone
        partner = self.res_partner_model.create(
            {
                "name": "Explicit Write Commercial Zone Partner",
                "country_id": self.country.id,
            }
        )

        partner.write(
            {
                "state_id": self.state.id,
                "commercial_zone_id": explicit_zone.id,
            }
        )

        self.assertEqual(partner.commercial_zone_id, explicit_zone)
