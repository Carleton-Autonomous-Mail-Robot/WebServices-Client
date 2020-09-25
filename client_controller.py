"""
This class is used for the Client in
the server, client pair.

"""
from cipher import Cipher
from flask import jsonify
from client_server_interface import Interface
import json

class Controller:
    def __init__(self):
        self.__cipher = Cipher()
        self.__clientID = self.__loadClientID()
        self.__serverPublicKey = ""
        self._interface = Interface()

    def __loadClientID(self):
        return "TEST ID"

    def send(self,msg):
        self._interface.send(status='good',id=self.__clientID,msg='test')
    
    def __configure(self):
        pass

    def __recieve(self,msg):
        pass


control = Controller()
control.send('test')