########### Problema 1: A Calculadora de Juros como uma Função ##################
def calcular_montante(capital, taxa_decimal, meses):
    montante=capital*(1+taxa_decimal)**meses
    return montante

# Pequeno ajuste na parte principal do script
print("--- Calculadora de Juros ---")
capital_usr = float(input("Digite o capital inicial (R$): "))
taxa_percentual_usr = float(input("Digite a taxa de juros mensal (ex: 0.5 para 0.5%): "))
meses_usr = int(input("Digite o número de meses: "))

# A conversão acontece AQUI, antes de chamar a função
taxa_decimal_calculo = taxa_percentual_usr / 100

# A função é chamada com os dados já tratados
montante_final = calcular_montante(capital_usr, taxa_decimal_calculo, meses_usr)

print(f"\nO valor final do montante será de R$ {montante_final:.2f}")

########### Problema 2: O Analisador de Dados como uma Função ##################
def analisar_dados(lista_de_valores):
    if not lista_de_valores:
        return None
    else:
        total_de_rodadas=len(lista_de_valores)
        valor_minimo=min(lista_de_valores)
        valor_maximo=max(lista_de_valores)
        valor_da_soma=sum(lista_de_valores)
        valor_da_media=sum(lista_de_valores) / len(lista_de_valores)
        return {
                'rodadas': total_de_rodadas,
                'minimo': valor_minimo,
                'maximo': valor_maximo,
                'soma': valor_da_soma,
                'media': valor_da_media
            }

tempos = []
while True:
    entrada = input("Insira um tempo de execução (ou 'fim' para parar): ")

    if entrada.lower() == 'fim':
        break

    try:
        # Tenta converter a entrada para float
        tempo_float = float(entrada)
        tempos.append(tempo_float)
        print(f"Tempo {tempo_float}s adicionado.")
    except ValueError:
        # Se a conversão falhar, avisa o usuário e continua o laço
        print("Entrada inválida. Por favor, digite um número ou 'fim'.")
        
# Na parte principal do script, após o laço:
resultados = analisar_dados(tempos)

# Primeiro, verificamos se a análise foi bem-sucedida
if resultados: # Se 'resultados' não for None
    print("\n--- Análise dos Tempos de Execução ---")
    print(f"Número de Rodadas: {resultados['rodadas']}")
    print(f"Tempo Mínimo: {resultados['minimo']:.2f}s")
    print(f"Tempo Máximo: {resultados['maximo']:.2f}s")
    print(f"Soma Total dos Tempos: {resultados['soma']:.2f}s")
    print(f"Tempo Médio: {resultados['media']:.2f}s")
else:
    print("\nNenhum dado foi inserido para análise.")