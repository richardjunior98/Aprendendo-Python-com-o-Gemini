###########Problema 1: Tabuada Interativa######################

num_int = int(input("Digite um número inteiro: "))

for multi in range(1, 11):
    multiplicacao=num_int*multi
    print(f"{num_int} X {multi} = {multiplicacao}")


###########Problema 2: Jogo de Adivinhação######################

# Versão Aprimorada (Padrão com 'while True' e 'break')
import random
numero_secreto = random.randint(1, 100)

print("--- Jogo de Adivinhação ---")
print("Eu pensei em um número entre 1 e 100. Tente adivinhar!")

while True: # Cria um laço que, a princípio, rodaria para sempre
    palpite = int(input("Seu palpite: "))

    if palpite == numero_secreto:
        print("Parabéns, você acertou!")
        break # A condição de saída foi atingida, então QUEBRAMOS o laço.
    elif palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    else:
        print("Muito alto! Tente novamente.")

# O código continua aqui depois que o 'break' é executado
print("Fim de jogo!")