import asyncio
import websockets

from src.server import WebSocket


class Client:

    def __init__(self, addr="localhost", port=8000):
        self.sock = WebSocket(addr, port)
        self.requests = []
        self.conn_uri = 'ws://' + addr + ":" + str(port)

    async def sendRequest(self):
        async with websockets.connect(self.conn_uri) as self.sock.x:
            for i in range(1, 100, 1):
                await self.sock.x.send("[Client][Sent]: Hewwo")
    #                 # data_rcv = await self.sock.y.recv();
    #                 # print("data received from server : " + data_rcv)

    def executeSend(self):
        try:
            asyncio.get_event_loop().run_until_complete(self.sendRequest())
            return True
        except:
            return False


if __name__ == "__main__":
    print("Client")