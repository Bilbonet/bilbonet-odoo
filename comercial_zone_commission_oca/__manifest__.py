# Copyright 2026 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Comercial Zone Commission OCA",
    "summary": "Create commercial zones and assign zone agents",
    "version": "18.0.1.0.0",
    "development_status": "Alpha",
    "category": "Sales",
    "website": "https://github.com/bilbonet/bilbonet-odoo",
    "author": "Jesus Ramiro (Bilbonet)",
    "maintainers": ["bilbonet"],
    "license": "AGPL-3",
    "depends": [
        "sale_commission_oca",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/commercial_zone_views.xml",
        "views/res_country_state_views.xml",
        "views/res_partner_views.xml",
    ],
}
