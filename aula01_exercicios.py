########### Problema 1: Calculadora Simples de Juros Compostos ##################

nome=input("Nome do cliente: ")
dinheiro=input("Capital inicial, em reais, do usuário (valor em dinheiro para investir): ")
print(f"{nome} investirá {dinheiro} reais no Nosso Banco.")

juros=input("Taxa de juros mensal: ")
juros_float=float(juros)
juros_float=juros_float*100
tempo=input("Número de meses que o dinheiro ficará investido: ")
print(f"O dinheiro ficará investido durante {tempo} meses sob uma taxa de juros de {juros_float}%")

juros_float=juros_float/100
dinheiro_float=float(dinheiro)
tempo_float=float(tempo)
montante=dinheiro_float*(1+juros_float)**tempo_float

print(f"O valor final do investimento será de R$ {montante}")

########### Problema 2: Gerador de Nome de Usuário ##################
nome=input("Primeiro nome do usuário: ")
sobrenome=input("Sobrenome do usuário: ")
ano_nascimento=input("Ano de nascimento do usuário: ")

nome=nome.lower()
sobrenome=sobrenome.lower()

print(f"Sugestão 1 de username: {nome[0:3]+sobrenome[0:3]+ano_nascimento[2:4]}")
print(f"Sugestão 2 de username: {nome[0]+sobrenome+ano_nascimento}")
print(f"Sugestão 3 de username: {nome+sobrenome+ano_nascimento[0:2]}")