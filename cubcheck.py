#!/usr/bin/env python3

import shutil
import psutil
import platform
import socket

def print_header(title):
    print(f"\n🧠 {title}")
    print("=" * (len(title) + 4))

# Host info
print_header("System Info")
print(f"Hostname     : {socket.gethostname()}")
print(f"OS           : {platform.system()} {platform.release()}")
print(f"Python Ver   : {platform.python_version()}")

# Memory
print_header("Memory Usage")
mem = psutil.virtual_memory()
print(f"Total        : {mem.total / (1024**3):.2f} GB")
print(f"Used         : {mem.used / (1024**3):.2f} GB")
print(f"Available    : {mem.available / (1024**3):.2f} GB")
print(f"Usage        : {mem.percent}%")

# Disk
print_header("Disk Usage")
du = shutil.disk_usage("/")
print(f"Root Mount   : /")
print(f"Total        : {du.total / (1024**3):.2f} GB")
print(f"Used         : {du.used / (1024**3):.2f} GB")
print(f"Free         : {du.free / (1024**3):.2f} GB")
print(f"Usage        : {du.used / du.total * 100:.1f}%")

# Partitions
print_header("Mounted Partitions")
for p in psutil.disk_partitions():
    warn = "⚠️" if 'rw' not in p.opts else ""
    print(f"{p.device} on {p.mountpoint} [{p.fstype}] {p.opts} {warn}")
