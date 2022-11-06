# Copyright (C) 2022 Jesus Remiro <bilbonet@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sale order line description extend",
    "version": "15.0.1.0.0",
    "category": "Sales Management",
    "author": "Bilbonet",
    "website": "https://github.com/Bilbonet/bilbonet-odoo/",
    "license": "AGPL-3",
    "depends": ["sale"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/sale_order_line_description_extend.xml",
        "views/sale_view.xml"
    ],
    "installable": True,
}
