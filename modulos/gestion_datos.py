"""
Gestión de productos, ventas y stock
"""

from modulos.validaciones import pedir_opcion, pedir_entero, confirmar
from modulos.utiles import mostrar_carta, mostrar_aviso_stock_bajo


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


def nueva_venta(productos, combos, total_vendido, stock_bajo, ventas_por_producto):
    carrito = []

    while True:
        print("\n=== NUEVA VENTA ===")
        print("1) Agregar producto")
        print("2) Agregar combo (-$300)")
        print("3) Finalizar venta")
        print("4) Cancelar venta")
        op = pedir_opcion("Elige opción: ", {"1", "2", "3", "4"})

        # 1) Agregar producto
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

            # Considerar carrito para no exceder stock
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

        # 2) Agregar combo
        elif op == "2":
            print("\n=== COMBOS ===")
            for i, c in enumerate(combos, start=1):
                print(f"{i}) {c['nombre']} (descuento -${c['descuento']})")

            idx = pedir_entero("Elige combo (número): ")
            if idx < 1 or idx > len(combos):
                print("Combo inválido.")
                continue

            combo = combos[idx - 1]

            # Validar stock mínimo (1 unidad por item)
            for pid in combo["items"]:
                p = buscar_producto_por_id(productos, pid)
                if not p or p["stock"] < 1:
                    print("No se puede agregar el combo (falta stock de algún producto).")
                    break
            else:
                # Validar considerando carrito
                puede = True
                for pid in combo["items"]:
                    p = buscar_producto_por_id(productos, pid)
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

                # Agregar items + descuento
                for pid in combo["items"]:
                    p = buscar_producto_por_id(productos, pid)
                    agregar_producto_a_carrito(carrito, p, 1)

                agregar_descuento_combo(carrito, combo["nombre"], combo["descuento"])
                print("Combo agregado al carrito.")

        # 3) Finalizar venta
        elif op == "3":
            if not carrito:
                print("Carrito vacío. No hay nada que vender.")
                continue

            total = calcular_total_carrito(carrito)
            mostrar_detalle_venta(carrito, total)

            if not confirmar("¿Confirmar venta?"):
                print("Venta cancelada.")
                return total_vendido

            # Descontar stock
            descontar_stock_por_carrito(productos, carrito)

            # Registrar vendido por producto
            for item in carrito:
                if item["id"] == DESCUENTO_ID:
                    continue

                pid = item["id"]
                cantidad = item["cantidad"]
                ingresos = item["precio"] * cantidad

                if pid not in ventas_por_producto:
                    ventas_por_producto[pid] = {"cantidad": 0, "ingresos": 0}
                ventas_por_producto[pid]["cantidad"] += cantidad
                ventas_por_producto[pid]["ingresos"] += ingresos

            total_vendido += total
            print("✅ Venta registrada.")

            # Avisos stock bajo (una vez por producto)
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

            print("\n¿Qué deseas hacer ahora?")
            print("1) Nueva venta")
            print("2) Volver al menú")
            sig = pedir_opcion("Elige: ", {"1", "2"})
            if sig == "1":
                carrito = []
                continue
            return total_vendido

        # 4) Cancelar venta
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


def reponer_stock(productos, stock_bajo):
    while True:
        print("\n=== REPONER STOCK ===")
        mostrar_carta(productos, stock_bajo)

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
                print("✅ Stock actualizado:")
                from modulos.utiles import mostrar_producto
                mostrar_producto(p, marca_stock_bajo=(p["stock"] <= stock_bajo))

        print("\n¿Qué deseas hacer ahora?")
        print("1) Reponer otro")
        print("2) Volver al menú")
        op = pedir_opcion("Elige: ", {"1", "2"})
        if op == "2":
            return


def administrar_productos(productos, ventas_por_producto):
    while True:
        print("\n=== ADMINISTRAR PRODUCTOS ===")
        print("1) Cambiar precio")
        print("2) Eliminar producto")
        print("3) Volver al menú")
        op = pedir_opcion("Elige: ", {"1", "2", "3"})

        if op == "3":
            return

        pid = pedir_entero("ID del producto: ")
        p = buscar_producto_por_id(productos, pid)
        if not p:
            print("Producto no encontrado.")
            continue

        if op == "1":
            nuevo_precio = pedir_entero("Nuevo precio (CLP): ")
            if nuevo_precio <= 0:
                print("Precio inválido.")
                continue
            p["precio"] = nuevo_precio
            print("✅ Precio actualizado.")
            from modulos.utiles import mostrar_producto
            mostrar_producto(p)

        elif op == "2":
            if pid in ventas_por_producto:
                print("⚠ Este producto aparece en el historial de ventas de esta sesión.")
                print("Si lo eliminas, en el resumen aparecerá como 'Producto eliminado'.")

            if not confirmar("¿Seguro que deseas eliminar este producto?"):
                print("Operación cancelada.")
                continue

            productos.remove(p)
            print("✅ Producto eliminado.")
