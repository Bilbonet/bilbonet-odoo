This module extends sales commissions to support commercial zones.

Commercial zones can be configured with one or more zone agents and assigned
to countries' states or provinces. When a state or province is selected on a
contact, the contact's commercial zone is filled from that state or province
unless a zone is explicitly set.

When a sales order is created for a customer assigned to a commercial zone,
the agents of that zone are added to the sales order line commissions together
with the standard agents provided by `sale_commission_oca`.
