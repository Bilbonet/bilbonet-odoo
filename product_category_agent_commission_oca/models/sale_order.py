# Copyright 2026 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.depends("product_id")
    def _compute_agent_ids(self):
        return super()._compute_agent_ids()

    def _prepare_agents_vals_partner(self, partner, settlement_type=None):
        """Add product category agents only when preparing main customer agents."""
        self.ensure_one()
        agent_vals = super()._prepare_agents_vals_partner(
            partner,
            settlement_type=settlement_type,
        )
        if partner == self.order_id.partner_id:
            self._add_product_category_agent_vals(agent_vals, settlement_type)
        return agent_vals

    def _add_product_category_agent_vals(self, agent_vals, settlement_type=None):
        self.ensure_one()
        agent_ids = self._get_agent_ids_from_vals(agent_vals)
        product_category = self.product_id.categ_id
        if not product_category:
            return
        for category_agent in product_category.product_manager_agent_ids:
            self._append_product_category_agent_vals(
                agent_vals,
                agent_ids,
                category_agent,
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
    def _append_product_category_agent_vals(
        self,
        agent_vals,
        agent_ids,
        category_agent,
        settlement_type=None,
    ):
        agent = category_agent.agent_id
        commission = category_agent.commission_id
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
