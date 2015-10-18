import base64

def encrypt(string):
    return base64.b64encode(string.encode('ascii'))

def decrypt(string):
    return base64.b64decode(string).decode(encoding='UTF-8')