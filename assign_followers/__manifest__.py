# Copyright 2025 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Assign and Unassign Followers",
    "summary": "Assign Followers to a Record of any Model",
    "version": "15.0.1.0.0",
    "development_status": "Alpha",
    "category": "Settings",
    "website": "https://github.com/OCA/account-financial-reporting",
    "author": "PPTS [India] Pvt.Ltd.",
    "maintainers": ["bilbonet"],
    "license": "AGPL-3",
    "auto_install": False,
    "installable": True,
    "application": False,
    "depends": ["base", "mail"],
    "data": [
        "security/base_groups.xml",
        "security/ir.model.access.csv",
        "views/assign_followers_view.xml",
    ],
}
