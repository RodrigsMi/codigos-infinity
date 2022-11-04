# Importa as funções aleatórias:
import random as rd

# and => E, or => OU
# AND: Quando for necessário que todas as condições sejam atendidas.
# OR: Quando uma ou mais condições for atendida.

lifePlayer = 5
lifeEnemy = 5

while lifePlayer>0 and lifeEnemy>0:
    # f = Interpolação de String (Texto)
    print(f"Vida do Jogador = {lifePlayer}")
    print(f"Vida do Inimigo = {lifeEnemy}")
    
    action = input("[A]taque ou [D]efesa? ").upper()
    bloke = input("Ação executada por [J]ogador ou [I]nimigo? ").upper()
    # Ternário
    action = "Ataque" if action=='A' else "Defesa"
    
    # Onde a ação acontece!!!
    if action=="Ataque":
        lifes = rd.randint(0, 3)
        
        #Ataque do Jogador
        if bloke=='J':
            print("Ataque do Jogador")
            lifeEnemy -= lifes
            print(f"Inimigo perdeu {lifes} vida(s)!")
            
        else: #Ataque do Inimigo
            print("Ataque do Inimigo")
            lifePlayer -= lifes
            print(f"Jogador perdeu {lifes} vida(s)!")
            
    else: # Relativo a Defesa
        if bloke=='J':
            print("Defesa do Jogador")
        else:
            print("Defesa do Inimigo")
            
            
    pause = input("Pressione qualquer tecla para continuar...")
if lifePlayer<1:
    print("IS DEAD!!")
else:
    print("YOU WON!!")
