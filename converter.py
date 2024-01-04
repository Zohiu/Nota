allcmds = ["help", "changeprefix", "changecolor", "stats", "timer", "remind", "save", "read", "delete", "files",
                   "share", "privatesave", "privateread", "privatedelete", "privatefiles", "calc", "ping", "embed",
                   "guilds", "premium", "uptime", "speed"]
                   
def update(input): 
        stripstring = input.split(".")
        output = ""

        if len(stripstring) > 1:
            stripstring.remove(stripstring[0])
            
        if stripstring[-1] == "dcsavepic":
            stripstring.remove(stripstring[-1])
            stripstring.append("dcsaveraw")
            
        elif stripstring[-1] == "usersavepic":
            stripstring.remove(stripstring[-1])
            stripstring.append("usersaveraw")
            
        for string in stripstring:
            output += string + "."
            
        output = output[:-1]
        
        for string in allcmds:
            if string == "changecolor":
                if output == "dc" + string + "uses":
                    output = "dc.setcoloruses"
                
                elif output == "user" + string + "uses":
                    output = "user.setcoloruses"
                    
            elif string == "changeprefix":
                if output == "dc" + string + "uses":
                    output = "dc.setprefixuses"
                
                elif output == "user" + string + "uses":
                    output = "user.setprefixuses"
             
            elif output == "dc" + string + "uses":
                output = "dc." + string + "uses"
                
            elif output == "user" + string + "uses":
                output = "user." + string + "uses"
                
        if output == "dclist":
            output = "dc.list"
        elif output == "dccolor":
            output = "dc.color"
        elif output == "dcprefix":
            output = "dc.prefix"
            
        elif output == "userlist":
            output = "user.list"
        elif output == "usercolor":
            output = "user.color"
        elif output == "userprefix":
            output = "user.prefix"
        
        
        if "converter.py" in input:
            return "converter.py"       
        else:
            return output

print("Converting...\n")

import os

dir = os.getcwd()
        
for d in os.walk(dir):
    for f in d:
        for string in f: 
            if len(update(string)) > 3:
                try:
                    print(string + "  >  " + update(string) + "\n")
                    
                    oldfilename = os.path.join(dir, os.path.join(d[0], string))
                    newfilename = os.path.join(dir, os.path.join(d[0], update(string)))
                    
                    with open(oldfilename, "r") as file:
                        content = file.read()
                        
                    os.remove(oldfilename)
                    
                    with open(newfilename, "w+") as file:
                            file.write(content)
                except Exception as e:
                    print(e)
                    continue
                        
input("\nDone! Press enter to exit... ")