# Copyright 2022 Trey, Kilobytes de Soluciones <www.trey.es>
# Copyright 2022 Jesus Remiro <bilbonet@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class ProjectProject(models.Model):
    _inherit = 'project.project'
    _rec_name = "full_name"

    code = fields.Char(string='Project Code', 
        required=True, default='/', copy=False)
    full_name = fields.Char(string="Full Name",
        compute="_compute_full_name", store=True
    )

    _sql_constraints = [
        (
            "project_code_company_uniq",
            "unique(code, company_id)",
            "A Project with the same code already exists for this company!",
        )
    ]

    @api.depends("name", "code")
    def _compute_full_name(self):
        for project in self:
            project.full_name = "{} {}".format(
                    project.code, project.name
                )

    @api.model
    def create(self, vals):
        if 'code' not in vals or vals.get('code', '/') == '/':
            vals['code'] = self.env['ir.sequence'].next_by_code(
                'project.sequence')
        return super(ProjectProject, self).create(vals)
