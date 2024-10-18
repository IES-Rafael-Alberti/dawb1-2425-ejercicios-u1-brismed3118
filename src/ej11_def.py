#       Número sumando todos los números del 1 a él
#
#

def calculo(num: int):
    suma = str((num * (num + 1)) / 2)
    return suma

def main():
    num = int(input("Introduce un numero: "))
    print(calculo(num))

if __name__ == "__main__":
    main()