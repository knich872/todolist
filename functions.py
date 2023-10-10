def get_todos(filepath):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def save_todos(filepath, todos_to_save):
    with open(filepath, 'w') as file:
        file.writelines(todos_to_save)
