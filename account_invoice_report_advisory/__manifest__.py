# Copyright 2023 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Account Invoice Report Advisory",
    "summary": "Financial Reports",
    "version": "14.0.1.0.0",
    "development_status": "Alpha",
    "category": "Reporting",
    "website": "https://github.com/Bilbonet/bilbonet-odoo",
    "author": "Jesus Ramiro, Bilbonet",
    "maintainers": ["bilbonet"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "account_financial_report",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizard/advisory_report_wizard_view.xml",
        "menuitems.xml",
        "report/advisory_report.xml",
    ],
}
