class Appointment:
  #each parameter is type string
  def __init__(self, title, start_time, end_time):
    self.title = title
    self.start_time = start_time
    self.end_time = end_time    
      
  def minutes(self, time):
    # use this to check the minutes arent the same the appointments because adding
    total = 0 
    hours, mins = time.split(":")
    hours = int(hours) * 60
    total = hours + int(mins)
    return total
    
    
  def time_check(self, time):
    #format check, must be HH:MM, even 9 AM for example, must be inputted as 09:00
    if((time[2] == ":") and (len(time) == 5)):
      hours, mins = time.split(':')
    else:
      return False  
    
    #hour and mins check
    
    if (len(hours) == 2 and hours.isdigit()) and (len(mins) == 2 and hours.isdigit()):
      if (int(hours) <= 23 and int(hours) >= 0) and (int(mins) <= 23 and int(mins) >= 0):
        return True
      else: 
        return False
    else:
      return False


  def overlap(self,other):
    if self.minutes(self.end_time) < other.minutes(other.start_time) or self.minutes(self.start_time) > other.minutes(other.end_time):
      return False
    return True
    
  def __str__(self):
    output = "Title: {}, Duration: {} to {}.".format(self.title, self.start_time, self.end_time)
    return output