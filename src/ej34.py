#
#
#

def edad_rest(edad:int) -> int:
    restante = 125 - edad

    return restante


def comprobar_edad(edad: int) -> bool:

    if edad < 0 or edad > 125:
        return False
    else:
        return True

def comprobar_nom(nombre: str) -> str:

    if nombre == "" or False:
        nombre = "**Desconocido**"
        
    return nombre


def main():
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))

    nombre =  comprobar_nom(nombre)


    while comprobar_edad(edad) == False:
        edad = int(input("**ERROR**, debe ser  un número entre 0 y 125: "))

    print(f"**Te llamas {nombre} y tienes {edad} años, te quedan aún {edad_rest(edad)} años por cumplir**")

    



if __name__ == "__main__":
    main()