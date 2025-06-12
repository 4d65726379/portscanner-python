import socket

target = input("Enter the IP address or domain to scan: ")
port_range = range(1, 1025)

print(f"\n[🔎] Starting port scan on {target}...\n")

for port in port_range:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"[✅] Port {port} is OPEN")
    sock.close()

print("\n[✔️] Scan complete.")
