# Copyright 2021 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Multi Pricelists Based Items',
    'version': '12.0.1.0.0',
    'category': 'Sales',
    'license': 'AGPL-3',
    'author': 'Jesus Ramiro (Bilbonet.NET)',
    'website': 'https://www.bilbonet.net',
    'depends': [
        'product',
    ],
    'data': [
        'views/product_pricelist_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
