# Copyright 2023 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Account Invoice Report Advisory",
    "version": "14.0.1.0.0",
    "category": "Reporting",
    "summary": "Financial Reports",
    "author": "Jesus Ramiro (Bilbonet.NET)",
    'website': 'https://www.bilbonet.net',
    "depends": ["account_financial_report",],
    "data": [
        "security/ir.model.access.csv",
        "wizard/advisory_report_wizard_view.xml",
        "menuitems.xml",
        "report/advisory_report.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "AGPL-3",
}
