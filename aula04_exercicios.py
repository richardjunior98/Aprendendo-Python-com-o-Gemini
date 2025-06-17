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
    elif escolha==2:
        if len(tarefas)==0:
            print(f"Não há tarefas ainda. Aperte 1 para adicionar alguma ou três para sair.")
        tarefa_minus=int(input(f"Digitar o número da tarefa a ser removida da lista: "))
        tarefas.pop(tarefa_minus-1)
        print(f"Item removido: {tarefa_minus}")
        print(f"A lista agora tem {len(tarefas)} tarefas.")
        for i, tarefa in enumerate(tarefas):
            print(f"{i+1}. {tarefa}")
    elif escolha==3:
        print(f"A lista tem {len(tarefas)} tarefas.")
        for i, tarefa in enumerate(tarefas):
            print(f"{i+1}. {tarefa}")
        break
    
###########Problema 2: Coletor e Analisador de Dados de Otimização######################

tempos = []

while True:
    print("Digite 'fim' para parar!")
    time=input(f"Insira o tempo de execução com até uma casa decimal (usar ponto antes do número decimal): ")
    if time != 'fim':
        tempos.append(float(time))
    else:
        break

print(f"Número de rodadas= {len(tempos)}.")
print(f"Tempo de execução mais rápido= {min(tempos)}.")
print(f"Tempo de execução mais lento= {max(tempos)}.")
print(f"Soma de todos os tempos= {sum(tempos)}.")
print(f"Tempo médio de execução= {sum(tempos) / len(tempos)}.")