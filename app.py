# TaskMaster App
import os

def display_tasks():
    filename = "tasks.txt"
    
    print("--- TASKMASTER: MY PROGRESS ---")
    
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("Your task list is empty!")
            for index, line in enumerate(tasks, start=1):
                print(f"{index}. {line.strip()}")
    else:
        print("Error: tasks.txt not found! Please create it first.")
    
    print("-------------------------------")

if __name__ == "__main__":
    display_tasks()