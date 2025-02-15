# Copyright 2025 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "TicketBAI - POS BBN",
    "summary": "Corrección de errores y mejoras en el módulo de TicketBAI para TPV",
    "version": "14.0.1.0.0",
    "development_status": "Alpha",
    "category": "Accounting & Finance",
    "website": "https://github.com/bilbonet/bilbonet-odoo/tree/14.0/l10n_es_ticketbai_pos_plus",
    "author": "Jesus Ramiro, Bilbonet",
    "maintainers": ["bilbonet"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "l10n_es_ticketbai_pos",
    ],
    "data": [
        "views/ticketbai_invoice_views.xml",
    ],
    "post_init_hook": "post_init_hook",
}
