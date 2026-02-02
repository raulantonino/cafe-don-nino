"""
Funciones útiles de salida (prints) y helpers visuales
"""

def pausa():
    input("\nPresiona Enter para volver al menú...")


def mostrar_producto(p, marca_stock_bajo=False):
    aviso = " ⚠ STOCK BAJO" if marca_stock_bajo else ""
    print(f"[{p['id']}] {p['nombre']} | {p['categoria']} | ${p['precio']} | stock: {p['stock']}{aviso}")


def mostrar_carta(productos, stock_bajo):
    print("\n=== CARTA (Productos) ===")
    for p in productos:
        marca = (p["stock"] <= stock_bajo)
        mostrar_producto(p, marca_stock_bajo=marca)


def mostrar_aviso_stock_bajo(p, stock_bajo):
    if p["stock"] <= stock_bajo:
        print(f"⚠ Te estás quedando sin {p['nombre']} (stock: {p['stock']}). Revisa bodega o haz el pedido.")
