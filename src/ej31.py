#
#
#

def divisores() -> str:

    num = int(input("Dime el número del que quieres saber los divisores: "))

    i = 1
    div = ""

    for i in range (i, num + 1):
        comprobar = num % i
        if comprobar == 0:
            div = str(div) + " " + str(i)

    return div

def main():
    print(divisores())

if __name__ == "__main__":
    main()