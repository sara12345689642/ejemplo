import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip

class Registro():
    def mostrarAyuda(self, event):
        messagebox.showinfo("Ayuda", "Debe diligenciar todos los campos marcados con '*',\n luego presione el boton registrarse")

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.resizable(0,0)
        self.ventana.config(width=275, height=225)


        self.lblTitulo= tk.Label(self.ventana, text= "Registrarse", fg="blue")
        self.lblTitulo.place(relx=0.5, y=65, anchor="center")

        iconoAyuda = tk.PhotoImage(file= r"C:\Users\sarac\OneDrive\Escritorio\proyectosPOE\ejemplo\icons\icons\application_edit.png")
        self.btnAyuda=tk.Button(self.ventana, image=iconoAyuda)
        self.btnAyuda.place(relx=1, x=-45, y=25, width=25, height=25 )
        Tooltip(self.btnAyuda, "Presione para obtener ayuda!\nAlt+a")
        self.btnAyuda.bind('<Button-1>', self.mostrarAyuda)
        self.ventana.bind('<Alt-a>', self.mostrarAyuda)

        self.ventana.mainloop()

app= Registro()