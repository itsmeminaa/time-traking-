import datetime


     #Decorator to ensure that an employee is set before executing the decorated method.
    #If no employee name is set, an error message is displayed, and the function will not execute.
def ensure_employee(func):
    def wrapper(self, *args, **kwargs):
        if not self.employee_name:
            print("Error: No employee set. Please set an employee first.")
            return
        return func(self, *args, **kwargs)
    return wrapper

class Logger:  #It stores all the logs in a list
    def __init__(self):
        # Initialize an empty list to store logs
        self.logs = []

    def add_log(self, log_type, time):#this function adds a new clock-in or clock-out
        self.logs.append({'type': log_type, 'time': time})
        #Adds a log entry to the list of logs.

class TimeTracker(Logger):#tracks the employee's working hours
  
    def __init__(self):
        super().__init__()
         # Calls the Logger's __init__ 
        self.employee_name = None #Place holder for the employees name

    def set_employee(self, name):
        self.employee_name = name.strip()

    @ensure_employee
    def start(self):
        clock_in_time = datetime.datetime.now() #Gets the current date and time.
        self.add_log('clock_in', clock_in_time) #Logs the clock-in time.
        print(f"{self.employee_name} started working at: {clock_in_time}") #Prints the start time.

    @ensure_employee
    #This stops the work timer for the employee.
    def stop(self):
        clock_out_time = datetime.datetime.now() #Gets the current date and time for stopping.
        self.add_log('clock_out', clock_out_time) #Logs the clock-out time.
        print(f"{self.employee_name} stopped working at: {clock_out_time}") #Logs the clock-out time.

    def worked_hours(self):
        #This calculates how much time the employee has worked in total.
        total_work_seconds = 0 
        clock_in_time = None #track clock-in time.

        for log in self.logs:  # here it Loops through all the logs to calculate work time
            if log['type'] == 'clock_in': #If it's a clocked in log, then it store the time.
                clock_in_time = log['time']
            elif log['type'] == 'clock_out' and clock_in_time: #If it's clocked out thencalculate the time worked.
                total_work_seconds += (log['time'] - clock_in_time).total_seconds()
                clock_in_time = None


        # Convert total work time to hours, minutes, and seconds.
        hours = total_work_seconds // 3600
        minutes = (total_work_seconds % 3600) // 60
        seconds = total_work_seconds % 60
        print(f"{self.employee_name} worked for a total of {int(hours)} hours, {int(minutes)} minutes, and {int(seconds)} seconds.")
        return total_work_seconds


# Creates a TimeTracker object.
tracker = TimeTracker()

# Asks for the employee name and sets it
employee_name = input("Enter the name of the employee: ")
tracker.set_employee(employee_name)

# Start tracking work.
input("Press Enter to start working")
tracker.start()

# Stop tracking work.
input("Press Enter to stop working")
tracker.stop()

# Calculate and display total worked hours.
input("Press Enter to see how much time was worked")
tracker.worked_hours()
