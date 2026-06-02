def calcular_iva(precio_base, porcentaje_iva=16):
    """
    Función para calcular el precio total con IVA incluido.
    Por defecto, el IVA es del 16%.
    """
    iva = precio_base * (porcentaje_iva / 100)
    precio_total = precio_base + iva
    return precio_total

# Probando la función
producto_precio = 100
total = calcular_iva(producto_precio)

print(f"El precio base es: ${producto_precio}")
print(f"El total con IVA es: ${total}")