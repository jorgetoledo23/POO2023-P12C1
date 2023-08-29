import os

#Listado de Alumnos y sus Respectivas Evaluaciones

#Class / Clase

from Alumno import Alumno

listaAlumnos = [] # Array

while True:

    os.system('cls')

    print("[1] - Ingresar Alumno")
    print("[2] - Ingresar Nota")
    print("[3] - Ver Notas Alumno")

    opcion = input("Selecciona una Opcion Valida: ")

    if(opcion == "1"):
        os.system('cls')
        rut = input("Ingrese Rut Alumno: ")
        nombre = input("Ingrese Nombre Alumno: ")
        apellido = input("Ingrese Apellido Alumno: ")
        edad = input("Ingrese Edad Alumno: ")

        AlumnoJhon = Alumno(rut, nombre, apellido, edad)

        listaAlumnos.append(AlumnoJhon)

        input("Alumno Ingresado Exitosamente!")


        #opcion = input("Desea seguir ingresando alumnos? (S/N)")

    if(opcion == "2"):
        os.system('cls')
        contador = 1
        for A in listaAlumnos:
            print(f"[{contador}] { A.Rut } { A.NombreCompleto }")
            contador += 1
        op = int(input("Ingresa Numero del Alumno al que deseas Ingresar una Nota: "))
        nota = input("Ingresa la Nota: ")

        listaAlumnos[op - 1].AgregarNota(nota)
        input("Nota Agregada! ")

    if(opcion == "3"):
        os.system('cls')
        contador = 1
        for A in listaAlumnos:
            print(f"[{contador}] { A.Rut } { A.NombreCompleto }")
            contador += 1
        op = int(input("Ingresa Numero del Alumno al que deseas ver sus Notas: "))

        listaAlumnos[op -1].VerNotas()
        input("Notas Listadas!")

    

for A in listaAlumnos:
    print(f"Bienvenido a Programacion Orientada a Objetos { A.NombreCompleto }") #Interpolar Strings
    
    #print("Bienvenido a Programacion Orientada a Objetos" + A.NombreCompleto ) 


