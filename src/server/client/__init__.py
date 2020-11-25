from src.server import WebSocket


class Client:

    def __init__(self, SERVER_ADDR = 'localhost', SERVER_PORT = 80, HEADER = 64, MSG_FORMAT = "utf-8"):
        ###
        print(f"[CLIENT] Connecting to server on port {SERVER_PORT}, address {SERVER_ADDR}...")

        self.sock = WebSocket()
        self.connected = True
        
        self.SERVER_ADDR = SERVER_ADDR
        self.SERVER_PORT = SERVER_PORT
        self.MSG_DISCONNECT = "!sayonara"
        self.HEADER = HEADER
        self.MSG_FORMAT = MSG_FORMAT

    def run(self):
        ###
        try:
            self.sock.x.connect((SERVER_ADDR, SERVER_PORT))
            while self.connected:
                client_input = input("[CLIENT] Type your input: ")
                if client_input:
                    if client_input == self.MSG_DISCONNECT:
                        self.connected = False
                    self.sendText(client_input)
            print(f"[CLIENT] Closing connection... :(")
        except:
            print("[CLIENT] Target machine refused the connection.")


    def sendText(self, txt):
        ###
        print(f"[CLIENT] Sending '{txt}'...")
        if self.connected:
            txt = txt.encode(self.MSG_FORMAT)
            send_length = str(len(txt)).encode(self.MSG_FORMAT)
            send_length += b' ' * (self.HEADER - len(send_length))
            self.sock.x.send(send_length)
            self.sock.x.send(txt)
        else:
            print("[CLIENT] Client not connected.")


if __name__ == "__main__":
    print("Client module...")