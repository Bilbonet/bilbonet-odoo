This module extends `stock.move` with a read-only related field that takes the
sales line description from `sale.order.line.name`.

In delivery operations on the picking form, it adds that value to the
`Operations` lines (`move_ids_without_package`) as an optional column hidden by
default, so users can show it when they need to compare the warehouse move with
the original sales line description.
