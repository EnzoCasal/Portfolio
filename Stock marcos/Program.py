import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from sqlite3 import *
from ManejoDB import *
from datetime import datetime
import string

class ConnectorDB:
    def __init__(self,root):
        self.root=root
        self.root.title("Inventario")
        self.root.geometry("900x824+500+50")
        self.root.resizable(width=False, height=False)

        MainFrame=Frame(self.root, bd=10, width=900, height=824, relief=RIDGE, bg='steel blue')
        MainFrame.grid()

        leftFrame=Frame(self.root, bd=10, width=750, height=804, relief=RIDGE)
        leftFrame.grid(row=0,column=0,padx=10, pady=10, sticky=NW)

        rightFrame=Frame(self.root, bd=10, width=130, height=804, relief=RIDGE,)
        rightFrame.grid(row=0, column=0, padx=10, pady=10, sticky=SE)

        treeviewFrame=Frame(self.root, bd=10, width=750, height=624, relief=RIDGE)
        treeviewFrame.grid(row=0,column=0,padx=10, pady=10, sticky=SW)

    #=====================================================Widgets=====================================================#

        self.lblbrand=Label(leftFrame, font=('arial',16, 'bold'), text="Marca",bd=7)
        self.lblbrand.grid(row=0,column=0, sticky=W, padx=5)
        self.entbrand=tk.Entry(leftFrame, font=('arial',12), bd=7, width=81, justify=LEFT, bg='grey90')
        self.entbrand.grid(row=0,column=1,sticky=W, padx=1, pady=7)

        self.lblModel=Label(leftFrame, font=('arial',16, 'bold'), text="Modelo",bd=7)
        self.lblModel.grid(row=1,column=0, sticky=W, padx=5)
        self.entModel=tk.Entry(leftFrame, font=('arial',12), bd=7, width=81, justify=LEFT, bg='grey90')
        self.entModel.grid(row=1,column=1,sticky=W, padx=1, pady=7)

        self.lblColor=Label(leftFrame, font=('arial',16, 'bold'), text="Color",bd=7)
        self.lblColor.grid(row=2,column=0, sticky=W, padx=5)
        self.entColor=tk.Entry(leftFrame, font=('arial',12), bd=7, width=81, justify=LEFT, bg='grey90')
        self.entColor.grid(row=2,column=1,sticky=W, padx=1, pady=7)

        self.lblAmount=Label(leftFrame, font=('arial',16, 'bold'), text="Cantidad",bd=7)
        self.lblAmount.grid(row=3,column=0, sticky=W, padx=5)
        self.entAmount=tk.Entry(leftFrame, font=('arial',12), bd=7, width=81, justify=LEFT, bg='grey90')
        self.entAmount.grid(row=3,column=1,sticky=W, padx=1, pady=7)

        self.lblPrice=Label(leftFrame, font=('arial',16, 'bold'), text="Precio",bd=7)
        self.lblPrice.grid(row=4,column=0, sticky=W, padx=5)
        self.entPrice=tk.Entry(leftFrame, font=('arial',12), bd=7, width=81, justify=LEFT, bg='grey90')
        self.entPrice.grid(row=4,column=1,sticky=W, padx=1, pady=6)

    #=====================================================Variables=====================================================#

        Marca=StringVar()
        Modelo=StringVar()
        Color=StringVar()
        Cantidad=int()

    #=====================================================Table treeview=====================================================#

        scroll_y=Scrollbar(treeviewFrame, orient=VERTICAL)

        self.stock=ttk.Treeview(treeviewFrame, height=25, columns=("id","Marca","Modelo","Color","Cantidad","Precio"), show="headings", displaycolumns=("Marca", "Modelo", "Color", "Cantidad", "Precio"), yscrollcommand=scroll_y.set)
        
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_y.config(command=self.stock.yview)

        self.stock.heading("Marca", text="Marca")
        self.stock.heading("Modelo", text="Modelo")
        self.stock.heading("Color", text="Color")
        self.stock.heading("Cantidad", text="Cantidad")
        self.stock.heading("Precio", text="Precio")
        self.stock.heading("id", text="")

        self.stock['show']='headings'

        self.stock.column("id", width=0, stretch=False)
        self.stock.column('Marca', width=200, anchor="center")
        self.stock.column('Modelo', width=200, anchor="center")
        self.stock.column('Color', width=150, anchor="center")
        self.stock.column('Cantidad', width=63, anchor="center")
        self.stock.column('Precio', width=100, anchor="center")

        self.stock.pack(fill=BOTH, expand=1)

    #=====================================================Buttons=====================================================#

        self.addButton=Button(rightFrame, font=('arial',16, 'bold'), text="Agregar", bd=5, padx=15, pady=2, width=5, height=2, command=self.add).grid(row=0,column=0)
        self.updateButton=Button(rightFrame, font=('arial',16, 'bold'), text="Actualizar", bd=5, padx=15, pady=3, width=5, height=2, command=self.update).grid(row=1,column=0)
        self.sellButton=Button(rightFrame, font=('arial',16, 'bold'), text="Vender", bd=5, padx=15, pady=2, width=5, height=2, command=self.sell).grid(row=2,column=0)
        self.searchNameButton=Button(rightFrame, font=('arial',16, 'bold'), text="Buscar", bd=6, padx=15, pady=2, width=5, height=2, command=self.filter).grid(row=3,column=0)
        self.deleteButton=Button(rightFrame, font=('arial',16, 'bold'), text="Eliminar", bd=6, padx=15, pady=2, width=5, height=2, command=self.delete).grid(row=4,column=0)
        self.recordButton=Button(rightFrame, font=('arial',16, 'bold'), text="Historial\nventas", bd=6, padx=15, pady=2, width=5, height=2, command=self.history).grid(row=5,column=0)
        self.exitButton=Button(rightFrame, font=('arial',16, 'bold'), text="Salir", bd=5, padx=15, pady=2, width=5, height=2, command=self.salir).grid(row=6,column=0)

        #=====================================================Functions=====================================================#

    def add(self):
        brand=self.entbrand.get()
        brand=brand.upper()
        model=self.entModel.get()
        model=model.upper()
        color=self.entColor.get()
        color=color.upper()
        amount=self.entAmount.get()
        amount=amount.upper()
        price=self.entPrice.get()
        price=price.upper()

        if any(field == "" for field in [brand, model, color, amount, price]):
            messagebox.showwarning("Alerta", "Por favor llene todos los campos de información")
            return

        if add_Glasses(brand,model,color,amount,price) > 0:
            messagebox.showerror("Error de carga","Esta intentando cargar un elemento que ya existe en el stock")
            self.load_treeview(brand,model)
            self.entModel.delete(0, tk.END)
            self.entColor.delete(0, tk.END)
            self.entAmount.delete(0, tk.END)
            self.entPrice.delete(0, tk.END)
            return
        
        self.load_treeview(brand,"")

        self.entModel.delete(0, tk.END)
        self.entColor.delete(0, tk.END)
        self.entAmount.delete(0, tk.END)
        self.entPrice.delete(0, tk.END)

    def salir(self):
        salir=messagebox.askyesno("Cerrar programa","¿Desea salir del programa?")
        if salir > 0:
            self.root.destroy()
            return

    def filter(self):
        brand=self.entbrand.get()
        model=self.entModel.get()
        self.load_treeview(brand,model)

    def load_treeview(self,Marca,modelo):
        conn = sql.connect("Anteojos.db")
        cursor = conn.cursor()
            
        for row in self.stock.get_children():
            self.stock.delete(row)

        if Marca=="" and modelo=="":
            cursor.execute("SELECT * FROM Modelos ORDER BY Modelo ASC")
            rows = cursor.fetchall()
        elif modelo=="":
            cursor.execute("SELECT * FROM Modelos WHERE Marca LIKE ? COLLATE NOCASE ORDER BY Modelo ASC",(f"%{Marca}%",))
            rows = cursor.fetchall()
        elif Marca=="":
            cursor.execute("SELECT * FROM Modelos WHERE Modelo LIKE ? COLLATE NOCASE ORDER BY Modelo ASC",(f"%{modelo}%",))
            rows = cursor.fetchall()
        else:
            cursor.execute("SELECT * FROM Modelos WHERE Marca LIKE ? COLLATE NOCASE AND Modelo LIKE ? COLLATE NOCASE ORDER BY Modelo ASC",(f"%{Marca}%", f"%{modelo}%",))
            rows = cursor.fetchall()

        for row in rows:
            self.stock.insert("", "end", values=row)
                
        conn.close()

    def showById(self,id):
        conn = sql.connect("Anteojos.db")
        cursor = conn.cursor()
            
        for row in self.stock.get_children():
            self.stock.delete(row)

        cursor.execute("SELECT * FROM Modelos WHERE id=?", (id))
        row=cursor.fetchall()
        self.stock.insert("", "end", values=row)

        conn.close()

    def update(self):
        seleccion = self.stock.selection()
        auxprice=self.entPrice.get()
        auxamount=self.entAmount.get()

        if not seleccion:
            messagebox.showwarning("Alerta","Por favor seleccione un elemento de la lista para actualizar")
            return

        if seleccion:
            item = self.stock.item(seleccion[0])
            valores = item["values"]

            if auxprice=="" and auxamount=="":
                messagebox.showwarning("Alerta","Por favor ingrese una cantidad o precio a actualizar")
                return

            if auxamount=="":
                update_price(valores[0],auxprice)
                self.entAmount.delete(0, tk.END)
                self.entPrice.delete(0, tk.END)
                self.load_treeview(valores[1],"")
                return
            
            if auxprice=="":
                auxamount=int(auxamount)
                update_amount(valores[0],auxamount)
                self.entAmount.delete(0, tk.END)
                self.entPrice.delete(0, tk.END)
                self.load_treeview(valores[1],"")
                return
               
            auxamount=int(auxamount)   
            update_price(valores[0],auxprice)
            update_amount(valores[0],auxamount)
            self.entAmount.delete(0, tk.END)
            self.entPrice.delete(0, tk.END)
            self.load_treeview(valores[1],"")
            return

    def delete(self):
        seleccion=self.stock.selection()
        if not seleccion:
            messagebox.showwarning("Alerta","Por favor seleccione un elemento de la lista para borrar")
            return
        
        borrar=messagebox.askyesno("Borrar","¿Esta seguro que desea eliminar el elemento seleccionado?")
        if borrar > 0:
            item=self.stock.item(seleccion[0])
            valores = item["values"]
            delete(valores[0])
            self.load_treeview("","")
            return

    def sell(self):
        seleccion=self.stock.selection()
        if not seleccion:
            messagebox.showwarning("Alerta","Por favor seleccione el elemento de la lista que haya vendido")
            return
        
        item=self.stock.item(seleccion[0])
        valores = item["values"]
        vendidos=self.entAmount.get()
        if vendidos == "":
            messagebox.showwarning("Alerta","Por favor ingrese la cantidad de unidades vendidas")
            return
        
        vendidos=int(vendidos)
        if vendidos<0:
            messagebox.showwarning("Alerta","Por favor ingrese un numero positivo")
            return

        if valores[4] < vendidos:
            messagebox.showwarning("Alerta","Ingreso una cantidad mayor de la que dispone")
            return
        
        sell(valores[0],vendidos)
        valores[4]=vendidos
        update_record(valores[1:])
        self.load_treeview("","")
        self.entAmount.delete(0, tk.END)
        return

    def history(self):
        historial=tk.Toplevel()
        historial.title("Historial")
        historial.geometry("800x725")

        MainFrame=Frame(historial, bd=10, width=700, height=628, relief=RIDGE, bg='steel blue')
        MainFrame.pack(fill=BOTH, expand=1)
        
        scroll_y=Scrollbar(MainFrame, orient=VERTICAL)

        treehistory=ttk.Treeview(MainFrame, height=29, columns=("Marca","Modelo","Color","Cantidad","Precio","Fecha"), yscrollcommand=scroll_y.set)
        
        scroll_y.pack(side=RIGHT, fill=Y)

        treehistory.heading("Marca", text="Marca")
        treehistory.heading("Modelo", text="Modelo")
        treehistory.heading("Color", text="Color")
        treehistory.heading("Cantidad", text="Cantidad")
        treehistory.heading("Precio", text="Precio")
        treehistory.heading("Fecha", text="Fecha")

        treehistory['show']='headings'

        treehistory.column('Marca', width=150, anchor="center")
        treehistory.column('Modelo', width=150, anchor="center")
        treehistory.column('Color', width=100, anchor="center")
        treehistory.column('Cantidad', width=63, anchor="center")
        treehistory.column('Precio', width=100, anchor="center")
        treehistory.column('Fecha', width=100, anchor="center")

        treehistory.pack(fill=BOTH, expand=1)

        conn = sql.connect("Historial.db")
        cursor = conn.cursor()
            
        for row in treehistory.get_children():
            treehistory.delete(row)

        cursor.execute("SELECT * FROM Record ORDER BY Fecha DESC")
        rows = cursor.fetchall()
                
        for row in rows:
            fecha_original=row[5]
            fecha_formateada=datetime.strptime(fecha_original, "%Y/%m/%d").strftime("%d/%m/%Y")

            datos_modificados = row[:5] + (fecha_formateada,) 
            treehistory.insert("", "end", values=datos_modificados)
                
        conn.close()
if __name__ =='__main__':
    createDB()
    root=Tk()
    Application = ConnectorDB(root)
    Application.load_treeview("","")
    root.mainloop()