import socket

# Doelinstellingen
target = input("Voer het IP-adres of domein in om te scannen: ")
port_range = range(1, 1025)

print(f"\n[🔎] Start poortscan voor {target}...\n")

for port in port_range:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)  # 0.5 seconde timeout

    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"[✅] Poort {port} is OPEN")
    sock.close()

print("\n[✔️] Scan voltooid.")
