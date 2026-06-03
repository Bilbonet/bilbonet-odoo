# Copyright 2026 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Product Category Agent Commission OCA",
    "summary": "Assign sale commission agents from product categories",
    "version": "18.0.1.0.0",
    "development_status": "Alpha",
    "category": "Sales",
    "website": "https://github.com/bilbonet/bilbonet-odoo",
    "author": "Jesus Ramiro (Bilbonet)",
    "maintainers": ["bilbonet"],
    "license": "AGPL-3",
    "depends": [
        "sale_commission_oca",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/product_category_views.xml",
    ],
}
