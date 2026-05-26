# AGENTS.md

Module-level guidance for an **Odoo 18 addon**.

This file should stay short, practical, and specific to the module.
It exists to capture context that an agent cannot reliably infer from:

- the source code
- `__manifest__.py`
- views, security, data, and tests
- repository configuration
- shared Odoo 18 and OCA skills

Do **not** duplicate generic Odoo, OCA, linting, formatting, migration, or
module structure rules here. Those are already covered by:

- the repository executable configuration
- the installed Odoo/OCA skills

Use this document for **functional intent, business constraints, sensitive
areas, operational assumptions, and module-specific change guidance**.

---

# 1. Module Identity

## Technical Name

`<module_name>`

## Functional Name

`<functional_name>`

## Status

`<draft / active / maintenance / deprecated>`

## Target Version

- Odoo: `18.0`
- Target branch: `18.0`

## Module Type

`<customization / extension / connector / reporting / localization / utility>`

---

# 2. Functional Intent

## Summary

<Explain in a short paragraph what the module is for and why it exists.>

## Business Need

<Describe the concrete business problem solved by the module.>

## Expected Outcome

<Describe what should be true for users or processes once the module is installed and configured.>

---

# 3. Scope

## Included

- `<main_feature_1>`
- `<main_feature_2>`
- `<main_feature_3>`

## Explicitly Out of Scope

- `<out_of_scope_1>`
- `<out_of_scope_2>`

## Main Use Cases

- `<use_case_1>`
- `<use_case_2>`

---

# 4. Functional Footprint

Document only the objects that matter to understand change impact.

## Main Models

| Model | Role | Notes |
|-------|------|-------|
| `<model.name>` | <main purpose> | <optional note> |
| `<existing.model>` | <extended purpose> | <optional note> |

## Main User Touchpoints

- `<form/list/report/wizard/menu/action_1>`
- `<form/list/report/wizard/menu/action_2>`

## Main Automations

- `<cron / automated action / computed side effect_1>`
- `<cron / automated action / computed side effect_2>`

---

# 5. Functional Flow

Summarize only the main operational flow.

## Primary Flow

1. `<step_1>`
2. `<step_2>`
3. `<step_3>`

## Secondary or Exceptional Flows

- `<secondary_flow_1>`
- `<secondary_flow_2>`

---

# 6. Dependencies and Configuration

Do not restate the full manifest. Document only what is relevant for reasoning.

## Important Odoo Dependencies

- `<dependency_1>`
- `<dependency_2>`

## External Systems

- `<system_1>`
- `<system_2>`

If relevant, note the integration direction:

- `Odoo -> external`
- `external -> Odoo`
- `bidirectional`

## Required Configuration

- `<mandatory_configuration_1>`
- `<mandatory_configuration_2>`

## Important Master Data or Parameters

- `<parameter_or_data_1>`
- `<parameter_or_data_2>`

---

# 7. Security and Risk Areas

## Security-Relevant Elements

- `<groups / record rules / sensitive ACL area_1>`
- `<groups / record rules / sensitive ACL area_2>`

## Sensitive Data or Operations

- `<critical_data_or_operation_1>`
- `<critical_data_or_operation_2>`

## Main Side Effects

- `<important_side_effect_1>`
- `<important_side_effect_2>`

Examples:

- state changes in business documents
- creation of accounting or stock records
- synchronization with third-party systems
- regeneration of documents or derived data

---

# 8. Critical Constraints

Document the rules that must not be broken without explicit review.

- `<critical_constraint_1>`
- `<critical_constraint_2>`
- `<critical_constraint_3>`

Examples:

- do not break existing XML IDs
- do not change posted accounting behavior without validation
- do not alter external identifiers already used in integrations
- do not introduce duplicate automation triggers

## Backward Compatibility Expectation

`<strict / reasonable / low-priority>`

---

# 9. Validation Guidance

Document only the validation that is especially relevant for this module.

## Minimum Validation

- `<test_or_check_1>`
- `<test_or_check_2>`

## Upgrade Expectations

- review whether module upgrade is needed after model, view, security, or data changes

## Functional Validation Focus

- `<functional_validation_focus_1>`
- `<functional_validation_focus_2>`

---

# 10. Guidance for Automated Changes

## Safe Changes

- fixes clearly inside the documented module scope
- tests and documentation aligned with those fixes
- small refactors that do not alter functional behavior

## Changes Requiring Extra Care

- manifest dependency changes
- security changes
- stored field logic changes
- XML ID renames
- cron or automation changes
- integration contract changes

## Do Not Assume

- undocumented business behavior
- permission to create new external dependencies
- permission to change workflows outside this module's purpose
- permission to modify integration contracts without review

---

# 11. Open Points

Use this section while the module is young and documentation is incomplete.

## Known Limitations

- `<limitation_1>`
- `<limitation_2>`

## Pending Clarifications

- `<pending_question_or_gap_1>`
- `<pending_question_or_gap_2>`

## Additional Notes

<Any short note useful for future agents or developers.>

---

# 12. History

| Date | Changes |
|------|---------|
| `2026-04-21` | Simplified module template to focus on module-specific context and avoid duplicating Odoo/OCA rules |
