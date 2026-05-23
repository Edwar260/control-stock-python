# Problema 3: Auditoría de inventario y reabastecimiento

def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


inventario = [
    ["P101", "Cuadernos", 12, 30],
    ["P102", "Lapiceros", 50, 40],
    ["P103", "Marcadores", 8, 20],
    ["P104", "Borradores", 25, 25],
    ["P105", "Carpetas", 10, 18]
]

print("LISTA DE REABASTECIMIENTO")
print("--------------------------------")

for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    print(f"Artículo: {nombre} | Cantidad a pedir: {cantidad_pedir}")
