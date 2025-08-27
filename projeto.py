### Projeto Grupo 4
##  - Membros: - Michel , Jessica , Nilson , Stenio , Elaine

print('-=====Projeto To do List-========')

print("""1.Adicionar Tarefas
2.Mostrar Tarefas
3.Marcar como Concluida
4.Remover Tarefas
5.Sair""")
lista_tarefas = []
while True:
    
    escolha_user = int(input('Informe oque quer fazer:'))
    if escolha_user == 1:
        tarefa = input('O que deseja Adicionar ?')
        lista_tarefas.append(tarefa)
        
    if escolha_user == 2:
        print('Tarefas:')
        for i, tarefa in enumerate(lista_tarefas, start=1):
            print(f'{i}. {tarefa}')   
            
    if escolha_user == 3:
        tarefa_concluida = int(input('Informe o numero da tarefa que deseja marcar como concluida:'))
        if 0 < tarefa_concluida <= len(lista_tarefas):
            lista_tarefas[tarefa_concluida - 1] += ' - Concluida'
        else:
            print('Numero invalido')
            
    if escolha_user == 4:
        tarefa_remover = int(input('Informe o numero da tarefa que deseja remover:'))
        if 0 < tarefa_remover <= len(lista_tarefas):
            lista_tarefas.pop(tarefa_remover - 1)
        else:
            print('Numero invalido')
            
    if escolha_user == 5:
        print('Saindo do programa...')
        break   
    