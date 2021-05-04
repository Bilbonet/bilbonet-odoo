==============================================
Personalizaciones relacionadas con los precios
==============================================

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

|badge1| |badge2|
https://groups.google.com/g/openerp-spain-users/c/bAFFgs6LFlw

https://github.com/odoo/odoo/pull/45281/files

Este módulo son personalizaciones de Odoo para Conifres relacionadas con los precios.

Listas de precios
=================
Una lista de precios se puede basar en otras listas de precios para sus cálculos.
Por ejemplo tenemos tres listas de precios:
* Publica: Tarifa general con todos los precios.
* Descuentos: Ciertos artículos tienen un descuento.
* Ofertas: Ofertas puntuales de artículos que están más rebajados.

Creamos una cuarta tarifa para cientos clientes que aglutina estas tres tarifas (Ofertas > Descuentos > Publica).
Necesitamos establecer la prioridad con la que se calculan los precios en la tarifa. Es decir, preferimos que
calcule primero el precios en la tarifa “Ofertas” antes que en la tarifa “Publica”.

Tal como se ordenan las tarifas por defecto no podemos decidir este orden::

    [applied_on, min_quantity desc, categ_id desc, id desc].

Añadimos la posibilidad de decidir el orden en las definiciones de las tarifas.


Credits
=======

Authors
~~~~~~~

* bilbonet.NET

Contributors
~~~~~~~~~~~~

* Jesus Ramiro <jesus@bilbonet.net>