import pytest, threading

from src.server.client import Client
from src.server import Server

### Client ###

class TestClient():

    cl = Client()

    def test_client_run(self):
        # No connection yet
        self.cl.connected = False
        self.cl.run()

    def test_client_sendTest(self):
        self.cl.connected = False
        self.cl.sendText("Bla bla")