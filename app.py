import os

def display_tasks():
    filename = "tasks.txt"
    print("\n--- TASKMASTER: CURRENT LIST ---")
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = file.readlines()
            for index, line in enumerate(tasks, start=1):
                print(f"{index}. {line.strip()}")
    else:
        print("List is empty.")
    print("-------------------------------\n")

def add_task():
    new_task = input("Enter the new task: ")
    with open("tasks.txt", "a") as file:
        file.write(new_task + "\n")
    print("Task added!")

def main():
    while True:
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()