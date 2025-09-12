# TODO List App

A simple command-line TODO list application written in Python. This app allows users to manage their daily tasks interactively from the terminal.

## Features
- **Add Tasks:** Add new tasks to your list at any time.
- **Update Tasks:** Change the name of an existing task.
- **Delete Tasks:** Remove tasks you no longer need.
- **View Tasks:** Display all current tasks in a numbered list.
- **Exit:** Quit the application when finished.

## How It Works
1. **Startup:**
   - When you run the app, you are greeted with a welcome message.
   - You are prompted to enter how many tasks you want to add initially. Enter a number (e.g., 3), then provide the names for each task.
   - The app displays your initial list of tasks.

2. **Main Menu:**
   - You are presented with a menu to choose an operation:
     - `1 - Add`: Add a new task by entering its name.
     - `2 - Update`: Update an existing task by providing its current name and the new name.
     - `3 - Delete`: Delete a task by entering its name.
     - `4 - View`: View all current tasks.
     - `5 - Exit`: Exit the application.
   - The menu repeats after each operation until you choose to exit.

3. **Input Validation:**
   - The app checks for valid numeric input when choosing menu options and when entering the initial number of tasks.
   - If you enter an invalid option or a task name that does not exist (for update/delete), you will be prompted again.

## Example Usage
```
---- Welcome to TODO App ----
Enter how many tasks you want to add initially: 2
Enter your task name 1: Buy groceries
Enter your task name 2: Read book

Today's tasks:
1. Buy groceries
2. Read book

Choose an operation:
1 - Add
2 - Update
3 - Delete
4 - View
5 - Exit
Your choice: 1
Enter the task you want to add: Exercise
Task 'Exercise' has been successfully added.
```

## How to Run
1. Make sure you have Python installed (version 3.x recommended).
2. Open a terminal and navigate to the project directory.
3. Run the app with:
   ```
   python todoapp.py
   ```

## File Structure
- `todoapp.py`: Main application code.
- `README.md`: Project documentation.

## Author
Nikhil Gupta

---
Feel free to modify or extend the app for your own needs!
