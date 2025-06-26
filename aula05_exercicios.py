########### Problema 1: A Calculadora de Juros como uma Função ##################
def calcular_montante(capital, taxa_decimal, meses):
    montante=capital*(1+taxa_decimal)**meses
    return montante

capital = float(input("Digite o capital inicial (R$): "))
taxa_decimal = float(input("Digite a taxa de juros mensal (%): "))
meses = int(input("Digite o número de meses: "))

valor=calcular_montante(capital, taxa_decimal, meses)
print(f"\nO valor final do montante será de R$ {valor:.2f}")

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
        
analise=analisar_dados(tempos)
print(analise)