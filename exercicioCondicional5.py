""" 5 - Faça um programa que receba um numero inteiro e diga se ele é par ou impar (utilize o operador %). """

num = int(input("Informe um número: "))
# 10 % 3 == 1
# 10 % 4 == 2
if num % 2 == 0:
    print(f"O número {num} é par")
else:
    print(f"O número {num} é ímpar")
