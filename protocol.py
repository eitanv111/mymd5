import socket


class Protocol:
    # <length><message>

    MESSAGE_LEN_FIELD = 2
    @staticmethod
    def getmsg(msg):
        data = msg.encode()
        data_length = len(data)
        length = str(data_length).zfill(Protocol.MESSAGE_LEN_FIELD).encode()

        return length+data


