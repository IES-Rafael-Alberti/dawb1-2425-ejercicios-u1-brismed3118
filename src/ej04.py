#Calculadora grados Cº a grados Fº
#
#

grad = float(input("Introduce la temperatura en grados Celsius: "))

faren = (grad * 1.8) + 32

print("Tus {} grados Celsius equivalen a {:.2f} grados Fahrenheit.".format(grad,faren))
