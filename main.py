def get_todos():
    with open('todos.txt', 'r') as file:
        todos_local = file.readlines()
    return todos_local


def save_todos(todos_to_save):
    with open('todos.txt', 'w') as file:
        file.writelines(todos_to_save)


while True:
    user_action = input("Enter add, show, edit, complete, or exit: ").strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = get_todos()

        todos.append(todo)

        save_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            print(f"{index + 1} - {todo}")
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            todos = get_todos()

            updated_todo = input("Enter the new todo: ")
            todos[number - 1] = updated_todo + '\n'

            save_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            completed = todos[number - 1].strip('\n')
            print(f"{completed} was removed from the list")

            todos.pop(number - 1)

            save_todos(todos)

        except IndexError:
            print("There is no todo with that number")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid.")

print('Goodbye!')
