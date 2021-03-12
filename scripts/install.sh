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
            cp -i /home/pi/moonraker-MQTT-plugin/scripts/Moonraker_mqtt.cfg /home/pi/klipper_config
            echo "========= Installing the Subsystem successful ========="
            exit
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
            cp -i /home/pi/moonraker-MQTT-plugin/scripts/Moonraker_mqtt.cfg /home/pi/klipper_config
            echo "========= Installieren des Basissystems Erfolgreich Abgeschlossen ========="
            exit
           elif [ "$opt" = "Quit" ]; then
            echo done
            exit
           else
            echo bad option
            exit
           fi
       done



#description