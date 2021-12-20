# Copyright 2021 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, SUPERUSER_ID


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def _read_group_zone_ids(self, zones, domain, order):
        """ Read group customization in order to display all the zones in the
            kanban view, even if they are empty
        """
        zone_ids = zones._search([], order=order, access_rights_uid=SUPERUSER_ID)
        return zones.browse(zone_ids)

    sequence = fields.Integer(string='Sequence', index=True, default=10,
        help="Gives the sequence order when displaying a list of Sale Orders.")
    delivery_zone_id = fields.Many2one(group_expand='_read_group_zone_ids')
    # In order to Show this fields in the kanban view
    zip_code = fields.Char(related='partner_id.zip', readonly=False)
    city = fields.Char(related='partner_id.city', readonly=False)
