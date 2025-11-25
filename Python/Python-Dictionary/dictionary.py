device = {
    "hostname": "fatih",
    "ip": "192.168.0.241",
    "os": "linux",
    "is_managed": True
}

# Access a value using its key
id_addr = device["ip"]
print(f"The device IP is: {id_addr}")

# Add key-value pair
device["location"] = "buchpora"

# Update a value
device["os"] = "kali linux"

# Print the dictionary
print(f"--- Device Dictionary ---: {device}")

# Example delete:  del device["os"]
# Example pop:     prev_ip = device.pop("ip")

# Operations on Dictionary
if "hostname" in device:
    print(f"The hostname exists and value is: {device['hostname']}")

if "ip" not in device:
    print("IP does not exist")

# Using for loop for operations on dictionary
for my_key, my_val in device.items():
    print(f"key is {my_key} ----- value is {my_val}")

