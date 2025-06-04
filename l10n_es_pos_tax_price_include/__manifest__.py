# Copyright 2022 Bilbonet - Jesus Ramiro
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
# See README.rst file on addon root folder for more details
{
    "name": "TPV Impuestos incluidos en precio",
    "summary": "Impuestos incluidos en precio y posicion fiscal para trabajar en TPV "
    "con precios con impuestos incluidos",
    "version": "14.0.1.0.0",
    "development_status": "Alpha",
    "category": "Point of Sale",
    "website": "https://github.com/Bilbonet/bilbonet-odoo",
    "author": "Jesus Ramiro, Bilbonet",
    "maintainers": ["bilbonet"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "l10n_es",
    ],
    "data": [
        "data/account_tax_data.xml",
        "data/account_fiscal_position_template_data.xml",
    ],
}
