from src.client_controller import Client_Controller
from src.message_listener import MessageListner
import json

class Dummy_Usecase(MessageListner):
    def __init__(self):
        self.__hasMessage
        self.__clientController = Client_Controller(self)

    def notify(self,msg):
        self.__msgHandler(msg)

    def __msgHandler(self,msg):
        self.__hasMessage = True

    def getHasMessage(self):
        if(self.__hasMessage):
            __hasMessage = False
            return True
        return False

    def sendGoodMessaage(self):
        self.__clientController.send(msg=json.load('{"payload" : "good" }'))

    def sendBadMessage(self):
        self.__clientController.send(msg=json.load('{"payload" : "bad" }'))