
# IPv4Finder

A python3 script that gets your internal ipv4 adress and send it to slack



### Installation

Run ```npm install requests```
### Run on startup (Ubuntu 18.04)

Clone the repository into ```/etc/```

Run ```crontab -e```

Insert ```@reboot python3 /etc/ipv4finder/main.py &``` at the end of the file



