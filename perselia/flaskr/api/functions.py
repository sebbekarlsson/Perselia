import base64
import string as _string
import random
from urllib.request import urlopen
import os
from flask import url_for


JSON_HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# Obviously, the encryption method will be changed in the final version
def encrypt(string):
    return base64.b64encode(string.encode('ascii'))

# Obviously, the encryption method will be changed in the final version
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

def generate_name(length=16):
    name = ''
    for i in range(0, length):
        char = random.choice(_string.ascii_letters)

        if random.randint(0, 3) == 0:
                char = str(random.randint(0, 9))

        name += char

    return name

def download_file(url, path):
    response = urlopen(url)
    content = response.read()

    with open(path, 'wb+') as f:
        f.write(content)
        f.close()