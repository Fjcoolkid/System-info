import os
import platform
import psutil
import time

print("Made by FoLaBi :)")
print("""
█▀ █▄█ █▀ ▀█▀ █▀▀ █▀▄▀█ ▄▄ █ █▄░█ █▀▀ █▀█
▄█ ░█░ ▄█ ░█░ ██▄ █░▀░█ ░░ █ █░▀█ █▀░ █▄█""")

print("Gathering Device Info Please Wait")
time.sleep(4)
def get_system_info():
    print("System Information:")
    print("-" * 20)
    
    # Operating System information
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"OS Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    
    # Memory information
    mem = psutil.virtual_memory()
    print(f"Total Memory: {mem.total / (1024**3):.2f} GB")
    print(f"Available Memory: {mem.available / (1024**3):.2f} GB")
    print(f"Memory Usage: {mem.percent}%")
    
    # Disk information
    disk = psutil.disk_usage('/')
    print(f"Total Disk Space: {disk.total / (1024**3):.2f} GB")
    print(f"Used Disk Space: {disk.used / (1024**3):.2f} GB")
    print(f"Free Disk Space: {disk.free / (1024**3):.2f} GB")
    print(f"Disk Usage: {disk.percent}%")
    
    # Network information
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for addr in interface_addresses:
            if str(addr.family) == 'AddressFamily.AF_INET':
                print(f"Interface: {interface_name}")
                print(f"IP Address: {addr.address}")
                print(f"Netmask: {addr.netmask}")
                print(f"Broadcast IP: {addr.broadcast}")

if __name__ == "__main__":
    get_system_info()   