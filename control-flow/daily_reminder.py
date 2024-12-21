
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
reminder = f"'{task}' is a {priority} priority task"

match priority:
    case "high":
        reminder += " that requires immediate attention"
    case "medium":
        reminder += " that should be completed soon"
    case "low":
        reminder += " that can be done at your convenience"
    case _:
        reminder += " with an unknown priority"

if time_bound == "yes":
    reminder += " today!"

# Provide a customized reminder
print(f"Reminder: {reminder}")