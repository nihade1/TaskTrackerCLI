import json
import datetime


task_list =  {}
id=0

def main():
    readfromfile()
    while True:
        print("=== Task Tracker Menu ===")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Change Task Status")
        print("5. View All Tasks")
        print("6. Save Tasks")
        print("7. Exit")
        print("========================")
        
        choice = input("Choose an option (1-7): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            try:
                task_id = int(input("Enter task ID: "))
                new_description =  input("Enter new description: ")
                update_task(task_id, new_description)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID: "))
            status = input("Enter new status (todo, in-progress, done): ")
            task_status(task_id, status)
        elif choice == '5':
            tasks_list()
        elif choice == '6':
            writetofile(task_list)
            print("Tasks saved to file!")
        elif choice == '7':
            print("Exiting Task Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        print()


def add_task():
    global id
    task = input("Enter the task description: ")
    while not task:
        print("Task description cannot be empty, Task not added. Please try again.")
        task = input("Enter the task description: ")
    
    # Set initial status as "todo"
    task_list[id] = {"task": task, "status": "todo"}
    task_list[id]["created_at"] = datetime.date.today().isoformat()
    task_list[id]["updated_at"] = datetime.date.today().isoformat()
    print(f"Task added successfully! ID: {id} (Status: todo)")
    id += 1

def update_task(task_id, new_description):
    if task_id in task_list:
        task_list[task_id]["task"] = new_description
        task_list[task_id]["updated_at"] = datetime.date.today().isoformat()
        print(f"Task {task_id} updated successfully!")

    else:
        print(f"Task with ID {task_id} does not exist.")

def delete_task(task_id):
    if task_id in task_list:
        del task_list[task_id]
        print(f"Task {task_id} deleted successfully!")
    else:
        print(f"Task with ID {task_id} does not exist.")

def task_status(task_id, status):
    validate_status = ["todo", "in-progress", "done"]
    
    if task_id in task_list:
        if status in validate_status:
            task_list[task_id]["status"] = status
            print(f"Task {task_id} status updated to {status} successfully!")
        else:
            print(f"Invalid status. Please choose from {validate_status}.")
    else:
        print(f"Task with ID {task_id} does not exist.")
        
#viewing tasks list
def tasks_list():
    if not task_list:
        print("No tasks found.")
        return
    
    print("\n--- Task List ---")
    for task_id, task_data in task_list.items():
        print(f"ID {task_id}: {task_data['task']} [Status: {task_data['status']}]")
    print()

#writing to json file
def writetofile(data):
    json_str = json.dumps(data, indent=4)
    with open("sample.json", "w") as f:
      f.write(json_str)
#reading from json file
def readfromfile():
    global task_list, id
    try:
        with open("sample.json", "r") as f:
            data = json.load(f)
            # Convert string keys back to integers
            task_list = {int(k): v for k, v in data.items()}
            # Update id to avoid duplicate IDs
            if task_list:
                id = max(task_list.keys()) + 1
            print("Tasks loaded from file!")
    except FileNotFoundError:
        print("No saved file found. Starting fresh.")
    return task_list

if __name__ == "__main__":
    main()






