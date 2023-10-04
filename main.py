todos = []

while True:
    user_action = input("Enter add, show, edit, or exit: ")

    match user_action.strip():
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                print(item)
        case 'edit':
            print(todos)
            number = int(input("Choose which todo to edit: "))
            updated_todo = input("Enter the new todo: ")
            todos[number -1] = updated_todo
        case 'exit':
            break


print('Goodbye!')
