============================
Multi Pricelists Based Items
============================

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

|badge1| |badge2|


This module adds to the pricelist the possibility of calculating prices based on other price lists and in a specific sequence.

By default, Odoo orders the price lists based on some fields of the price list:

    * [applied_on, min_quantity desc, categ_id desc, id desc]

We can't set a specific order .

You can click these links for more information.

https://groups.google.com/g/openerp-spain-users/c/bAFFgs6LFlw

https://github.com/odoo/odoo/pull/45281/files

Usage
=====
A price list can be based on another price list for the prices calc.
For example, we have three price lists:
    * Public: Price list with general with all prices
    * Discounts: Some products with a specific discount.
    * Offers: Ofertas flash para productos específicos con precios muy bajos.

We can create a fourth price list with which include these three price lists (Public / Discount / Offers)
and set the specific sequence for reckoning the prices.

If the same product is in the three price lists, we need that the system chooses the price in the first price list of the list.

Credits
=======

Authors
~~~~~~~

* bilbonet.NET

Contributors
~~~~~~~~~~~~

* Jesus Ramiro <jesus@bilbonet.net>