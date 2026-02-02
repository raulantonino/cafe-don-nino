# Café Don Nino — Sistema de Gestión (Python)

Proyecto de consola en Python para la cafetería ficticia **Café Don Nino**.  
Permite gestionar productos, registrar ventas (incluyendo combos con descuento), controlar stock y obtener reportes de ventas y stock durante la sesión.

> Este sistema funciona solo durante la sesión. Al cerrar el programa, los datos vuelven a su estado inicial.

---

## 🎯 Objetivo del proyecto
Desarrollar un sistema simple por consola que permita:
- Gestionar productos de una cafetería
- Registrar ventas con validaciones
- Aplicar combos con descuento
- Controlar stock y alertas de stock bajo
- Visualizar reportes de ventas y stock

---

## ✅ Funcionalidades
### Menú principal
1. Nueva venta  
2. Carta  
3. Buscar producto  
4. Reponer stock  
5. Estado de stock  
6. Resumen de ventas  
7. Administrar productos  
8. Cerrar turno  

### Detalles importantes
- **Nueva venta**
  - Agregar productos al carrito
  - Agregar combos con descuento fijo (-$300)
  - Validación de stock antes de vender
  - Confirmación de la venta

- **Resumen de ventas**
  - Total vendido en la sesión
  - Detalle de unidades e ingresos por producto
  - Productos con stock bajo

- **Administrar productos**
  - Cambiar precio
  - Eliminar productos
  - Los productos eliminados que ya fueron vendidos aparecen como “Producto eliminado” en el resumen

---

## 🧠 Validaciones implementadas
- Opciones de menú válidas
- Ingreso de números enteros (validación recursiva)
- Confirmaciones s/n
- Control de stock antes de agregar al carrito
- Reposición de stock con valores válidos

---

## 🗂️ Estructura del proyecto
CafeDonNino/
│ main.py
│ README.md
│ .gitignore
└─ modulos/
    │ init.py
    │ datos_basicos.py
    │ validaciones.py
    │ menu.py
    │ gestion_datos.py
    │ reportes.py
    │ funciones_utiles.py

### Responsabilidad de los módulos
- **main.py**: punto de entrada y control del flujo
- **datos_basicos.py**: carga de productos y combos iniciales
- **validaciones.py**: validación de entradas (incluye recursividad)
- **menu.py**: menú principal
- **gestion_datos.py**: lógica de ventas, stock y administración
- **reportes.py**: reportes de stock y ventas
- **funciones_utiles.py**: funciones de impresión y ayuda visual

---

## ▶️ Cómo ejecutar el programa
1. Abrir una terminal en la carpeta raíz del proyecto
2. Ejecutar:

```bash
python main.py

## 🧪 Ejemplo de uso

1. Ingresar al menú **Nueva venta**
2. Agregar uno o más productos
3. Finalizar y confirmar la venta
4. Revisar **Resumen de ventas** y **Estado de stock**


## 👤 Contexto académico

Proyecto desarrollado como ABP para practicar:

- Estructuras de datos (listas y diccionarios)
- Control de flujo
- Funciones con parámetros y retorno
- Recursividad
- Modularización y buenas prácticas de orden

---

## ✅ Qué hacer ahora (pasos claros)
1. Abre `README.md`
2. **Borra todo**
3. **Pega el bloque completo de arriba**
4. Guarda el archivo

Luego:

```powershell
git add README.md
git commit -m "Agrega README con documentación del proyecto"
git push