import Funciones_BD
import sqlite3
from PySide6.QtWidgets import QTableWidget
from PySide6.QtGui import QColor

COLOR_ROJO_SUAVE = QColor("#f8d7da")
COLOR_AMARILLO_SUAVE = QColor("#fff3cd")
COLOR_VERDE_SUAVE = QColor("#d4edda")

def actualizar_colores(tablas):
    filas = tablas.rowCount()
    columnas = tablas.columnCount()

    for fila in range(filas):
        for col in range(0, columnas, 2):  
            item_actual = tablas.item(fila, col)
            item_minimo = tablas.item(fila, col + 1)

            if item_actual is None or item_minimo is None:
                continue

            try:
                actual = float(item_actual.text())
                minimo = float(item_minimo.text())
            except ValueError:
                item_actual.setBackground(QColor(255, 255, 255))
                continue

            if actual < minimo:
                item_actual.setBackground(QColor(COLOR_ROJO_SUAVE))
            elif actual == minimo:
                item_actual.setBackground(QColor(COLOR_AMARILLO_SUAVE))
            else:
                item_actual.setBackground(QColor(COLOR_VERDE_SUAVE))


def actualizar_y_colorear(tabla, nombre_tabla_bd, fila, columna):
    tabla.blockSignals(True)
    Funciones_BD.actualizar_bd(tabla, nombre_tabla_bd, fila, columna)
    actualizar_colores(tabla)
    tabla.blockSignals(False)

def cambiar_pagina(stack, botones, indice):
    stack.setCurrentIndex(indice)
    resaltar_boton_activo(botones, indice)

def resaltar_boton_activo(botones, indice_activo):
    for i, boton in enumerate(botones):
        if i == indice_activo:
            boton.setStyleSheet("""
                background-color: #0078d7;
                color: white;
                font-weight: bold;
                border: 2px solid #005a9e;
                border-radius: 5px;
            """)
        else:
            boton.setStyleSheet("")

def guardar_tabla_completa(tabla: QTableWidget, tipo_lente: str, db_path: str = "Stock_lentes.db"):
    conexion = sqlite3.connect(db_path)
    cursor = conexion.cursor()

    for fila in range(tabla.rowCount()):
        for columna in range(tabla.columnCount()):
            item = tabla.item(fila, columna)
            if item is None or item.text().strip() == "":
                valor = None
            else:
                try:
                    valor = float(item.text().strip())
                except ValueError:
                    valor = None  

            cursor.execute("""
                INSERT INTO lentes (tipo_lente, fila, columna, stock)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(tipo_lente, fila, columna)
                DO UPDATE SET stock = excluded.stock;
            """, (tipo_lente, fila, columna, valor))

    conexion.commit()
    conexion.close()

def guardar_tabla_actual(stack, index, ventana):
    
    if index == 0:
        guardar_tabla_completa(ventana.tabla1, "ORG BLANCO")
    elif index == 1:
        guardar_tabla_completa(ventana.tabla2, "BLUE")
    elif index == 2:
        guardar_tabla_completa(ventana.tabla3, "BLUE RE")
    elif index == 3:
        guardar_tabla_completa(ventana.tabla4, "ORG AR")
    elif index == 4:
        guardar_tabla_completa(ventana.tabla5, "ORG AR RE")
    elif index == 5:
        guardar_tabla_completa(ventana.tabla6, "ORG PH AR")
    elif index == 6:
        guardar_tabla_completa(ventana.tabla7, "ORG PH RE")
    elif index == 7:
        guardar_tabla_completa(ventana.tabla8, "ANTIAGE")
    elif index == 8:
        guardar_tabla_completa(ventana.tabla9, "ANTIAGE RE")