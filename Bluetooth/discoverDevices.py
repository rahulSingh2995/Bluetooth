# simple inquiry example
import bluetooth
import time

while True:
    nearby_devices = bluetooth.discover_devices(duration=20, lookup_names=True)
    print("Found {} devices.".format(len(nearby_devices)))

    for addr, name in nearby_devices:
        print("  {} - {}".format(addr, name))
