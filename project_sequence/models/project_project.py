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

    _sql_constraints = [
        (
            "project_code_company_uniq",
            "unique(code, company_id)",
            "A Project with the same code already exists for this company!",
        )
    ]

    def write(self, vals):
        res = super(ProjectProject, self).write(vals) if vals else True

        if ('name' in vals or 'code' in vals) and self.analytic_account_id:
            projects_read_group = self.env['project.project'].read_group(
                [('analytic_account_id', 'in', self.analytic_account_id.ids)],
                ['analytic_account_id'],
                ['analytic_account_id']
            )
            analytic_account_to_update = self.env['account.analytic.account'].browse([
                res['analytic_account_id'][0]
                for res in projects_read_group
                if res['analytic_account_id'] and res['analytic_account_id_count'] == 1
            ])
            analytic_account_to_update.write({'name': '[' + self.code + '] ' + self.name})
        return res