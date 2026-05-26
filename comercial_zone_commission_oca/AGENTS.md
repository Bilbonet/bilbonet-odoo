# AGENTS.md

Module-level context for the Odoo 18 addon `comercial_zone_commission_oca`.

This file captures stable functional context for future automated changes. It does not
replace workspace-wide Odoo/OCA instructions.

---

# 1. Module Identity

## Technical Name

`comercial_zone_commission_oca`

## Functional Name

Commercial Zone Commission OCA

## Status

Alpha

## Target Version

- Odoo: `18.0`
- Target branch: `18.0`

## Module Type

Extension/customization of OCA sales commissions.

---

# 2. Functional Intent

This module adds commercial zones to the sales commission workflow.

Customers can be assigned to a commercial zone. Each commercial zone can have one or
more zone agents. When sales order line commission agents are computed, the agents
configured on the customer's commercial zone are added to the standard agents provided
by `sale_commission_oca`.

---

# 3. Scope

## Included

- Maintain commercial zones from the commissions configuration menu.
- Assign zone agents and their commissions to commercial zones.
- Assign one commercial zone to a contact.
- Add commercial zone agents to sales order line commission agents.

## Explicitly Out of Scope

- Province, territory, or sub-zone delegation rules.
- Using delivery, invoice, or other secondary partner addresses to determine the
  commercial zone.
- Automatic recomputation of existing sales orders when zone configuration changes.

---

# 4. Functional Footprint

## Main Models

| Model                   | Role                             | Notes                                                 |
| ----------------------- | -------------------------------- | ----------------------------------------------------- |
| `commercial.zone`       | Commercial zone master data      | Holds the zone name and zone agents.                  |
| `commercial.zone.agent` | Zone-agent assignment line       | Points to a commission agent partner and commission.  |
| `res.partner`           | Extended contact                 | Adds `commercial_zone_id`.                            |
| `sale.order.line`       | Extended sales commission source | Adds zone agents during commission agent preparation. |

## Main User Touchpoints

- `Commissions > Configuration > Commercial Zones`
- Contact form: `Commercial Zone` field near the existing commission agents.
- Sale order button `Regenerate agents` from `sale_commission_oca` for manual refresh of
  draft/sent order agents.

---

# 5. Functional Flow

1. Configure a commercial zone.
2. Add one or more zone agents to the commercial zone.
3. Assign the commercial zone to the customer contact.
4. Create or recompute a sales order for that customer.
5. Sales order lines receive the standard commission agents plus the zone agents,
   without duplicating the same agent on a line.

Only `order_id.partner_id.commercial_zone_id` determines the commercial zone.

---

# 6. Dependencies and Configuration

## Important Odoo Dependencies

- `sale_commission_oca`

The module deliberately does not depend on `idc_commission`. It should coexist with that
module without requiring it.

## Required Configuration

- Zone agents must be partners marked as commission agents.
- Zone agent commissions must be compatible with sales invoice settlement when sales
  order line agents are computed with `settlement_type="sale_invoice"`.

---

# 7. Security and Risk Areas

## Security-Relevant Elements

- `commercial.zone` and `commercial.zone.agent` have ACLs for
  `commission_oca.group_commission_user` and `commission_oca.group_commission_manager`.
- Commission users can read zones and zone agents.
- Commission managers can create, edit, and delete zones and zone agents.

## Main Side Effects

- Sales order line commission agent lines can include additional agents from the
  customer's commercial zone.
- Invoice propagation follows the standard `sale_commission_oca` behavior after agents
  are present on sales order lines.

---

# 8. Critical Constraints

- Do not introduce province, territory, or sub-zone behavior without explicit functional
  review.
- Do not use `partner_shipping_id`, invoice address, or child contact addresses to
  determine the commercial zone unless explicitly requested.
- Keep automatic recomputation aligned with `sale_commission_oca`: agent recomputation
  depends on `order_id.partner_id`; zone setup changes should be applied to existing
  draft/sent orders through the standard manual regenerate action.
- Avoid duplicate agents on the same sales order line; OCA commission line models
  enforce uniqueness by parent object and agent.
- Do not add a hard dependency on `idc_commission`.

## Backward Compatibility Expectation

Reasonable while the module remains alpha; avoid renaming XML IDs or model fields once
the module is used in real databases.

---

# 9. Validation Guidance

## Minimum Validation

- Python syntax check for the module.
- XML parse check for module views.
- When requested, run the module tests covering zone agent assignment and duplicate
  avoidance.

## Functional Validation Focus

- A customer with a commercial zone receives zone agents on sales order lines.
- Existing partner agents and zone agents coexist.
- The same agent is not duplicated when assigned both directly on the customer and
  through the commercial zone.
- Changing zone configuration does not automatically update existing orders until agents
  are regenerated.

---

# 10. History

| Date       | Changes                                                                                           |
| ---------- | ------------------------------------------------------------------------------------------------- |
| 2026-05-26 | Initial module context after implementing commercial zones and zone agents for sales commissions. |
