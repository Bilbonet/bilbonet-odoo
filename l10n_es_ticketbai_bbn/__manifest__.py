# Copyright 2025 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "TicketBAI BBN",
    "summary": "Corrección de errores y mejoras en el módulo de TicketBAI API",
    "version": "14.0.1.0.0",
    "development_status": "Alpha",
    "category": "Accounting & Finance",
    "website": "https://github.com/Bilbonet/bilbonet-odoo",
    "author": "Jesus Ramiro, Bilbonet",
    "maintainers": ["bilbonet"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "l10n_es_ticketbai",
    ],
    "data": [
        "views/ticketbai_invoice_views.xml",
    ],
}
