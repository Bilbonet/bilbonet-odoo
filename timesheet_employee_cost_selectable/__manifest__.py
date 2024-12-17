# Copyright 2024 - Bilbonet <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Timesheet Employee Cost Selectable",
    "summary": "Select cost in timesheet",
    "version": "15.0.1.0.0",
    "development_status": "Alpha",
    "category": "Services/Timesheets",
    "website": "https://github.com/OCA/bilbonet-odoo/tree/15.0/timesheet_employee_cost_selectable",
    "author": "Bilbonet",
    "maintainers": ["bilbonet"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "preloadable": True,
    "depends": [
        "hr_timesheet",
        "account",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/timesheet_employee_cost_views.xml",
        "views/hr_timesheet_views.xml",
    ],
}
