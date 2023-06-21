def get_todos(filepath):
    """
    Read a text file and return the list of to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    """
    Write the to-do items list in the text file.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


def display_list():
    """
    Display contents of to-do list with complete status
    """

    todos_loc2 = get_todos('List.txt')

    if not todos_loc2:
        print("Your to-do list is empty. Add tasks.")
    else:
        print("\n<---To-do List--->")
        todos_loc2 = get_todos("List.txt")

        for index, item in enumerate(todos_loc2):
            index += 1
            item = item.strip('\n')
            status = '(p)' if not item.endswith('(c)') else ''
            print(f"{index}. {item} {status}")
        return todos_loc2
