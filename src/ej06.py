#  Calculadora de precio sin IVA reducido
#
#

pref = int(input("Introduce el precio con IVA de tu articulo: "))

presi = pref / 1.1

iva = str(pref - presi)

presi = str(presi)

print("El precio del artículo sin IVA es de " + presi + " euros y el IVA que se ha pagado son " + iva + " euros." )