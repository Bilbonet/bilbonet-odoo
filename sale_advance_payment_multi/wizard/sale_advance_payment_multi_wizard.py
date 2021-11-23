# Copyright 2021 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class AccountVoucherWizard(models.TransientModel):
    _inherit = "account.voucher.wizard"

    count = fields.Integer(string='Orders Count', default=0)

    @api.constrains("amount_advance")
    def check_amount(self):
        if self.count < 1:
            super().check_amount()

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        sale_ids = self.env.context.get("active_ids", [])
        if len(sale_ids) <=1:
            return res

        sales = self.env["sale.order"].browse(sale_ids)
        amount_total = 0
        for so in sales:
            amount_total += so.amount_residual

        res.update(
                {
                    "count": len(sale_ids),
                    "amount_total": amount_total,
                    "amount_advance": amount_total,
                }
            )
        return res

    def make_advance_payments(self):
        """Create customer paylines and validates the payment for each sale order"""
        payment_obj = self.env["account.payment"]
        sale_obj = self.env["sale.order"]

        sale_ids = self.env.context.get("active_ids", [])
        if sale_ids:
            for so in sale_ids:
                sale = sale_obj.browse(so)
                if sale.amount_residual <= 0:
                    continue
                payment_vals = self._prepare_payment_vals(sale)
                payment_vals.update(
                        {
                            "amount": sale.amount_residual,
                        }
                    )
                payment = payment_obj.create(payment_vals)
                sale.account_payment_ids |= payment
                payment.action_post()
        
        return {
            "type": "ir.actions.act_window_close",
        }
