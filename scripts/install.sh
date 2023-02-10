#!/bin/bash
       OPTIONS="Englisch Deutsch Quit"
       select opt in $OPTIONS; do
           if [ "$opt" = "Englisch" ]; then
            echo "========= Moonraker-MQTT-plugin - Installation Script ==========="
            echo "========= Update the Subsystem ========="
            sudo apt update && sudo apt upgrade -y
            sudo apt install curl
            --version
            curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
            sudo python3 get-pip.py
            sudo pip3 install paho-mqtt
            sudo pip3 install requests
            sudo pip3 install ConfigParser         
            cp -i ~/Moonraker-MQTT-plugin/scripts/moonraker_mqtt.cfg ~/klipper_config
            echo "========= Installing successful ========="
            exit
           elif [ "$opt" = "Deutsch" ]; then
            echo "========= Moonraker-MQTT-plugin - Installations Script ==========="
            echo "========= Aktualisiere das System ========="
            sudo apt update && sudo apt upgrade -y
            sudo apt install curl
            --version
            curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
            sudo python3 get-pip.py
            sudo pip3 install paho-mqtt
            sudo pip3 install requests
            sudo pip3 install ConfigParser         
            cp -i ~/Moonraker-MQTT-plugin/scripts/moonraker_mqtt.cfg ~/klipper_config
            echo "========= Installation Abgeschlossen ========="
            exit
           elif [ "$opt" = "Quit" ]; then
            echo done
            exit
           else
            echo bad option
            exit
           fi
       done