# OPC UA Simple Client Test Script
# Requirements: pip install opcua

from opcua import Client
import logging

# Optional: Enable logging
logging.basicConfig(level=logging.INFO)

# Replace with your OPC UA server endpoint
url = "opc.tcp://192.168.0.10:4840"
client = Client(url)

try:
    client.connect()
    print(f"Connected to OPC UA server at {url}")

    # Browse root
    root = client.get_root_node()
    print("Root node is:", root)
    print("Children of root are:", root.get_children())

    # Read a specific tag (modify as per your node)
    node = client.get_node("ns=2;i=2")
    value = node.get_value()
    print("Value of node:", value)

except Exception as e:
    print(f"Connection failed: {e}")
finally:
    client.disconnect()
    print("Disconnected from server.")
