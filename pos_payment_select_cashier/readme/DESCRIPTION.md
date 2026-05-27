This module extends Point of Sale to require cashier selection before opening
the payment screen.

When a POS user clicks *Payment*, the standard Odoo cashier selection popup is
shown. The payment flow continues only after a cashier is selected, using the
standard `pos_hr` employee and PIN behavior.
