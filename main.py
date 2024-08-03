while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        # Add case which writes the todo list into an external file todos.txt
        case 'add' | 'Add' | '+':
            todo = input("Enter a todo: ") + "\n"

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show' | 'Show' | 'Display':

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = [item.strip('\n') for item in todos]  = list comprehension

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}.{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('files/todos.txt', 'w') as file:
                todos = file.writelines()
        case "complete":
            number = int(input("Number of the todo to complete: "))

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todo_to_remove = todos[number - 1]

            todos.pop(number) - 1

            with open('files/todos.txt', 'w') as file:
                todos = file.writelines()

            print(f"Todo {todo_to_remove} was removed from the list")

        case 'exit':
            break

print("Bye!")
