import functions
import PySimpleGUI
import time

PySimpleGUI.theme('TealMono')
clock = PySimpleGUI.Text('', key='clock')
label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter todo", key='todo')
add_button = PySimpleGUI.Button('Add')
list_box = PySimpleGUI.Listbox(values=functions.get_todos(), key='todos',
                               enable_events=True, size=[45, 10])
edit_button = PySimpleGUI.Button('Edit')
complete_button = PySimpleGUI.Button('Complete')
close_button = PySimpleGUI.Button('Close')

window = PySimpleGUI.Window('My To-Do App',
                            layout=[[clock],
                                    [label],
                                    [input_box, add_button],
                                    [list_box],
                                    [edit_button, complete_button, close_button]],
                            font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=500)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.save_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.save_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                PySimpleGUI.popup("Please select an item first", font=('Helvetica', 20))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.save_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                PySimpleGUI.popup("Please select and item first", font=('Helvetica', 20))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Close':
            break
        case PySimpleGUI.WIN_CLOSED:
            break


window.close()
