import os
import tkinter as tk
from tkinter import *
from zipfile import ZipFile
from tkinter import messagebox, filedialog

def unzipNavegar():
	vn.unzipArchivoLista= filedialog.askopenfilename(initialdir = "H:\\Users\\jonny\\Desktop")
	vn.unzipEntry.insert("1.0", "Los Siguientes archivos seran descomprimidos\n")
	vn.archivos = os.path.basename(vn.unzipArchivoLista)
	vn.unzipEntry.insert("2.0", vn.archivos+"\n")
	vn.unzipEntry.config(state=DISABLED)

def unzipArchivo():
	#Creando carpeta que el usuario introdujo
	os.makedirs(vn.unzipNombreEntry.get())
	#Abrir el archivo
	with ZipFile(vn.unzipArchivoLista, "r") as UNzip1:
		#Extraer archivo
		UNzip1.extractall(vn.unzipNombreEntry.get())
		#Mostrar aviso
		messagebox.showinfo("Exito", "Archivos descomprimidos exitosamente")


def crearWidgets():
	unzipArchLabel = Label(vn,text= "Archivo para descomprimir: ", bg="steelblue", font= ("", 10, 'bold'))
	unzipArchLabel.grid(row = 0, column= 0, padx=5, pady=5)

	vn.unzipEntry = Text(vn, height= 4, width=45, font=("Arial, 10"))
	vn.unzipEntry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

	unzipBotonNavegar = Button(vn, text="Navegar", height= 2, width=20, command= unzipNavegar)
	unzipBotonNavegar.grid(row=0, column=3, padx=5, pady=5)

	unzipNombreArchLabel = Label(vn,text= "Nombre de la Carpeta: ", bg="steelblue", font= ("", 10, 'bold'))
	unzipNombreArchLabel.grid(row = 1, column= 0, padx=5, pady=5)

	vn.unzipNombreEntry = Entry(vn, width=45, font=('Arial', 10))
	vn.unzipNombreEntry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

	unzipBoton = Button(vn, text="Descomprimir", width= 20, command= unzipArchivo)
	unzipBoton.grid(row=1, column=3, padx=5, pady=5)

vn = tk.Tk()
vn.title("ZipUnzip")
vn.config(background = "steelblue")
crearWidgets()

vn.mainloop()