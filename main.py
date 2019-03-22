import socket
import os
from slackclient import SlackClient
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# Get Internal IPv4 adress
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ipv4 = s.getsockname()[0]
s.close()
print('My internal ipv4 adress is: ' + ipv4)



#Send it to slack
slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="C0XXXXXX",
  text="Hello from Python! :tada:"
)