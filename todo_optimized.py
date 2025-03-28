# TO DO LIST APP

#... Define an empty task list to which the user can add or remove items.
task_list = []

#... Greet and welcome the user to the app.
print("""\n Hello! Welcome to your To-Do List app!""")

#... use try/except for error handling
#... Define the function 'prompts', which handles any input the user enters.
def prompts():
    try:
        choice = int(input("""\nTo select an option, type its number then press enter: """))
    # If the user enters anything besides an integer 1-4, a custom error message will be displayed.
    except ValueError: 
        print("""\nOops! That's not a number on the menu. \nTry entering 1, 2, or 3 (or 4 to quit app.)""")
        prompts() # Prompt the user for input.
    # Use if, elif, else statement to handle the user's input. 
    if choice == 1: # User chooses to add task to list:
        add_task()    
    elif choice == 2: # User chooses to remove a task from the list.
        remove_task() 
    elif choice == 3: # User chooses to view their task list. 
        view_task_list()
    # User chooses to quit app.    
    elif choice == 4:
        quit() # Quits app if user types '4'
    # If user enters any integer besides 1-4, display error message.
    else:
        print("""\nOops! That didn't work. Let's try again. \nRemember to enter 1, 2, 3, or 4 from the menu.""")
        commands() # Display menu
        prompts() # Display prompt

# Define a menu with options to add, view, delete tasks, or quit the application.
def commands():
    print("""\nHere are your options: \n1. Add a task \n2. Delete a task \n3. View your to-do list \n4. Quit""")

def add_task():
    # Ask user to input a task.
    task = input("""Type the task, then press enter: """).lower()
    # Check if item is already in list. If it is not in the list, add it.
    if task not in task_list:
        task_list.append(task) 
        # Display message confirming task has been added to the list.
        print(f"""Great! {task.capitalize()} has been added to your to-do list! \nIf you would like to add another task, type 1, or choose a number from the menu.""") 
    else:
        print(f"\nLooks like {task} is already on your list. If you would like to add a new item, enter 1.")
    commands() # Display the menu again.
    prompts() # Prompt the user for input.

def remove_task():
    # Test to see if task can be removed from list.
    try: 
        task_to_remove = input("""\nType the task you wish to remove, then press enter: """).lower()
        # Task is removed from list.
        task_list.remove(task_to_remove) 
        # Display message confirming task is removed from list.
        print(f"""\nCongratulations! You've removed {task_to_remove} from your to-do list.""") 
    # If task cannot be removed from list, display error message.
    except ValueError:
        print("""\nSorry, that task is not on your list. \nLet's try something else.""")
    commands() # Display menu.
    prompts() # Display prompt.

def view_task_list():
    # If there are no tasks in list, display message.
    if not task_list:
        print("""\nYour list is empty! Add a task by entering 1.""")
    # If there are tasks in list, display list.
    else:
            print(f"""\nHere is your to-do list:""")
            for x in task_list:
                print(f"""-{x}""")
    # Follow up message.
    print("""\nYou may continue by entering a number below. \nIf you're all finished, enter '4' to quit.""")
    commands() # Display menu
    prompts() # Display prompt

# Display the menu to the command line.
commands()
prompts()

