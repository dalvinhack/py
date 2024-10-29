import socket

def check_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  #Set timeout to 1 second
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

ip_address = "192.168.1.1"
ports = [443, 8080]

for port in ports:
    if check_port(ip_address, port):
        print(f"Port {port} on {ip_address} is open")
    else:
        print(f"Port {port} on {ip_address} is closed or unreachable")