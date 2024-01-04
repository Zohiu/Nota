from base64 import *

def encrypt(string : str):
    base16_string = b16encode(string.encode()[::-1]).decode()[::-1]
    base32_string = b32encode(base16_string.encode()).decode()[::-1]
    base64_string = b64encode(base32_string.encode()).decode()[::-1]
    base85_string = b85encode(base64_string.encode()).decode()[::-1]
    return base85_string

def decrypt(input : str):
    print(input)
    base64_string = b85decode(input.encode()[::-1]).decode()[::-1]
    base32_string = b64decode(base64_string.encode()).decode()[::-1]
    base16_string = b32decode(base32_string.encode()).decode()[::-1]
    string = b16decode(base16_string.encode()).decode()[::-1]
    return string