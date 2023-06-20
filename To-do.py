import functions
import time

now = time.strftime("%d %b, %Y \n %H:%M")
print("Hello! It is currently", now)

print("\n<---To-do List--->")
# menu-driven program

while True:
    print("\n--MENU--")
    print("1. Add task")
    print("2. Display pending tasks list")
    print("3. Edit task")
    print("4. Complete task")
    print("5. Exit")
    action = input("Enter either 'add', 'display', 'edit', 'complete' or 'exit' :")
    if action.startswith("add"):
        task = action[4:]

        Todos = functions.get_todos("List.txt")

        Todos.append(task + "\n")

        functions.write_todos('List.txt', Todos)

    elif action.startswith("display"):
        functions.display_list()

    elif action.startswith("edit"):
        try:
            number = int(action[5:])
            print(number)
            number = number - 1

            Todos = functions.get_todos("List.txt")

            new_task = input("Enter new task: ")
            # swapping
            existing_task = Todos[number]
            Todos[number] = new_task + "\n"

            functions.write_todos('List.txt', Todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif action.startswith("complete"):
        try:
            number = int(action[9:])
            number = number - 1
            removed = Todos[number]
            if removed.endswith('(p)'):
                new = [com.replace('(p)', '(c)') for com in Todos]
                # Todos[number] = removed + ' (c)'
                # Completed.append(removed)

                Todos = functions.get_todos("List.txt")

            else:
                print("Task already completed.")
            # Todos.insert(number, removed + ' (c)')
            # print("Task completed --> " + removed)
            # Completed.append(removed)
        except IndexError:
            print("There is no item with that number.")
            continue
        
    elif action.startswith("exit"):
        print("\nThank you!!!!\n")
        exit()
    else:
        print("Invalid input! Please try again.")
