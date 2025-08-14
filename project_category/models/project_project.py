# Copyright 2025 - Bilbonet <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    category_id = fields.Many2one(
        comodel_name="project.category",
        string="Category",
        copy=False,
        domain="[('project_ok', '=', True)]",
    )
