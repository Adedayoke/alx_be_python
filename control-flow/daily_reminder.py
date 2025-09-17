# daily_reminder.py
# Personal Daily Reminder System
# This program provides customized task reminders based on priority and time sensitivity

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on priority using Match Case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Make sure to complete it as soon as possible."
        print(f"Reminder: {reminder}")
    
    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Consider completing it when you have time."
        print(f"Reminder: {reminder}")
    
    case "low":
        reminder = f"'{task}' is a low priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Consider completing it when you have free time."
        print(f"Note: {reminder}")
    
    case _:
        print("Invalid priority level entered.")