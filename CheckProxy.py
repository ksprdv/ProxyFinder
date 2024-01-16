
import random, socks, requests

ip = "103.53.228.217"
port = 7497

server_ip = "104.21.6.173"
server_port = 80

client = socks.socksocket()
client.settimeout(1)
client.set_proxy(socks.SOCKS5, ip, port)
client.connect((server_ip, server_port))
print(f"Host {ip}:{port} connected!")

