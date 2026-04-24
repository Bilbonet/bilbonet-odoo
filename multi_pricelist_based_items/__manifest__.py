# Copyright 2021 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Multi Pricelists Based Items",
    "summary": "Calculate prices based on other price lists in a specific sequence",
    "version": "16.0.1.0.0",
    "development_status": "Beta",
    "category": "Sales",
    "website": "https://github.com/Bilbonet/bilbonet-odoo",
    "author": "Jesus Ramiro (Bilbonet)",
    "maintainers": ["bilbonet"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "product",
    ],
    "data": [
        "views/product_pricelist_views.xml",
    ],
}
