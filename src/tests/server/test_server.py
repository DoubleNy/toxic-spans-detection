import pytest

from src.server import Server, WebSocket, RequestHandler

### WebSocket ###

class TestWebSocket():

    ws = WebSocket(80)

    def test_websocket_prep(self):
        self.ws.prep()
        assert type(self.ws.x) != None
        self.ws.x.close()

### Server - RequestHandler ###

class TestServerHandler():

    sv = Server()

    def test_server_start_run(self):
        self.sv.running_mode = "test"
        self.sv.start()

    def test_server_handleClient(self):
        queue_0 = len(self.sv.queue)
        self.sv.handleClient("bla", "bla")
        assert len(self.sv.queue) > queue_0