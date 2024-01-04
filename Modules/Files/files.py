import Functions
import discord
import json
import os

fileDir = os.path.join(os.getcwd(), "Files")

async def run(message, prefix, msglst, id):
    file_lines_2 = ""
    file_lines = []
    counter = 0

    file = open(os.path.join(fileDir, '{}.json'.format(id)), "r")
    s = json.loads(file.read())
    file.close()

    color = s["settings"]["color"]
    embed = discord.Embed(title="All files:", description="", colour=discord.Color(value=int(color, 16)))


    file = open(os.path.join(fileDir, '{}.json'.format(id)), "r")
    s = json.loads(file.read())
    file.close()

    totalcounter = 0

    for i in s["files"]:
        file_lines.append('"' + i["name"] + '"' + " Author: " + i["author_name"] + "\n")
        counter += 1
        totalcounter += 1

        if counter == 24:
            for thing in file_lines:
                file_lines_2 += str(thing)

            embed.add_field(name=8*"```\u200b``` ", value=file_lines_2, inline=False)
            file_lines = []
            file_lines_2 = ""
            counter = 0

    for thing in file_lines:
        file_lines_2 += str(thing)

    embed.add_field(name=8*"```\u200b``` ", value=file_lines_2, inline=False)
    embed.add_field(name=8*"```\u200b``` " + "\nTotal files:", value=str(totalcounter), inline=False)

    if len(file_lines) == 0:
        await Functions.embed(message, "All saved files:", "There are no files saved.")
    else:
        await message.channel.send(embed=embed)

    await Functions.bot_used(message, "files", message.channel.type)