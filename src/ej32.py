#
#
#

def fibonacci(num: int) -> str:

    sucesion = ""
    siguiente = 1
    numero_ant1 = 0
    numero_ant2 = 0

    while numero_ant2 <= num:

        sucesion = str(sucesion) + " " + str(numero_ant2)
        numero_ant2 = siguiente
        siguiente = numero_ant1 + numero_ant2
        numero_ant1 = numero_ant2
               

    return sucesion

def main():
    num = int(input("Dime un número: "))
    print(f"Los números de la sucesión de fibonacci hasta {num} son ->{fibonacci(num)}")

if __name__ == "__main__":
    main()