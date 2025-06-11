nome = "Richard" # Uma string (texto)
idade = 27    # Um integer (número inteiro)
altura = 1.83 # Um float (número com ponto flutuante)
e_aluno = True # Um boolean (verdadeiro ou falso)

print("Olá, mundo!")
print(f"O nome dele é {nome} e ele tem {idade} anos.") # f-string: a forma mais moderna de formatar texto

cidade_natal = input("Qual é a sua cidade natal? ")
print(f"Que legal! Eu gosto de {cidade_natal}.")

ano_nascimento_str = input("Em que ano você nasceu? ")
ano_nascimento = int(ano_nascimento_str) # Converte string para inteiro
idade_calculada = 2025 - ano_nascimento
print(f"Você fará aproximadamente {idade_calculada} anos em 2025.")