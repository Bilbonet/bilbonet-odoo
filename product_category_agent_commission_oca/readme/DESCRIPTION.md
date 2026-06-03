This module extends OCA sales commissions to support product manager
commissions based on the product category of each sale order line.

Product categories can be configured with one or more commission agents. When a
product is added to a sale order, the agents configured on its category are
added to the sale order line commissions together with the standard agents
provided by `sale_commission_oca`.

Category agents are not duplicated if the same agent is already present on the
sale order line through another commission rule.
