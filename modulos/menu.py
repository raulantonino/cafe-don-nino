"""
Menú principal del sistema
"""

from modulos.validaciones import pedir_opcion


def mostrar_menu_principal():
    print("\n==============================")
    print("   Café Don Nino — Menú")
    print("==============================")
    print("1) Nueva venta")
    print("2) Carta")
    print("3) Buscar producto")
    print("4) Reponer stock")
    print("5) Estado de stock")
    print("6) Resumen de ventas")
    print("7) Cerrar turno")

    return pedir_opcion("Elige una opción: ", {"1", "2", "3", "4", "5", "6", "7"})
