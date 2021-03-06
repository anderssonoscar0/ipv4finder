import socket
import os
import configparser
import requests
import json

# Import config file
config = configparser.ConfigParser()
config.read('config.ini')

# Get Internal IPv4 adress
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ipv4 = s.getsockname()[0]
s.close()

# Send slack message
headers = {'content-type': 'application/json'}
url = config["DEFAULT"]["SLACK_HOOK_URL"]
payload = {"text": ipv4}
r = requests.post(url, data=json.dumps(payload), headers=headers)
print(r.status_code, r.reason)
