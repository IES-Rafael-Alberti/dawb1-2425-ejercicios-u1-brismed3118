#   Simplemente el ejercicio 13
#   Calculadoras de números enteros y su resto
#

print("Buenas vamos a hacer una división")

import time
time.sleep(1)

print("Para ello necesito que me des dos números")

time.sleep(1)

n = int(input("Introduce el número que quieres dividir: "))     #   Dividendo
m = int(input("Introduce el número divisor: "))                 #   Divisor
c = str(int(n / m))                                             #   Cociente
r = str(int(n % m))                                             #   Resto

n = str(n)
m = str(m)

print("la división de " + n + " entre " + m + " da un cociente " + c + " y un resto " + r + ".")
