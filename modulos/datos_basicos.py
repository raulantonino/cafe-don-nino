"""
Datos base del sistema Café Don Nino
- Productos iniciales
- Combos iniciales
"""

def cargar_productos_iniciales():
    """
    Retorna una lista de productos base.
    Cada producto es un diccionario con:
    id, nombre, categoria, precio, stock
    """
    return [
        {"id": 1, "nombre": "Espresso", "categoria": "Bebidas calientes", "precio": 2300, "stock": 30},
        {"id": 2, "nombre": "Americano", "categoria": "Bebidas calientes", "precio": 2500, "stock": 30},
        {"id": 3, "nombre": "Cortado", "categoria": "Bebidas calientes", "precio": 2700, "stock": 25},
        {"id": 4, "nombre": "Latte", "categoria": "Bebidas calientes", "precio": 3200, "stock": 20},
        {"id": 5, "nombre": "Macchiato", "categoria": "Bebidas calientes", "precio": 2800, "stock": 20},
        {"id": 6, "nombre": "Mocachino", "categoria": "Bebidas calientes", "precio": 3500, "stock": 15},
        {"id": 7, "nombre": "Flat White", "categoria": "Bebidas calientes", "precio": 3200, "stock": 20},

        {"id": 8, "nombre": "Iced Latte", "categoria": "Bebidas frías", "precio": 3700, "stock": 15},
        {"id": 9, "nombre": "Cold Brew", "categoria": "Bebidas frías", "precio": 4000, "stock": 12},

        {"id": 10, "nombre": "Muffin", "categoria": "Pastelería", "precio": 2400, "stock": 10},
        {"id": 11, "nombre": "Croissant", "categoria": "Pastelería", "precio": 2600, "stock": 12},
        {"id": 12, "nombre": "Torta del día", "categoria": "Pastelería", "precio": 3800, "stock": 8},

        {"id": 13, "nombre": "Café grano 250g", "categoria": "Granos y café", "precio": 7900, "stock": 8},
        {"id": 14, "nombre": "Café molido 250g", "categoria": "Granos y café", "precio": 7500, "stock": 8},
    ]


def cargar_combos():
    """
    Retorna una lista de combos base.
    Cada combo es un diccionario con:
    nombre, items (lista de IDs), descuento
    """
    return [
        {"nombre": "Combo Clásico (Americano + Croissant)", "items": [2, 11], "descuento": 300},
        {"nombre": "Combo Dulce (Latte + Muffin)", "items": [4, 10], "descuento": 300},
        {"nombre": "Combo Italiano (Espresso + Torta del día)", "items": [1, 12], "descuento": 300},
    ]
