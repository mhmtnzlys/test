import os

'''A hello world class contains a Hello World! message'''
class helloWorld:
    '''constructor'''
    def __init__(self):
        self.message = "1"
    def create(self):
        with open("DigiCertGlobalRootCA.crt.pem", "w") as f:
            f.write("CERT")