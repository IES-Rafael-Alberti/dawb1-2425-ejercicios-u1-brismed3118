#  Calculadora de precio sin IVA reducido
#
#

pref = float(input("Introduce el precio con IVA de tu articulo: "))

presi = pref / 1.1

iva = pref - presi


print("El precio del artículo sin IVA es de {:.2f} euros y el IVA que se ha pagado son {:.2f} euros.".format(pref,iva) )