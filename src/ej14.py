#   Peso del paquete de la jugueteria
#
#

npay = int(input("Introduce el número de payasos: "))
nmuñ = int(input("Introduce el número de muñecas: "))

pay = 112
muñ = 75

total = str((npay * pay) + (nmuñ * muñ))

print("El peso total del envio será de: " + total + "g.")