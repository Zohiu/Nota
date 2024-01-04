import Functions
import speedtest
import discord
import json
import os

threads = None
fileDir = os.path.join(os.getcwd(), "Files")

async def run(message):
    if str(message.channel.type) == "private":
        id = str(message.author.id)
    else:
        id = str(message.guild.id)

    file = open(os.path.join(fileDir, '{}.json'.format(id)), "r")
    s = json.loads(file.read())
    file.close()

    color = s["settings"]["color"]


    embed = discord.Embed(title="Nota's internet speed:", description="Currently getting the best server...", colour=color)
    msg = await message.channel.send(embed=embed)

    s = speedtest.Speedtest()
    s.get_best_server()

    await msg.delete()
    embed = discord.Embed(title="Nota's internet speed:", description="Download: Currently testing...\nUpload: NaN.", colour=color)
    msg = await message.channel.send(embed=embed)

    download = s.download(threads=threads)

    await msg.delete()
    embed = discord.Embed(title="Nota's internet speed:", description="Download: " + str(round(download/1000/1000)) + " Mbps\n" + "Upload: NaN.", colour=color)
    msg = await message.channel.send(embed=embed)

    msg = await message.channel.send(embed=embed)

    await Functions.bot_used(message, "speed", message.channel.type)