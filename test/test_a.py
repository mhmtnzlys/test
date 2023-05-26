import unittest
from src.a import helloWorld

'''Test class for helloWorld class'''
class helloWorldTestCase(unittest.TestCase):

    '''test case to test if the message in helloWorld class is Hello World!'''
    def test_hello_world(self):
        myHelloWorld = helloWorld()
        self.assertEqual(myHelloWorld.message, '1')
    
    def test_a(self):
        m = helloWorld()
        m.create()