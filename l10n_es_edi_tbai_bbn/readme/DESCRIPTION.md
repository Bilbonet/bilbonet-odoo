This module extends the official ``l10n_es_edi_tbai`` module with two TicketBAI-specific adjustments.

When the TicketBAI invoice payload contains a ``NoSujeta`` section with ``ImportePorArticulos7_14_Otros``, the module forces the ``nosujeto_causa`` value to ``OT`` instead of the default code inherited from the base implementation.

It also prevents TicketBAI XML EDI documents (format ``es_tbai``) from being added automatically as attachments in the ``Send & Print`` email wizard.
