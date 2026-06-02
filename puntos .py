def calcular_iva(precio_base, porcentaje_iva=16):
    """
    Calcula el precio total de un producto sumándole el IVA.
    Por defecto, el porcentaje de IVA es del 16%.
    """
    iva = precio_base * (porcentaje_iva / 100)
    precio_total = precio_base + iva
    return precio_total

# --- PRUEBA DEL PROGRAMA ---
# Definimos el precio de prueba
producto_precio = 100

# Llamamos a la función para obtener el total
total = calcular_iva(producto_precio)

# Mostramos los resultados en la pantalla
print(f"El precio base es: ${producto_precio}")
print(f"El total con IVA es: ${total}")