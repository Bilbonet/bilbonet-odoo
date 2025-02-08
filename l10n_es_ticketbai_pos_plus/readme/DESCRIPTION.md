Este módulo añade las siguientes mejoras en el módulo Ticketbai del POS:

# Correcciones

### Facturas simplificadas rechazadas pero con estado 'enviadas'
- Las facuras ticketbai del POS si dan error al ser enviadas y se rechazan, estas se quedaban en estado  **enviada**.
Al instalar este módulo, se actualizan al estado **error** las facturas ticketbai del POS que tengan una respuesta diferente a **Recibida**. Y por lo tanto han  daddo error.

- Las facuras ticketbai del POS en estado **error** se pueden cancelar y recrear para volver a realizar el envío.


### Respuesta factura ticketbai ya registrada
- El envío de las facturas ticketbai puede recibir las siguientes contestcioes:
  - TicketBai (Invoice)
      - 005: Invoice already registered -> mark as sent.
  - AnulaTicketBai (Cancellation)
      - 011: Invoice already registered -> mark as sent.

En estos casos la factura se marca como enviada. Corregimso esto y marcamos la factura como error para que un responsable revise si la facturaq esta realmente registrada o se trata de un error de la aplicación que esta repitiendo números.


# Mejoras

### Vista formulario facturas ticketba
- Muestrar la orden del POS enlazada con la factura ticketbai.
- Las facturas en estado error añadimos los botones para solo cambiar nel estado a "enviada" o "cancelada".
- Mostramos la respues del envío.
