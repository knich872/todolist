while True:
    user_action = input("Enter add, show, edit, complete, or exit: ").strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            print(f"{index + 1} - {todo}")
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            updated_todo = input("Enter the new todo: ")
            todos[number - 1] = updated_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            completed = todos[number - 1].strip('\n')
            print(f"{completed} was removed from the list")

            todos.pop(number - 1)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except IndexError:
            print("There is no todo with that number")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid.")

print('Goodbye!')
