public class Doctor {

    public string Rut { get; set; }
    public string Nombre { get; set; }
    public string Especialidad { get; set; }

}

public class Paciente {

    public string Rut { get; set; }
    public string Nombre { get; set; }

}

public class HoraMedica{
    public int CodigoHora { get; set; }
    public Datetime Fecha { get; set; }
    public Doctor Doctor {get ; set;}
    public Paciente Paciente {get; set;}
}