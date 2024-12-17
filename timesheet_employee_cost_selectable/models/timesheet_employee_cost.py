# Copyright 2024 - Bilbonet <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class TimesheetEmployeeCost(models.Model):
    _name = "timesheet.employee.cost"
    _description = "Employee cost in timesheet"
    _rec_name = "full_name"
    _order = "sequence"

    active = fields.Boolean(default=True)
    sequence = fields.Integer("Sequence", default=10)
    name = fields.Char(
        string="Description",
        required=True,
        default=False,
        copy=False,
    )
    employee_cost = fields.Monetary(
        string="Employee Cost",
        currency_field="currency_id",
        required=True,
        default=0.0,
    )
    currency_id = fields.Many2one(
        comodel_name="res.currency",
        string="Currency",
        default=lambda self: self.env.user.company_id.currency_id,
        readonly=True,
    )
    full_name = fields.Char(string="Full Name",
        compute="_compute_full_name", store=True,
    )
    
    @api.depends("name", "employee_cost")
    def _compute_full_name(self):
        for cost in self:
            cost.full_name = "{} ({}€)".format(
                    cost.name, cost.employee_cost
                )