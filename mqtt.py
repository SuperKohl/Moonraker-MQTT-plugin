#bibs
import random
import time
from configparser import ConfigParser
from paho.mqtt import client as mqtt_client
#cfg
cfgfile = ConfigParser()
cfgfile.read("/home/pi/klipper_config/moonraker_mqtt.cfg")
#var
broker = (cfgfile.get("Broker", "IP"))    #'192.168.178.130'
port = 1883
topic = (cfgfile.get("MQTT-Config", "topic"))
client_id = (cfgfile.get("MQTT-Config", "client_id"))
username = (cfgfile.get("Broker", "Username"))
password = (cfgfile.get("Broker", "Password"))

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
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()