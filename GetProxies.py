from socks import socksocket, SOCKS5
from requests import get
from time import time
from colorama import Back, Style
from threading import Thread
import socket
from random import choice
import os

server_ip = "104.21.6.173"
#server_ip = "127.0.0.1" # Example Server
server_port = 80

sites = [
    "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=10000&country=all",
    "https://www.proxy-list.download/api/v1/get?type=socks5"
]


req = get(choice(sites)).text
req2 = get(choice(sites)).text
#req3 = get("https://advanced.name/freeproxy/62fbc91709204").text
hosts = req.split()
hosts2 = req2.split()
#hosts3 = req3.split()

os.remove("proxy_list.txt")

def connect(ip, port):
    port = int(port)
    client = socksocket()
    try:
        Tm = time()
        client.settimeout(0.8)
        client.set_proxy(SOCKS5, ip, port)
        client.connect((server_ip, server_port))
        New_Tm = int(time()) - int(Tm)
        print("{}{}{}:{} is valid!{}".format("\033[1m", Back.GREEN, ip, port, Style.RESET_ALL))
        with open("proxy_list.txt", "a") as f:
            f.write("{}:{}\n".format(ip, port))
            f.close()
    except Exception as a:
            print("{}{}{}:{} is invalid!{}".format("\033[1m", Back.RED, ip, port, Style.RESET_ALL))

def start():
    for host in hosts:
        ip = host.split(":")[0]
        port = host.split(":")[1]
        connect(ip, port)
    for host2 in hosts2:
        ip2 = host2.split(":")[0]
        port2 = host2.split(":")[1]
        connect(ip2, port2)
    #for host3 in  hosts3:
    #    ip3 = host3.split(":")[0]
    #    port3 = host3.split(":")[1]
    #    connect(ip3, port3)

start()