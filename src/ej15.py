#   Calculadora de interés
#
#

capital = float(input("Dime cuanto dinero hay depositada en la cuenta de ahorros: "))

año1 = capital * 1.04
año2 = (año1) * 1.04
año3 = (año2) * 1.04


print("El primer año ganarás " + str(round(año1, 2)) + "€. El segundo ganarás " + str(round(año2, 2)) + "€. Y el tercer año ganarás " + str(round(año3, 2)) + "€.")