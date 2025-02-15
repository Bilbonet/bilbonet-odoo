Este módulo añade las siguientes mejoras en el módulo Ticketbai del POS:

# Correcciones

### Facturas simplificadas rechazadas pero con estado 'enviadas'
- Las facuras ticketbai del POS si daban error al ser enviadas y se rechazan, estas se quedaban en estado  **enviada**.
Al instalar este módulo, se actualizan al estado **error** las facturas ticketbai del POS que tengan una respuesta diferente a **Recibida**. Y por lo tanto han  dado error.

- Las facuras ticketbai del POS en estado **error** se pueden cancelar y recrear para volver a realizar el envío.

# Mejoras

### Vista formulario facturas ticketba
- Muestrar la orden del POS enlazada con la factura ticketbai.

