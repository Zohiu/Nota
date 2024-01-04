import Functions
import json
import os

fileDir = os.path.join(os.getcwd(), "Files")

async def run(message, prefix, msglst, id):

    premium = await Functions.get_premium_status(message)
    if premium == "default" or premium == "pro" or premium == "ultra":
        with open(os.path.join(fileDir, '{}.json'.format(id)), "r") as file:
            s = json.loads(file.read())

        if len(msglst[1]) < 11:
            s["settings"]["prefix"] = msglst[1]
            with open(os.path.join(fileDir, '{}.json'.format(id)), "w") as file:
                file.write(json.dumps(s))
            await Functions.embed(message, "<:nota_success:796499295980617739> Your new prefix is: " + msglst[1])
            del s
            await Functions.bot_used(message, "setprefix", message.channel.type)
        else:
            await Functions.embed(message, "<:nota_error:796499987949027349> The max length for prefixes is 10!")
    else:
        await Functions.embed(message, "<:nota_error:796499987949027349> You need at least premium default to use this command!")