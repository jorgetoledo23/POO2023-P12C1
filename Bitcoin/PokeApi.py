import requests

n = input("Ingresa nombre del Pokemon: ")
mov = input("Ingresa movimiento del Pokemon: ")
r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{n}")
data = r.json()

movimientos = data['moves']
puede = False
for m in movimientos:
    if(m["move"]["name"] == mov):
        puede = True
if(puede):  
    print(f"{n} puede aprender {mov}")
else:
    print(f"{n} no puede aprender {mov}")    



