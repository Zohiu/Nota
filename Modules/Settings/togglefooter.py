import Functions
import json
import os

fileDir = os.path.join(os.getcwd(), "Files")

async def run(message, prefix, msglst, id):  # PREMIUM
    premium = await Functions.get_premium_status(message)
    if premium == "ultra":
        with open(os.path.join(fileDir, '{}.json'.format(id)), "r") as file:
            s = json.loads(file.read())

        if s["settings"]["read_footer"] == True:
            s["settings"]["read_footer"] = False
        else:
            s["settings"]["read_footer"] = True

        with open(os.path.join(fileDir, '{}.json'.format(id)), "w") as file:
            file.write(json.dumps(s))

        await Functions.embed(message, "Footer toggled!", "New state: " + str(s["settings"]["read_footer"]))
        del s
    else:
        await Functions.embed(message, "Error!", "You need at least premium ultra to use this command!")