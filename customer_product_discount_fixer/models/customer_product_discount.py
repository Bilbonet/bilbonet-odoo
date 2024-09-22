# Copyright 2024 bilbonet.net - Jesus Ramiro
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class CustomerProductDiscount(models.Model):
    _name = "customer.product.discount"
    _description = "Customer Product Discount Fixed"
    _order = "id"

    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Customer",
        ondelete="cascade",
        required=True,
        index=True,
        domain=[("parent_id", "=", False)],
        help="Customer for this fixed discounts",
        check_company=True,
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        default=lambda self: self.env.company.id,
        index=1,
    )
    sequence = fields.Integer(
        string="Sequence",
        default=1,
        help="Assigns the priority to the list of customer product discount.",
    )
    product_id = fields.Many2one(
        comodel_name="product.product",
        string="Product Variant",
        check_company=True,
        help="If not set, discounts will apply to all variants of this product.",
    )
    product_tmpl_id = fields.Many2one(
        comodel_name="product.template",
        string="Product Template",
        required=True,
        check_company=True,
        index=True,
        ondelete="cascade",
    )
    # product_uom = fields.Many2one(
    #     comodel_name="uom.uom",
    #     string="Unit of Measure",
    #     related="product_tmpl_id.uom_id",
    #     help="This comes from the product form.",
    # )
    min_qty = fields.Float(
        string="Min. Quantity",
        default=0.0,
        required=True,
        digits="Product Unit Of Measure",
        help="The quantity to sale to this customer to benefit the discounts, "
        "expressed in the sale Product Unit of Measure if not any, "
        "in the default unit of measure of the product otherwise.",
    )
    discount = fields.Float(string="Discount (%)", digits="Discount", default=0.0)
    discount2 = fields.Float(string="Discount 2 (%)", digits="Discount", default=0.0)
    discount3 = fields.Float(string="Discount 3 (%)", digits="Discount", default=0.0)
    discounting_type = fields.Selection(
        string="Discounting type",
        selection=[("additive", "Additive"), ("multiplicative", "Multiplicative")],
        default="multiplicative",
        required=True,
        help="Specifies whether discounts should be additive "
        "or multiplicative.\nAdditive discounts are summed first and "
        "then applied.\nMultiplicative discounts are applied sequentially.\n"
        "Multiplicative discounts are default",
    )
    date_start = fields.Date(string="Start Date", help="Start date for these discounts")
    date_end = fields.Date(string="End Date", help="End date for these discounts")
