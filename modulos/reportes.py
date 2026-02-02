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


def resumen_ventas(total_vendido, productos, ventas_por_producto, stock_bajo):
    print("\n=== RESUMEN DE VENTAS ===")
    print(f"Total vendido en la sesión: ${total_vendido}")

    print("\n--- Detalle vendido por producto ---")
    if not ventas_por_producto:
        print("Aún no hay ventas registradas.")
    else:
        mapa = {p["id"]: p for p in productos}
        for pid, info in ventas_por_producto.items():
            if pid in mapa:
                nombre = mapa[pid]["nombre"]
            else:
                nombre = f"Producto eliminado (ID {pid})"
            print(f"- {nombre}: {info['cantidad']} unid. | ingresos: ${info['ingresos']}")

    print(f"\n--- Stock bajo (≤ {stock_bajo}) ---")
    hay_stock_bajo = False
    for p in productos:
        if p["stock"] <= stock_bajo:
            hay_stock_bajo = True
            mostrar_producto(p, marca_stock_bajo=True)

    if not hay_stock_bajo:
        print("No hay productos con stock bajo.")

    pausa()
