# Copyright 2026 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.depends("order_id.partner_id")
    def _compute_agent_ids(self):
        return super()._compute_agent_ids()

    def _prepare_agents_vals_partner(self, partner, settlement_type=None):
        self.ensure_one()
        agent_vals = super()._prepare_agents_vals_partner(
            partner,
            settlement_type=settlement_type,
        )
        if partner == self.order_id.partner_id:
            self._add_commercial_zone_agent_vals(agent_vals, settlement_type)
        return agent_vals

    def _add_commercial_zone_agent_vals(self, agent_vals, settlement_type=None):
        self.ensure_one()
        agent_ids = self._get_agent_ids_from_vals(agent_vals)
        commercial_zone = self.order_id.partner_id.commercial_zone_id
        if not commercial_zone:
            return
        for zone_agent in commercial_zone.agent_ids:
            self._append_commercial_zone_agent_vals(
                agent_vals,
                agent_ids,
                zone_agent,
                settlement_type=settlement_type,
            )

    @api.model
    def _get_agent_ids_from_vals(self, agent_vals):
        return {
            command[2]["agent_id"]
            for command in agent_vals
            if (
                len(command) == 3
                and isinstance(command[2], dict)
                and command[2].get("agent_id")
            )
        }

    @api.model
    def _append_commercial_zone_agent_vals(
        self,
        agent_vals,
        agent_ids,
        zone_agent,
        settlement_type=None,
    ):
        agent = zone_agent.agent_id
        commission = zone_agent.commission_id
        if (
            not agent
            or not commission
            or agent.id in agent_ids
            or (
                settlement_type
                and commission.settlement_type not in (False, settlement_type)
            )
        ):
            return
        agent_vals.append(
            (
                0,
                0,
                {
                    "agent_id": agent.id,
                    "commission_id": commission.id,
                },
            )
        )
        agent_ids.add(agent.id)
