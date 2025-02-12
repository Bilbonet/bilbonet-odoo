# Copyright 2025 - Bilbonet <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Project Categories",
    "summary": "Classify projects by category",
    "version": "15.0.1.0.0",
    "development_status": "Alpha",
    "category": "Project",
    "website": "https://github.com/OCA/bilbonet-odoo/tree/15.0/project_category",
    "author": "Bilbonet",
    "maintainers": ["bilbonet"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "project",
    ],
    "data": [
        "views/project_category_views.xml",
        "views/project_project_views.xml",
        "views/project_task_views.xml",
        "security/ir.model.access.csv",
    ],
}
