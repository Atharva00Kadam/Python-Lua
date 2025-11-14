# Author   : Atharva Kadam
# Email    : aakdam@umass.edu
# Spire ID : 12345678

#it is something like 'time'-> temperature
class Thermostat:
  def __init__(self, default_temp=68):
    self.default_temp = default_temp
    self.the_schedule = {}
 
  def add_schedule(self, time, temp):
    self.the_schedule[f'{time}'] = temp
    print(self.the_schedule)
   
  def __str__(self):
    return (f"Default temperature: {default_temp} degrees {{[time] i[time] 'degrees'} for i in self.the_schedule}")
   
  def get_target_temperature(self, arbit_time):
    the_list = sorted(list(self.schedule))
    the_new_list = []
    # [key, value, key, value]
    for i in the_list:
      if i % 2 != 0:
        the_new_list.append(i)
        if (i) <= arbit_time < (i + 1)
          return temp
        elif i[0]:
          return default_temp

   
   
   
dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
print(dev.__str__())
