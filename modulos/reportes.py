"""
Reportes del sistema
- Estado de stock (opción 5)
- Resumen de ventas (opción 6)
"""

from modulos.utiles import mostrar_producto, pausa


def estado_stock(productos, stock_bajo):
    print("\n=== ESTADO DE STOCK ===")
    for p in productos:
        mostrar_producto(p, marca_stock_bajo=(p["stock"] <= stock_bajo))
    pausa()


def resumen_ventas(total_vendido):
    print("\n=== RESUMEN DE VENTAS ===")
    print(f"Total vendido en la sesión: ${total_vendido}")
    pausa()
