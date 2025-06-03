# daily_reminder.py

def create_daily_reminder():
    """
    Prompts the user for a single task, its priority, and time sensitivity,
    then provides a customized reminder based on the input.
    """
    # Prompt for a Single Task
    task = input("Enter your task: ")
    
    # Prompt for the task's priority (high, medium, low)
    # Convert input to lowercase for case-insensitive comparison
    priority = input("Priority (high/medium/low): ").lower()
    
    # Ask if the task is time-bound (yes or no)
    # Convert input to lowercase for case-insensitive comparison
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    reminder_message = "" # Initialize an empty string to build the reminder

    # Process the Task Based on Priority and Time Sensitivity
    # Use a Match Case statement to react differently based on the task’s priority.
    match priority:
        case "high":
            # Check if the task is time-bound for high priority
            if time_bound == "yes":
                reminder_message = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
            else:
                reminder_message = f"Reminder: '{task}' is a high priority task. Aim to complete it today."
        
        case "medium":
            # Check if the task is time-bound for medium priority
            if time_bound == "yes":
                reminder_message = f"Note: '{task}' is a medium priority task that requires timely completion today!"
            else:
                reminder_message = f"Note: '{task}' is a medium priority task. Try to complete it soon."
        
        case "low":
            # Check if the task is time-bound for low priority
            if time_bound == "yes":
                # As per example, for low priority and time-bound, it's still a "Note"
                reminder_message = f"Note: '{task}' is a low priority task that is time-bound. Consider prioritizing it if possible."
            else:
                reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        
        case _: # This case handles any invalid priority input
            reminder_message = "Sorry, I don't have a specific reminder for that priority level."

    # Output the Customized Reminder
    print(reminder_message)

# Run the reminder creation function when the script is executed
if __name__ == "__main__":
    create_daily_reminder()