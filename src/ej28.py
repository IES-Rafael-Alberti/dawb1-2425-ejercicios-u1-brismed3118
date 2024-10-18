#   Función que calcula areas
# 
#

import math

def calcular_area(a: float, b: float, c: float) -> float:
    s = (a + b + c) / 2
    area = math.sqrt(s * ( s - a ) * ( s - b ) * ( s - c ))
    return area

def comprobar_float(valor: str) -> bool:
    if valor.startswith("-"):
        valor = valor[1:]
    
    pos_punto = valor.find(".")
    if pos_punto >= 0:
        valor = valor[:pos_punto] + valor[pos_punto + 1:]
    
    return valor.isdigit()

def introduce_numero(msj: str) -> float:
    valor = input(str).strip().replace(",", ".")

    while not comprobar_float(valor):
        print("\n**ERROR** Número inválido")
        valor = input(str).strip().replace(",", ".")

    return float(valor)
    
def main():
    print("Dame los tres lados del triángulo...")
    lado_a = introduce_numero("Lado 1: ")
    lado_b = introduce_numero("Lado 2: ")
    lado_c = introduce_numero("Lado 3: ")
    area = calcular_area(lado_a, lado_b , lado_c)
    print("El área del triángulo es de con lados ({:.2f}, {:.2f}, {:.2f}) es {:.2f}.".format(lado_a, lado_b, lado_c, area))

if __name__ == "__main__":
    main()