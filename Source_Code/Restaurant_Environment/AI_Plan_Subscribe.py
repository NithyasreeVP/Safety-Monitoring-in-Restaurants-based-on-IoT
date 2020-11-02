import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

MQTT_SERVER = "192.168.0.107"
MQTT_PATH = "actuator"

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(26, GPIO.OUT, initial=GPIO.HIGH)
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    m_decode=str(msg.payload.decode("utf-8"))
    #print(m_decode)
    if "no_notifi" in m_decode:
        print("False1")
        GPIO.output(19, GPIO.LOW)
    else:
        print("True")
        GPIO.output(19, GPIO.HIGH)
    if "off_hvac" in m_decode:
        print("False2")
        GPIO.output(16, GPIO.LOW)
    else:
        print("True2")
        GPIO.output(16, GPIO.HIGH)
    if "close_window" in m_decode:
        print("False3")
        GPIO.output(8, GPIO.LOW)
    else:
        print("True3")
        GPIO.output(8, GPIO.HIGH)
    if "switchoff" in m_decode:
        print("False4")
        GPIO.output(26, GPIO.LOW)
    else:
        print("True4")
        GPIO.output(26, GPIO.HIGH)
    
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_SERVER, 1883, 60)
 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

