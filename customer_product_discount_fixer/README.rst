================================
Customers Product Discount Fixer
================================

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3


|badge1| |badge2|


This module allows to fix discounts for products in the form of the customer. 
Also to indicate a period of time when the discounts are available.


**Table of contents**

.. contents::
   :local:

Configuration
=============

There's a new tab called *Product Discounts* in the partner form,
where you can fix discounts for products. These discounts will be 
automatically set in a sale order for that partner and product.


In price list configuration > discount policy there is a new 
option *Do not apply any calculations with discounts* to avoid 
calculations in unit price field.

Usage
=====

#. Navigate to a customer page. In the *Product Discounts* tab, add a new line to the table to add a specify discounts for a given product.
#. Create a Sales Order for the customer you chose. Add a line with the product: the discounts will reflect the ones added in the customer form.

Note: You can define different discounts to apply by quantity or dates.

Known issues / Roadmap
======================



Bug Tracker
===========

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Bilbonet

Contributors
~~~~~~~~~~~~

