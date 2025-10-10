# Copyright <2021> bilbonet.net - Jesus Ramiro
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class Pricelist(models.Model):
    _inherit = "product.pricelist"

    def _get_applicable_rules(self, products, date, **kwargs):
        """Override to include sequence in the ordering of pricelist items."""
        domain = self._get_applicable_rules_domain(products, date, **kwargs)

        # Add sequence to the beginning of the order
        return self.env["product.pricelist.item"].search(
            domain + [("pricelist_id", "=", self.id)],
            order="sequence, applied_on, min_quantity desc, categ_id desc, id desc",
        )


class ProductPricelistItem(models.Model):
    _inherit = "product.pricelist.item"
    _order = "sequence, applied_on, min_quantity desc, categ_id desc, id desc"

    sequence = fields.Integer(
        default=10,
        help="""
            Gives the sequence order when applying pricelist items.
            You can fix it manually instead dragging lines.
            Lower values are applied first.""",
    )
