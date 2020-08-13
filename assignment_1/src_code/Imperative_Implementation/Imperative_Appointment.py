Week = { "Monday": [],
         "Tuesday": [],
         "Wednesday": [],
         "Thursday": [],
         "Friday": [],
         "Saturday": [],
         "Sunday": [],}
         
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
      
def minutes(time):
   # use this to check the minutes arent the same the appointments because adding
  total = 0 
  hours, mins = time.split(":")
  hours = int(hours) * 60
  total = hours + int(mins)
  return total 
 
def time(minutes):
  hours, mins = divmod(minutes,60)
  
  if mins == 0:
    mins = '00'
  
  return ':'.join([str(hours),str(mins)])
  
 
def overlap(appointment, other):
  #check if mins are the same, if the start of within the start or end of other or end is within bracket.
  #how did i check overlap in oo -> 
  if appointment[2] < other[1] or appointment[1] > other[2]:
    return False
  return True
  
def time_check(time):
  if time[2] == ":" and len(time) == 5:
    hours, mins = time.split(':')
    
    if (len(hours) == 2 and hours.isdigit()) and (len(mins) == 2 and hours.isdigit()):
      if (int(hours) <= 23 and int(hours) >= 0) and (int(mins) <= 23 and int(mins) >= 0):
        return True
      else: 
        return False
    else:
      return False
  else:
    return False  
         
def add_appointment(day, title, start_time, end_time):
  output = ""
  day = day.capitalize()
  if day in Week:
    #need to make sure the time is in correct format before converting
    
    if time_check(start_time) and time_check(end_time):
      start = minutes(start_time)
      end= minutes(end_time)
      appointment = [title, start, end]
      for app in Week[day]:
        if overlap(appointment,app): #if true = 
          app = app[0] + " at " + time(app[1]) + " until " + time(app[2])
          return "Appointment overlaps with " + app +  ", please try again with an different time."
      Week[day].append(appointment)
      return "Appointment added successfully."
      
    elif not (time_check(start_time)) and time_check(end_time):
      return ("Time is not in the correct format (HH:MM), please try again.")
    
  else:
    return "Day not found"
    #test to see what it looks like once added..
    
#order items based on the start_time of inner lists 
def order_appointments(day):
  if day in Week:
    daylist = Week[day]
    return sorted(daylist, key=lambda x: x[2])
  
def remove_appointment(day,title,start):
  if day in Week:
    for appointment in Week[day]:
      if appointment[0] == title and time(appointment[1]) == start:
        Week[day].remove(appointment)
        return "Appointment has been successfully deleted"
    return "Appointment not found"
    
  else:
    return "Day not found"
  
  
  
def show_day(day):
  output = ""
  appointment = ""
  print("\n      " + day + "\n ------------------- ")
  if day in Week:
    if len(Week[day]) == 0:
      output += "\n" + "- You have no scheduled appointments"
    else:
      AppointmentList = order_appointments(day)
      for i in order_appointments(day):
        output +=  "- " + i[0] + " " + time(i[1]) + " " + time(i[2]) + "\n"
        
      output = output.strip()
      
  else:
    output += "does not exist."
    
  return output
  
  
def show_week():

  for day in Week:
    print(show_day(day))
    
def main():
  print("Welcome to your appointment Scheduler! \n - To add a new appointment, enter add \n - To remove an existing appointment, enter remove \n - To view your scheduled appointments for a specific day, enter show day \n - To view all scheduled appointments for the week, enter show week \n - To exit the scheduler, enter exit")
  func = input()
  
  while func != "exit":
     #make sure days is lower and then capitalize
    if func == "add":
      new = input("Please enter the title of your appointment, the day, starting time and end time (HH:MM).\n")
      title,day,start,end = new.split(" ")
      print(add_appointment(day.lower(),title.lower().capitalize(),start,end))
      #if new == "exit":
        #sys.exit(0)
      
    if func == "remove":
      remove = input("Please enter the title, the day and starting time of the appointment you wish to delete: (Example: Gym Monday 11:00)\n")
      title,day,time = remove.split(" ")
      print(remove_appointment(day.lower().capitalize(),title.lower().capitalize(),time))
      
    if func == "show day":
      showDay = input("Please enter the day you wish to view.\n")
      print(show_day(showDay.lower().capitalize()))
    
    if func == "show week":
      show_week()
     
    #else:
      #print("Please enter a valid option")
    
    func = input()
    


main()
