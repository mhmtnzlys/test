import os
from dotenv import load_dotenv
load_dotenv()

'''A hello world class contains a Hello World! message'''
class helloWorld:
    '''constructor'''
    def __init__(self):
        self.message = os.environ.get("MY_SECRET")
print(helloWorld())