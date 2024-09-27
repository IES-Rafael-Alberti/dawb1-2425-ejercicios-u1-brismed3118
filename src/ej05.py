#Calculadora de IVA
#
#

print("Hola! Esto es una calculadora de IVA.")

import time
time.sleep(1)

ivag = float(0.21)   #IVA general
ivar = float(0.1)    #IVA reducido
ivas = float(0.04)   #IVA superreducido

precio = float(input("Dime el precio final del artículo sin IVA: "))

iva = str(input("Dime si tu artículo tiene un IVA general, reducido o superreducido: "))


if iva == "general":
    precio = str(precio + (precio * ivag))
    print("El precio final del artículo es de " + precio + " euros.")

elif iva == "reducido":
    precio = str(precio + (precio * ivar))
    print("El precio final del artículo es de " + precio + " euros.")

elif iva == "superreducido":
    precio = str(precio + (precio * ivas))
    print("El precio final del artículo es de " + precio + " euros.")

else:
    print("Lo siento. No existe ese tipo de IVA...")