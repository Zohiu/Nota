import Functions
import discord
import json
import os
import asyncio

fileDir = os.path.join(os.getcwd(), "Files")

async def run(message, prefix, msglst):
    premium = await Functions.get_premium_status(message)

    if premium == "ultra":
        timerGoing = True
        counter = int(msglst[1])

        if str(message.channel.type) == "private":
            id = message.author.id
        else:
            id = message.guild.id

        file = open(os.path.join(fileDir, '{}.json'.format(id)), "r")
        s = json.loads(file.read())
        file.close()

        color = s["settings"]["color"]
        embed = discord.Embed(title="Timer:", description=str(counter), colour=discord.Color(value=int(color, 16)))



        msg = await message.channel.send(embed=embed)

        while timerGoing:
            embed = discord.Embed(title="Timer:", description=str(counter), colour=discord.Color(value=int(color, 16)))

            await msg.delete()
            msg = await message.channel.send(embed=embed)

            counter -= 1

            if counter == 0:
                timerGoing = False

            await asyncio.sleep(1)



        embed = discord.Embed(title="Timer:", description="Time is up!",
                                  colour=discord.Color(value=int(color, 16)))

        await msg.delete()
        msg = await message.channel.send(embed=embed)

        await Functions.bot_used(message, "timer", message.channel.type)

    else:
        await Functions.embed(message, "<:nota_error:796499987949027349> You need at least premium ultra to use this command!")