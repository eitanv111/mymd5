import socket
import protocol


class client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.mysocket = socket.socket()

    def connect(self):
        self.mysocket.connect((self.host, self.port))

    def send(self, msg):
        self.mysocket.send(protocol.Protocol.getmsg(msg))

if __name__ == "__main__":

    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    myclient = client(HOST, PORT)
    myclient.connect()
    while True:
        tosend = input()

        myclient.send(tosend)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")
