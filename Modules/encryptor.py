from base64 import *
import emoji

def encrypt(string : str):
    base16_string = b16encode(emoji.demojize(string).encode()[::-1]).decode()[::-1]
    base32_string = b32encode(base16_string.encode()).decode()[::-1]
    base64_string = b64encode(base32_string.encode()).decode()[::-1]
    base85_string = b85encode(base64_string.encode()).decode()[::-1]
    try:
        base64_string = b85decode(base85_string.encode()[::-1]).decode()[::-1]
        base32_string = b64decode(base64_string.encode()).decode()[::-1]
        base16_string = b32decode(base32_string.encode()).decode()[::-1]
        string = b16decode(base16_string.encode()).decode()[::-1]
        return base85_string
    except:
        return "%/$§➔_xXEnCrYpTi0n dIdN't W0RkXx_➔§$/%" + string

def decrypt(input : str):
    if "%/$§➔_xXEnCrYpTi0n dIdN't W0RkXx_➔§$/%" in input:
        return input.strip("%/$§➔_xXEnCrYpTi0n dIdN't W0RkXx_➔§$/%")

    base64_string = b85decode(input.encode()[::-1]).decode()[::-1]
    base32_string = b64decode(base64_string.encode()).decode()[::-1]
    base16_string = b32decode(base32_string.encode()).decode()[::-1]
    string = b16decode(base16_string.encode()).decode()[::-1]
    return emoji.emojize(string)

