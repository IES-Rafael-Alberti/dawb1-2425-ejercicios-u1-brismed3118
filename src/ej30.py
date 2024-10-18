#
#
#

def division_num(num:int) -> bool:

    i = 1
    multi = 1

    for i in range (1,num):
        multi = multi * i

    resto = (multi + 1) % num

    if resto == 0:
        return True
    else:
        return False

def main():

    num = int(input("> "))

    if division_num(num) == True:
        print(f"El número {num} es primo")

    else:
        print(f"El número {num} no es primo")



if __name__ == "__main__":
    main()