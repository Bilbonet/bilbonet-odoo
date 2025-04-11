# Copyright (C) 2025 Jesus Remiro <bilbonet@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, fields, models


class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    check_in_map_link = fields.Char(
        string="Check In Map Link",
        compute="_compute_check_in_map_link",
        store=True,
    )
    check_out_map_link = fields.Char(
        string="Check Out Map Link",
        compute="_compute_check_out_map_link",
        store=True,
    )
    
    def _compute_check_in_map_link(self):
        for record in self:
            if record.check_in_latitude and record.check_in_longitude:
                record.check_in_map_link = (
                    f"https://maps.google.com/?q={record.check_in_latitude},{record.check_in_longitude}"
                )
            else:
                record.check_in_map_link = False

    def _compute_check_out_map_link(self):
        for record in self:
            if record.check_out_latitude and record.check_out_longitude:
                record.check_out_map_link = (
                    f"https://maps.google.com/?q={record.check_out_latitude},{record.check_out_longitude}"
                )
            else:
                record.check_out_map_link = False
    
    def action_check_in_map_link(self):
        self.ensure_one()
        if self.check_in_map_link:
            return {
                "type": "ir.actions.act_url",
                "url": self.check_in_map_link,
                "target": "_blank",
            }

    def action_check_out_map_link(self):    
        self.ensure_one()
        if self.check_out_map_link:
            return {
                "type": "ir.actions.act_url",
                "url": self.check_out_map_link,
                "target": "_blank",
            }
