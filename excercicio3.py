# 3 - Faça um programa que receba três numeros (A, B e C), e diga se A + B é maior que C.

numA = int(input("Informe o número A: "))
numB = int(input("Informe o número B: "))
numC = int(input("Informe o número C: "))

if numA+numB>numC:
    print("A + B é maior que C")
elif numA+numB<numC:
    print("C é maior que A + B")
else:
    print("A soma de A + B é igual a C")
