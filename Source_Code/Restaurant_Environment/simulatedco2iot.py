from random import random

import numpy as np


class CO2Sensor:
    sensor_type = "co2"
    unit="ppm" 
    instance_id="284h62gsj"
    
     #initialisation
              
    def __init__(self, average_co2, co2_variation, min_co2, max_co2):
        self.average_co2 = average_co2
        self.co2_variation = co2_variation
        self.min_co2 = min_co2       
        self.max_co2= max_co2
        self.value = 0.0 #initialise current temp value
        
    #sensing 
    def sense(self):
        #self.value = self.value + self.simple_random()
        self.value = self.complex_random() + self.noise()
        return self.value
        
    #noise
    def noise(self):
        self.noise_value = np.random.normal(0,25)
        return self.noise_value
    
    #helper function for generating values with min temp as its base
    def simple_random(self):
        value = self.min_co2 + (random() * (self.max_co2 - self.min_co2)) #so that it is in the range
        return value
    
    def complex_random(self):
        value = self.average_co2 * (1 + (self.co2_variation/100) * (1 * random() -1))
        value = max(value,self.min_co2)
        value = min(value,self.max_co2)
        return value
    
#creating instance of sensor
cs = CO2Sensor(400,10,350,2000)


