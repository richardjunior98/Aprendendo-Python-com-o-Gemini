###########Problema 1: Análise de Risco de Investimento######################

capital_inicial = float(input("Digite o capital inicial (R$): "))
taxa_mensal_percentual = float(input("Digite a taxa de juros mensal (%): "))
tempo_meses = int(input("Digite o número de meses: "))

taxa_mensal_decimal = taxa_mensal_percentual / 100

# Calcula o montante usando a fórmula
montante = capital_inicial * (1 + taxa_mensal_decimal) ** tempo_meses

# Exibe o resultado final formatado
print(f"\nO valor final do investimento será de R$ {montante:.2f}")

if taxa_mensal_percentual < 0.5:
    print(f"Perfil de risco: Conservador.")
elif taxa_mensal_percentual >= 0.5 and taxa_mensal_percentual < 1:
    print(f"Perfil de risco: Moderado.")
else:
    print(f"Perfil de risco: Agressivo.")
    
###########Problema 2: Verificador de Ano Bissexto######################

# Versão Aprimorada do Problema 2
ano = int(input("Digite um ano qualquer d.C.: ")) # Usando int()

# A condição (A e B) ou (C) captura toda a regra em uma linha
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.") # Frase um pouco mais natural