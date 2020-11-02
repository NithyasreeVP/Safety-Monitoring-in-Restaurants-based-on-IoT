import paho.mqtt.client as mqtt
import time
import json
import csv

def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection
        mqtt_subscriber.subscribe("Restaurant/#")     #subscribe multiple topics    
 
    else:
 
        print("Connection failed")
 
def on_message(client, userdata, message):
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
    m_temp_decode=str(message.payload.decode("utf-8","ignore"))
    m_temp_in=json.loads(m_temp_decode) #decode json data
    print(m_temp_in)
    y1 = m_temp_in['value']
    x1 = m_temp_in['timestamp']
    
    def write_to_csv():
        with open('temp_readings3.csv', mode='a') as temp_readings:
            temp_write = csv.writer(temp_readings, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            write_to_log = temp_write.writerow([x1,y1])
            return(write_to_log)
    write_to_csv()
    
def sub_cb_humidity(topic, message):
    m_hum_decode=str(message.payload.decode("utf-8","ignore"))
    m_hum_in=json.loads(m_hum_decode) #decode json data
    print(m_hum_in)
    y2 = m_hum_in['value']
    x2 = m_hum_in['timestamp']
    
    def write_to_csv():
        with open('hum_readings3.csv', mode='a') as hum_readings:
            hum_write = csv.writer(hum_readings, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            write_to_log = hum_write.writerow([x2,y2])
            return(write_to_log)
    write_to_csv()
    
def sub_cb_gas(topic, message):
    m_gas_decode=str(message.payload.decode("utf-8","ignore"))
    m_gas_in=json.loads(m_gas_decode) #decode json data
    print(m_gas_in)
    y3 = m_gas_in['value']
    x3 = m_gas_in['timestamp']
    
    def write_to_csv():
        with open('gas_readings3.csv', mode='a') as gas_readings:
            gas_write = csv.writer(gas_readings, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            write_to_log = gas_write.writerow([x3,y3])
            return(write_to_log)
    write_to_csv()
    
def sub_cb_co2(topic, message):
    m_co2_decode=str(message.payload.decode("utf-8","ignore"))
    m_co2_in=json.loads(m_co2_decode) #decode json data
    print(m_co2_in)
    y4 = m_co2_in['value']
    x4 = m_co2_in['timestamp']
    
    def write_to_csv():
        with open('co2_readings3.csv', mode='a') as co2_readings:
            co2_write = csv.writer(co2_readings, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            write_to_log = co2_write.writerow([x4,y4])
            return(write_to_log)
    write_to_csv()
    
def sub_cb_weight(topic, message):
    m_weight_decode=str(message.payload.decode("utf-8","ignore"))
    m_weight_in=json.loads(m_weight_decode) #decode json data
    print(m_weight_in)
    y5 = m_weight_in['value']
    x5 = m_weight_in['timestamp']
    
    def write_to_csv():
        with open('weight_readings3.csv', mode='a') as weight_readings:
            weight_write = csv.writer(weight_readings, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            write_to_log = weight_write.writerow([x5,y5])
            return(write_to_log)
    write_to_csv()
    
def sub_cb_flame(topic, message):
    m_flame_decode=str(message.payload.decode("utf-8","ignore"))
    m_flame_in=json.loads(m_flame_decode) #decode json data
    print(m_flame_in)
    y6 = m_flame_in['value']
    x6 = m_flame_in['timestamp']
    
    def write_to_csv():
        with open('flame_readings3.csv', mode='a') as weight_readings:
            flame_write = csv.writer(weight_readings, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            write_to_log = flame_write.writerow([x6,y6])
            return(write_to_log)
    write_to_csv()
 
Connected = False   #global variable for the state of the connection
 
broker_address= "192.168.0.107"  #Broker address
port = 1883                         #Broker port
user = "pi"                    #Connection username
password = "pi123"            #Connection password
 
mqtt_subscriber = mqtt.Client()               #create new instance
mqtt_subscriber.on_connect= on_connect                      #attach function to callback
mqtt_subscriber.on_message= on_message                      #attach function to callback
 
mqtt_subscriber.connect(broker_address, port=port, keepalive=70)          #connect to broker
 
mqtt_subscriber.loop_forever()        #start the loop