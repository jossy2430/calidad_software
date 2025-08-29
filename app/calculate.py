from math import sqrt

def calcular_hipotenusa(cateto1, cateto2):
    hipotenusa = sqrt(cateto1 ** 2 + cateto2 ** 2)
    return hipotenusa

print("resultado es "+str(calcular_hipotenusa(-8,-6)))