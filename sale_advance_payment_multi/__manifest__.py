# Copyright 2021 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Sale Advance Payment Multi",
    "version": "14.0.1.0.0",
    "author": "Bilbonet",
    "website": "https://github.com/Bilbonet/bilbonet-odoo",
    "category": "Sales",
    "license": "AGPL-3",
    "summary": "Extends the module (oca/sale-workflow/sale_advance_payment) to make it multi",
    "depends": ["sale_advance_payment"],
    "data": [
        "wizard/sale_advance_payment_multi_wizard_view.xml",
    ],
    "installable": True,
}
