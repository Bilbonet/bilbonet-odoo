# Copyright 2025 - Bilbonet <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProjectCategory(models.Model):
    _name = "project.category"
    _description = "Project Category"
    _rec_name = "complete_name"

    parent_id = fields.Many2one(
        comodel_name="project.category", string="Parent Category"
    )
    child_ids = fields.One2many(
        comodel_name="project.category", inverse_name="parent_id", string="Subtypes"
    )
    name = fields.Char(required=True, translate=True)
    complete_name = fields.Char(
        compute="_compute_complete_name", store=True, recursive=True
    )
    description = fields.Text(translate=True)
    project_ok = fields.Boolean(string="Can be applied for projects", default=True)
    task_ok = fields.Boolean(string="Can be applied for tasks")
    code = fields.Char(copy=False)

    @api.constrains("parent_id")
    def check_parent_id(self):
        if not self._check_recursion():
            raise ValidationError(_("You cannot create recursive project categories."))

    @api.depends("name", "parent_id.complete_name")
    def _compute_complete_name(self):
        for project_category in self:
            if project_category.parent_id:
                project_category.complete_name = "{} / {}".format(
                    project_category.parent_id.complete_name, project_category.name
                )
            else:
                project_category.complete_name = project_category.name
