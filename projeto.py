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