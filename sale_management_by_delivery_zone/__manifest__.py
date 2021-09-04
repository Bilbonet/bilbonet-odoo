# Copyright 2021 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Sale Management by Delivery Zone',
    'version': '14.0.1.0.0',
    'category': 'Sales',
    'summary': 'Allow managing sales organizing and ordering them by zone.',
    'license': 'AGPL-3',
    'author': 'Jesus Ramiro (Bilbonet.NET)',
    'website': 'https://www.bilbonet.net',
    'depends': ['sale', 'partner_delivery_zone'],
    'data': [
        'views/sale_by_delivery_zone_views.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
