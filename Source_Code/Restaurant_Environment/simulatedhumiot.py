from random import random

import numpy as np


class HumiditySensor:
    sensor_type = "humidity"
    unit="percentage"
    instance_id="281h62gsj"
    
     #initialisation
              
    def __init__(self, average_humidity, humidity_variation, min_humidity, max_humidity):
        self.average_humidity = average_humidity
        self.humidity_variation = humidity_variation
        self.min_humidity = min_humidity       
        self.max_humidity= max_humidity
        self.value = 0.0 #initialise current temp value
        
    #sensing 
    def sense(self):
        #self.value = self.value + self.simple_random()
        self.value = self.complex_random() + self.noise()
        return self.value
    
    #noise
    def noise(self):
        self.noise_value = np.random.normal(0,2)
        return self.noise_value
    
    #helper function for generating values with min temp as its base
    def simple_random(self):
        value = self.min_humidity + (random() * (self.max_humidity - self.min_humidity)) #so that it is in the range
        return value
    
    def complex_random(self):
        value = self.average_humidity * (1 + (self.humidity_variation/100) * (1 * random() -1))
        value = max(value,self.min_humidity)
        value = min(value,self.max_humidity)
        return value
    
#creating instance of sensor
hs = HumiditySensor(65, 10, 55, 75)


