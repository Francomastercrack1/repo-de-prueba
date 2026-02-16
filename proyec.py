import mysql.connector
import tkinter as tk 
from tkinter import messagebox


def control_de_error():
    try:
        conexion = mysql.connector.connect(
        host="localhost",user="root",
        database="practica_py",password="francom")

        cursor = conexion.cursor()

        cursor.execute("""
           create table pacientes(
            id_paciente INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(50) NOT NULL,
            edad INT NOT NULL,
            direccion VARCHAR(50),
            fech_naci DATE
            );
        """)
        
        conexion.commit()

        messagebox.showinfo("exito","la conexion fue realizada")

    except mysql.connector.Error as e:
        messagebox.showerror("error",f"la conexion no fue realizada:{e}")

control_de_error()


