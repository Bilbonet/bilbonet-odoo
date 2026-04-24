To use this module, you need to:

- Open a customer and go to the *Contacts & Addresses* tab.
- Edit or create a child contact with an email address and enable
  *Used like mail for picking*.
- Save the contact and return to the parent partner.
- Check the *Mail Addresses* tab. The marked contact is listed in the
  *Pickings* section.
- Send a delivery order by email with the standard *Send by Email* action.
  The stock delivery template will include the marked picking contacts in
  `partner_to`.

If no picking recipients are configured, the template falls back to the
picking partner when it has an email address, or to its parent partner
otherwise.
