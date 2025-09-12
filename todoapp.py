def task():
    tasks = []
    print("---- Welcome to TODO App ----")

    # Initial task input with validation 
    while True:
        try:
            total_task = int(input("Enter how many tasks you want to add initially: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    for i in range(1, total_task + 1):
        task_name = input(f"Enter your task name {i}: ")
        tasks.append(task_name)

    print("\nToday's tasks:")
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t}")

    # Main loop
    while True:
        print("\nChoose an operation:")
        print("1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit")
        try:
            operation = int(input("Your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if operation == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added.")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update: ")
            if updated_val in tasks:
                up = input("Enter the new task name: ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task: '{updated_val}' → '{up}'")
            else:
                print("Task not found.")

        elif operation == 3:
            del_val = input("Which task do you want to delete? ")
            if del_val in tasks:
                tasks.remove(del_val)
                print(f"Task '{del_val}' has been deleted.")
            else:
                print("Task not found.")

        elif operation == 4:
            if tasks:
                print("\nCurrent tasks:")
                for i, t in enumerate(tasks, start=1):
                    print(f"{i}. {t}")
            else:
                print("No tasks available.")

        elif operation == 5:
            print("Closing the program... Goodbye!")
            break

        else:
            print("Invalid input. Please choose a valid operation.")

# Run the app 
task()
