import os

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task deleted successfully.")
        else:
            print("Invalid task index.")

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks):
                status = "[ ]" if not task["completed"] else "[X]"
                print(f"{i + 1}. {status} {task['task']}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    todo_list = TodoList()

    while True:
        clear_screen()
        print("To-Do List Application\n")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. View To-Do List")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.display_tasks()
            task_index = int(input("Enter the task index to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == "3":
            todo_list.display_tasks()
            task_index = int(input("Enter the task index to mark as completed: ")) - 1
            todo_list.mark_completed(task_index)
        elif choice == "4":
            todo_list.display_tasks()
            input("Press Enter to continue...")
        elif choice == "5":
            print("Thanks for being us. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
