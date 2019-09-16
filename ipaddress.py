import socket
import re
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
reg = re.sub("[0-9]+$", "1", ip)
if reg:
    print(reg)
s.close()
