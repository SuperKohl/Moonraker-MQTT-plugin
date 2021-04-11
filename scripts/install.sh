#!/bin/bash
       OPTIONS="Englisch Deutsch Quit"
       select opt in $OPTIONS; do
           if [ "$opt" = "Englisch" ]; then
            echo "========= Moonraker-MQTT-plugin - Installation Script ==========="
            echo "========= Update the Subsystem ========="
            sudo apt update && sudo apt upgrade -y
            echo "========= Install Curl ========="
            sudo apt install curl
            curl --version
            echo "========= Install pip ========="
            sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
            sudo python3 get-pip.py
            sudo pip3 install paho-mqtt
            sudo pip3 install requests
            sudo pip3 install ConfigParser
            echo "========= Copy the Config file ========="           
            cp -i /home/pi/Moonraker-MQTT-plugin/scripts/moonraker_mqtt.cfg /home/pi/klipper_config
            echo "========= Installing successful ========="
            exit
           elif [ "$opt" = "Deutsch" ]; then
            echo "========= Moonraker-MQTT-plugin - Installations Script ==========="
            echo "========= Update das Betiebssystem ========="
            sudo apt update && sudo apt upgrade -y
            echo "========= Installiere Curl ========="
            sudo apt install curl
            curl --version
            echo "========= Installiere pip ========="
            sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
            sudo python3 get-pip.py
            sudo pip3 install paho-mqtt
            sudo pip3 install requests
            sudo pip3 install ConfigParser
            echo "========= Kopiere die Config Datei ========="           
            cp -i /home/pi/Moonraker-MQTT-plugin/scripts/moonraker_mqtt.cfg /home/pi/klipper_config
            echo "========= Insterllation Abgeschlossen ========="
            exit
           elif [ "$opt" = "Quit" ]; then
            echo done
            exit
           else
            echo bad option
            exit
           fi
       done