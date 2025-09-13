# Step 1: Create your checklist
checklist = ["Wake up early", "Exercise", "Attend class", "Finish homework", "Read a book", "Clean your room"]

# Step 2: Create empty lists for completed and incomplete tasks
completed_tasks = []
incomplete_tasks = []

# Step 3: Ask the user about each task
for task in checklist:
    answer = input(f"Did you complete this task: '{task}'? (yes/no): ").strip().lower()
    
    if answer == "yes":
        completed_tasks.append(task)
    else:
        incomplete_tasks.append(task)

# Step 4: Show results
print("\n Completed Tasks:")
for task in completed_tasks:
    print(f"- {task}")

print("\n Incomplete Tasks:")
for task in incomplete_tasks:
    print(f"- {task}")
