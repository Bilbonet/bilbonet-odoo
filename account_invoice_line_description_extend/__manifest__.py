# Copyright (C) 2022 Jesus Remiro <bilbonet@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Account Invoice line description extend",
    "version": "15.0.1.0.0",
    "category": "Account",
    "author": "Bilbonet",
    "website": "https://github.com/Bilbonet/bilbonet-odoo/",
    "license": "AGPL-3",
    "depends": ["account"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/account_invoice_line_description_extend.xml",
        "views/account_move_views.xml"
    ],
    "installable": True,
}
