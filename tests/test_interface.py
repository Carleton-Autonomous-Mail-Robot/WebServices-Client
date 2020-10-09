import unittest
from tests.dummy_usecase import Dummy_Usecase

class TestInterface(unittest.TestCase):


    def test_good_send(self):
        good = Dummy_Usecase()
        good.sendGoodMessaage()
        
        self.assertTrue(good.getHasMessage)

    def test_bad_send(self):
        bad = Dummy_Usecase()
        bad.sendBadMessage()
        
        self.assertFalse(bad.getHasMessage)

