from typing import List
class Alumno:

    def __init__(self, rut, nombre:str, apellido:str):
        self.Rut = rut
        self.Nombre = nombre.title() + " " + apellido.title()
        self.LibroNotas:List[int] = []

    def getInfo(self):
        return f"Alumno Rut: {self.Rut} Nombre: {self.Nombre}"
    
    def AgregarNota(self, nota:int):
        if (not isinstance(nota, int)):
            raise TypeError("La nota debe ser un Entero!")
        self.LibroNotas.append(nota)
        input("Nota Ingresada Correctamente")

    def VerNotas(self):
        for n in self.LibroNotas:
            print(n)
        input("Notas Listadas")

    #Task 1 => Metodo para retornar el Promedio