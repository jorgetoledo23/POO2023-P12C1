class Alumno:
    
    #Constructor
    def __init__(self, rut, nombre, apellido, edad):
        #print("se esta ejecutando el metodo init")
        self.Rut = rut
        self.NombreCompleto = f"{apellido} , {nombre}"
        self.Edad = edad
        self.ListadoNotas = []

    def AgregarNota(self, Nota):
        self.ListadoNotas.append(Nota)

    def VerNotas(self):
        for nota in self.ListadoNotas:
            print(nota)
