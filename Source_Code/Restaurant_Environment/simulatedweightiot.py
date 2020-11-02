from random import random

import numpy as np


class WeightSensor:
    sensor_type = "weight"
    unit="kg" 
    instance_id="285h62gsj"
    
     #initialisation
              
    def __init__(self, average_weight, weight_variation, min_weight, max_weight):
        self.average_weight = average_weight
        self.weight_variation = weight_variation
        self.min_weight = min_weight       
        self.max_weight= max_weight
        self.value = 0.0 #initialise current temp value
        
    #sensing 
    def sense(self):
        #self.value = self.value + self.simple_random()
        self.value = self.complex_random() + self.noise()
        return self.value
    
    #noise
    def noise(self):
        self.noise_value = np.random.normal(0,0.5)
        return self.noise_value
        
    #helper function for generating values with min temp as its base
    def simple_random(self):
        value = self.min_weight + (random() * (self.max_weight - self.min_weight)) #so that it is in the range
        return value
    
    def complex_random(self):
        value = self.average_weight * (1 + (self.weight_variation/100) * (1 * random() -1))
        value = max(value,self.min_weight)
        value = min(value,self.max_weight)
        return value
    
#creating instance of sensor
ws = WeightSensor(25,30,15.3,29.5)


