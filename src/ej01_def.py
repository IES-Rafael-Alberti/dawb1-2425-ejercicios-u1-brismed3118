#   Hola
#
#

def cadena(nombre: str):
    frase = "Hola " + nombre
    return frase

def  main():
    nombre = str(input("Escribe tu nombre: "))
    print(cadena(nombre))

if __name__ == "__main__":
    main()