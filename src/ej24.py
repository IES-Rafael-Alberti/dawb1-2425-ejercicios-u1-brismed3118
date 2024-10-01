#   Euros y decimales
#
#

precio = round(float(input("Introduce el precio del producto con dos decimales: ")),2)

precio = str(precio)

eur, cent = precio.split(".")

print (f"El precio en euros es: {eur} euros y {cent} céntimos")