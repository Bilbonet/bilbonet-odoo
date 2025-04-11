# -*- encoding: utf-8 -*-
{
    "name": "Assign and Unassign Followers",
    "description": """
	Assign Followers to a Record of any Model
	""",
    "version": "15.0.1.0.0",
    "category": "Settings",
    "license": "LGPL-3",
    "author": "PPTS [India] Pvt.Ltd.",
    "website": "http://www.pptssolutions.com",
    "depends": ["base", "mail"],
    "data": [
        "security/base_groups.xml",
        "security/ir.model.access.csv",
        "views/assign_followers_view.xml",
    ],
    "auto_install": False,
    "installable": True,
    "application": False,
}
