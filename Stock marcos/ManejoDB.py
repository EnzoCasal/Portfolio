import sqlite3 as sql
from datetime import datetime

def createDB():
    conn = sql.connect("Anteojos.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Modelos(
            Marca TEXT,
            Modelo TEXT,
            Color TEXT,       
            Cantidad INTEGER,
            Precio INTEGER,
            UNIQUE (Marca, Modelo, Color)              
            )
        """)
    conn.commit()
    conn.close()

    conn = sql.connect("Historial.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Record(
            Marca TEXT,
            Modelo TEXT,
            Color TEXT,       
            Cantidad INTEGER,
            Precio INTEGER,
            Fecha DATETIME              
            )
        """)
    conn.commit()
    conn.close()

def add_Glasses(marca,modelo,color,cantidad,precio):
    conn = sql.connect("Anteojos.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Modelos (Marca, Modelo, Color, Cantidad, Precio) VALUES (?, ?, ?, ?, ?)", (marca, modelo, color, cantidad, precio))
        conn.commit()
        conn.close()
        return 0
    except sql.IntegrityError:
        conn.close()
        return 1

def update_amount(id,cantidad):
    conn = sql.connect("Anteojos.db")
    cursor = conn.cursor()
    aux = cursor.execute("SELECT Cantidad FROM Modelos WHERE id=?", (id,))
    aux1=aux.fetchone()
    aux1=aux1[0]+cantidad
    cursor.execute("UPDATE Modelos SET Cantidad=? WHERE id=?", (aux1,id))
    conn.commit()
    conn.close()

def update_price(id,precio):
    conn = sql.connect("Anteojos.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE Modelos SET Precio=? WHERE id=?", (precio,id))
    conn.commit()
    conn.close()

def sell(id,cantidad):
    conn = sql.connect("Anteojos.db")
    cursor = conn.cursor()
    aux = cursor.execute("SELECT Cantidad FROM Modelos WHERE id=?", (id,))
    aux1 = aux.fetchone()
    aux1=aux1[0]-cantidad
    cursor.execute("UPDATE Modelos SET Cantidad=? WHERE id=?", (aux1, id))
    conn.commit()
    conn.close()

def delete(id):
    conn = sql.connect("Anteojos.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Modelos WHERE ID=?", (id,))
    conn.commit()
    conn.close()

def update_record(data):
    conn = sql.connect("Historial.db")
    cursor = conn.cursor()
    date=datetime.now().strftime("%Y/%m/%d")
    cursor.execute("INSERT INTO Record VALUES(?, ?, ?, ?, ?, ?)",(*data, date,))
    conn.commit()
    conn.close()
