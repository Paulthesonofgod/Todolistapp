def get_todos(filepath="files/todos.txt"):
    """Gets todos from a specified file """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="files/todos.txt"):
    """Writes the output in a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    # Add case which writes the todo list into an external file todos.txt
    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)
    elif user_action.startswith('show'):

        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos]  = list comprehension

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print("Invalid command.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            print(f"Todo {todo_to_remove} has been completed and was removed from the list")
        except ValueError:
            print("Invalid Input")
        except IndexError:
            print("Not within range")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command Invalid")

print("Bye!")
