def add_task(tasks, name_task):
    task = {"nome": name_task, "completada": False}
    tasks.append(task)
    print(f"Tarefa {name_task} foi adicionada com sucesso!")
    return

tasks = []
while True:
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    choice = input("Digite a sua escolha: ")

    if choice == "1":
        name_task = input("Digite o nome da tarefa que deseja adicionar:")
        add_task(tasks, name_task)
    elif choice == "6":
        break

print("Programa finalizado")