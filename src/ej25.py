#   Fecha nacimiento
#
#

nacimiento = input("Introduce el día de tu nacimiento en formato dd/mm/aaaa: ")

dia, mes, año =  nacimiento.split("/")

print(f"Naciste el {dia} en el mes {mes} del año {año}")