import Functions
import json
import os

fileDir = os.path.join(os.getcwd(), "Files")

async def run(message, prefix, msglst, id):

    premium = await Functions.get_premium_status(message)
    if premium == "default" or premium == "pro" or premium == "ultra":
        with open(os.path.join(fileDir, '{}.json'.format(id)), "r") as file:
            s = json.loads(file.read())

        s["settings"]["prefix"] = msglst[1]
        with open(os.path.join(fileDir, '{}.json'.format(id)), "w") as file:
            file.write(json.dumps(s))

        await Functions.embed(message, "Success!", "Your new prefix is: " + msglst[1])
        del s

    else:
        await Functions.embed(message, "Error!", "You need at least premium default to use this command!")