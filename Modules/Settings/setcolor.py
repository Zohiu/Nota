import Functions
import discord
import json
import os

fileDir = os.path.join(os.getcwd(), "Files")

async def run(message, prefix, msglst, id):  # PREMIUM
    premium = await Functions.get_premium_status(message)
    if premium == "ultra":
        try:
            embed = discord.Embed(
                title="title",
                description="describtion",
                colour=discord.Color(value=int(msglst[1].replace('#', ''), 16))
            )

            with open(os.path.join(fileDir, '{}.json'.format(id)), "r") as file:
                s = json.loads(file.read())

            s["settings"]["color"] = msglst[1].replace("#", "")

            with open(os.path.join(fileDir, '{}.json'.format(id)), "w") as file:
                file.write(json.dumps(s))

            await Functions.embed(message, "Color changed!", "New color: " + msglst[1])

            await Functions.bot_used(message, "changecolor", message.channel.type)

        except ValueError:
            await Functions.embed(message, "Error!",
                                  "You have to use a hex color. You can generate hex colors here: https://www.rapidtables.com/convert/color/rgb-to-hex.html\nUsage: changecolor <colorhex>")

        del s
    else:
        await Functions.embed(message, "Error!", "You need at least premium ultra to use this command!")
