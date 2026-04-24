This module enhances Partner management by allowing users to define specific email purposes.
When creating or editing a contact in a Partner form, two checkboxes let you mark the email as used for **sales** or **invoicing**.

![Multi Mail Contact Fomr](static/description/contact_form.png)

Marked contacts are automatically listed under the **Email Addresses** tab in their respective sections and are included by default when sending sales or invoice-related emails.

To use these role-based recipients in a mail template, add the corresponding
expression to the `partner_to` field of the template.

For sales templates, use:

`{{ ','.join(map(str, object.partner_id.mail_addresses_sale.ids)) or object.partner_id.id }}`

For invoice templates, use:

`{{ ','.join(map(str, object.partner_id.mail_addresses_invoice.ids)) or object.partner_id.id }}`

If no role-based recipients are configured, the template falls back to the
main partner.

This module already applies that change to the default templates
`sale.email_template_edi_sale`, `sale.mail_template_sale_confirmation`, and
`account.email_template_edi_invoice`.

![Multi Mail Partner Fomr](static/description/partner_form.png)
