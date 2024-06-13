import functions
import PySimpleGUI as sg
import time
import os


if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkPurple4")

clock = sg.Text("", key = "clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = "Enter to-do", key = "todo")
add_button = sg.Button(size = 5,
                       image_source= "/Users/airelking/Desktop/NewRising/Projects/Todo_App/add.png",
                       mouseover_colors="LightBlue2",
                       tooltip = "Add Todo",
                       key = "Add")
list_box = sg.Listbox(values = functions.get_todos(), key = "todos",
                      enable_events = True, size = [45,10])
edit_button = sg.Button("Edit",
                        size = 5,
                        mouseover_colors="LightBlue")
complete_button = sg.Button(size = 5,
                            image_source = "/Users/airelking/Desktop/NewRising/Projects/Todo_App/complete.png",
                            mouseover_colors="LightBlue",
                            tooltip="Complete Todo",
                            key = "Complete")
exit_button = sg.Button("Exit",
                        size = 5,
                        mouseover_colors="LightBlue")

window = sg.Window("My To-Do App",
                   layout = [[clock],
                             [label],
                             [input_box, add_button],
                             [list_box, edit_button, complete_button],
                             [exit_button]],
                   font = ("Helvetica", 20))

while True:
    event, values = window.read(timeout = 20)
    window["clock"].update(value = time.strftime("%b %d, %Y %H:%M:%S"))
    print(1, event)
    print(2, values)
    if values["todos"] is not None:  # Add this check
        print(3, values["todos"])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values = todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values = todos)
            except IndexError:
                sg.popup("Please select an item first.", font = ("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values = todos)
                window["todo"].update(value = "")
            except IndexError:
                sg.popup("Please select an item first.", font = ("Helvetica", 20))

        case "Exit":
            break

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break


window.close()






