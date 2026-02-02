"""
Funciones de validación de entrada
"""

def pedir_entero(mensaje):
    """
    Pide un entero (recursivo).
    Acepta positivos y negativos.
    """
    texto = input(mensaje).strip()

    if texto.startswith("-") and texto[1:].isdigit():
        return int(texto)
    if texto.isdigit():
        return int(texto)

    print("⚠ Entrada inválida. Debes ingresar un número entero.")
    return pedir_entero(mensaje)


def pedir_opcion(mensaje, opciones_validas):
    """
    Pide una opción dentro de un conjunto/lista permitido (recursivo).
    Ideal: opciones_validas como set de strings.
    """
    op = input(mensaje).strip()
    if op in opciones_validas:
        return op

    print("⚠ Opción inválida. Intenta nuevamente.")
    return pedir_opcion(mensaje, opciones_validas)


def confirmar(mensaje):
    """
    Pregunta s/n y retorna True/False (recursivo).
    """
    resp = input(f"{mensaje} (s/n): ").strip().lower()
    if resp == "s":
        return True
    if resp == "n":
        return False

    print("⚠ Respuesta inválida. Escribe 's' o 'n'.")
    return confirmar(mensaje)
