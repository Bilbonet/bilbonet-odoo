# Copyright 2024 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Customer Product Discount Fixer",
    "summary": "Allows to define discounts for products in the customer form",
    "version": "14.0.1.0.0",
    "development_status": "Beta",
    "author": "Bilbonet, ",
    "website": "https://github.com/Bilbonet/bilbonet-odoo",
    "category": "Sales Management",
    "license": "AGPL-3",
    "maintainers": [
        "bilbonet",
    ],
    "depends": ["sale_triple_discount"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
        "views/customer_product_discount_views.xml",
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
    "application": False,
}
