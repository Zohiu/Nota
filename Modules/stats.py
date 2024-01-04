import Functions
import discord
import json
import os

fileDir = os.path.join(os.getcwd(), "Files")

async def run(message, prefix, msglst, id):
    premium = await Functions.get_premium_status(message)

    if premium == "default" or premium == "pro" or premium == "ultra":
        file = open(os.path.join(fileDir, '{}.json'.format(id)), "r")
        s = json.loads(file.read())
        file.close()

        color = s["settings"]["color"]
        embed = discord.Embed(title="Stats:", description="", colour=discord.Color(value=int(color, 16)))

        for i in s["stats"]:
            embed.add_field(name=i["name"] + " uses:", value=i["value"], inline=True)

        await message.channel.send(embed=embed)


    else:
        await Functions.embed(message, "Error!", "You need at least premium default to use this command!")

    await Functions.bot_used(message, "stats", message.channel.type)