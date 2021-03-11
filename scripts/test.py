#bibs
import random
import time
import requests
import json
from configparser import ConfigParser
from paho.mqtt import client as mqtt_client
#cfg
cfgfile = ConfigParser()
cfgfile.read("/home/pi/klipper_config/moonraker_mqtt.cfg")
#var
broker = (cfgfile.get("Broker", "IP"))
port = 1883
topic = (cfgfile.get("MQTT-Config", "topic"))
client_id = (cfgfile.get("MQTT-Config", "client_id"))
username = (cfgfile.get("Broker", "Username"))
password = (cfgfile.get("Broker", "Password"))
##########_TELE_##########
#####host_information#####
#requests.get(url="http://127.0.0.1/printer/gcode/script?script=" + "G28")
#host_information_mqtt = host_information.json()
#####query_endstops#####
#query_endstops = requests.get(url="http://127.0.0.1/printer/query_endstops/status")
#query_endstops_mqtt = query_endstops.json()

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client
    
def publish(client):
    time.sleep(1)
    host_information = requests.get(url="http://127.0.0.1/printer/info")
    host_information_mqtt = host_information.json()
    client.publish(topic + "/connected", str(host_information_mqtt ["result"] ["state_message"]))
    query_endstops = requests.get(url="http://127.0.0.1/printer/query_endstops/status")
    query_endstops_mqtt = query_endstops.json()
    client.publish(topic + "/status/query_endstop_x", str(query_endstops_mqtt ["result"] ["x"]))
    client.publish(topic + "/status/query_endstop_y", str(query_endstops_mqtt ["result"] ["y"]))
    client.publish(topic + "/status/query_endstop_z", str(query_endstops_mqtt ["result"] ["z"]))      

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

def lololoop():
    client = connect_mqtt()
    while True:
        time.sleep(1)
        publish(client)
        subscribe(client)
        
def run():
    client = connect_mqtt()
    #subscribe(client)
    lololoop()
    #client.loop_forever()
    client.loop_start()

if __name__ == '__main__':
    run()

