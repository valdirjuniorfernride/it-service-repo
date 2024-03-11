import subprocess

def ping_ip(ip):
    # Ping the IP address
    print(f"Pinging {ip}...")
    result = subprocess.call(['ping', '-c', '1', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result == 0

def check_unused_ips(ip_start, ip_end):
    unused_ips = []
    for i in range(ip_start, ip_end + 1):
        ip = f"172.16.103.{i}"
        if not ping_ip(ip):
            unused_ips.append(ip)
    return unused_ips

# Define the IP range
ip_start = 91
ip_end = 253

unused_ips = check_unused_ips(ip_start, ip_end)
print("\nUnused IPs:")
for ip in unused_ips:
    print(ip)