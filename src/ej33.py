#
#
#

def numerositer(num1:int, num2:int) -> int:
    entre = 0   

    for num1 in range (num1, num2):
        entre  += 1
        
    return entre


def mayorymenor(num1:int, num2:int) -> int: 
    if num1 > num2:
        return num1
    else:
        return num2

def comprobar_numeros(num1:int, num2:int) -> bool:

    if num1 == num2:
        return False
    else:
        return True
    

def main():
    num1 = int(input("Introduce dos números para saber cuál es menor y cuál es mayor\nIntrodcue el primer número: "))
    num2 = int(input("Introdcue el segundo número: "))

    while comprobar_numeros(num1,num2) == False:
        print("**Los números no pueden ser iguales**")
        num1 = int(input("Introdcue el primer número: "))
        num2 = int(input("Introdcue el segundo número: "))

    print(f"El número mayor es el {mayorymenor(num1,num2)} y entre ellos existen {numerositer(num1,num2)} numeros")

if __name__ == "__main__":
    main()