###########Problema 1: Tabuada Interativa######################

num_int = int(input("Digite um número inteiro: "))

for multi in range(1, 11):
    multiplicacao=num_int*multi
    print(f"{num_int} X {multi} = {multiplicacao}")


###########Problema 2: Jogo de Adivinhação######################

import random
numero_secreto = random.randint(1, 100)

palpite=False

while palpite != numero_secreto:
    palpite = int(input("Seu palpite: "))
    
    if palpite == numero_secreto:
        print(f"Parabéns, você acertou!")
    elif palpite < numero_secreto:
        print(f"Muito baixo!")
    else:
        print(f"Muito alto!")