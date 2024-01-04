import Functions
import discord
import json
import os

fileDir = os.path.join(os.getcwd(), "Files")

async def run(message, prefix, msglst, id, bot):
    if str(message.channel.type) == "private":
        id = os.path.join(str(message.author.id), str(message.author.id))
    else:
        id = os.path.join(str(message.guild.id), str(message.guild.id))

    file = open(os.path.join(fileDir, '{}.json'.format(id)), "r")
    s = json.loads(file.read())
    file.close()

    color = s["settings"]["color"]
    embed = discord.Embed(title=msglst[1], description=msglst[2], colour=discord.Color(value=int(color, 16)))

    sentto = 0
    guilds = []

    for guild in bot.guilds:
        for channel in guild.channels:
            if "nota-news" in channel.name:
                try:
                    await channel.send(embed=embed)
                    guilds.append({"name": str(guild), "id": str(guild.id)})
                    sentto += 1
                except:
                    continue

    await Functions.embed(message, "Broadcast", "Sent to " + str(sentto) + " guilds!")

    for guild in guilds:
        await message.channel.send(guild["name"] + " | " + guild["id"])