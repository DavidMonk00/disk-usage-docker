import socket
import re


def get():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    reg = re.sub("[0-9]+$", "1", ip)
    if reg:
        return reg


if __name__ == '__main__':
    print(get())
