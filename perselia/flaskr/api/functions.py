import base64

def encrypt(string):
    return base64.b64encode(string)

def decrypt(string):
    return base64.b64decode(string)