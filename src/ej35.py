# 
# 
#

def secuencia(num:int, incremento:int, total:int) -> str:

    secuencia = ""
    inicio = num

    
    if num != total:
        for num in range (num, total + 1, incremento):
            if num == inicio:
                secuencia = secuencia + str(num) + "-"

            elif num == total - incremento:
                secuencia = secuencia + str(num) + "-"

            elif num != inicio and num != total:
                secuencia = secuencia + str(num) + "..."

            elif num == total:
                secuencia = secuencia + str(num) 
    else:
        secuencia = num       

    return secuencia

def main():
    num =  int(input("Introduce el número de inicio de la serie: "))
    incremento =  int(input("Introduce los saltos que quieres que haya entre números: "))
    total =  int(input("Introduce hasta que número quieres la serie: "))

    print(secuencia(num, incremento, total))


if __name__ == "__main__":
    main()