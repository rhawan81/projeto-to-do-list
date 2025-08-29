# PROJETO TO DO LIST

tarefas = [] # lista para guardar as tarefas

while True: # mantém o menu repetindo em loop          
    print("\nMENU")  #\n serve para quebrar linhas
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar como concluída")
    print("4 - Remover tarefa")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ") ## peder a opção do usuário

    if opcao == "1":  # adiciona a nova tarefa
        nome = input("Adicionar tarefa: ")
        tarefas.append(nome) # append adiciona o nome no final da lista
        print("Tarefa adicionada.") # confirma que a tarefa foi adicionada

    elif opcao == "2": # lista tarefas
        if tarefas == []: # verifica se a lista está vazia
            print("Nenhuma tarefa.") # se estiver vazia, avisa que não há tarefas
        else:
            print("\nLISTA DE TAREFAS") # se não estiver vazia, lista as tarefas
            for i, nome in enumerate(tarefas, start=1): # enumerate cria uma lista enumerada, start=1 começa a contagem do 1
                print(f"{i}. {nome}") # imprime a lista enumerada e o nome da tarefa

    elif opcao == "3":  # marca como concluída alguma tarefa
        if tarefas == []: # verifica se a lista está vazia
            print("Nenhuma tarefa.") 
        else:
            for i, nome in enumerate(tarefas, start=1): # lista as tarefas numeradas
                print(f"{i}. {nome}") # imprime a lista enumerada e o nome da tarefa
            numero = int(input("Número da tarefa a concluir: ")) # pergunta ao usuário o número da tarefa a concluir
            tarefas[numero-1] = tarefas[numero-1] + " - Concluída" # marca a tarefa como concluída
             # o -1 é para ajustar o índice da lista, pois a contagem do usuário começa em 1 e a do Python em 0
             # o += não funciona aqui, pois ele tenta modificar a string original, o que não é permitido em Python
             # então usamos a atribuição normal com o sinal de = para criar uma nova string
            print("Tarefa concluída.")

    elif opcao == "4":  # remove tarefas
        if tarefas == []: # verifica se a lista está vazia
            print("Nenhuma tarefa.")
        else:
            for i, nome in enumerate(tarefas, start=1): # lista as tarefas numeradas
                print(f"{i}. {nome}")
            numero = int(input("Número da tarefa para remover: "))
            nova_lista = [] # cria uma nova lista vazia
            for i, nome in enumerate(tarefas, start=1):
                if i != numero: # se o número da tarefa for diferente do número escolhido pelo usuário
                    nova_lista = nova_lista + [nome] # adiciona a tarefa na nova lista
            tarefas = nova_lista # substitui a lista original pela nova lista
            print("A tarefa foi removida com sucesso") # confirma que a tarefa foi removida

    elif opcao == "5":  # comando de sair 
        print("Saindo do programa. Até logo!")
        break  # sai do loop e termina o programa

    else:
        print("Opção inválida.") # avisa que a opção é inválida e volta ao menu
