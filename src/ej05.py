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
    precio = precio + (precio * ivag)
    print("El precio final del artículo es de {:.2f} euros.".format(precio))

elif iva == "reducido":
    precio = precio + (precio * ivar)
    print("El precio final del artículo es de {:.2f} euros.".format(precio))

elif iva == "superreducido":
    precio = precio + (precio * ivas)
    print("El precio final del artículo es de  {:.2f} euros.".format(precio))

else:
    print("Lo siento. No existe ese tipo de IVA...")
    