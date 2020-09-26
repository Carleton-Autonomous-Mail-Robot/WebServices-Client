
from cipher import Cipher
from flask import jsonify
from client_server_interface import Interface
import json

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

    '''
        Loads ClientID from a configuration file
        @Author Gabriel Ciolac
    '''
    def __loadClientID(self):
        return "TEST ID"


    '''
        Forwards a message to the client-server interface.
        Takes the response from server and turns it into a JSON.
        Sends that JSON to the controller function which determins
        what todo with the response.

        Returns True if client was able to process response.
        Returns False if response was unable to be processed.

        @Author Gabriel Ciolac
    '''
    def send(self,msg):
        res = self._interface.send(status='good',id=self.__clientID,msg='test')
        try:
            payload = json.load(res)
        except:
            return False
        return self.__controller(payload)
        

    '''
        Decides what todo next with a server response depending
        on status.

        @Author Gabriel Ciolac
    '''
    def __controller(self,payload):
        if payload['status'] is 'done':
            return True
        elif payload['status'] is 'good':
            return self.__recieve(payload['package'])
        elif payload['status'] is 'configure':
            return self.__configure()
        return False
        
    '''
        Negotiates a key exhange with the server
        @Author Gabriel Ciolac
    '''
    def __configure(self):
        return True

    '''
        Decrypts payload using private key
        
        @Author Gabriel Ciolac
    '''
    def __recieve(self,msg):
        return True
        


control = Client_Controller()
control.send('test')