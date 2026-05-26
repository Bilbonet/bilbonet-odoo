# Copyright 2026 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    commercial_zone_id = fields.Many2one(
        comodel_name="commercial.zone",
        string="Commercial Zone",
        ondelete="restrict",
        index=True,
    )

    @api.onchange("state_id")
    def _onchange_state_id_commercial_zone(self):
        for partner in self:
            partner.commercial_zone_id = partner.state_id.commercial_zone_id

    @api.model_create_multi
    def create(self, vals_list):
        if not self.env.context.get("import_file"):
            self._add_commercial_zone_vals_from_state(vals_list)
        return super().create(vals_list)

    def write(self, vals):
        vals = vals.copy()
        self._add_commercial_zone_vals_from_state([vals])
        return super().write(vals)

    def _commercial_fields(self):
        fields_to_sync = super()._commercial_fields()
        fields_to_sync.append("commercial_zone_id")
        return fields_to_sync

    @api.model
    def _check_import_consistency(self, vals_list):
        result = super()._check_import_consistency(vals_list)
        self._add_commercial_zone_vals_from_state(vals_list)
        return result

    @api.model
    def _add_commercial_zone_vals_from_state(self, vals_list):
        state_ids = {
            vals["state_id"]
            for vals in vals_list
            if "state_id" in vals
            and "commercial_zone_id" not in vals
            and vals.get("state_id")
        }
        state_to_zone = {
            state.id: state.commercial_zone_id.id
            for state in self.env["res.country.state"].browse(state_ids)
        }
        for vals in vals_list:
            if "state_id" in vals and "commercial_zone_id" not in vals:
                vals["commercial_zone_id"] = (
                    state_to_zone.get(vals.get("state_id")) or False
                )
