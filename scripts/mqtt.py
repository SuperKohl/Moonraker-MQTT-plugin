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
host_information = requests.get(url="http://127.0.0.1/printer/info")
host_information_json = host_information.json()
#####printer_objects#####
printer_objects = requests.get(url="http://127.0.0.1/printer/objects/list")
printer_objects_json = printer_objects.json()
#####_#####


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
    while True:
        time.sleep(10)
        result = client.publish(topic + "/stat", str(host_information_json ["result"] ["state_message"]))
        status = result[0]






def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()