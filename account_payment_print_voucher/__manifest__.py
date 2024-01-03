# Copyright 2024 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Acount Payment Print Voucher',
    'version': '15.0.1.0.0',
    'category': 'Account',
    'license': 'AGPL-3',
    'author': 'Jesus Ramiro (Bilbonet.NET)',
    'website': 'https://www.bilbonet.net',
    'depends': ['account_due_list'],
    'data': [
        'report/account_payment_print_voucher_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
