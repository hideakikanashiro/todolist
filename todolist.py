def to_do_list():
    lista = []

    while True:
        print ("1: Adicionar uma tarefa;")
        print ("2: Mostrar todas as tarefas;")
        print ("3: Remover uma tarefa;")
        print ("4: Sair.")

        escolher = input ("Digite uma opção: ")

        if escolher == "1":
            tarefa = input("Digite qual a sua tarefa: ")
            lista.append(tarefa)
        
        elif escolher == "2":
            for index, valor in enumerate (lista, 1):
                print (f"Tarefa {index}: {valor}\n")

        elif escolher == "3":
            tarefa = input("Digite qual task deseja deletar.")
            if tarefa in lista:
                lista.remove(tarefa)
            else:
                print ("Não foi encontrado a tarefa digitada. Por favor repita o processo como o nome correto.")

        elif escolher == "4":
            print ("Operação encerrada.")
            break
        else:
            print ("Opção invalida. Repita o processo novamente.")

to_do_list()

