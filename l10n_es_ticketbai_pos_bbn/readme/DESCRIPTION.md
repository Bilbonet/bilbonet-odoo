Este módulo añade las siguientes mejoras en el módulo Ticketbai del POS:

# Correcciones

### Facturas simplificadas rechazadas pero con estado 'enviadas'

En ocasiones cuando el TPV se queda sin conexión y se siguen realizando ventas, la
numeración de facturas simplificadas es posible que duplique numeros. O en ocasiones
aunque no duplique numeros realice de manera incorrecta las encedenación de facturas
Ticketbai.

Estos errores probocan que al enviar las facturas a Hacienda estas sean rechazadas con
la respuesta:

- **005: (ES): Registro duplicado.(EU): Erregistro bikoiztua.**

El módulo de ticketbai da por enviadas las factursa con esta respuesta, cuando en
realidad no lo están, ya que se trata de errores en la numeración.

Corregimos este comportamiento y ahora se marcan con **error** las facturas rechazadas
con la respuesta con código 005.

> Al instalar este módulo se buscan las facturas de TPV marcadas como enviadas pero que
> tienen respuesta de error y se establecen en estado **error**. De esta forma se pueden
> localizar y reenviar si fuera necesario.

### Cancelar y recrear ventas de TPV

Las ventas de TPV en estado error no se podía realizar la cancelación y recreación para
su reenvio una vez subsanado el problema. Se implementa la función para subsanar este
problema.

Se añaden dos nuevos botones:

- **Establecer Enviada:** La factura está en estado error y no es necesario enviarla por
  alguna razón.
- **Establecer Cancelada:** La fctura está en estado error y se prefiere marcar su
  estado como cancelada por alguna razón.

### Renumerar Facturas Duplicadas

En ocasiones las ventas de TPV enumeran mal las facturas Ticketbai o incluso numeran
bien las factura pero numeran mal la factura en el envío. Por esta razon en ocasiones se
dan numeros de factura duplicados.

Cuando tenemos un numero de factura duplicada, en el envío obtenemos la respuesta [005 -
Registro duplicado].

En el formulario de factutra Ticketbai disponemos de un nuevo botón **Renumerar
Factura**. Este boton cambia el número de factura, añadiendo una **R** al final. De esta
manera corregimos la repetición.

El propio botón de renumerar, cancela el envío y genera un nuevo envío con la nueva
numeración.

# Mejoras

### Vista formulario facturas ticketbai

- Mostramos el campo **nombre**.
- Al acceder a la vista formulario de la Factura Ticketbai ahora muestrar la orden del
  POS enlazada con la factura Ticketbai.
