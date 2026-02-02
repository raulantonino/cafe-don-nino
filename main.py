from modulos.datos_basicos import cargar_productos_iniciales, cargar_combos

def main():
    productos = cargar_productos_iniciales()
    combos = cargar_combos()

    print("Productos cargados:", len(productos))
    print("Primer producto:", productos[0])
    print("Combos cargados:", len(combos))
    print("Primer combo:", combos[0])

if __name__ == "__main__":
    main()
