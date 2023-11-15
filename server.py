import socket


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.serversocket = socket.socket()

    def serverinit(self):
        self.serversocket.bind((self.host, self.port))
        self.serversocket.listen()

if __name__ == "__main__":
    HOST = "0.0.0.0"  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    myserver = Server(HOST, PORT)
    myserver.serverinit()

    while True:
        pass
