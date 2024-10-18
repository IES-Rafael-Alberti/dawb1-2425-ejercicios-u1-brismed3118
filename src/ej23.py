#    Reemplazo correo
#
#

correo = input("Introduce tu correo electrónico: ")
dominio = "@ceu.es"
nombre, antdominio =  correo.split("@")
correonuevo = nombre + dominio

print(correonuevo)