todos = []

while True:
    user_action = input("Enter add, show, edit, complete, or exit: ")

    match user_action.strip():
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for index, todo in enumerate(todos):
                print(f"{index + 1} - {todo}")
        case 'edit':
            for index, todo in enumerate(todos):
                print(f"{index + 1} - {todo}")
            number = int(input("Choose which todo to edit: "))
            updated_todo = input("Enter the new todo: ")
            todos[number - 1] = updated_todo
        case 'complete':
            number = int(input("Choose which todo to edit: "))
            todos.pop(number - 1)
        case 'exit':
            break


print('Goodbye!')
