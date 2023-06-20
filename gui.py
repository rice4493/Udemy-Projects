import functions
import PySimpleGUI as sg
import time

sg.theme("DarkBlue3")

now = time.strftime("%d %b, %Y \n %H:%M")
clock = sg.Text('', key='clock')
label = sg.Text("Type in a task")
input_box = sg.InputText(tooltip="Enter todo", key="Todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("To-do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=now)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                # use [0] to extract list
                todo_to_edit = values['todos'][0]
                new_todo = values['Todo']

                todos.functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write(todos)
                window['todos'].update(values=todos)
                window['Todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "Exit":
            break
        case "todos":
            window["Todo"].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
