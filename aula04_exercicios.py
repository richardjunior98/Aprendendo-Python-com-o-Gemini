###########Problema 1: Lista de Tarefas Interativa######################

tarefas = []

while True:
    escolha=int(input(f"O que ele deseja fazer: Adicionar(aperte 1), Remover(aperte 2) ou Sair(aperte 3)? "))
    if escolha==1:
        tarefa_plus=input(f"Digitar a tarefa para adiciona-la à lista: ")
        tarefas.append(tarefa_plus)
        print(f"Item adicionado: {tarefa_plus}")
        print(f"A lista agora tem {len(tarefas)} tarefas.")
        for i, tarefa in enumerate(tarefas):
            print(f"{i+1}. {tarefa}")
    elif escolha == 2:
        if len(tarefas) == 0:
            print("A lista de tarefas está vazia.")
        else:
            num_tarefa_remover = int(input("Digitar o número da tarefa a ser removida: "))
            # Verifica se o número digitado é válido
            if 1 <= num_tarefa_remover <= len(tarefas):
                # Captura o texto da tarefa removida
                tarefa_removida = tarefas.pop(num_tarefa_remover - 1)
                print(f"Tarefa '{tarefa_removida}' foi removida com sucesso.")
            else:
                print("Número de tarefa inválido.")
        for i, tarefa in enumerate(tarefas):
            print(f"{i+1}. {tarefa}")
    elif escolha==3:
        print(f"A lista tem {len(tarefas)} tarefas.")
        for i, tarefa in enumerate(tarefas):
            print(f"{i+1}. {tarefa}")
        break
    
###########Problema 2: Coletor e Analisador de Dados de Otimização######################

# Versão Aprimorada (com try-except)
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

print(f"Número de rodadas= {len(tempos)}.")
print(f"Tempo de execução mais rápido= {min(tempos)}.")
print(f"Tempo de execução mais lento= {max(tempos)}.")
print(f"Soma de todos os tempos= {sum(tempos)}.")
print(f"Tempo médio de execução= {sum(tempos) / len(tempos)}.")