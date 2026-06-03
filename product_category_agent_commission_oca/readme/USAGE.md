To use this module:

- Configure product manager agents on the relevant product categories.
- Create or edit a sale order.
- Add a product whose category has product manager agents configured.
- Open the commission agents of the sale order line to review the generated
  agents and commissions.

When the product of a sale order line changes, the line commissions are
recomputed and the product category agents are updated.

If the same agent is already assigned to the line by another commission rule,
the product category agent line is not added again.
