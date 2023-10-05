while True:
    user_action = input("Enter add, show, edit, complete, or exit: ")

    match user_action.strip():
        case 'add':
            todo = input("Enter a todo: ") + '\n'

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, todo in enumerate(todos):
                todo = todo.strip('\n')
                print(f"{index + 1} - {todo}")
        case 'edit':
            for index, todo in enumerate(todos):
                todo = todo.strip('\n')
                print(f"{index + 1} - {todo}")
            number = int(input("Choose which todo to edit: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            updated_todo = input("Enter the new todo: ")
            todos[number - 1] = updated_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'complete':
            number = int(input("Choose which todo to complete: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            completed = todos[number - 1].strip('\n')
            print(f"{completed} was removed from the list")

            todos.pop(number - 1)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'exit':
            break


print('Goodbye!')
