import Functions
import discord
import json
import os

fileDir = os.path.join(os.getcwd(), "Files")


async def run(message, prefix, msglst, id2, bot):
    if str(message.channel.type) == "private":
        id = os.path.join(str(message.author.id), str(message.author.id))
    else:
        id = os.path.join(str(message.guild.id), str(message.guild.id))

    file = open(os.path.join(fileDir, '{}.json'.format(id)), "r")
    s = json.loads(file.read())
    file.close()

    color = s["settings"]["color"]
    embed = discord.Embed(title=msglst[1], description=msglst[2], colour=discord.Color(value=int(color, 16)))

    sendto = 0
    owners = []

    for guild in bot.guilds:
        owner = guild.owner_id
        try:
            if not {"name": str(bot.get_user(owner)), "id": str(guild.owner_id)} in owners:
                await bot.get_user(owner).send(embed=embed)
                owners.append({"name": str(bot.get_user(owner)), "id": str(guild.owner_id)})
                sendto += 1
        except Exception as e:
            print(e)
            continue

    await Functions.embed(message, "Broadcast", "Sent to " + str(sendto) + " owners!")

    for owner in owners:
        await message.channel.send(owner["name"] + " | " + owner["id"])
