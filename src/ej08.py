#  Con solo una variable...
#
#

print("Hola! Esto es una calculadora de 3 números...")

import time
time.sleep(1)

num1 = float(input("Introudce el primer número: "))
num1 = num1 + float(input("Introudce el segundo número: "))
num1 = num1 + float(input("Introudce el tercer número: "))

print("La suma total de los 3 números introducidos es {:.2f}.".format(num1))