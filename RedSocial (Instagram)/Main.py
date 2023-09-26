from Model import *
import os
os.system("cls")
#Creacion de Cuentas de Usuarios
cr7 = Usuario("elbicho@cr7.com", 38, "Cristiano", "Ronaldo", "1234", "cr7oficial", "1")
messi = Usuario("lmessi@messi.com", 36, "Lionel", "FifaMessi", "1234", "messi", "123")
colocolo = Usuario("colocolo@chile.cl", 30, "Colo Colo", "Colo Colo", "1234", "ColoColoOficial", "1234")

#Acciones
messi.Seguir(cr7)
messi.Seguir(colocolo)
colocolo.Seguir(cr7)
cr7.Seguir(messi)

print("Seguidores de CR7")
cr7.VerSeguidores()
print("Seguidos de CR7")
cr7.VerSeguidos()

print("Seguidores de Messi")
messi.VerSeguidores()
print("Seguidos de Messi")
messi.VerSeguidos()

print("Seguidores de ColoColo")
colocolo.VerSeguidores()
print("Seguidores de Messi")
colocolo.VerSeguidos()

input()