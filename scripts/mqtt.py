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
client_id = (cfgfile.get("MQTT-Config", "client_id"))
username = (cfgfile.get("Broker", "Username"))
password = (cfgfile.get("Broker", "Password"))
refresh_time = (cfgfile.get("MQTT-Config", "refresh_time"))


def on_message(client, userdata, message):
    time.sleep(1)
    if (message.topic) == (topic + "/control/run_gcode"):
        requests.get(url="http://127.0.0.1/printer/gcode/script?script=" + str(message.payload.decode("utf-8")))

client= paho.Client(client_id)
client.on_message=on_message
client.username_pw_set(username, password)
client.connect(broker)
client.publish(topic + "/status", "")
client.publish(topic + "/control/run_gcode", "")
client.subscribe(topic + "/control/run_gcode")
client.loop_start()

while True:
    time.sleep(int(refresh_time))
    ####Get Status#####
    octoprint_api = requests.get(url="http://127.0.0.1/api/printer")
    octoprint_api_mqtt = octoprint_api.json()
    host_information = requests.get(url="http://127.0.0.1/printer/info")
    host_information_mqtt = host_information.json()
    query_endstops = requests.get(url="http://127.0.0.1/printer/query_endstops/status")
    query_endstops_mqtt = query_endstops.json()
    query_server_info = requests.get(url="http://127.0.0.1/server/info")
    query_server_info_mqtt = query_server_info.json()
    file_operations = requests.get(url="http://127.0.0.1/server/files/list?root=gcodes")
    file_operations_mqtt = file_operations.json()
    if str(octoprint_api_mqtt ["state"] ["flags"] ["paused"]) == "True":
        client.publish(topic + "/status", "paused")
    elif str(octoprint_api_mqtt ["state"] ["flags"] ["printing"]) == "True":
        client.publish(topic + "/status", "printing")
    elif str(octoprint_api_mqtt ["state"] ["flags"] ["ready"]) == "True":
        client.publish(topic + "/status", "ready")
    client.publish(topic + "/printer_status/info/hostname", str(host_information_mqtt ["result"] ["hostname"]))
    client.publish(topic + "/printer_status/info/software_version", str(host_information_mqtt ["result"] ["software_version"]))
    client.publish(topic + "/printer_status/info/cpu_info", str(host_information_mqtt ["result"] ["cpu_info"])) 
    client.publish(topic + "/printer_status/klipper/klippy_connected", str(query_server_info_mqtt ["result"] ["klippy_connected"]))
    client.publish(topic + "/printer_status/klipper/klippy_state", str(query_server_info_mqtt ["result"] ["klippy_state"]))
    client.publish(topic + "/printer_status/temperature/bed/actual", str(octoprint_api_mqtt ["temperature"] ["bed"] ["actual"]))
    client.publish(topic + "/printer_status/temperature/bed/target", str(octoprint_api_mqtt ["temperature"] ["bed"] ["target"]))
    client.publish(topic + "/printer_status/temperature/tool0/actual", str(octoprint_api_mqtt ["temperature"] ["tool0"] ["actual"]))
    client.publish(topic + "/printer_status/temperature/tool0/target", str(octoprint_api_mqtt ["temperature"] ["tool0"] ["target"]))  
    client.publish(topic + "/printer_status/query_endstops/query_endstop_x", str(query_endstops_mqtt ["result"] ["x"]))
    client.publish(topic + "/printer_status/query_endstops/query_endstop_y", str(query_endstops_mqtt ["result"] ["y"]))
    client.publish(topic + "/printer_status/query_endstops/query_endstop_z", str(query_endstops_mqtt ["result"] ["z"]))
    #client.publish(topic + "/file_operations/files", (file_operations_mqtt ["result"] ["filename"]))