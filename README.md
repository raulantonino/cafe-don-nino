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
  - Cambiar precio de productos
  - Eliminar productos
  - Si un producto fue vendido y luego eliminado, aparece como *Producto eliminado* en el resumen

---

## 🧠 Validaciones implementadas

- Opciones de menú válidas
- Ingreso de números enteros (validación recursiva)
- Confirmaciones s/n
- Control de stock antes de agregar al carrito
- Reposición de stock con valores válidos

---

## 🗂️ Estructura del proyecto

´´´
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
´´´

---

## ▶️ Cómo ejecutar el programa

1. Abrir una terminal en la carpeta raíz del proyecto
2. Ejecutar:

```bash
python main.py

```
---

## 🧪 Ejemplo de uso

- Ingresar al menú Nueva venta
- Agregar uno o más productos
- Finalizar y confirmar la venta
- Revisar Resumen de ventas y Estado de stock

## 👤 Contexto académico

- Proyecto desarrollado como ABP para practicar:
- Estructuras de datos (listas y diccionarios)
- Control de flujo
- Funciones con parámetros y retorno
- Recursividad
- Modularización y buenas prácticas de orden