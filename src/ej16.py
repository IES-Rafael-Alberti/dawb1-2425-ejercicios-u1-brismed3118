#
#
#

barras = int(input("Dime el número de barras vendidas que no son del día: "))
PAN = 3.49 
prect = PAN * barras
desc = prect * 0.6
total = prect - desc

import time
time.sleep(1)

print("El precio habitual de la barra de pan es de " + str(PAN) + "€.")

time.sleep(1)

print("Como no son del día se les hace un descuento del 60%" + " lo que vienen siendo " + str(desc) + "€.")

time.sleep(1)

print("Así que se quedaría en " + str(total) + "€.")