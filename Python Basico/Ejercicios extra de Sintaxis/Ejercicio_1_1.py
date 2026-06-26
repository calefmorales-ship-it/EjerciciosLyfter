"""Calcular el descuento de un producto, si el precio es menor a 100 el descuento es del % y si es mayor o igual a 100 el descuento es del 10%."""
price_product = float(input("Ingrese el precio del producto: "))
if price_product < 100:
    print('Descuento:', price_product * 0.02)
    final_price = price_product - (price_product * 0.02)
    print('Precio final:', final_price)
else:
    print('Descuento:', price_product * 0.10)
    final_price = price_product - (price_product * 0.10)
    print('Precio final:', final_price)
    