#def evaluaEdad(edad):
#    if edad<0:
#        raise  TypeError("No se permiten edades negativas")
#    if edad<20:
#        return "Eres muy joven"
#    elif edad<40:
#        return "Eres joven"
#    elif edad<65:
#        return "Eres maduro"
#    elif edad<100:
#        return "Cuidate..."
#print(evaluaEdad(15))

import math
def calculaRaiz(num1):
    if num1<0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num1)
    
op1=(int(input("Introduce un numero: ")))

try:
    print(calculaRaiz(op1))
except ValueError as ErrordeNumeroNegativo:
    print(ErrordeNumeroNegativo)

print("Programa terminado")