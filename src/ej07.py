#   Calculadora que te suma 3 números
#
#

print("Hola! Esto es una calculadora de 3 números...")

import time
time.sleep(1)

num1 = float(input("Introudce el primer número: "))
num2 = float(input("Introudce el segundo número: "))
num3 = float(input("Introudce el tercer número: "))

tot = str(num1 + num2 + num3)

print("La suma total de los 3 números introducidos es " + tot + ".")