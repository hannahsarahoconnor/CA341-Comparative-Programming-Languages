from day import Day

class Calendar:
  #dictionary 
  def __init__(self):
    self.week = {"Monday": Day("Monday"),
            "Tuesday": Day("Tuesday"),
            "Wednesday": Day("Wednesday") ,
            "Thursday": Day("Thursday"),
            "Friday": Day("Friday"),
            "Saturday": Day("Saturday"),
            "Sunday":Day("Sunday"), }
            
 #use ___str__ to print out the days in the week and their list of appointments
   
  def __str__(self):
    output = "" 
    for day in self.week:
        output += "\n      " + day + "\n ------------------- \n" + self.week[day].__str__() + "\n"
    return output

