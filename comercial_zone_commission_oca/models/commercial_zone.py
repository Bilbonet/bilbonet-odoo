# Copyright 2026 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class CommercialZone(models.Model):
    _name = "commercial.zone"
    _description = "Commercial Zone"
    _order = "name"

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    agent_ids = fields.One2many(
        comodel_name="commercial.zone.agent",
        inverse_name="zone_id",
        string="Zone Agents",
        copy=True,
    )


class CommercialZoneAgent(models.Model):
    _name = "commercial.zone.agent"
    _description = "Commercial Zone Agent"
    _rec_name = "agent_id"
    _order = "id"

    _sql_constraints = [
        (
            "unique_zone_agent",
            "UNIQUE(zone_id, agent_id)",
            "The same agent can only be assigned once per commercial zone.",
        )
    ]

    zone_id = fields.Many2one(
        comodel_name="commercial.zone",
        required=True,
        ondelete="cascade",
        index=True,
    )
    agent_id = fields.Many2one(
        comodel_name="res.partner",
        string="Agent",
        domain=[("agent", "=", True)],
        required=True,
        ondelete="restrict",
    )
    commission_id = fields.Many2one(
        comodel_name="commission",
        compute="_compute_commission_id",
        store=True,
        readonly=False,
        required=True,
    )

    @api.depends("agent_id")
    def _compute_commission_id(self):
        for zone_agent in self:
            zone_agent.commission_id = zone_agent.agent_id.commission_id
