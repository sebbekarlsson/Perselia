import base64
import string as _string
import random


def encrypt(string):
    return base64.b64encode(string.encode('ascii'))

def decrypt(string):
    return base64.b64decode(string).decode(encoding='UTF-8')

def generate_token(length=32):
    token = ''
    for i in range(0, length):
        char = None
        r = random.randint(0, 10)
        if r == 0:
            char = random.choice(_string.ascii_letters)

        else:
            char = r

        if random.randint(0, 3) == 0:
                char = '{}$@?[]%#_;&'
                char = char[random.randint(0, len(char)-1)]

        token += str(char)

    return token