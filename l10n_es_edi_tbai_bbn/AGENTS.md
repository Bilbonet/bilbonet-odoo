# AGENTS.md

## Purpose of this file

This file provides **mandatory instructions** for AI agents working on this Odoo module.
The agent must read and follow this document **before analyzing or modifying any code**.

This module follows **OCA standards and conventions** unless explicitly stated otherwise.

---

## Module Overview (TO BE COMPLETED)

### Functional Description
Extension of Odoo's official `l10n_es_edi_tbai` module for TicketBAI (Bizkaia / Basque Country).
It aims to cover gaps in the official module needed by a specific client, without rewriting it.
Currently improves handling of VAT‑exempt invoices (No Sujeta) for unsupported cases.

### Functional Scope
- Provides targeted adjustments over the official TicketBAI sending flow.
- Covers VAT‑exempt (No Sujeta) cases not contemplated by the official module.
- Does not aim to replace or duplicate the full `l10n_es_edi_tbai` logic.

### Target Users
- Odoo integrators/consultants who need to adapt TicketBAI to real client cases.
- Indirect use by end users through the invoicing flow.

---

## Odoo & Technical Context (TO BE COMPLETED)

### Odoo Version(s)
- Odoo 16.0 (confirm Community/Enterprise edition if applicable).

### Python Version
- Python 3.10 (standard in Odoo 16; confirm if different).

### Module Type
- Business addon that extends models/logic of the official TicketBAI module.

---

## OCA Compliance (MANDATORY)

This module **must comply with OCA standards**, including but not limited to:

- OCA module structure
- OCA naming conventions
- OCA coding guidelines
- OCA manifest conventions
- OCA migration and compatibility rules

The agent must assume:
- Code quality is more important than speed
- Backward compatibility matters
- Explicit is better than implicit

If unsure, **follow OCA conventions by default**.

---

## Repository & Module Structure

### Addon Structure
The agent must respect the existing structure:
- `__manifest__.py`
- `models/`
- `views/`
- `security/`
- `data/`
- `wizards/` (if present)
- `migrations/` (if present)

No structural changes unless explicitly requested.

---

## Development Rules for AI Agents

### What You MAY Do
- Read and analyze existing code
- Extend models using standard Odoo patterns
- Add fields, methods, and views consistently
- Refactor code **only when requested**
- Follow existing architectural decisions

### What You MUST NOT Do
- Do not rewrite the module from scratch
- Do not invent new features
- Do not change the data model without request
- Do not introduce new dependencies
- Do not break Odoo version compatibility
- Do not bypass OCA linting rules

---

## Coding Conventions

### Python
- Follow OCA Python style
- Use explicit method names
- Avoid magic values
- Respect inheritance chains

### XML
- Keep views minimal and readable
- Use `xpath` properly
- Never duplicate views unnecessarily

### Security
- Always define access rights explicitly
- Do not assume admin-level permissions
- Follow least-privilege principle

---

## Data & Migrations (TO BE COMPLETED)

### Existing Data Model
- Relies on models from the official `l10n_es_edi_tbai` module and invoicing.
- Does not introduce new models (to be confirmed).

### Migrations
- No migrations defined so far (to be confirmed).

---

## Integrations & Dependencies (TO BE COMPLETED)

### Internal Dependencies
- `l10n_es_edi_tbai` (Odoo official TicketBAI module).

### External Systems
- TicketBAI / Hacienda Foral (Bizkaia / Basque Country), via the official module.

---

## Testing & Quality (TO BE COMPLETED)

### Tests
- No specific tests documented (to be confirmed).

### CI / Linting
- Follow OCA expectations; CI/linting pending confirmation.

---

## How the Agent Should Work

The agent should:
1. Read this file entirely
2. Analyze existing code before proposing changes
3. Ask for clarification if requirements are ambiguous
4. Minimize changes
5. Respect existing patterns

If something is unclear, **ask before acting**.

---

## Forbidden Assumptions

The agent must NOT assume:
- That missing code is intentional
- That refactoring is always welcome
- That newer Odoo APIs can replace older ones
- That performance optimizations are needed

---

## Final Notes (TO BE COMPLETED)

<!--
Any extra constraints, warnings, or project-specific rules.
-->
