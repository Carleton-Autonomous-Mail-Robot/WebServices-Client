"""
This class is used for the Client in
the server, client pair.

"""
from cipher import Cipher
from flask import jsonify
import json

class Client:
    def __init__(self):
        self.__cipher = Cipher()
        self.__clientID = self.__loadClientID()
        self.__serverPublicKey = ""
        self.__listners = {}

    def __loadClientID(self):
        return "TEST ID"

    def __notifyListner(self):
        pass

    def __send(self,msg):
        return msg

    def recieve(self,msg):
        if self.__serverPublicKey == "":
            return jsonify(status = "configure")

        

    