#Sistema Centro Medico

#Deben transformarse en Class (Clases)
class Usuarios:

    #Atributos
    Rol = None
    Nombre = None
    Password = None
    Email = None
    Id = None
    Area = None
    Telefono = None
    Rut = None

    #Metodos
    def IngresarAlSistema(self, email, password):
        pass



class Doctor:
    Rut = None
    Nombre = None
    Apellidos = None 
    Especiliadad = None
    Correo = None
    Telefono = None

class Paciente:

    def __init__(self):
        pass
    Rut = None
    Nombre = None
    Apellidos = None
    Correo = None
    Telefono = None
    SistemaSalud = None
    Expediente = None

class Hora_Medica:
    """Define el modelo para construir objetos de tipo Hora Medica"""
    #Constructor
    def __init__(self, fecha:str, hora:str, doctor:Doctor, paciente:Paciente):
        self.Fecha = fecha
        self.Hora = hora

        if(not isinstance(doctor, Doctor)):
            raise TypeError("Tipos Incorrectos")
        else:
            self.Doctor = doctor
        if(not isinstance(paciente, Paciente)):
            raise TypeError("Tipos Incorrectos")
        else:
            self.Paciente = paciente

    def getInfo(self):
        """ Metodo que retorna una cadena de texto con la informacion de la Hora Medica"""
        return f"Fecha: {self.Fecha} \nHora: {self.Hora} \nPaciente: {self.Paciente.Nombre} \nDoctor: {self.Doctor.Nombre}"



D1 = Doctor()
D1.Nombre = "Doctor Pedro"

P2 = Paciente()
P2.Nombre = "Paciente Jhon"

Hora1 = Hora_Medica("05/09/2023", "15:30", D1, P2)
#Hora2 = Hora_Medica()


#print(Hora1.Doctor.Nombre)
#print(Hora1.Paciente.Nombre)
print(Hora1.getInfo())


#Bono
#Examenes
#Expediente
#AtencionMedica






#Sistema Ventas

#Sistema Intranet Universidad