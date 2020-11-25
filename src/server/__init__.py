from src.server.postprocessor import PostProcessor
from src.server.preprocessor import PreProcessor
from src.server.core import Core
import socket, threading


class WebSocket:

    def __init__(self, port = None, addr = None):
        ###
        self.port = port
        self.addr = addr
        self.x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def prep(self):
        ###
        if self.addr == None:
            self.addr = socket.gethostbyname(socket.gethostname()) #192.168.56.1
        self.x.bind((self.addr, self.port))

    def start(self):
        ###
        self.x.listen()

class RequestHandler:
    ### Is instantiated by client request
    def __init__(self, conn, addr, HEADER = 64, MSG_FORMAT = "utf-8"):
        self.conn = conn
        self.addr = addr
        self.connected = True
        self.thread = threading.Thread(target=self.handle)
        self.thread.start()

        self.HEADER = HEADER
        self.MSG_FORMAT = MSG_FORMAT
        self.MSG_DISCONNECT = "!sayonara"

    def handle(self):
        """
         Actual execution logic
         input -> preproc -> core (dl/ml) -> postproc -> response
        """
        print(f"[CLIENT - {self.addr}] > CONNECTED")
        while self.connected:
            msg = self.conn.recv(self.HEADER).decode(self.MSG_FORMAT)
            if msg:
                length = int(msg)
                msg = self.conn.recv(length).decode(self.MSG_FORMAT)
                print(f"[CLIENT - {self.addr}]: {msg}")
                if msg == self.MSG_DISCONNECT:
                    self.connected = False
        print(f"[CLIENT - {self.addr}] > DISCONNECTED")
        self.conn.close()

class Server:
    ###
    def __init__(self, port = 80, addr = None):
        ###
        
        self.queue = []
        self.sock = WebSocket(port, addr)
        self.running_mode = "default"

        self.core = core.Core()
        self.preproc = PreProcessor()
        self.postproc = PostProcessor()

    def start(self):
        # Starting up the server
        print("[SERVER] Starting...")
        self.sock.prep()
        self.run()

    def run(self):
        # Server is running, waiting for clients
        self.sock.start()
        print(f"[SERVER] Listening for clients on port {self.sock.port}, address {self.sock.addr}...")
        if self.running_mode != "test":
            while True:
                conn, addr = self.sock.x.accept()
                self.handleClient(conn, addr)
                print(f"[SERVER] Active connections: {threading.activeCount() - 1}")

    def handleClient(self, conn, addr):
        # Instantiates request handler that processes/executes client requests
        print("[SERVER] Handling new client...")
        req_handler = RequestHandler(conn, addr)
        self.queue.append(req_handler)


if __name__ == "__main__":
    print("bEst SeRVeR e")