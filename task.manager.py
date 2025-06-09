# Importing datetime to handle dates
from datetime import datetime  

# Welcome greeting, login page.
print("Welcome, please enter your login details.")

# Read existing users from 'user.txt'
with open("user.txt", "r") as file:
    for line in file:
        user = line.strip().split(", ")
        
user = {}

# Validate user login
while True:
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    # Check if credentials are correct
    if username == "admin":
        if  password == "adm1n":
            print("Login successful!\n")
            break
    else:
        # Keep prompting until correct login
        print("Invalid username or password. Please try again.")  

# Menu Loop - User can continuously perform actions until they choose to exit
while True:
    menu = input('''\nSelect one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    # Register a new user (Admin only)
    if menu == 'r' and username == "admin":  
        while True:
            new_user = input("Enter new username: ")
  
            # Check if username already exists
            if new_user in user:  
                print("Username already exists! Try another one.")
                continue

            password = input("Enter new password: ")
            confirm_pass = input("Confirm password: ")

            # Ensure passwords match
            if password != confirm_pass:  
                print("Passwords do not match. Try again.\n")
            else:
                with open("user.txt", "a") as file:
                    # Append new user to file
                    file.write(f"\n{new_user}, {password}")  
                # Update in-memory dictionary
                user[new_user] = password  
                print("User registered successfully!\n")
                break

    # Add a new task
    elif menu == 'a':
        task_assign = input("Who is this task being assigned to? ")
        # Ensure assigned user exists
        if task_assign not in user:  
            print("User does not exist. Please enter a valid username.")
            continue

        task_title = input("Assigned task: ")
        task_description = input("Task description: ")
        task_due = input("Date that this task is due (YYYY-MM-DD): ")
        # Get today's date as assignment date
        task_date = datetime.today().date()  

        # Write task details to 'tasks.txt'
        with open("tasks.txt", "a") as file:
            file.write(f"\n{task_assign}, {task_title}, {task_description}, {task_date}, {task_due}, no")

        print("\nYou have successfully assigned a task!")

    # View all tasks
    elif menu == 'va':
        try:
            with open("tasks.txt", "r") as file:
                # Read all tasks from file
                tasks = file.readlines()  

            if not tasks:
                # If file is empty, notify user
                print("No tasks available.")  
            else:
                for task in tasks:
                    # Split task details
                    task_data = task.strip().split(", ")  
                    # Ensure correct format
                    if len(task_data) == 6:  
                        print(f"""
Task: {task_data[1]}
Assigned to: {task_data[0]}
Date assigned: {task_data[3]}
Task due: {task_data[4]}
Task description: {task_data[2]}
Task Completed: {task_data[5]}
""")
        except FileNotFoundError:
            # Handle missing file error
            print("Task file not found.")  

    # View tasks assigned to the logged-in user
    # View tasks assigned to the logged-in user
    elif menu == 'vm':
        # Track if user has any tasks assigned
        found_tasks = False  

    try:
        with open("tasks.txt", "r") as file:
            # Read all tasks from file
            tasks = file.readlines()  

        for task in tasks:
            task_data = task.strip().split(", ")

            # Check task format & assignment
            if len(task_data) == 6 and task_data[0] == username:  
                found_tasks = True
                print(f"""
Task: {task_data[1]}
Date assigned: {task_data[3]}
Task due: {task_data[4]}
Task description: {task_data[2]}
Task Completed: {task_data[5]}
""")

        if not found_tasks:
            # Notify user if no tasks were found
            print("You have no tasks assigned.")  

    except FileNotFoundError:
        # Handle missing file error
        print("Task file not found. No tasks are available.")  
