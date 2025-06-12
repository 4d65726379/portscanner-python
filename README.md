# Nederlandse uitleg
# 🔎 Portscanner in Python

Een simpele poortscanner geschreven in Python, bedoeld voor educatieve doeleinden. Deze tool scant een IP-adres of domeinnaam op open TCP-poorten (1–1024).

## ⚙️ Functionaliteit

- Scant poorten 1 t/m 1024
- Toont welke poorten open zijn
- Gebruikt Python's `socket`-module
- Werkt via command line (cmd/terminal)

## 🚀 Uitvoeren

### ✅ Vereisten

- Python 3.x (https://python.org)

### ▶️ Gebruik

1. Clone deze repository of download `portscanner.py`
2. Open een terminal en ga naar de map:
   ```bash
   cd pad/naar/de/map
3. Start het script:
   ```bash
   python portscanner.py

4. Vul het doeladres in wanneer erom gevraagd wordt:
   ```bash
   Voer het IP-adres of domein in om te scannen:
   scanme.nmap.org

## 🔐 Let op

Gebruik deze scanner alleen op:

    Jouw eigen netwerkapparaten

    Testdomeinen zoals scanme.nmap.org

    Apparaten waarvoor je toestemming hebt

Illegaal scannen van systemen zonder toestemming is strafbaar (Computercriminaliteit wetgeving).

## 🛠️ Hoe werkt het?

De scanner gebruikt een socket-verbinding per poort en probeert TCP-connecties te maken. Als poort open is, wordt deze gemeld. Poorten die niet reageren of dicht zijn worden genegeerd.

## 🧠 Gemaakt door

    Espey

    Gemaakt tijdens mijn MBO ICT opleiding (Expert Systemen & Devices)

# English Version
# 🔎 Portscanner in Python

A simple Python-based port scanner, created for educational purposes. This tool scans a given IP address or domain for open TCP ports (1–1024).

## ⚙️ Features

- Scans ports 1 to 1024
- Displays which ports are open
- Uses Python's `socket` module
- Runs via the command line (cmd/terminal)

## 🚀 How to Run

### ✅ Requirements

- Python 3.x (https://python.org)

### ▶️ Usage

1. Clone this repository or download `portscanner.py`
2. Open a terminal and navigate to the folder:
   ```bash
   cd path/to/your/folder
   
3. Run the script:
   ```bash
   python portscanner.py

4. Enter the target IP or domain when prompted:
   ```bash
   Enter the IP address or domain to scan:
   scanme.nmap.org 

## 🔐 Legal Notice

Only use this scanner on:

    Your own network devices

    Test domains like scanme.nmap.org

    Systems you have permission to scan

Unauthorized scanning of external systems is illegal and may result in prosecution.

### 🛠️ How it Works

The scanner creates a socket connection for each port and attempts a TCP connection. If the port is open, it is reported. Closed or unresponsive ports are ignored.

## 🧠 Created by

    Espey

    Built as part of my MBO ICT education (Expert Systems & Devices)