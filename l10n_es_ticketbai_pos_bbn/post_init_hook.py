# Copyright 2025 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

logger = logging.getLogger(__name__)


def post_init_hook(cr, registry):
    logger.info(
        "Change to error, the state of ticketbai pos invoices with a not ok response."
    )
    cr.execute(
        """
            UPDATE tbai_invoice AS ti
            SET state = 'error'
            WHERE ti.state = 'sent'
            and ti.pos_order_id notnull and invoice_id isnull
            AND (
                select state
                from tbai_response
                where tbai_invoice_id = ti.id
                ORDER BY id DESC
                LIMIT 1
            ) != '00';
        """
    )
