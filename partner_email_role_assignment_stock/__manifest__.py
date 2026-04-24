# Copyright 2026 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Partner Email Role Assignment Stock",
    "summary": "Add role-based partner email recipients for stock pickings",
    "version": "16.0.1.0.0",
    "development_status": "Beta",
    "category": "Inventory",
    "website": "https://github.com/Bilbonet/bilbonet-odoo",
    "author": "Jesus Ramiro (Bilbonet)",
    "maintainers": ["bilbonet"],
    "license": "AGPL-3",
    "depends": [
        "partner_email_role_assignment",
        "stock",
        "stock_picking_send_by_mail",
    ],
    "data": [
        "data/mail_template_data.xml",
        "views/res_partner_views.xml",
    ],
}
