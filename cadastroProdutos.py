nomes = []
precos = []
qts = []
num = int(input("Quantidade de Produtos para cadastrar: "))
for cadastro in range(num):
    print("Digite Cadastro N.", cadastro)
    nomes.append(input("Digite o Nome do Produto: "))
    precos.append(float(input("Digite o preço: ")))
    qts.append(int(input("Digite a Quantidade: ")))
 
for prod in range(len(nomes)):
    print(f"{nomes[prod]} - R$ {precos[prod]} , QT = {qts[prod]}")
