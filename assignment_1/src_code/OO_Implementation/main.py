import sys 
from calendar import Calendar
from appointment import Appointment
from day import Day


def main():

  scheduler = Calendar()
  
  
  print("Welcome to your appointment Scheduler! \n - To add a new appointment, enter add \n - To remove an existing appointment, enter remove \n - To view your scheduled appointments for a specific day, enter show day \n - To view all scheduled appointments for the week, enter show week \n - To exit the scheduler, enter exit")
  func = input()
  while func != "exit":
  
    if func == "add":
      new = input("Please enter the title of your appointment, the day, starting time and end time (HH:MM).\n")
      title,day,start,end = new.split(" ")
      #within appointment we can check for valid time.
      
      newAppointment = Appointment(title.lower().capitalize(),start,end)
      
      
      scheduler.week[day.lower().capitalize()].add_appointment(newAppointment)
      #if new == "exit":
        #sys.exit(0)
      
    #do capitalize and lower for titles too.
  
    if func == "remove":
      remove = input("Please enter the title, the day, starting and ending time of the appointment you wish to delete: (Example: Gym Monday 11:00 13:00)\n")
      title,day,start,end = remove.split(" ")
      
      appointment = Appointment(title.lower().capitalize(),start,end)
      scheduler.week[day.lower().capitalize()].remove_appointment(appointment)
      
    if func == "show day":
      show_day = input("Please enter the day you wish to view.\n")
      print(scheduler.week[show_day.lower().capitalize()].__str__())
    
    if func == "show week":
      print(scheduler.__str__())
      
      
    func = input()   
    
    
    
if __name__ == '__main__':
  main()

