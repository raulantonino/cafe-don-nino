"""
Sistema de Gestión - Café Don Nino
Menú principal (consola) + flujo del programa
"""

from modulos.datos_basicos import cargar_productos_iniciales, cargar_combos
from modulos.menu import mostrar_menu_principal
from modulos.gestion_datos import nueva_venta, buscar_producto_interactivo, reponer_stock
from modulos.reportes import estado_stock, resumen_ventas
from modulos.validaciones import confirmar


STOCK_BAJO = 5


def main():
    productos = cargar_productos_iniciales()
    combos = cargar_combos()

    total_vendido = 0

    while True:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            total_vendido = nueva_venta(productos, combos, total_vendido, STOCK_BAJO)

        elif opcion == "2":
            # Carta
            from modulos.utiles import mostrar_carta, pausa
            mostrar_carta(productos, STOCK_BAJO)
            pausa()

        elif opcion == "3":
            buscar_producto_interactivo(productos, STOCK_BAJO)

        elif opcion == "4":
            reponer_stock(productos)

        elif opcion == "5":
            estado_stock(productos, STOCK_BAJO)

        elif opcion == "6":
            resumen_ventas(total_vendido)

        elif opcion == "7":
            if confirmar("¿Deseas cerrar turno?"):
                print(f"\nTurno cerrado. Total vendido en la sesión: ${total_vendido}")
                print("¡Hasta luego!\n")
                break


if __name__ == "__main__":
    main()
