#    Nombre producto, precio y unidades
#
#

prod = input("Introduce el producto que has comprado: ")
precio = float(input("Ahora dime cuanto ha costado: "))
unidades = float(input("Introduce la cantidad de producto que has comprado: "))

total =  precio * unidades

print("El producto {} ha costado {:09.2f} euros, has comprado {:04.0f} unidades y el total ha sido de {:011.2f}".format(prod,precio,unidades,total))

###SOLUCIONAR POR FAVOR###