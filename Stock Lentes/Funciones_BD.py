import sqlite3
import os
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

def actualizar_bd(tabla, tipo_lente, fila, columna):
    stock_item = tabla.item(fila, columna)
    if stock_item is None:
        return

    texto = stock_item.text().strip()

    if texto == "":
        nuevo_valor = None
    else:
        try:
            nuevo_valor = float(texto)
        except ValueError:
            return  

    db_path=os.path.abspath("Stock_lentes.db")
    conexion = sqlite3.connect(db_path)
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO lentes (tipo_lente, fila, columna, stock)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(tipo_lente, fila, columna)
        DO UPDATE SET stock = excluded.stock;
    """, (tipo_lente, fila, columna, nuevo_valor))

    conexion.commit()
    conexion.close()

def cargar_datos_a_tabla(tabla: QTableWidget, tipo_lente: str, db_path: str = "Stock_lentes.db"):

    conexion = sqlite3.connect(db_path)
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT fila, columna, stock FROM lentes
        WHERE tipo_lente = ?
    """, (tipo_lente,))
    datos = cursor.fetchall()

    for fila, columna, stock in datos:
        texto = "" if stock is None else str(stock)
        tabla.setItem(fila, columna, QTableWidgetItem(texto))

    conexion.close()

def guardar_tabla_completa(tabla: QTableWidget, tipo_lente: str, db_path: str = "Stock_lentes.db"):
    
    filas = tabla.rowCount()
    columnas = tabla.columnCount()

    conexion = sqlite3.connect(db_path)
    cursor = conexion.cursor()

    for fila in range(filas):
        for columna in range(columnas):
            item = tabla.item(fila, columna)
            if item is None or item.text().strip() == "":
                valor = None
            else:
                try:
                    valor = float(item.text().strip())
                except ValueError:
                    valor = None  # si no es número válido, lo tratamos como vacío

            cursor.execute("""
                INSERT INTO lentes (tipo_lente, fila, columna, stock)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(tipo_lente, fila, columna)
                DO UPDATE SET stock = excluded.stock;
            """, (tipo_lente, fila, columna, valor))

    conexion.commit()
    conexion.close()