# Copyright 2020 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models,  _
from random import randint


class SaleLineInfoTags(models.Model):
    _name = "sale.line.info.tags"
    _description = "Tags in sale order line"

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char(string='Tag Name', required=True, translate=True)
    active = fields.Boolean(default=True, help="The active field allows you to hide the tag without removing it.")
    color = fields.Integer(string='Color Index', default=_get_default_color)

    _sql_constraints = [
        ('sale_line_info_tag_name_uniq', 'unique (name)',
         _('Tag name already exists !')),
    ]