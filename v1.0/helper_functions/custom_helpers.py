# import ctypes
import jwt

class app:
    def __init__(self):
        self.connector = None
        self.environment_details = {}
        self.assign_environment_details()
    
    def assign_environment_details(self):
        file = open("environment.txt","r")
        for line in file:
            if(line != "\n" and line.replace(" ","")!=""):
                for[key,value] in [line.rstrip().split(" = ")]:
                    self.environment_details[key] = value
    
    def __str__(self) -> str:
        return (f'{self.connector} - {self.environment_details} ')

main_app = app()
# 
# # the below 2 functions are used to get address of variable, then use that address to access the value 
# # stored in that variable
# # Use these functions for storing any variables in local or session variable in web browser and later 
# # access those variables when needed
# def get_address(object):
#     return id(object)

# def get_object_from_address(address):
#     return ctypes.cast(address,ctypes.py_object).value

def create_token(payload, 
                secret_key = main_app.environment_details['secret_key'], 
                algorithm = main_app.environment_details['algorithm']):
    return jwt.encode(payload, secret_key, algorithm)

def decode_token(token, 
                secret_key = main_app.environment_details['secret_key'], 
                algorithm = main_app.environment_details['algorithm']):
    return jwt.decode(token, secret_key, algorithm)
    

