from Model import Alumno
import os
from typing import List
listaAlumnos:List[Alumno] = []
while 10>5:
    os.system("cls")
    print("[1] - Ingreso Alumno")
    print("[2] - Listar Alumnos")
    print("[3] - Insertar Nota")
    print("[0] - Salir")
    opcion = input("Cual es tu Opcion: ")
    if(opcion == "1"):
        r = input("Ingresa el Rut del Alumno: ")
        n = input("Ingresa el Nombre del Alumno: ")
        a = input("Ingresa el Apellido del Alumno: ")
        alumno = Alumno(r,n,a)
        listaAlumnos.append(alumno)
        input(alumno.getInfo() + " Guardado!")
    if(opcion == "2"):
        for a in listaAlumnos:
            print(a.getInfo())
        input("Alumnos Listados")
    if(opcion == "3"):
        r = input("Ingresa Rut del Alumno: ")
        alumnoEncontrado = None
        for a in listaAlumnos:
            if(a.Rut == r):
                alumnoEncontrado = a
        
        if(alumnoEncontrado == None):
            input("Alumno No Encontrado!")
        else:
            try:
                nota = int(input("Ingresa la Nota: "))
                alumnoEncontrado.AgregarNota(nota)
            except:
                input("Ocurrio un Error!")
    if(opcion == "4"):
        r = input("Ingresa Rut del Alumno: ")
        alumnoEncontrado = None
        for a in listaAlumnos:
            if(a.Rut == r):
                alumnoEncontrado = a
        
        if(alumnoEncontrado == None):
            input("Alumno No Encontrado!")
        else: 
            alumnoEncontrado.VerNotas()
    
    if(opcion == "0"):
        break