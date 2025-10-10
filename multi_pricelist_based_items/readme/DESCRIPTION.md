This module adds the possibility of calculating pricelist prices based on other pricelists in a specific sequence.

By default, Odoo orders pricelist items based on the following fields:

    * [applied_on, min_quantity desc, categ_id desc, id desc]

However, we cannot set a custom order manually.

This module provides two solutions:

**By drag and drop to reorder pricelist items:**

![Reordering by drag and drop](../static/description/pricelist_example.png)

**By setting sequence numbers manually:**

![Setting sequence manually](../static/description/pricelist_example.png)

This allows for better control over price calculation priority and enables more flexible pricing strategies based on multiple pricelist hierarchies.
