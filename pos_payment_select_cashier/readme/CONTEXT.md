Some businesses need the cashier responsible for payment to be selected
explicitly at the payment step. This avoids completing payments under an
implicit cashier or under the cashier selected earlier in the session.

This module enforces that confirmation while reusing the standard Odoo 16
cashier selection behavior from `pos_hr`.
