# Issues del taller

## Issue 1: El total del carrito ignora la cantidad

**Descripción**
Al añadir un producto con `quantity` mayor que 1, `Cart.total()` solo cuenta el
precio una vez.

Reproducción:

```python
cart = Cart()
cart.add("café", 2.50, quantity=3)
cart.total()  # devuelve 2.5
```

**Criterios de aceptación**
- El ejemplo anterior devuelve `7.50`.
- El total es la suma de `precio × cantidad` de todos los productos.
- Un carrito vacío sigue devolviendo `0`.
- Los tests existentes siguen pasando.

**Ficheros:** `shop/cart.py`

## Issue 2: Código de descuento WORKSHOP10

**Descripción**
Añadir `apply_discount(total, code)` que aplica un descuento a un total en euros.

**Criterios de aceptación**
- Con el código `WORKSHOP10` se descuenta un 10 % del total: `apply_discount(20.00, "WORKSHOP10")` devuelve `18.00`.
- Cualquier otro código lanza `ValueError`.
- El resultado se redondea a céntimos (redondeo half up, es decir, 0,5 céntimos sube).
- Los totales que recibe son importes en euros con dos decimales como máximo.

**Ficheros:** `shop/discounts.py`

## Issue 3: Formato de precio en español

**Descripción**
`format_price(amount)` debe devolver el precio con formato español: punto como
separador de miles, coma decimal y el sufijo ` €`.

**Criterios de aceptación**
- `format_price(1234.5)` devuelve `"1.234,50 €"`.
- `format_price(0)` devuelve `"0,00 €"`.
- Siempre se muestran dos decimales.
- Los tests existentes que ya no reflejen el formato antiguo se actualizan.

**Ficheros:** `shop/formatting.py`
