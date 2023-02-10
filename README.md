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
    <a href=""><strong>Siehe das Wiki »</strong></a>
    <br />
    <br />
    <a href="https://github.com/SuperKohl/Moonraker-MQTT-plugin/issues">Report Bug</a>
    ·
    <a href="https://github.com/SuperKohl/Moonraker-MQTT-plugin/issues/1">Request Feature</a>
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
    <li><a href="#Deinstallieren">Deinstallieren</a></li>
    <li><a href="#Nutzung">Nutzung</a></li>
    <li><a href="#Zukünftige-Änderungen">Zukünftige Änderungen</a></li>
    <li><a href="#Lizenz">Lizenz</a></li>
    <li><a href="#Kontakt">Kontakt</a></li>
    <li><a href="#Danksagungen">Danksagungen</a></li>
  </ol>
</details>



<!-- Über das Projekt -->
## Über das Projekt

Ein Skript/Programm zum Überwachen/Steuern des Druckers über MQTT.

### Programmiert mit

Das Plugin wurde Programmiert mit:
* [Python3](https://www.python.org/)
* [Json](https://www.json.org/)
* [Bash](https://www.gnu.org/software/bash/)

<!-- Installieren -->
## Installieren

### Voraussetzungen

Vorausgesetzt wird eines der Installationen:
* [MainsailOS](https://github.com/meteyou/mainsail)
* [Fluidd](https://github.com/cadriel/fluidd)

### Installation

1. Gehe in das Home Verzeichnis:
   ```sh
   cd ~
   ```
2. Clone das Repository
	```sh
   git clone https://github.com/SuperKohl/Moonraker-MQTT-plugin.git
   ```
3. Führe das Installation-Script aus: bash ./Moonraker-MQTT-plugin/scripts/install.sh
	```sh
   bash ./Moonraker-MQTT-plugin/scripts/install.sh
   ```
5. Füge in der moonraker.conf die Zeilen hinzu:
	```sh
   [octoprint_compat]

   [update_manager]

   [update_manager client Moonraker-MQTT-plugin]
   type: git_repo
   path: ~/Moonraker-MQTT-plugin
   origin: https://github.com/SuperKohl/Moonraker-MQTT-plugin.git
   ```

	In MainsailOS:
	1. Gehe zu Mainsail -> Settings -> Maschine
	2. Klicke auf die Datei moonraker.conf
	3. Füge die zeilen hinzu	
	4. Klicke oben Rechts auf Save

	In Fluidd:
	1. Gehe zu Printer -> config
	2. Klicke auf die Datei moonraker.conf
	3. Füge die zeilen hinzu
	4. Klicke oben Rechts auf Save

6. Konfiguriere nun die moonraker_mqtt.cfg Datei mit den Daten von deinem Mqtt Broker.
7. Damit das Plugin jedes mal Automatisch gestartet wird, konfiguriere die /etc/crontab Datei
```sh
   crontab -e
   ```
  füge folgende Zeile ab ende ein
```sh
   @reboot ~/Moonraker-MQTT-plugin/scripts/mqtt.py
   ```
   Dann mit Strg+o Enter speichern und mit Strg+x verlassen.

<!-- Deinstallieren -->
## Deinstallieren
Zum Deinstallieren
<!-- Nutzung -->
## Nutzung
Das Plugin Startet beim Start Automatisch.
Sie können nun die Werte vom Drucker in ihrer Smart Home Installation nutzen. 
<!-- Zukünftige Änderungen -->
## Zukünftige Änderungen
Ihr könnt mir Vorschläge per Email Schicken oder im Tab Issures Vorschläge hinterlassen. [Email](mailto:maltekollasch2003@gmail.com)
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
