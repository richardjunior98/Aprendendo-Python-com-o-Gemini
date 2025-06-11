# Versão Aprimorada do Problema 1
print("### Calculadora de Juros Compostos ###")

capital_inicial = float(input("Digite o capital inicial (R$): "))
taxa_mensal_percentual = float(input("Digite a taxa de juros mensal (%): "))
tempo_meses = int(input("Digite o número de meses: "))

# Converte a taxa para o formato decimal para usar na fórmula
taxa_mensal_decimal = taxa_mensal_percentual / 100

# Calcula o montante usando a fórmula
montante = capital_inicial * (1 + taxa_mensal_decimal) ** tempo_meses

# Exibe o resultado final formatado
print(f"\nO valor final do investimento será de R$ {montante:.2f}")

########### Problema 2: Gerador de Nome de Usuário ##################
nome=input("Primeiro nome do usuário: ")
sobrenome=input("Sobrenome do usuário: ")
ano_nascimento=input("Ano de nascimento do usuário: ")

nome=nome.lower()
sobrenome=sobrenome.lower()

print(f"Sugestão 1 de username: {nome[0:3]+sobrenome[0:3]+ano_nascimento[2:4]}")
print(f"Sugestão 2 de username: {nome[0]+sobrenome+ano_nascimento}")
print(f"Sugestão 3 de username: {nome+sobrenome+ano_nascimento[0:2]}")