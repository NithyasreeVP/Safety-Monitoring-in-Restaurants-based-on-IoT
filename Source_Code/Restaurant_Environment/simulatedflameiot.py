from random import random
import math


class FlameSensor:
    sensor_type = "flame"
    unit="no unit"
    instance_id="286h62gsj"
    
     #initialisation
              
    def __init__(self, average_flame, flame_variation, min_flame, max_flame):
        self.average_flame = average_flame
        self.flame_variation = flame_variation
        self.min_flame = min_flame       
        self.max_flame= max_flame
        self.value = 0.0 #initialise current temp value
        
    #sensing 
    def sense(self):
        self.value = self.value + self.simple_random()
        self.value = math.floor(self.value)
        return self.value
    
      
    #helper function for generating values with min temp as its base
    def simple_random(self):
        value = self.min_flame + (random() * (self.max_flame - self.min_flame)) #so that it is in the range
        return value
    
    
    
#creating instance of sensor
fs = FlameSensor(0,0,0,1)
print(fs.sense())




