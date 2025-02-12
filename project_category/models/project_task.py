# Copyright 2025 - Bilbonet <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    category_id = fields.Many2one(
        comodel_name="project.category",
        string="Category",
        domain="[('task_ok', '=', True)]",
    )
