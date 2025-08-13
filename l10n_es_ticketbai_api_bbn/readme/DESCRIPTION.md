Este módulo añade las siguientes mejoras en el módulo Ticketbai API:

## Correcciones


### Respuesta factura ticketbai ya registrada
- El envío de las facturas ticketbai puede recibir las siguientes contestacioes:
  - TicketBai (Invoice)
      - 005: Invoice already registered -> mark as sent.
  - AnulaTicketBai (Cancellation)
      - 011: Invoice already registered -> mark as sent.

En estos casos la factura se marca como enviada. Corregimos esto y marcamos la factura como error, para que un responsable revise si la factura esta realmente registrada, o se trata de un error de la aplicación y esta repitiendo números.
