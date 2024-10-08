#  Con ninguna variable...
#
#

import time

def suma():
    return float(input("Introduce el primer número: ")) + float(input("Introduce el segundo número: ")) + float(input("Introduce el tercer número: "))

def main():
    print("Hola! Esto es una calculadora de 3 números...")
    time.sleep(1)
    print("La suma de los tres números es: {:.2f}".format(suma()))

    

if __name__ == "__main__":
    main()