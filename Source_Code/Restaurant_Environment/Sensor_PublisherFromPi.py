#Publisher
import time
from datetime import datetime
import json
import paho.mqtt.client as mqtt

from simulatedtempiot import TemperatureSensor
from simulatedhumiot import HumiditySensor
from simulatedlpgiot import MQ2Sensor
from simulatedweightiot import WeightSensor
from simulatedco2iot import CO2Sensor
from simulatedflameiot import FlameSensor


class Simulator:
    
    #interval
    def __init__(self,interval):
        self.interval = interval
    
    #instance to start the sensor    
    def start(self):
      ts = TemperatureSensor(30,10,16,35)
      ws = WeightSensor(28,30,15.3,29.5)
      ms = MQ2Sensor(2200,30,250,2500)
      hs = HumiditySensor(66, 10, 55, 75)
      cs = CO2Sensor(1900,10,350,2000)
      fs = FlameSensor(1,0,0,1)
      
      mqtt_publisher = mqtt.Client('Sensor publisher')
      mqtt_publisher.connect('192.168.0.107', 1883, 70)
      mqtt_publisher.loop_start()
      
      while True:
       dt = datetime.now().strftime("%H:%M:%S")
       message1 = {
       "type-id": "Restaurant.Kitchen." + ts.sensor_type,
       "instance-id": ts.instance_id,
       "timestamp": dt,
       "value": ts.sense()
       }
       jmsg1 = json.dumps(message1, indent=4)
       message2 = {
       "type-id": "Restaurant.Kitchen." + hs.sensor_type,
       "instance-id": hs.instance_id,
       "timestamp": dt,
       "value": hs.sense()
       }
       jmsg2 = json.dumps(message2, indent=4)
       message3 = {
       "type-id": "Restaurant.Kitchen." + ms.sensor_type,
       "instance-id": ms.instance_id,
       "timestamp": dt,
       "value": ms.sense()
       }
       jmsg3 = json.dumps(message3, indent=4)
       message4 = {
       "type-id": "Restaurant.Kitchen." + cs.sensor_type,
       "instance-id": cs.instance_id,
       "timestamp": dt,
       "value": cs.sense()
       }
       jmsg4 = json.dumps(message4, indent=4)
       message5 = {
       "type-id": "Restaurant.Kitchen." + ws.sensor_type,
       "instance-id": ws.instance_id,
       "timestamp": dt,
       "value": ws.sense()
       }
       jmsg5 = json.dumps(message5, indent=4)
       message6 = {
       "type-id": "Restaurant.Kitchen." + fs.sensor_type,
       "instance-id": fs.instance_id,
       "timestamp": dt,
       "value": fs.sense()
       }
       jmsg6 = json.dumps(message6, indent=4)
       
       mqtt_publisher.publish('Restaurant/' + ts.sensor_type + '/' + ts.instance_id, jmsg1, 2)
       mqtt_publisher.publish('Restaurant/' + hs.sensor_type + '/' + hs.instance_id, jmsg2, 2)
       mqtt_publisher.publish('Restaurant/' + ms.sensor_type + '/' + ms.instance_id, jmsg3, 2)
       mqtt_publisher.publish('Restaurant/' + cs.sensor_type + '/' + cs.instance_id, jmsg4, 2)
       mqtt_publisher.publish('Restaurant/' + ws.sensor_type + '/' + ws.instance_id, jmsg5, 2)
       mqtt_publisher.publish('Restaurant/' + fs.sensor_type + '/' + fs.instance_id, jmsg6, 2)
       print(message1)
       print(message2)
       print(message3)
       print(message4)
       print(message5)
       print(message6)
       time.sleep(self.interval)
            
#instance of the simulator
s = Simulator(5);
s.start()
