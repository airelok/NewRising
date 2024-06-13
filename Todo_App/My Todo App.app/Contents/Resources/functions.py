# placing logical parts of the code, processes, functions etc
# must be in the same directory as the script


FILEPATH = ("/Users/airelking/Desktop/NewRising/Projects/Todo_App/todos.txt")

def get_todos(filepath = FILEPATH):

    """ Read a text file content and returns a list object"""

    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):

    """ Write the to-do item list in the text file """

    with open(filepath, "w") as file:
        file.writelines(todos_arg)



if __name__ == "__main__":
    print("Hello")
    print(get_todos())

print("Hello from functions!!!")