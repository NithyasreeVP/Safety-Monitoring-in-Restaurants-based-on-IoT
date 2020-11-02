from random import random

import numpy as np


class MQ2Sensor:
    sensor_type = "gas"
    unit="ppm"
    instance_id="282h62gsj"
    
     #initialisation
              
    def __init__(self, average_gas, gas_variation, min_gas, max_gas):
        self.average_gas = average_gas
        self.gas_variation = gas_variation
        self.min_gas = min_gas       
        self.max_gas= max_gas
        self.value = 0.0 #initialise current temp value
        
    #sensing 
    def sense(self):
        #self.value = self.value + self.simple_random()
        self.value = self.complex_random() + self.noise()
        return self.value
    
    #noise
    def noise(self):
        self.noise_value = np.random.normal(0,15)
        return self.noise_value
    
    #helper function for generating values with min temp as its base
    def simple_random(self):
        value = self.min_gas + (random() * (self.max_gas - self.min_gas)) #so that it is in the range
        return value
    
    def complex_random(self):
        value = self.average_gas * (1 + (self.gas_variation/100) * (1 * random() -1))
        value = max(value,self.min_gas)
        value = min(value,self.max_gas)
        return value
    
#creating instance of sensor
ms = MQ2Sensor(250,10,200, 2500)





