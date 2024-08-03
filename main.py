while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        # Add case which writes the todo list into an external file todos.txt
        case 'add' | 'Add' | '+':
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show' | 'Show' | 'Display':

            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # new_todos = [item.strip('\n') for item in todos]  = list comprehension

            for index, item in enumerate(todos):
                todos = todos.strip('\n')
                row = f"{index + 1}.{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Number of the todo to complete: "))
            todos.pop(number) - 1

        case 'exit':
            break

print("Bye!")
