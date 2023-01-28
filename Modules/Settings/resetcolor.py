import Functions
import json
import os

fileDir = os.path.join(os.getcwd(), "Files")

async def run(message, prefix, msglst, id):  # PREMIUM
    premium = await Functions.get_premium_status(message)
    if premium == "ultra":
        with open(os.path.join(fileDir, '{}.json'.format(id)), "r") as file:
            s = json.loads(file.read())

        s["settings"]["color"] = "68C60E"
        with open(os.path.join(fileDir, '{}.json'.format(id)), "w") as file:
            file.write(json.dumps(s))

        await Functions.embed(message, "<:nota_success:796499295980617739> New color: #68C60E")
        del s
        await Functions.bot_used(message, "resetcolor", message.channel.type)
    else:
        await Functions.embed(message, "<:nota_error:796499987949027349> You need at least premium ultra to use this command!")