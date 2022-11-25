''' 7 - Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir
para ler qual acondição de pagamento escolhida e efetuar o cálculo adequado.
Código Condição de pagamento
1 À vista em dinheiro ou cheque, recebe 10% de desconto
2 À vista no cartão de crédito, recebe 15% de desconto
3 Em 2x, preço normal de etiqueta sem juros
4 Em 2x, preço normal de etiqueta mais juros de 10% '''

preco = float(input("Informe o preço do produto: "))
print("Condições de pagamento: ")
print("1 - À vista em dinheiro ou cheque")
print("2 - À vista no cartão de crédito")
print("3 - Em 2x sem juros")
print("4 - Em 2x com juros")
condPag = input("Informe a condição de pagamento: ")

if condPag == "1":
    precoFinal = preco - (preco*(10/100))
    print(f"Você recebeu 10% de desconto e o valor pago foi {precoFinal}!")
elif condPag == "2":
    precoFinal = preco - (preco*(15/100))
    print(f"Você recebeu 15% de desconto e o valor pago foi {precoFinal}!")
elif condPag == "3":
    print(f"O valor pago foi {preco}!")
else:
    precoFinal = preco + (preco*(10/100))
    print(f"Foi acrescido 10% de juros e o valor final foi {precoFinal}")
