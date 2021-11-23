==========================
Sale Advance Payment Multi
==========================

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

|badge1| |badge2| 

Extends the module "oca/sale-workflow/sale_advance_payment" to make it multi. 
You can choose several sale orders and add an advance payment of the total 
from each of them in one click.

**Table of contents**

.. contents::
   :local:

Usage
=====


To use this module, you need to:

* Go to a sale order tree.
* Select some of them and click on "Action > Pay Sale Advance".
* Select the Journal.
* "Make Advance Payment".

When generating the invoice, the system displays the advanced payments, select those you want to add to the invoice.


Known issues / Roadmap
======================

Split several computed values in separate fields (mls, advance_amount, amount_residual).
This allows a better comprehension of logic, and a better inheritance possibility.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/Bilbonet/bilbonet-odoo/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Bilbonet

Contributors
~~~~~~~~~~~~

* Jesus Ramiro Martinez <jesus@bilbonet.net>

Maintainers
~~~~~~~~~~~

This module is maintained by Bilbonet.
