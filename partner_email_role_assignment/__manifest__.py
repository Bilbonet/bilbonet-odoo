# Copyright (C) 2026 Jesus Remiro <bilbonet@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Partner Email Role Assignment",
    "summary": "Assign email roles to partner contacts for targeted "
    "communication in email templates",
    "version": "16.0.1.0.0",
    "category": "Base",
    "website": "https://github.com/Bilbonet/bilbonet-odoo",
    "author": "Jesus Ramiro (Bilbonet)",
    "maintainers": ["bilbonet"],
    "license": "AGPL-3",
    "depends": [
        "account",
        "sale",
    ],
    "data": [
        "data/mail_template_data.xml",
        "views/res_partner_views.xml",
    ],
}
