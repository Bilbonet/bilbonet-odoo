# Copyright 2023 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def button_confirm(self):
        res = super().button_confirm()
        for line in self.order_line:
            vals = dict()
            # Do not add a contact as a supplier
            partner = self.partner_id if not self.partner_id.parent_id else self.partner_id.parent_id
            supplierinfo = line.product_id.seller_ids.filtered(
                lambda l: l.name == partner
                and l.company_id == line.company_id
            )

            if supplierinfo:
                # Convert the price in the right currency.
                currency = partner.property_purchase_currency_id or self.env.company.currency_id
                price = self.currency_id._convert(
                    line.price_unit, currency, line.company_id, 
                    line.date_order or fields.Date.today(), round=False
                )
                # Compute the price for the template's UoM, because the supplier's UoM is related to that UoM.
                if line.product_id.product_tmpl_id.uom_po_id != line.product_uom:
                    default_uom = line.product_id.product_tmpl_id.uom_po_id
                    price = line.product_uom._compute_price(price, default_uom)

                if price != supplierinfo.price:
                    vals['price'] = price
                
                discount = line.discount or False
                if discount and discount != supplierinfo.discount:
                    vals['discount'] = discount
                
                if len(vals) > 0:
                    supplierinfo.write(vals)
            
        return res
