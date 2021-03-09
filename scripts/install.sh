#!/bin/bash
       OPTIONS="Englisch Deutsch Quit"
       select opt in $OPTIONS; do
           if [ "$opt" = "Englisch" ]; then
            echo "========= moonraker-mqtt-plugin - Installation Script ==========="
            echo "========= Install the Subsystem ========="
            sudo apt update && sudo apt upgrade
            sudo apt install curl
            curl --version
            curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
            python3 get-pip.py
            pip3 install paho-mqtt
            pip3 install requests
            pip3 install ConfigParser            
            touch /home/pi/klipper_config/moonraker_mqtt.cfg
            echo "========= Installing the Subsystem successful ========="
           elif [ "$opt" = "Deutsch" ]; then
            echo "========= Moonraker-MQTT-plugin - Installations Script ==========="
            echo "========= Installiere MQTT moonraker Plugin ========="
            sudo apt update && sudo apt upgrade
            echo "========= Installiere curl und pip ========="
            sudo apt install curl
            curl --version
            curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
            python3 get-pip.py
            pip3 install paho-mqtt
            pip3 install requests
            pip3 install ConfigParser
            touch /home/pi/klipper_config/moonraker_mqtt.cfg
            echo "========= Installieren des Basissystems Erfolgreich Abgeschlossen ========="
           elif [ "$opt" = "Quit" ]; then
            echo done
            exit
           else
            echo bad option
           fi
       done