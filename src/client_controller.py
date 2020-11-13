
from src.cipher import Cipher
from flask import jsonify
from src.client_server_interface import Interface
import json
from random import randrange

"""
This class is used for the Client in
the server-client pair.

"""
class Client_Controller:

    '''
        Constructor for Client_Controller
        @Author Gabriel Ciolac
    '''
    def __init__(self):
        self.__cipher = Cipher()
        self.__clientID = self.__loadClientID()
        self.__serverPublicKey = ""
        self._interface = Interface()
        self.__message = None

    '''
        Loads ClientID from a configuration file
        @Author Gabriel Ciolac
    '''
    def __loadClientID(self):
        return randrange(10000000)


    '''
        Forwards a message to the client-server interface.
        Takes the response from server and turns it into a JSON.
        Sends that JSON to the controller function which determins
        what todo with the response.

        Returns True if client was able to process response.
        Returns False if response was unable to be processed.

        @Author Gabriel Ciolac
    '''
    def send(self,msg,opperation):
        res = self._interface.send(status='good',id=self.__clientID,opperation=opperation,msg=msg)
        try:
            self.__message = json.load(res['payload'])
        except:
            return False

    def getReciever(self)->str:
        pass
    def getSender(self)->str:
        pass
    def getDock(self)->str:
        pass
       
        
