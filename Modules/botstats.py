from pathlib import Path
import Functions
import datetime
import discord
import json
import os

threads = None
fileDir = os.path.join(os.getcwd(), "Files")

async def run(message, bot, start_time, time, id):
    file = open(os.path.join(fileDir, '{}.json'.format(id)), "r")
    s = json.loads(file.read())
    file.close()

    color = s["settings"]["color"]

    # Getting the total users
    files = folders = 0
    for _, dirnames, filenames in os.walk(fileDir):
        files += len(filenames)
        folders += len(dirnames)

    # Getting the total uses
    with open("Data/totaluses.dat", "r") as file:
        totaluses = file.read()

    # Getting the uptime
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))

    used_space = round(sum(f.stat().st_size for f in Path(os.getcwd()).glob('**/*') if f.is_file()) / (1024*1024), 2)

    embed = discord.Embed(title="Nota's statistics:", colour=int(color, 16))
    embed.add_field(name="**Total guilds:** ", value=str(len(bot.guilds)), inline=True)
    embed.add_field(name="**Total users:** ", value=str(folders), inline=True)
    embed.add_field(name="**Ping:** ", value=str(round(bot.latency * 1000)), inline=True)
    embed.add_field(name="**Total uses since 03/2021:** ", value=str(totaluses), inline=False)
    embed.add_field(name="**Time since last restart:** ", value=str(text), inline=False)
    embed.add_field(name="**Total used space:** ", value=str(used_space) + " MB", inline=False)

    await message.channel.send(embed=embed)

    await Functions.bot_used(message, "botstats", message.channel.type)