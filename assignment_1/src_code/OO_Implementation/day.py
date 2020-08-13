from appointment import Appointment

class Day:

  def __init__(self, name, appointments=None):
    if appointments is None:
      self.appointments = []
    self.name = name
    
  def add_appointment(self, new):
    #before adding a new appointment for that day, check it doesnt overlap with any others
    #if new.starttime
    for app in self.appointments:
      if new.overlap(app):
        print("This appointment clashes with a pre-existing appointment, try again or remove the other appointment.")
    self.appointments.append(new)
    print("Appointment added successfully.")
    

  def remove_appointment(self, appointment):
  
    found = False
    for i, app in enumerate(self.appointments):
      if app.title == appointment.title and app.start_time == appointment.start_time and found != True:
        del self.appointments[i]
        print("Appointment has been successfully deleted") 
        found = True
        
    if found == False:
      print("Appointment does not exist")
    
  def order_appointments(self):
    self.appointments.sort(key=lambda x: x.minutes(x.start_time), reverse=False)
    
  #return the list of appointments for that day as a string, formatted with \n
  def __str__(self):
    output = ""
    self.order_appointments()
    
    if len(self.appointments) != 0 :
      for appointment in self.appointments:
      #function to sort these appointment according to TIME? remember in first year i did something like this for races.. look at that
        output += "- " + appointment.__str__() + "\n"
    else:
      output += "- You have no scheduled appointments for this day"
      
    output = output.strip() #remove the extra newline at end
    return output
