#   Lo que vas a ganar en total canijo
#
#

def total(cost: int, horas:int):
    total = cost * horas
    return total

def main():

    horas = int(input("Horas de trabajo: "))
    cost = int(input("Coste por hora: "))
    sueldo = total(horas, cost)

    print(f"Importe total: {sueldo}")

if __name__ == "__main__":
    main()