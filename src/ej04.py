#Calculadora grados Cº a grados Fº
#
#

grad = int(input("Introduce la temperatura en grados Celsius: "))

faren = str((grad * 1.8) + 32 )

grad = str(grad)

print("Tus " + grad + " grados Celsius equivalen a " + faren + " grados Fahrenheit.")