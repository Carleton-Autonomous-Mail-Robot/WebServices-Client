import unittest
from src.client_server_interface import Interface

class TestClientServerInterface(unittest.TestCase):


    def test_send(self):
        interface = Interface()
        self.assertIsNotNone(interface.send('good','test','00'))