def update(input): 
        stripstring = input.split(".")
        output = ""

        if "pic" in stripstring[-1]:
            pic = True
            list = False
        elif "dclist" in stripstring[-1]:
            list = True
                        
        else:
            pic = False
            list = False

        if len(stripstring) > 3:
            if "#" in stripstring[1]:
                stripstring.remove(stripstring[1])
        
        stripstring.remove(stripstring[-1])
            
        for string in stripstring:
            output += string + "."
          
        if list:
            output += "dclist"
        else:
            if pic:
                output += "dcsavepic"
            else:
                output += "dcsave"
        
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
        
            if len(update(string)) > 15:
                print(string + "  >  " + update(string) + "\n")
                try:
                    oldfilename = os.path.join(dir, os.path.join(string.split(".")[0], string))
                    newfilename = os.path.join(dir, os.path.join(update(string).split(".")[0], update(string)))
                    
                    with open(oldfilename, "r") as file:
                        content = file.read()
                        
                    os.remove(oldfilename)
                    
                    with open(newfilename, "w+") as file:
                            file.write(content)
                except:
                    continue
                        
input("\nDone! Press enter to exit... ")