import paho.mqtt.client as paho
import time

broker = "192.168.0.107"
topic = "actuator"
port = 1883

def on_publish(client,userdata,result):
    print("published data is : ")
    pass

client1 = paho.Client("control1")
client1.on_publish = on_publish
client1.connect(broker,port,keepalive=70) 

while True:
    myfile = open("plan.ipc", "rt") # open lorem.txt for reading text
    payload = myfile.read()         # read the entire file to string
    myfile.close()   
   
   
    ret = client1.publish(topic,payload)
  
    print(payload);
    print("Please check data on your Subscriber \n")
    time.sleep(5)