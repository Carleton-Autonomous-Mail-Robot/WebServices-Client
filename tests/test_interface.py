import unittest
from tests.dummy_usecase import Dummy_Usecase

class TestInterface(unittest.TestCase):


    def test_round_trip(self):
        usecase = Dummy_Usecase()

        usecase.sendInit()
        usecase.sendNewMessage()
        usecase.getMessage()

        self.assertTrue(usecase.getHasMessage())

