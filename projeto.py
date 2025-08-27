### Projeto Grupo 4
##  - Membros: - Michel , Jessica , Nilson , Stenio , Elaine

print('-=====Projeto To do List-========')

lista_tarefas = []


while True: ## Enquanto for verdadeiro ele ira se repetir

    print("""1.Adicionar Tarefas
2.Mostrar Tarefas
3.Marcar como Concluida
4.Remover Tarefas
5.Sair""")
   ## mostrar as opçoes ao usuario
    escolha_user = int(input('O que deseja Fazer ?'))
    if escolha_user == 1:
        adicionar = input('O que deseja Adicionar ?') .capitalize()
        lista_tarefas.append(adicionar)
        print(f'Tarefa {adicionar} foi  Adicionada com sucesso')
    elif escolha_user == 2:
        for  listar, tarefa in enumerate(lista_tarefas, start=1):
            print(f'{listar}. {tarefa}')
    elif escolha_user == 3:
        if not lista_tarefas:
            print("Nenhuma tarefa para marcar.")
        else:
        # 1. Mostra a lista inteira primeiro
            print("Qual tarefa você deseja concluir?")
            for i, t in enumerate(lista_tarefas, start=1):
                print(f"{i}. {t}")

        # 2. Depois que a lista acaba, pergunta ao usuário
            numero_tarefa_str = input("Digite o número: ")
            numero_int = int(numero_tarefa_str)
            indice = numero_int - 1
            tarefa_selecionada = lista_tarefas[indice]
            print(f'Sua Tarefa {tarefa_selecionada} foi concluida com Sucesso !')

    elif escolha_user == 4:
        for mostrar , task in enumerate(lista_tarefas,start=1):
            print(f'{mostrar}. {task}')
        remover  = int(input('Qual tarefa voce quer remover'))
        indice_remover = remover - 1
        lista_tarefas.pop(indice_remover)
        print(f'A Tarefa {lista_tarefas[indice_remover]} foi removida com Sucesso !')
        
    elif escolha_user == 5:
        print('------Saindo Programa , até Logo ------')
        break    
        
