from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QWidget,
    QVBoxLayout, QLabel, QLineEdit, QStackedWidget,
    QScrollArea, QTabWidget, QHBoxLayout, QTableWidget, QTableWidgetItem
)
from PySide6.QtGui import QColor
import sys, Funciones_lentes,Funciones_BD

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lentes")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        self.stack = QStackedWidget()
        self.pagina_anterior = 0 
        self.stack.currentChanged.connect(self.guardar_pagina_anterior)
        self.stack.currentChanged.connect(
        lambda index: Funciones_lentes.guardar_tabla_actual(self.stack, index, self))

        boton_layout = QHBoxLayout()

        btn_pagina1 = QPushButton("ORG BLANCO")
        btn_pagina2 = QPushButton("BLUE")
        btn_pagina3 = QPushButton("BLUE RE")
        btn_pagina4 = QPushButton("ORG AR")
        btn_pagina5 = QPushButton("ORG AR RE")
        btn_pagina6 = QPushButton("ORG PH AR")
        btn_pagina7 = QPushButton("ORG PH RE")
        btn_pagina8 = QPushButton("ANTIAGE")
        btn_pagina9 = QPushButton("ANTIAGE RE")

        self.botones = [
        btn_pagina1, btn_pagina2, btn_pagina3, btn_pagina4, btn_pagina5,
        btn_pagina6, btn_pagina7, btn_pagina8, btn_pagina9]

        for i, boton in enumerate(self.botones):
            boton.clicked.connect(lambda checked, idx=i: Funciones_lentes.cambiar_pagina(self.stack, self.botones, idx))

        Funciones_lentes.cambiar_pagina(self.stack, self.botones, 0)

        btn_pagina1.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        btn_pagina2.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        btn_pagina3.clicked.connect(lambda: self.stack.setCurrentIndex(2))
        btn_pagina4.clicked.connect(lambda: self.stack.setCurrentIndex(3))
        btn_pagina5.clicked.connect(lambda: self.stack.setCurrentIndex(4))
        btn_pagina6.clicked.connect(lambda: self.stack.setCurrentIndex(5))
        btn_pagina7.clicked.connect(lambda: self.stack.setCurrentIndex(6))
        btn_pagina8.clicked.connect(lambda: self.stack.setCurrentIndex(7))
        btn_pagina9.clicked.connect(lambda: self.stack.setCurrentIndex(8))

        boton_layout.addWidget(btn_pagina1)
        boton_layout.addWidget(btn_pagina2)
        boton_layout.addWidget(btn_pagina3)
        boton_layout.addWidget(btn_pagina4)
        boton_layout.addWidget(btn_pagina5)
        boton_layout.addWidget(btn_pagina6)
        boton_layout.addWidget(btn_pagina7)
        boton_layout.addWidget(btn_pagina8)
        boton_layout.addWidget(btn_pagina9)

        #-----------pagina 1-----------#
        pagina1 = QWidget()
        layout1 = QVBoxLayout(pagina1)
        self.tabla1 = QTableWidget(49, 20)

        Funciones_BD.cargar_datos_a_tabla(self.tabla1, "ORG BLANCO")
        
        graduaciones = [0.00, -0.25, -0.50, -0.75, -1.00, -1.25, -1.50, -1.75, -2.00]
        headers = []
        for grado in graduaciones:
            headers.append(f"{grado:+.2f}")
            headers.append("Mínimo") 
        self.tabla1.setColumnCount(len(headers))
        self.tabla1.setHorizontalHeaderLabels(headers)
        etiquetas_filas = [f"{-6.00 + i * 0.25:.2f}" for i in range(49)]
        self.tabla1.setVerticalHeaderLabels(etiquetas_filas)

        self.tabla1.cellChanged.connect(
        lambda fila, columna: Funciones_lentes.actualizar_y_colorear(self.tabla1, "ORG BLANCO", fila, columna))

        layout1.addWidget(self.tabla1)
        self.stack.addWidget(self.tabla1)

        #-----------pagina 2-----------#
        pagina2 = QWidget()
        layout2 = QVBoxLayout(pagina2)
        self.tabla2 = QTableWidget(49, 20)

        Funciones_BD.cargar_datos_a_tabla(self.tabla2, "BLUE")

        graduaciones = [0.00, -0.25, -0.50, -0.75, -1.00, -1.25, -1.50, -1.75, -2.00]
        headers = []
        for grado in graduaciones:
            headers.append(f"{grado:+.2f}")
            headers.append("Mínimo") 
        self.tabla2.setColumnCount(len(headers))
        self.tabla2.setHorizontalHeaderLabels(headers)
        etiquetas_filas = [f"{-6.00 + i * 0.25:.2f}" for i in range(49)]
        self.tabla2.setVerticalHeaderLabels(etiquetas_filas)

        self.tabla2.cellChanged.connect(
        lambda fila, columna: Funciones_lentes.actualizar_y_colorear(self.tabla2, "BLUE", fila, columna))

        layout2.addWidget(self.tabla2)
        self.stack.addWidget(self.tabla2)

        #-----------pagina 3-----------#
        pagina3 = QWidget()
        layout3 = QVBoxLayout(pagina3)
        self.tabla3 = QTableWidget(49, 18)

        Funciones_BD.cargar_datos_a_tabla(self.tabla3, "BLUE RE")
        
        graduaciones = [-2.25, -2.50, -2.75, -3.00, -3.25, -3.50, -3.75, -4.00]
        headers = []
        for grado in graduaciones:
            headers.append(f"{grado:+.2f}")
            headers.append("Mínimo") 
        self.tabla3.setColumnCount(len(headers))
        self.tabla3.setHorizontalHeaderLabels(headers)
        etiquetas_filas = [f"{-6.00 + i * 0.25:.2f}" for i in range(49)]
        self.tabla3.setVerticalHeaderLabels(etiquetas_filas)

        self.tabla3.cellChanged.connect(
        lambda fila, columna: Funciones_lentes.actualizar_y_colorear(self.tabla3, "BLUE RE", fila, columna))

        layout3.addWidget(self.tabla3)
        self.stack.addWidget(self.tabla3)
        
        #-----------pagina 4-----------#
        pagina4 = QWidget()
        layout4 = QVBoxLayout(pagina4)
        self.tabla4 = QTableWidget(49, 20)

        Funciones_BD.cargar_datos_a_tabla(self.tabla4, "ORG AR")
        
        graduaciones = [0.00, -0.25, -0.50, -0.75, -1.00, -1.25, -1.50, -1.75, -2.00]
        headers = []
        for grado in graduaciones:
            headers.append(f"{grado:+.2f}")
            headers.append("Mínimo") 
        self.tabla4.setColumnCount(len(headers))
        self.tabla4.setHorizontalHeaderLabels(headers)
        etiquetas_filas = [f"{-6.00 + i * 0.25:.2f}" for i in range(49)]
        self.tabla4.setVerticalHeaderLabels(etiquetas_filas)

        self.tabla4.cellChanged.connect(
        lambda fila, columna: Funciones_lentes.actualizar_y_colorear(self.tabla4, "ORG AR", fila, columna))

        layout4.addWidget(self.tabla4)
        self.stack.addWidget(self.tabla4)

        #-----------pagina 5-----------#
        pagina5 = QWidget()
        layout5 = QVBoxLayout(pagina5)
        self.tabla5 = QTableWidget(49, 18)

        Funciones_BD.cargar_datos_a_tabla(self.tabla5, "ORG AR RE")
        
        graduaciones = [-2.25, -2.50, -2.75, -3.00, -3.25, -3.50, -3.75, -4.00]
        headers = []
        for grado in graduaciones:
            headers.append(f"{grado:+.2f}")
            headers.append("Mínimo") 
        self.tabla5.setColumnCount(len(headers))
        self.tabla5.setHorizontalHeaderLabels(headers)
        etiquetas_filas = [f"{-6.00 + i * 0.25:.2f}" for i in range(49)]
        self.tabla5.setVerticalHeaderLabels(etiquetas_filas)

        self.tabla5.cellChanged.connect(
        lambda fila, columna: Funciones_lentes.actualizar_y_colorear(self.tabla5, "ORG AR RE", fila, columna))

        layout5.addWidget(self.tabla5)
        self.stack.addWidget(self.tabla5)

        #-----------pagina 6-----------#
        pagina6 = QWidget()
        layout6 = QVBoxLayout(pagina6)
        self.tabla6 = QTableWidget(49, 20)

        Funciones_BD.cargar_datos_a_tabla(self.tabla6, "ORG PH AR")

        graduaciones = [0.00, -0.25, -0.50, -0.75, -1.00, -1.25, -1.50, -1.75, -2.00]
        headers = []
        for grado in graduaciones:
            headers.append(f"{grado:+.2f}")
            headers.append("Mínimo") 
        self.tabla6.setColumnCount(len(headers))
        self.tabla6.setHorizontalHeaderLabels(headers)
        etiquetas_filas = [f"{-6.00 + i * 0.25:.2f}" for i in range(49)]
        self.tabla6.setVerticalHeaderLabels(etiquetas_filas)

        self.tabla6.cellChanged.connect(
        lambda fila, columna: Funciones_lentes.actualizar_y_colorear(self.tabla6, "ORG PH AR", fila, columna))

        layout6.addWidget(self.tabla6)
        self.stack.addWidget(self.tabla6)

        #-----------pagina 7-----------#
        pagina7 = QWidget()
        layout7 = QVBoxLayout(pagina7)
        self.tabla7 = QTableWidget(49, 18)

        Funciones_BD.cargar_datos_a_tabla(self.tabla7, "ORG PH ER")
        
        graduaciones = [-2.25, -2.50, -2.75, -3.00, -3.25, -3.50, -3.75, -4.00]
        headers = []
        for grado in graduaciones:
            headers.append(f"{grado:+.2f}")
            headers.append("Mínimo") 
        self.tabla7.setColumnCount(len(headers))
        self.tabla7.setHorizontalHeaderLabels(headers)
        etiquetas_filas = [f"{-6.00 + i * 0.25:.2f}" for i in range(49)]
        self.tabla7.setVerticalHeaderLabels(etiquetas_filas)

        self.tabla7.cellChanged.connect(
        lambda fila, columna: Funciones_lentes.actualizar_y_colorear(self.tabla7, "ORG PH ER", fila, columna))

        layout7.addWidget(self.tabla7)
        self.stack.addWidget(self.tabla7)

        #-----------pagina 8-----------#
        pagina8 = QWidget()
        layout8 = QVBoxLayout(pagina8)
        self.tabla8 = QTableWidget(49, 20)

        Funciones_BD.cargar_datos_a_tabla(self.tabla8, "ANTIAGE")
        
        graduaciones = [0.00, -0.25, -0.50, -0.75, -1.00, -1.25, -1.50, -1.75, -2.00]
        headers = []
        for grado in graduaciones:
            headers.append(f"{grado:+.2f}")
            headers.append("Mínimo") 
        self.tabla8.setColumnCount(len(headers))
        self.tabla8.setHorizontalHeaderLabels(headers)
        etiquetas_filas = [f"{-6.00 + i * 0.25:.2f}" for i in range(49)]
        self.tabla8.setVerticalHeaderLabels(etiquetas_filas)

        self.tabla8.cellChanged.connect(
        lambda fila, columna: Funciones_lentes.actualizar_y_colorear(self.tabla8, "ANTIAGE", fila, columna))

        layout8.addWidget(self.tabla8)
        self.stack.addWidget(self.tabla8)

        #-----------pagina 9-----------#
        pagina9 = QWidget()
        layout9 = QVBoxLayout(pagina9)
        self.tabla9 = QTableWidget(49, 18)

        Funciones_BD.cargar_datos_a_tabla(self.tabla9, "ANTIAGE RE")

        graduaciones = [-2.25, -2.50, -2.75, -3.00, -3.25, -3.50, -3.75, -4.00]
        headers = []
        for grado in graduaciones:
            headers.append(f"{grado:+.2f}")
            headers.append("Mínimo") 
        self.tabla9.setColumnCount(len(headers))
        self.tabla9.setHorizontalHeaderLabels(headers)
        etiquetas_filas = [f"{-6.00 + i * 0.25:.2f}" for i in range(49)]
        self.tabla9.setVerticalHeaderLabels(etiquetas_filas)

        self.tabla9.cellChanged.connect(
        lambda fila, columna: Funciones_lentes.actualizar_y_colorear(self.tabla9, "ANTIAGE RE", fila, columna))

        layout9.addWidget(self.tabla9)
        self.stack.addWidget(self.tabla9)

        main_layout.addLayout(boton_layout)
        main_layout.addWidget(self.stack)

        self.tablas = [
            self.tabla1, self.tabla2, self.tabla3,
            self.tabla4, self.tabla5, self.tabla6,
            self.tabla7, self.tabla8, self.tabla9
        ]

        self.nombres = ["ORG BLANCO", "BLUE", "BLUE RE","ORG AR", "ORG AR RE", "ORG PH AR", "ORG PH RE", "ANTIAGE", "ANTIAGE RE"]

        for tabla in self.tablas:
            Funciones_lentes.actualizar_colores(tabla)

    def guardar_pagina_anterior(self, index_nuevo):

        if self.pagina_anterior == 0:
            Funciones_lentes.guardar_tabla_completa(self.tabla1, "ORG BLANCO")
        elif self.pagina_anterior == 1:
            Funciones_lentes.guardar_tabla_completa(self.tabla2, "BLUE")
        elif self.pagina_anterior == 2:
            Funciones_lentes.guardar_tabla_completa(self.tabla3, "BLUE RE")
        elif self.pagina_anterior == 3:
            Funciones_lentes.guardar_tabla_completa(self.tabla4, "ORG AR")
        elif self.pagina_anterior == 4:
            Funciones_lentes.guardar_tabla_completa(self.tabla5, "ORG AR RE")
        elif self.pagina_anterior == 5:
            Funciones_lentes.guardar_tabla_completa(self.tabla6, "ORG PH AR")
        elif self.pagina_anterior == 6:
            Funciones_lentes.guardar_tabla_completa(self.tabla7, "ORG PH RE")
        elif self.pagina_anterior == 7:
            Funciones_lentes.guardar_tabla_completa(self.tabla8, "ANTIAGE")
        elif self.pagina_anterior == 8:
            Funciones_lentes.guardar_tabla_completa(self.tabla9, "ANTIAGE RE")

        self.pagina_anterior = index_nuevo

    def closeEvent(self, event):

        Funciones_lentes.guardar_tabla_completa(self.tabla1, "ORG BLANCO")
        Funciones_lentes.guardar_tabla_completa(self.tabla2, "BLUE")
        Funciones_lentes.guardar_tabla_completa(self.tabla3, "BLUE RE")
        Funciones_lentes.guardar_tabla_completa(self.tabla4, "ORG AR")
        Funciones_lentes.guardar_tabla_completa(self.tabla5, "ORG AR RE")
        Funciones_lentes.guardar_tabla_completa(self.tabla6, "ORG PH AR")
        Funciones_lentes.guardar_tabla_completa(self.tabla7, "ORG PH RE")
        Funciones_lentes.guardar_tabla_completa(self.tabla8, "ANTIAGE")
        Funciones_lentes.guardar_tabla_completa(self.tabla9, "ANTIAGE RE")

        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.showMaximized()
    sys.exit(app.exec())