import requests
import os
import time
from babel.numbers import format_currency

#pip install requests
os.system("cls")
while True:
    
    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    datos = request.json()
    data = datos["bpi"]
    dataUSD = data["USD"]
    #valorUSD = dataUSD['rate_float']
    valorUSD = format_currency(float(dataUSD['rate_float']), 'USD', locale='en_US')

    print(f"El Valor actual del BITCOIN en USD es de: {valorUSD}")
    time.sleep(10)
