# Copyright 2026 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class MailTemplate(models.Model):
    _inherit = "mail.template"

    def _get_edi_attachments(self, document):
        # Prevent TicketBAI XML documents from being added in "SEND & PRINT" wizard.
        if (
            document.name
            and document.name.endswith(".xml")
            and document.edi_format_id.code == "es_tbai"
        ):
            return {}
        return super()._get_edi_attachments(document)
