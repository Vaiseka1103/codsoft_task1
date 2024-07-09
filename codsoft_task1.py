def main():

  tasks = []

  while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      task = input("Enter a task: ")
      tasks.append(task)
      print("Task added!")
    elif choice == '2':
      if not tasks:
        print("No tasks to display.")
      else:
        print("Your tasks:")
        for i, task in enumerate(tasks):
          print(f"{i+1}. {task}")
    elif choice == '3':
      if not tasks:
        print("No tasks to mark as done.")
      else:
        print("Your tasks:")
        for i, task in enumerate(tasks):
          print(f"{i+1}. {task}")

        try:
          choice = int(input("Enter the number of the task to mark done: ")) - 1
          if choice < 0 or choice >= len(tasks):
            raise ValueError
          tasks.pop(choice)
          print("Task marked done successfully!")
        except ValueError:
          print("Invalid task number. Please try again.")

    elif choice == '4':
      print("Exiting the To-Do List.")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()


