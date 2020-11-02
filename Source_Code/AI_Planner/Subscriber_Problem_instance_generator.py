import paho.mqtt.client as mqtt
import time
import json
import re

def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection
        mqtt_subscriber.subscribe("Restaurant/#") #subscribe multiple topics    
 
    else:
 
        print("Connection failed")
 
def on_message(client, userdata, message):
    print("On_Message invoked")
    #Filter the messages based on topic
    topic=message.topic   
    if topic == "Restaurant/temperature/283h62gsj":
        sub_cb_temp(topic, message)
    elif topic =="Restaurant/humidity/281h62gsj":
        sub_cb_humidity(topic, message)
    elif topic =="Restaurant/gas/282h62gsj":
        sub_cb_gas(topic, message)
    elif topic =="Restaurant/co2/284h62gsj":
        sub_cb_co2(topic, message)
    elif topic =="Restaurant/weight/285h62gsj":
        sub_cb_weight(topic, message)
    elif topic =="Restaurant/flame/286h62gsj":
        sub_cb_flame(topic, message)
       
        
def sub_cb_temp(topic, message):
    print("Temperature topic decoded")
    m_temp_decode=str(message.payload.decode("utf-8","ignore"))
    m_temp_in=json.loads(m_temp_decode) #decode json data
    print(m_temp_in)
    m_temp = str(m_temp_in['value']) #Extract the sensor value from json message
    
    #Updating Load cell sensor values in problem.pddl
    def write_to_pddl():        
        f = open('C:\\Users\\TOSHIBA\\MQTT_PUBLISHER\\problem.pddl', 'r')
        print(f)
        line = f.read() 
        print("Opened the file")
        #print(line)
        line_new = re.sub(r'temp r1\) ([0-9]+\.\d+)', r'temp r1) '+m_temp, line)
        f.close()
        print("Going to replace_Temperature")
        f = open('C:\\Users\\TOSHIBA\\MQTT_PUBLISHER\\problem.pddl', 'w')
        f.write(line_new)
        print(line_new)
        f.close()
    write_to_pddl()        
    
def sub_cb_humidity(topic, message):
    m_Hum_decode=str(message.payload.decode("utf-8","ignore"))
    m_Hum_in=json.loads(m_Hum_decode) #decode json data
    print(m_Hum_in)
    m_Hum = str(m_Hum_in['value']) #Extract the sensor value from json message
    
    #Updating Load cell sensor values in problem.pddl
    def write_to_pddl():  
        f = open('C:\\Users\\TOSHIBA\\MQTT_PUBLISHER\\problem.pddl', 'r')
        print(f)
        line = f.read() 
        print("Opened the file")
        #print(line)
        line_new = re.sub(r'hum r1\) ([0-9]+\.\d+)', r'hum r1) '+m_temp, line)
        f.close()
        f = open('C:\\Users\\TOSHIBA\\MQTT_PUBLISHER\\problem.pddl', 'w')
        f.write(line_new)
        print(line_new)
        f.close()
    write_to_pddl()        
    
def sub_cb_gas(topic, message):
    m_Gas_decode=str(message.payload.decode("utf-8","ignore"))
    m_Gas_in=json.loads(m_Gas_decode) #decode json data
    print(m_Gas_in)
    m_Gas = str(m_Gas_in['value']) #Extract the sensor value from json message
    
    #Updating Load cell sensor values in problem.pddl
    def write_to_pddl():  
        f = open('C:\\Users\\TOSHIBA\\MQTT_PUBLISHER\\problem.pddl', 'r')
        print(f)
        line = f.read() 
        print("Opened the file")
        #print(line)
        line_new = re.sub(r'lpg r1\) ([0-9]+\.\d+)', r'lpg r1) '+m_Gas, line)
        f.close()
        f = open('C:\\Users\\TOSHIBA\\MQTT_PUBLISHER\\problem.pddl', 'w')
        f.write(line_new)
        print(line_new)
        f.close()
    write_to_pddl()

def sub_cb_co2(topic, message):
    m_co2_decode=str(message.payload.decode("utf-8","ignore"))
    m_co2_in=json.loads(m_co2_decode) #decode json data
    print(m_co2_in)
    m_co2 = str(m_co2_in['value'])  #Extract the sensor value from json message
    
    #Updating Load cell sensor values in problem.pddl
    def write_to_pddl():  
        f = open('C:\\Users\\TOSHIBA\\MQTT_PUBLISHER\\problem.pddl', 'r')
        print(f)
        line = f.read() 
        print("Opened the file")
        #print(line)
        line_new = re.sub(r'co2 r1\) ([0-9]+\.\d+)', r'co2 r1) '+m_co2, line)
        f.close()
        f = open('C:\\Users\\TOSHIBA\\MQTT_PUBLISHER\\problem.pddl', 'w')
        f.write(line_new)
        print(line_new)
        f.close()
    write_to_pddl() 

def sub_cb_weight(topic, message):
    m_load_decode=str(message.payload.decode("utf-8","ignore"))
    m_load_in=json.loads(m_load_decode) #decode json data
    print(m_load_in)
    m_load = str(m_load_in['value'])  #Extract the sensor value from json message
    
    #Updating Load cell sensor values in problem.pddl
    def write_to_pddl():  
        f = open('C:\\Users\\TOSHIBA\\MQTT_PUBLISHER\\problem.pddl', 'r')
        print(f)
        line = f.read() 
        print("Opened the file")
        #print(line)
        line_new = re.sub(r'weight r1\) ([0-9]+\.\d+)', r'weight r1) '+m_load, line)
        f.close()
        f = open('C:\\Users\\TOSHIBA\\MQTT_PUBLISHER\\problem.pddl', 'w')
        f.write(line_new)
        print(line_new)
        f.close()
    write_to_pddl() 
    
def sub_cb_flame(topic, message):
    m_flame_decode = str(message.payload.decode("utf-8","ignore"))
    m_load_in=json.loads(m_load_decode) #decode json data
    print(m_load_in)
    m_load = str(m_load_in['value'])  #Extract the sensor value from json message
    
    #Updating Load cell sensor values in problem.pddl
    def write_to_pddl():  
        f = open('C:\\Users\\TOSHIBA\\MQTT_PUBLISHER\\problem.pddl', 'r')
        print(f)
        line = f.read() 
        print("Opened the file")
        #print(line)
        line_new = re.sub(r'weight r1\) ([0-9]+)', r'weight r1) '+m_load, line)
        f.close()
        f = open('C:\\Users\\TOSHIBA\\MQTT_PUBLISHER\\problem.pddl', 'w')
        f.write(line_new)
        print(line_new)
        f.close()
    write_to_pddl()
  
Connected = False   #global variable for the state of the connection
 
broker_address= "192.168.0.107"  #Broker address
port = 1883                      #Broker port

mqtt_subscriber = mqtt.Client()             #create new instance    
mqtt_subscriber.on_connect= on_connect      #attach function to callback
mqtt_subscriber.on_message= on_message      #attach function to callback
 
mqtt_subscriber.connect(broker_address, port=port, keepalive=70)   #connect to broker
 
mqtt_subscriber.loop_forever()        #start the loop
 
