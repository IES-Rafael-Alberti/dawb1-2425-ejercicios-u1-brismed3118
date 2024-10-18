#Calculadora grados Cº a grados Fº
#
#

def calc_temp() -> tuple:
    grad = float(input("Introduce la temperatura en grados Celsius: "))

    faren = (grad * 1.8) + 32
    return grad, faren

def main():
    grad, faren= calc_temp()
    print("Tus {} grados Celsius equivalen a {:.2f} grados Fahrenheit.".format(grad,faren))

if __name__ == "__main__":
    main()