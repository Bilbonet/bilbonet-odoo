# Copyright 2024 - Bilbonet <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Partner Delivery Zone Extended",
    "summary": "Extend the functionality of partner zones in inventory application",
    "version": "15.0.1.0.0",
    "development_status": "Alpha",
    "category": "Delivery",
    "website": "https://github.com/OCA/bilbonet-odoo/tree/15.0/partner_delivery_zone_extended",
    "author": "Bilbonet",
    "maintainers": ["bilbonet"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "preloadable": True,
    "depends": [
        "partner_delivery_zone",
        "stock_picking_batch",
    ],
    "data": [
        "views/stock_batch_picking.xml",
    ],
}
