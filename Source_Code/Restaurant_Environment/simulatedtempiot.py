from random import random

import numpy as np

class TemperatureSensor:
    sensor_type = "temperature"
    unit="celsius"
    instance_id="283h62gsj"
    
     #initialisation
              
    def __init__(self, average_temperature, temperature_variation, min_temperature, max_temperature):
        self.average_temperature = average_temperature
        self.temperature_variation = temperature_variation
        self.min_temperature = min_temperature       
        self.max_temperature= max_temperature
        self.value = 0.0 #initialise current temp value
        
    #sensing 
    def sense(self):
        #self.value = self.value + self.simple_random()
        self.value = self.complex_random() + self.noise()
        return self.value
    
    #noise
    def noise(self):
        self.noise_value = np.random.normal(0,1)
        return self.noise_value
        
    #helper function for generating values with min temp as its base
    def simple_random(self):
        value = self.min_temperature + (random() * (self.max_temperature - self.min_temperature)) #so that it is in the range
        return value
        
    def complex_random(self):
        value = self.average_temperature * (1 + (self.temperature_variation/100) * (1 * random() -1))
        value = max(value,self.min_temperature)
        value = min(value,self.max_temperature)
        return value
    
#creating instance of sensor
ts = TemperatureSensor(25,10,16,35)

