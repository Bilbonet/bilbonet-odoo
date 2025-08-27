# Copyright 2025 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import json

from odoo import models


class PaymentProvider(models.Model):
    _inherit = "payment.provider"

    def _prepare_merchant_parameters(self, tx_values):
        # Check multi-website
        base_url = self._get_website_url()
        callback_url = self._get_website_callback_url()
        values = {
            "Ds_Sermepa_Url": self.redsys_get_form_action_url(),
            "Ds_Merchant_Amount": str(int(round(tx_values["amount"] * 100))),
            "Ds_Merchant_Currency": self.redsys_currency or "978",
            # Extends the character limit from 12 to to 20.
            "Ds_Merchant_Order": (
                tx_values["reference"] and tx_values["reference"][-20:] or False
            ),
            "Ds_Merchant_MerchantCode": (
                self.redsys_merchant_code and self.redsys_merchant_code[:9]
            ),
            "Ds_Merchant_Terminal": self.redsys_terminal or "1",
            "Ds_Merchant_TransactionType": (self.redsys_transaction_type or "0"),
            "Ds_Merchant_Titular": tx_values.get(
                "billing_partner", self.env.user.partner_id
            ).display_name[:60],
            "Ds_Merchant_MerchantName": (
                self.redsys_merchant_name and self.redsys_merchant_name[:25]
            ),
            "Ds_Merchant_MerchantUrl": (
                "%s/payment/redsys/return" % (callback_url or base_url)
            )[:250],
            "Ds_Merchant_MerchantData": self.redsys_merchant_data or "",
            "Ds_Merchant_ProductDescription": (
                self._product_description(tx_values["reference"])
                or self.redsys_merchant_description
                and self.redsys_merchant_description[:125]
            ),
            "Ds_Merchant_ConsumerLanguage": (self.redsys_merchant_lang or "001"),
            "Ds_Merchant_UrlOk": "%s/payment/redsys/result/redsys_result_ok" % base_url,
            "Ds_Merchant_UrlKo": "%s/payment/redsys/result/redsys_result_ko" % base_url,
            "Ds_Merchant_Paymethods": self.redsys_pay_method or "T",
        }
        return self._url_encode64(json.dumps(values)).decode("utf-8")
