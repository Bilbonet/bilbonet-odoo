# Copyright 2023 Jesus Ramiro <jesus@bilbonet.net>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import operator

from odoo import api, models


class AdvisoryReport(models.AbstractModel):
    _name = "report.account_invoice_report_advisory.advisory_report"
    _description = "Advisory Report"

    def _get_move_data(self, move_ids):
        moves = self.env["account.move"].browse(move_ids)
        move_data = {}
        for move in moves:
            move_data.update(
                {
                    move.id: {
                        "id": move.id,
                        "name": move.name,
                        "date": move.invoice_date,
                        "partner_name": move.partner_id.name,
                        "vat": move.partner_id.vat,
                        "net": move.amount_untaxed,
                        "tax": move.amount_tax,
                        "total": move.amount_total,
                    }
                }
            )
        return move_data

    def _get_tax_data(self, tax_ids):
        taxes = self.env["account.tax"].browse(tax_ids)
        tax_data = {}
        for tax in taxes:
            tax_data.update(
                {
                    tax.id: {
                        "id": tax.id,
                        "name": tax.name,
                        "tax_group_id": tax.tax_group_id.id,
                        "type_tax_use": tax.type_tax_use,
                        "amount_type": tax.amount_type,
                        "tags_ids": tax.invoice_repartition_line_ids.tag_ids.ids,
                    }
                }
            )
        return tax_data

    @api.model
    def _get_tax_report_domain(self, company_id, date_from, date_to, only_posted_moves, journal_ids):
        domain = [
            ("company_id", "=", company_id),
            ("date", ">=", date_from),
            ("date", "<=", date_to),
            ("move_id.journal_id", "in", journal_ids),
            ("tax_line_id", "!=", False),
            ("tax_exigible", "=", True),
        ]
        if only_posted_moves:
            domain += [("move_id.state", "=", "posted")]
        else:
            domain += [("move_id.state", "in", ["posted", "draft"])]
        return domain

    @api.model
    def _get_net_report_domain(self, company_id, date_from, date_to, only_posted_moves, journal_ids):
        domain = [
            ("company_id", "=", company_id),
            ("date", ">=", date_from),
            ("date", "<=", date_to),
            ("move_id.journal_id", "in", journal_ids),
            ("tax_exigible", "=", True),
        ]
        if only_posted_moves:
            domain += [("move_id.state", "=", "posted")]
        else:
            domain += [("move_id.state", "in", ["posted", "draft"])]
        return domain

    def _get_vat_report_data(
        self, company_id, date_from, date_to, only_posted_moves, journal_ids
    ):
        ml_fields = self._get_ml_fields_vat_report()

        tax_domain = self._get_tax_report_domain(
            company_id, date_from, date_to, only_posted_moves, journal_ids
        )
        tax_move_lines = self.env["account.move.line"].search_read(
            domain=tax_domain,
            fields=ml_fields,
            order='journal_id, move_id desc',
        )

        net_domain = self._get_net_report_domain(
            company_id, date_from, date_to, only_posted_moves, journal_ids
        )
        taxed_move_lines = self.env["account.move.line"].search_read(
            domain=net_domain,
            fields=ml_fields,
            order='journal_id, move_id desc',
        )
        taxed_move_lines = list(filter(lambda d: d["tax_ids"], taxed_move_lines))

        vat_data = []
        for tax_move_line in tax_move_lines:
            vat_data.append(
                {
                    "net": 0.0,
                    "tax": tax_move_line["balance"],
                    "tax_line_id": tax_move_line["tax_line_id"][0],
                    "move_id": tax_move_line["move_id"][0],
                }
            )
        for taxed_move_line in taxed_move_lines:
            for tax_id in taxed_move_line["tax_ids"]:
                vat_data.append(
                    {
                        "net": taxed_move_line["balance"],
                        "tax": 0.0,
                        "tax_line_id": tax_id,
                        "move_id": taxed_move_line["move_id"][0],
                    }
                )
        tax_ids = list(map(operator.itemgetter("tax_line_id"), vat_data))
        tax_ids = list(set(tax_ids))
        tax_data = self._get_tax_data(tax_ids)
        return vat_data, tax_data

    def _get_tax_group_data(self, tax_group_ids):
        tax_groups = self.env["account.tax.group"].browse(tax_group_ids)
        tax_group_data = {}
        for tax_group in tax_groups:
            tax_group_data.update(
                {
                    tax_group.id: {
                        "id": tax_group.id,
                        "name": tax_group.name,
                        "code": str(tax_group.sequence),
                    }
                }
            )
        return tax_group_data

    def _get_advisor_report_data(self, vat_report_data, tax_data):
        adv_report = {}
        for tax_move_line in vat_report_data:
            tax_id = tax_move_line["tax_line_id"]
            if tax_data[tax_id]["amount_type"] == "group":
                pass
            else:
                group_move_id = tax_move_line["move_id"]
                if group_move_id not in adv_report.keys():
                    adv_report[group_move_id] = {}
                    adv_report[group_move_id][tax_id] = dict(tax_data[tax_id])
                    adv_report[group_move_id][tax_id].update({"net": 0.0, "tax": 0.0})
                else:
                    if tax_id not in adv_report[group_move_id].keys():
                        adv_report[group_move_id][tax_id] = dict(tax_data[tax_id])
                        adv_report[group_move_id][tax_id].update(
                            {"net": 0.0, "tax": 0.0}
                        )
                adv_report[group_move_id][tax_id]["net"] += tax_move_line["net"]
                adv_report[group_move_id][tax_id]["tax"] += tax_move_line["tax"]

        move_group_data = self._get_move_data(adv_report.keys())
        adv_report_list = []
        for move_id in adv_report.keys():
            adv_report[move_id]["name"] = move_group_data[move_id]["name"]
            adv_report[move_id]["date"] = move_group_data[move_id]["date"]
            adv_report[move_id]["partner_name"] = move_group_data[move_id]["partner_name"]
            adv_report[move_id]["vat"] = move_group_data[move_id]["vat"]
            adv_report[move_id]["net"] = move_group_data[move_id]["net"]
            adv_report[move_id]["tax"] = move_group_data[move_id]["tax"]
            adv_report[move_id]["total"] = move_group_data[move_id]["total"]
            #Tax Lines
            adv_report[move_id]["taxes"] = []
            for tax_id in adv_report[move_id]:
                if isinstance(tax_id, int):
                    adv_report[move_id]["taxes"].append(
                        adv_report[move_id][tax_id]
                    )
            adv_report_list.append(adv_report[move_id])

        return adv_report_list

    def _get_report_values(self, docids, data):
        wizard_id = data["wizard_id"]
        company = self.env["res.company"].browse(data["company_id"])
        company_id = data["company_id"]
        date_from = data["date_from"]
        date_to = data["date_to"]
        only_posted_moves = data["only_posted_moves"]
        journal_ids = data["journal_ids"]
        vat_report_data, tax_data = self._get_vat_report_data(
            company_id, date_from, date_to, only_posted_moves, journal_ids
        )
        adv_report = self._get_advisor_report_data(
                vat_report_data, tax_data
            )

        return {
            "doc_ids": [wizard_id],
            "doc_model": "open.items.report.wizard",
            "docs": self.env["open.items.report.wizard"].browse(wizard_id),
            "company_name": company.display_name,
            "currency_name": company.currency_id.name,
            "date_to": data["date_to"],
            "date_from": data["date_from"],
            "adv_report": adv_report,
        }

    def _get_ml_fields_vat_report(self):
        return [
            "id",
            "move_id",
            "journal_id",
            "balance",
            "tax_line_id",
            "tax_ids",
        ]