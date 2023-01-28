import Functions
import discord
import json
import os

fileDir = os.path.join(os.getcwd(), "Files")

async def run(message, prefix, msglst, id):
    file = open(os.path.join(fileDir, '{}.json'.format(id)), "r")
    s = json.loads(file.read())
    file.close()

    color = s["settings"]["color"]
    embed = discord.Embed(title="All files:", description="", colour=discord.Color(value=int(color, 16)))

    totalcounter = 0
    file_lines = ""

    for i in s["files"]:
        new_line = '"' + i["name"] + '"' + " Author: " + i["author_name"] + "\n"
        if len(file_lines) + len(new_line) < 1024:
            file_lines += new_line
            totalcounter += 1
        else:
            embed.add_field(name=8 * "```\u200b``` ", value=file_lines, inline=False)
            file_lines = ""

    if len(file_lines) > 0:
        embed.add_field(name=8 * "```\u200b``` ", value=file_lines, inline=False)

    embed.add_field(name=8*"```\u200b``` " + "\nTotal files:", value=str(totalcounter), inline=False)

    if totalcounter == 0:
        await Functions.embed(message, "All saved files:", "There are no files saved.")
    else:
        await message.channel.send(embed=embed)

    await Functions.bot_used(message, "files", message.channel.type)