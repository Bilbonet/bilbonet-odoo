# Copyright 2022 Trey, Kilobytes de Soluciones <www.trey.es>
# Copyright 2022 Jesus Remiro <bilbonet@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class ProjectProject(models.Model):
    _inherit = 'project.project'

    code = fields.Char(
        string='Code', 
        copy=False,
    )

    @api.model
    def create(self, vals):
        if 'code' not in vals:
            vals['code'] = self.env['ir.sequence'].next_by_code(
                'project.sequence')
        return super().create(vals)
