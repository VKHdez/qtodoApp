# IMPORTS
from tkinter import *
from tkinter import messagebox, Tk
from task import task

from tkcalendar import DateEntry

import datetime as dt
import os
from pathlib import Path


homeFolder = os.path.expanduser('~')
directory  = homeFolder+'\.qtodo'

def rawTask_conv():
    print('conversion')

def createFolder():
    os.makedirs(directory)

# Load Data
def cargar_Datos():

    if not os.path.exists(directory):
        createFolder()
    else:

        with open(directory+'\list.qtodo', 'rb') as datafile:
            rawTask = datafile.readlines()

            rawTask_conv(rawTask)
            #listbox.insert(END, item)

def guardarDatos():
    task_list

def crearFecha(cadenaFecha):
    return cadenaFecha.split("/")


def nuevaTarea():

    if titulo != "" and fecha != "":

        try:
            mes, dia, anio = crearFecha(fecha.get())
            fecha_termino = dt.datetime(int(anio), int(mes), int(dia))

            if desc != "":
                tarea = task(titulo.get(), dt.datetime.now(), fecha_termino, desc.get("1.0", END))


                print (tarea.__dict__)
                task_list.append( tarea.__dict__ )
                lb.insert(END, tarea.task_title)

            else:

                tarea = task(titulo.get(), dt.datetime.now(), fecha_termino, "N/A")

                task_list.append(tarea.__dict__)
                lb.insert(END, tarea.task_title)

        except Exception as e:
            alert = messagebox.showerror('Formato Incorrecto', 'Formato incorrecto de fecha')
            print(e)


def borrarTarea():
    lb.delete(ANCHOR)


ws = Tk()
ws.geometry('500x520+500+200')
ws.title('QTODO APP')
ws.config(bg='#f7f3ed')
ws.resizable(width=False, height=False)


barra_menu = Menu(ws)
ws.config(menu=barra_menu)

file_menu = Menu(barra_menu, tearoff=0)
file_menu.add_command( label='Guardar', command=guardarDatos)

file_menu.add_separator()

file_menu.add_command( label='Salir', command=ws.destroy)

barra_menu.add_cascade(
    label='Archivo',
    menu=file_menu
)

# -------------------------------------

# task list

task_list = []

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=37,
    height=10,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)

# -----------------
# Campos de datos

titulo = Entry(
    ws,
    font=('arial', 15),
    width=25
)

titulo.pack(pady=10)
titulo.place(x=20, y=310)
titulo.insert(0, 'Titulo')

fecha = DateEntry(
    ws,
    font=('arial', 15),
    selectmode='day',
    width=10
)

#fecha.grid(row=1, column=1, padx=15)
#fecha.pack(pady=10)
fecha.place(x=348, y=310)

desc = Text(
    ws,
    font=('times', 14),
    width=51,
    height=4
)

desc.pack(pady=10)
desc.place(x=20, y=355)
# desc.insert(0,'Descripcion')

# ---------------
# BUTTONS
boton_frame = Frame(ws)
boton_frame.pack(pady=10)
boton_frame.config(bg="#f7f3ed", width=464, height=60)
boton_frame.place(x=20, y=455)

addTarea_btn = Button(
    boton_frame,
    text='Agregar',
    font=('arial', 12),
    bg="#93b89e",
    padx=20,
    pady=15,
    command=nuevaTarea
)

addTarea_btn.pack(fill=BOTH, expand=True, side=LEFT)
addTarea_btn.place(x=110, y=0)

borrarTarea_btn = Button(
    boton_frame,
    text='Borrar',
    font=('arial', 12),
    bg="#ff8b61",
    padx=20,
    pady=15,
    command=borrarTarea
)

borrarTarea_btn.pack(fill=BOTH, expand=True, side=LEFT)
borrarTarea_btn.place(x=230, y=0)

# ---------------
# FRAME SETTINGS

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

lb.pack(side=LEFT, fill=BOTH)

# CARGAR DATOS
cargar_Datos()

ws.mainloop()
