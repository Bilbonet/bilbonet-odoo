# Copyright 2024 - Bilbonet <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    employee_cost = fields.Many2one(
        comodel_name="timesheet.employee.cost",
        string="Cost",
        store=True,
        readonly=False,
    )

    def _employee_timesheet_cost(self):
        self.ensure_one()
        if self.employee_cost:
            return self.employee_cost.employee_cost
        else:
            return super()._employee_timesheet_cost()

    def _timesheet_postprocess_values(self, values):
        """take into account employee_cost field to update amount"""
        if not any(field_name in values for field_name in ["employee_cost"]):
            return super()._timesheet_postprocess_values(values)
        else:
            result = {id_: {} for id_ in self.ids}
            sudo_self = (
                self.sudo()
            )  # this creates only one env for all operation that required sudo()
            # (re)compute the amount (depending on unit_amount, employee_id for the cost, and account_id for currency)
            for timesheet in sudo_self:
                cost = timesheet._employee_timesheet_cost()
                amount = -timesheet.unit_amount * cost
                amount_converted = timesheet.employee_id.currency_id._convert(
                    amount,
                    timesheet.account_id.currency_id or timesheet.currency_id,
                    self.env.company,
                    timesheet.date,
                )
                result[timesheet.id].update(
                    {
                        "amount": amount_converted,
                    }
                )
            return result
