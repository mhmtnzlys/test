import os

'''A hello world class contains a Hello World! message'''
class helloWorld:
    '''constructor'''
    def __init__(self):
        self.message = "1"
    def create(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        new_file_path = os.path.join(
            current_directory, "DigiCertGlobalRootCA.txt")
        with open(new_file_path, "w") as f:
            f.write("CERT")