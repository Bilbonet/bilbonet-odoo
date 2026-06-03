# Copyright 2026 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProductCategory(models.Model):
    _inherit = "product.category"

    product_manager_agent_ids = fields.One2many(
        comodel_name="product.category.agent",
        inverse_name="category_id",
        string="Product Manager Agents",
        copy=True,
    )


class ProductCategoryAgent(models.Model):
    _name = "product.category.agent"
    _description = "Product Category Agent"
    _rec_name = "agent_id"
    _order = "id"

    _sql_constraints = [
        (
            "unique_category_agent",
            "UNIQUE(category_id, agent_id)",
            "The same agent can only be assigned once per product category.",
        )
    ]

    category_id = fields.Many2one(
        comodel_name="product.category",
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
        for category_agent in self:
            category_agent.commission_id = category_agent.agent_id.commission_id
