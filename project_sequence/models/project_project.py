# Copyright 2022 Trey, Kilobytes de Soluciones <www.trey.es>
# Copyright 2022 Jesus Remiro <bilbonet@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models, _


class ProjectProject(models.Model):
    _inherit = 'project.project'

    code = fields.Char(string='Project Code', 
        required=True, default='/', copy=False)

    _sql_constraints = [
        (
            "project_code_company_uniq",
            "unique(code, company_id)",
            "A Project with the same code already exists for this company!",
        )
    ]

    @api.model
    def create(self, vals):
        if 'code' not in vals or vals.get('code', '/') == '/':
            vals['code'] = self.env['ir.sequence'].next_by_code(
                'project.sequence')
        return super(ProjectProject, self).create(vals)

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
            analytic_account_to_update.write({'name': self.code})
        return res

    @api.model
    def _create_analytic_account_from_values(self, values):
        analytic_account = self.env['account.analytic.account'].create({
            'name': values.get('code', _('Unknown Analytic Account')),
            'company_id': values.get('company_id') or self.env.company.id,
            'partner_id': values.get('partner_id'),
            'active': True,
        })
        return analytic_account

    def _create_analytic_account(self):
        for project in self:
            analytic_account = self.env['account.analytic.account'].create({
                'name': project.code,
                'company_id': project.company_id.id,
                'partner_id': project.partner_id.id,
                'active': True,
            })
            project.write({'analytic_account_id': analytic_account.id})