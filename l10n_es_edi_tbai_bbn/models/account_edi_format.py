# Copyright 2026 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class AccountEdiFormat(models.Model):
    _inherit = 'account.edi.format'

    def _l10n_es_tbai_get_invoice_values(self, invoice, cancel):
        res = super()._l10n_es_tbai_get_invoice_values(invoice, cancel)
        invoice_info = res.get('invoice_info') or {}

        # If there's a NoSujeta amount for Art. 7/14, use OT instead of default RL.
        def _iter_no_sujeta_nodes(info):
            if info.get('DesgloseFactura'):
                yield info['DesgloseFactura'].get('NoSujeta', {})
                return
            desglose_tipo = info.get('DesgloseTipoOperacion') or {}
            for key in ('PrestacionServicios', 'Entrega'):
                node = desglose_tipo.get(key)
                if node:
                    yield node.get('NoSujeta', {})

        for no_sujeta in _iter_no_sujeta_nodes(invoice_info):
            if no_sujeta.get('ImportePorArticulos7_14_Otros'):
                res['nosujeto_causa'] = 'OT'
                break
        return res
