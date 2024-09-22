# Copyright 2024 bilbonet.net - Jesus Ramiro
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models
from odoo.osv import expression
from odoo.tools import float_compare


class ResPartner(models.Model):
    _inherit = "res.partner"

    discount_ids = fields.One2many(
        "customer.product.discount",
        "partner_id",
        string="Customer Product Discount Fixed",
        depends_context=("company",),
        help="Define fixed discounts for products in this customer.",
    )

    def _prepare_domain_product_discounts(self, params):
        self.ensure_one()
        date = fields.Date.to_string(
            params.get("date") or fields.Date.context_today(self)
        )
        product_id = params.get("product_id")
        domain = [
            "|",
            ("company_id", "=", False),
            ("company_id", "=", self.env.company.id),
            "|",
            ("product_id", "=", product_id.id),
            "&",
            ("product_tmpl_id", "=", product_id.product_tmpl_id.id),
            ("product_id", "=", False),
            "|",
            ("date_start", "=", False),
            ("date_start", "<=", date),
            "|",
            ("date_end", "=", False),
            ("date_end", ">=", date),
        ]
        domain = expression.AND(
            [
                domain,
                [("partner_id", "=", self.id)],
            ]
        )
        return domain

    def _discounts_filter_by_quantity(self, discounts, quantity):
        res = self.env["customer.product.discount"]
        precision = self.env["decimal.precision"].precision_get(
            "Product Unit of Measure"
        )
        for discount in discounts:
            if quantity:
                if (
                    float_compare(
                        quantity,
                        discount.min_qty,
                        precision_digits=precision,
                    )
                    == -1
                ):
                    continue
            else:
                if discount.min_qty:
                    continue
            res |= discount
        return res

    def get_product_discounts(self, product, quantity=0.0, date=None, params=None):
        self.ensure_one()
        if not params:
            params = {}
        params.update({"date": date, "product_id": product})
        domain = self._prepare_domain_product_discounts(params)
        params["domain"] = domain

        discounts = self.env["customer.product.discount"].search(
            params.get("domain", []), order="min_qty desc"
        )
        if not discounts:
            return None

        discounts = self._discounts_filter_by_quantity(discounts, quantity)
        if discounts:
            return discounts[0]

        return discounts
