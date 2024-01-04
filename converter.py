import shutil
import json
import os

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

toremove = []

for dir in os.walk("G:/Dokumente/1ANOTA/NotaBotTest/Convertion"):
    if not dir[1] == []:
        new_list = {"files": [], "settings": {"prefix": "-", "color": "68C60E", "read_footer": True, "show_ads": True, "show_favourites": True},"stats": [], "favourites": []}
        current_dir = dir[0]
        files = dir[2]
        
        for file in files:
            continue1 = True
            print(file.split(".")[-1])
            if file.split(".")[-1] == "dcsave":
                filetype = "text"
            elif file.split(".")[-1] == "dcsaveraw":
                filetype = "raw"   
            elif file.split(".")[-1] == "dcfilesave":
                filetype = "file"
                
            elif file.split(".")[-1] == "files":
                os.remove(os.path.join(current_dir, file))
                continue1 = False
            elif file.split(".")[-1] == "list":
                os.remove(os.path.join(current_dir, file))
                continue1 = False
            elif file.split(".")[-1] == "info":
                os.remove(os.path.join(current_dir, file))
                continue1 = False
              
            else:
                filetype = None
                continue1 = False
                    
            file1 = file.split(".")[:-1]
            filetemp = ""
            for text in file1:
                filetemp += text
                    
            if continue1:
                try:
                    new_list["files"].append({"name": str(filetemp), "content": encrypt(str(open(os.path.join(current_dir, file), "r").read())), "author_name": "NaN", "author_id": "NaN", "type": str(filetype), "save_time": "NaN"})
                    os.remove(os.path.join(current_dir, file))
                except UnicodeDecodeError:
                    os.remove(os.path.join(current_dir, file))
            
        open(os.path.join(current_dir, current_dir.split("\\")[-1] + ".json"), "w").write(json.dumps(new_list))
            
        print("\n" + "", current_dir, new_list, "" + "\n")
        
    else:
        toremove.append(dir[0])

for dir in toremove:
    shutil.rmtree(dir)
      
json.dumps({"files": [], "settings": {"prefix": "-", "color": "68C60E", "read_footer": True, "show_ads": True, "show_favourites": True},"stats": [], "favourites": []})
