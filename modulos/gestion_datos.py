"""
Gestión de productos, ventas y stock
"""

from modulos.validaciones import pedir_opcion, pedir_entero, confirmar
from modulos.utiles import mostrar_carta, mostrar_aviso_stock_bajo, pausa


DESCUENTO_ID = -1  # item especial en carrito


def buscar_producto_por_id(productos, pid):
    for p in productos:
        if p["id"] == pid:
            return p
    return None


def buscar_producto_por_nombre(productos, nombre):
    nombre = nombre.strip().lower()
    for p in productos:
        if p["nombre"].lower() == nombre:
            return p
    return None


def agregar_producto_a_carrito(carrito, producto, cantidad):
    # Si ya existe en carrito, suma
    for item in carrito:
        if item["id"] == producto["id"]:
            item["cantidad"] += cantidad
            return
    carrito.append({
        "id": producto["id"],
        "nombre": producto["nombre"],
        "precio": producto["precio"],
        "cantidad": cantidad
    })


def agregar_descuento_combo(carrito, nombre_combo, descuento):
    carrito.append({
        "id": DESCUENTO_ID,
        "nombre": f"Descuento combo: {nombre_combo}",
        "precio": -descuento,
        "cantidad": 1
    })


def calcular_total_carrito(carrito):
    total = 0
    for item in carrito:
        total += item["precio"] * item["cantidad"]
    return max(total, 0)


def mostrar_detalle_venta(carrito, total):
    print("\n=== DETALLE DE VENTA ===")
    for item in carrito:
        subtotal = item["precio"] * item["cantidad"]
        if item["precio"] >= 0:
            print(f"- {item['nombre']} x{item['cantidad']} = ${subtotal}")
        else:
            print(f"- {item['nombre']} = -${abs(subtotal)}")
    print(f"TOTAL: ${total}")


def descontar_stock_por_carrito(productos, carrito):
    for item in carrito:
        if item["id"] == DESCUENTO_ID:
            continue
        p = buscar_producto_por_id(productos, item["id"])
        if p:
            p["stock"] -= item["cantidad"]


def nueva_venta(productos, combos, total_vendido, stock_bajo):
    carrito = []

    while True:
        print("\n=== NUEVA VENTA ===")
        print("1) Agregar producto")
        print("2) Agregar combo (-$300)")
        print("3) Finalizar venta")
        print("4) Cancelar venta")
        op = pedir_opcion("Elige opción: ", {"1", "2", "3", "4"})

        # 1) Producto
        if op == "1":
            mostrar_carta(productos, stock_bajo)

            pid = pedir_entero("ID del producto: ")
            producto = buscar_producto_por_id(productos, pid)
            if not producto:
                print("Producto no encontrado.")
                continue

            cantidad = pedir_entero("Cantidad: ")
            if cantidad <= 0:
                print("Cantidad inválida.")
                continue

            if cantidad > producto["stock"]:
                print(f"Stock insuficiente. Disponible: {producto['stock']}")
                continue

            # Si ya estaba en carrito, verificar que no exceda stock
            cantidad_en_carrito = 0
            for it in carrito:
                if it["id"] == producto["id"]:
                    cantidad_en_carrito = it["cantidad"]
                    break
            if cantidad_en_carrito + cantidad > producto["stock"]:
                print("Stock insuficiente para sumar esa cantidad (considerando el carrito).")
                continue

            agregar_producto_a_carrito(carrito, producto, cantidad)
            print("Producto agregado al carrito.")

        # 2) Combo
        elif op == "2":
            print("\n=== COMBOS ===")
            for i, c in enumerate(combos, start=1):
                print(f"{i}) {c['nombre']} (descuento -${c['descuento']})")

            idx = pedir_entero("Elige combo (número): ")
            if idx < 1 or idx > len(combos):
                print("Combo inválido.")
                continue

            combo = combos[idx - 1]

            # validar stock para todos los items del combo (1 unidad cada uno)
            puede = True
            for pid in combo["items"]:
                p = buscar_producto_por_id(productos, pid)
                if not p or p["stock"] < 1:
                    puede = False
                    break

            if not puede:
                print("No se puede agregar el combo (falta stock de algún producto).")
                continue

            # Agregar 1 unidad de cada producto del combo al carrito
            for pid in combo["items"]:
                p = buscar_producto_por_id(productos, pid)

                # verificar que no exceda stock considerando carrito
                cantidad_en_carrito = 0
                for it in carrito:
                    if it["id"] == p["id"]:
                        cantidad_en_carrito = it["cantidad"]
                        break
                if cantidad_en_carrito + 1 > p["stock"]:
                    print(f"No se puede agregar combo: stock insuficiente de {p['nombre']} considerando el carrito.")
                    puede = False
                    break

            if not puede:
                continue

            for pid in combo["items"]:
                p = buscar_producto_por_id(productos, pid)
                agregar_producto_a_carrito(carrito, p, 1)

            agregar_descuento_combo(carrito, combo["nombre"], combo["descuento"])
            print("Combo agregado al carrito.")

        # 3) Finalizar
        elif op == "3":
            if not carrito:
                print("Carrito vacío. No hay nada que vender.")
                continue

            total = calcular_total_carrito(carrito)
            mostrar_detalle_venta(carrito, total)

            if not confirmar("¿Confirmar venta?"):
                print("Venta cancelada.")
                return total_vendido

            descontar_stock_por_carrito(productos, carrito)
            total_vendido += total

            print("✅ Venta registrada.")

            # Avisos de stock bajo (solo productos reales)
            vistos = set()
            for item in carrito:
                if item["id"] == DESCUENTO_ID:
                    continue
                if item["id"] in vistos:
                    continue
                vistos.add(item["id"])

                p = buscar_producto_por_id(productos, item["id"])
                if p:
                    mostrar_aviso_stock_bajo(p, stock_bajo)

            # ¿Nueva venta o menú?
            print("\n¿Qué deseas hacer ahora?")
            print("1) Nueva venta")
            print("2) Volver al menú")
            sig = pedir_opcion("Elige: ", {"1", "2"})
            if sig == "1":
                carrito = []
                continue
            return total_vendido

        # 4) Cancelar
        elif op == "4":
            print("Venta cancelada.")
            return total_vendido


def buscar_producto_interactivo(productos, stock_bajo):
    while True:
        print("\n=== BUSCAR PRODUCTO ===")
        modo = pedir_opcion("Buscar por: (1) ID  (2) Nombre: ", {"1", "2"})

        if modo == "1":
            pid = pedir_entero("Ingresa ID: ")
            p = buscar_producto_por_id(productos, pid)
        else:
            nombre = input("Ingresa nombre exacto: ")
            p = buscar_producto_por_nombre(productos, nombre)

        if p:
            print("\nProducto encontrado:")
            from modulos.utiles import mostrar_producto
            mostrar_producto(p, marca_stock_bajo=(p["stock"] <= stock_bajo))
            mostrar_aviso_stock_bajo(p, stock_bajo)
        else:
            print("No se encontró el producto.")

        print("\n¿Qué deseas hacer ahora?")
        print("1) Buscar otro")
        print("2) Volver al menú")
        op = pedir_opcion("Elige: ", {"1", "2"})
        if op == "2":
            return


def reponer_stock(productos):
    while True:
        print("\n=== REPONER STOCK ===")
        from modulos.utiles import mostrar_carta
        mostrar_carta(productos, stock_bajo=5)

        pid = pedir_entero("ID del producto a reponer: ")
        p = buscar_producto_por_id(productos, pid)
        if not p:
            print("Producto no encontrado.")
        else:
            cant = pedir_entero("Cantidad a sumar: ")
            if cant <= 0:
                print("Cantidad inválida.")
            else:
                p["stock"] += cant
                print("Stock actualizado:")
                from modulos.utiles import mostrar_producto
                mostrar_producto(p)

        print("\n¿Qué deseas hacer ahora?")
        print("1) Reponer otro")
        print("2) Volver al menú")
        op = pedir_opcion("Elige: ", {"1", "2"})
        if op == "2":
            return
