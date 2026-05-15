import json
import os

def task():
    tasks = []
    print("---- Welcome to TODO App ----")

    # Load existing tasks if file exists
    load_tasks(tasks)

    # Initial task input with validation
    if not tasks:
        while True:
            try:
                total_task = int(input("Enter how many tasks you want to add initially: "))
                break
            except ValueError:
                print("Please enter a valid number.")

        for i in range(1, total_task + 1):
            task_name = input(f"Enter your task name {i}: ")
            priority = input(f"Enter priority for '{task_name}' (high/medium/low): ").lower()
            if priority not in ['high', 'medium', 'low']:
                priority = 'medium'
            tasks.append({'name': task_name, 'completed': False, 'priority': priority})

    print("\nToday's tasks:")
    display_tasks(tasks)

    # Main loop
    while True:
        print("\nChoose an operation:")
        print("1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Mark Complete/Incomplete")
        print("6 - Set Priority\n7 - Search\n8 - Save\n9 - Load\n10 - Exit")
        try:
            operation = int(input("Your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")
            continue

        if operation == 1:
            add_task(tasks)

        elif operation == 2:
            update_task(tasks)

        elif operation == 3:
            delete_task(tasks)

        elif operation == 4:
            display_tasks(tasks)

        elif operation == 5:
            mark_complete(tasks)

        elif operation == 6:
            set_priority(tasks)

        elif operation == 7:
            search_tasks(tasks)

        elif operation == 8:
            save_tasks(tasks)

        elif operation == 9:
            load_tasks(tasks)
            print("Tasks loaded successfully.")

        elif operation == 10:
            save_tasks(tasks)  # Auto-save before exit
            print("Closing the program... Goodbye!")
            break

        else:
            print("Invalid input. Please choose a valid operation.")

def add_task(tasks):
    add = input("Enter the task you want to add: ")
    priority = input(f"Enter priority for '{add}' (high/medium/low): ").lower()
    if priority not in ['high', 'medium', 'low']:
        priority = 'medium'
    tasks.append({'name': add, 'completed': False, 'priority': priority})
    print(f"Task '{add}' has been successfully added.")

def update_task(tasks):
    updated_val = input("Enter the task name you want to update: ")
    for task in tasks:
        if task['name'] == updated_val:
            up = input("Enter the new task name: ")
            task['name'] = up
            print(f"Updated task: '{updated_val}' → '{up}'")
            return
    print("Task not found.")

def delete_task(tasks):
    del_val = input("Which task do you want to delete? ")
    for i, task in enumerate(tasks):
        if task['name'] == del_val:
            tasks.pop(i)
            print(f"Task '{del_val}' has been deleted.")
            return
    print("Task not found.")

def display_tasks(tasks):
    if tasks:
        print("\nCurrent tasks:")
        priority_order = {'high': 0, 'medium': 1, 'low': 2}
        sorted_tasks = sorted(tasks, key=lambda x: priority_order[x['priority']])
        for i, task in enumerate(sorted_tasks, start=1):
            status = "[✓]" if task['completed'] else "[ ]"
            print(f"{i}. {status} {task['name']} ({task['priority']} priority)")
    else:
        print("No tasks available.")

def mark_complete(tasks):
    task_name = input("Enter the task name to mark complete/incomplete: ")
    for task in tasks:
        if task['name'] == task_name:
            task['completed'] = not task['completed']
            status = "completed" if task['completed'] else "incomplete"
            print(f"Task '{task_name}' marked as {status}.")
            return
    print("Task not found.")

def set_priority(tasks):
    task_name = input("Enter the task name to set priority: ")
    for task in tasks:
        if task['name'] == task_name:
            priority = input(f"Enter new priority for '{task_name}' (high/medium/low): ").lower()
            if priority in ['high', 'medium', 'low']:
                task['priority'] = priority
                print(f"Priority for '{task_name}' set to {priority}.")
            else:
                print("Invalid priority. Use high, medium, or low.")
            return
    print("Task not found.")

def search_tasks(tasks):
    search_term = input("Enter search term: ").lower()
    found_tasks = [task for task in tasks if search_term in task['name'].lower()]
    if found_tasks:
        print("\nSearch results:")
        for task in found_tasks:
            status = "[✓]" if task['completed'] else "[ ]"
            print(f"{status} {task['name']} ({task['priority']} priority)")
    else:
        print("No tasks found matching the search term.")

def save_tasks(tasks):
    try:
        with open('tasks.json', 'w') as f:
            json.dump(tasks, f, indent=4)
        print("Tasks saved successfully.")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def load_tasks(tasks):
    if os.path.exists('tasks.json'):
        try:
            with open('tasks.json', 'r') as f:
                loaded_tasks = json.load(f)
            tasks.clear()
            tasks.extend(loaded_tasks)
            print("Tasks loaded from file.")
        except Exception as e:
            print(f"Error loading tasks: {e}")
    else:
        print("No saved tasks file found.")

# Run the app
task()
