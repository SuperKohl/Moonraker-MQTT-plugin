import time
import random
import time
import requests
import json
from configparser import ConfigParser
import paho.mqtt.client as paho
#cfg
cfgfile = ConfigParser()
cfgfile.read("/home/pi/klipper_config/moonraker_mqtt.cfg")
#var
broker = (cfgfile.get("Broker", "IP"))
topic = (cfgfile.get("MQTT-Config", "topic"))
#client_id = (cfgfile.get("MQTT-Config", "client_id"))
username = (cfgfile.get("Broker", "Username"))
password = (cfgfile.get("Broker", "Password"))


def on_message(client, userdata, message):
    time.sleep(1)
    print(f"Received `{message.payload.decode()}` from `{message.topic}` topic")
    if (message.topic) == (topic + "/gcode_controls/run"):
        requests.get(url="http://127.0.0.1/printer/gcode/script?script=" + str(message.payload.decode("utf-8")))
    #elif (message.topic) == "moonraker/gcode":
        #requests.get(url="http://127.0.0.1/printer/gcode/script?script=" + str(message.payload.decode("utf-8")))


client= paho.Client("client-001") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
client.on_message=on_message
print("connecting to broker ",broker)
client.username_pw_set(username, password)
client.connect(broker)
###subscribe###
print("subscribing ")
client.subscribe(topic + "/gcode_controls/run")
#client.subscribe(topic + "/printer_administration")
#client.subscribe(topic + "/printer_status")

while True:
    client.loop_start() #start loop to process received messages
    time.sleep(1)
    print("publishing ")
    #####host_information#####
    host_information = requests.get(url="http://127.0.0.1/printer/info")
    host_information_mqtt = host_information.json()
    client.publish(topic + "/status", str(host_information_mqtt ["result"] ["state"]))
    client.publish(topic + "/printer_status/info/hostname", str(host_information_mqtt ["result"] ["hostname"]))
    client.publish(topic + "/printer_status/info/software_version", str(host_information_mqtt ["result"] ["software_version"]))
    client.publish(topic + "/printer_status/info/cpu_info", str(host_information_mqtt ["result"] ["cpu_info"]))
    #####query_endstops#####
    query_endstops = requests.get(url="http://127.0.0.1/printer/query_endstops/status")
    query_endstops_mqtt = query_endstops.json()
    client.publish(topic + "/printer_status/query_endstops/query_endstop_x", str(query_endstops_mqtt ["result"] ["x"]))
    client.publish(topic + "/printer_status/query_endstops/query_endstop_y", str(query_endstops_mqtt ["result"] ["y"]))
    client.publish(topic + "/printer_status/query_endstops/query_endstop_z", str(query_endstops_mqtt ["result"] ["z"]))
    #####query_server_info#####
    query_server_info = requests.get(url="http://127.0.0.1/server/info")
    query_server_info_mqtt = query_server_info.json()
    client.publish(topic + "/printer_status/klipper/klippy_connected", str(query_server_info_mqtt ["result"] ["klippy_connected"]))
    client.publish(topic + "/printer_status/klipper/klippy_state", str(query_server_info_mqtt ["result"] ["klippy_state"]))
    #####file_operations#####
    #file_operations = requests.get(url="http://127.0.0.1/server/files/list?root=gcodes")
    #file_operations_mqtt = file_operations.json()
    #client.publish(topic + "/file_operations/files", (file_operations_mqtt ["result"] ["filename"]))

#/print_status/