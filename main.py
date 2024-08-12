while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    # Add case which writes the todo list into an external file todos.txt
    if 'add' in user_action:
        todo = user_action[4:]

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)
    elif 'show' in user_action:

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        # new_todos = [item.strip('\n') for item in todos]  = list comprehension

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)
    elif 'edit' in user_action:
        number = int(user_action[5:])
        number = number - 1

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        with open('files/todos.txt', 'w') as file:
            todos = file.writelines(todos)
    elif "complete" in user_action:
        number = int(user_action[9:])

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        index = number - 1

        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open('files/todos.txt', 'w') as file:
            todos = file.writelines(todos)

        print(f"Todo {todo_to_remove} has been completed and was removed from the list")

    elif 'exit' in user_action:
        break
    else:
        print("Command Invalid")

print("Bye!")
