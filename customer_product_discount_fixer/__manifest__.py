# Copyright 2024 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Customer Product Discount Fixer",
    "summary": "Allows to define discounts for products in the customer form",
    "version": "16.0.1.0.0",
    "development_status": "Beta",
    "category": "Sales Management",
    "website": "https://github.com/Bilbonet/bilbonet-odoo",
    "author": "Jesus Ramiro (Bilbonet)",
    "maintainers": ["bilbonet"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["product", "sale_triple_discount"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
        "views/customer_product_discount_views.xml",
    ],
}
