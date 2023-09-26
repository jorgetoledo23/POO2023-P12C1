import datetime

class Usuario:

    def __init__(self, correo, edad, nombre, apellido, clave, nombreusuario, telefono):
        self.Correo = correo
        self.Edad = edad
        self.Nombre = nombre
        self.Username = nombreusuario
        self.Apellido = apellido
        self.Clave = clave
        self.Telefono = telefono
        self.Seguidos = []
        self.Seguidores = []
        self.Posts = []

    def Seguir(self, seguido):
        self.Seguidos.append(seguido)
        seguido.Seguidores.append(self)

    def Postear(self, desc, img, lugar):
        post = Post(self, img, lugar, desc)
        self.Posts.append(post)

    def DarLike():
        pass

    def Comentar():
        pass


class Post:
     
    def __init__(self, user, img, lugar, descripcion ):
        self.Usuario = user
        self.Imagen = img
        self.Ubicacion = lugar
        self.Fecha = datetime.datetime.now()
        self.Descripcion = descripcion
        self.Comentarios = []
        self.Likes = []


class Like:

    def __init__(self, user, post):
        self.Usuario = user
        self.Post = post
        self.Fecha = datetime.datetime.now()