<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/SuperKohl/Moonraker-MQTT-plugin">
    <img src="https://github.com/SuperKohl/Moonraker-MQTT-plugin/blob/master/images/logo.PNG" alt="Logo" width="158,5" height="116.6">
  </a>

  <h3 align="center">Moonraker-MQTT-plugin</h3>

  <p align="center">
    Ein MQTT Plugin für die moonraker API
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Siehe das Wiki »</strong></a>
    <br />
    <br />
    <a href="https://github.com/SuperKohl/Moonraker-MQTT-plugin/issues">Report Bug</a>
    ·
    <a href="https://github.com/SuperKohl/Moonraker-MQTT-plugin/issues">Request Feature</a>
  </p>
</p>


<!-- Inhaltsverzeichnis -->
<details open="open">
  <summary>Inhaltsverzeichnis</summary>
  <ol>
    <li>
      <a href="#Über-das-Projekt">Über das Projekt</a>
      <ul>
        <li><a href="#Programmiert-mit">Programmiert mit</a></li>
      </ul>
    </li>
    <li>
      <a href="#Installieren">Installieren</a>
      <ul>
        <li><a href="#Voraussetzungen">Voraussetzungen</a></li>
        <li><a href="#Installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#Nutzung">Nutzung</a></li>
    <li><a href="#Zukünftige-Änderungen">Zukünftige Änderungen</a></li>
    <li><a href="#Lizenz">Lizenz</a></li>
    <li><a href="#Kontakt">Kontakt</a></li>
    <li><a href="#Danksagungen">Danksagungen</a></li>
  </ol>
</details>



<!-- Über das Projekt -->
## Über das Projekt

Ein Skript/Programm zum Überwachen/Steuern des Druckers vor, während und nach einem Druck über das MQTT Protokoll.

### Programmiert mit

Das Plugin wurde Programmiert mit:
* [Python3](https://www.python.org/)
* [Jsonl](https://www.json.org/)
* [Bash](https://www.gnu.org/software/bash/)

<!-- Installieren -->
## Installieren

### Voraussetzungen

Vorausgesetzt wird eins der Betriebssyteme:
* [MainsailOS](https://github.com/meteyou/mainsail)
* [Fluidd](https://github.com/cadriel/fluidd)

### Installation

1. Gehe in das Verzeichnis: /home/pi
   ```sh
   cd /home/pi
   ```
2. Clone das Repository
	```sh
   git clone https://github.com/SuperKohl/Moonraker-MQTT-plugin.git
   ```
3. Führe das Installation-Script aus: bash ./Moonraker-MQTT-plugin/scripts/install.sh
	```sh
   bash ./Moonraker-MQTT-plugin/scripts/install.sh
   ```
4. Füge in der moonraker.conf die Zeile [octoprint_compat] hinzu
	
	In MainsailOS:
	1. Gehe zu Mainsail -> Settings -> Maschine
	2. Klicke auf die Datei moonraker.conf
	3. Füge am Ende die zeile [octoprint_compat] hinzu	
	4. Klicke oben Rechts auf Save

	In Fluidd:
	1. Gehe zu  Mainsail -> Printer -> config
	2. Klicke auf die Datei moonraker.conf
	3. Füge am Ende die zeile [octoprint_compat] hinzu
	4. Klicke oben Rechts auf Save

5. Konfigurieren der moonraker_mqtt.cfg Datei

	Konfiguriere nun die moonraker_mqtt.cfg Datei. Siehe dazu das <a href="https://github.com/othneildrew/Best-README-Template"><strong>Wiki</strong></a>

<!-- Nutzung -->
## Nutzung 

<!-- Zukünftige Änderungen -->
## Zukünftige Änderungen

<!-- Lizenz -->
## Lizenz

Unterliegt der GNU General Public License v3.0. Siehe  `LICENSE` Für mehr Informationen.

<!-- Kontakt -->
## Kontakt

Malte Kollasch -  maltekollasch2003@gmail.com

Projekt Link: [https://github.com/SuperKohl/moonraker-MQTT-plugin](https://github.com/SuperKohl/moonraker-MQTT-plugin)

<!-- Danksagungen -->
## Danksagungen

Ich bedanke mich hiermit bei [Arksine](https://github.com/Arksine) für die Moonraker API, 
[meteyou](https://github.com/meteyou) für das MainsailOS und
[cadriel](https://github.com/cadriel) für das Fluidd.
