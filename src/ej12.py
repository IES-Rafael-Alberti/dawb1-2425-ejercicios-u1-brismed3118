#  Calculadora de índice masa corporal
#
#

peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))

masa = str(peso / altura)

print("El índice de masa corporal en kg/m es de: " + masa)