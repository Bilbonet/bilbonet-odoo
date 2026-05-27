# Copyright 2026 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "POS Payment Select Cashier",
    "summary": "Force cashier selection when accessing the POS payment screen.",
    "version": "16.0.1.0.0",
    "development_status": "Alpha",
    "category": "Point of Sale",
    "website": "https://github.com/Bilbonet/bilbonet-odoo",
    "author": "Jesus Ramiro (Bilbonet)",
    "maintainers": ["bilbonet"],
    "license": "AGPL-3",
    "depends": [
        "point_of_sale",
        "pos_hr",
    ],
    "assets": {
        "point_of_sale.assets": [
            "pos_payment_select_cashier/static/src/js/product_screen.js",
        ],
    },
    "installable": True,
}
