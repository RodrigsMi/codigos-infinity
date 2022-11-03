salBruto = float(input("Digite o salário bruto:  "))
adicional = input("Tem adicional? (S/N)")
if adicional.upper() == 'S':
    salBruto = salBruto + (salBruto* 10/100)
dependentes = float(input("Informe a quantidade de dependentes: "))
if salBruto-(dependentes*180)<=1000:
    print("Você está isento de dedução do INSS")
    salLiquido = salBruto
elif salBruto-(dependentes*180)<=4000:
    salLiquido = salBruto - (salBruto * 5/100)
else:
    salLiquido = salBruto - (salBruto * 9/100)
print("Salário Líquido (INSS) = R$ ", salLiquido)
if salLiquido<=2000:
    print("Você está isento de dedução IRPF")
elif salLiquido<=5000:
    salLiquido = salLiquido - (salLiquido * 2.5/100)
elif salLiquido<=12000:
    salLiquido = salLiquido - (salLiquido * 11/100)
else:
    salLiquido = salLiquido - (salLiquido * 25/100)
print("Salário Líquido (IRRF) = R$ ", salLiquido)
