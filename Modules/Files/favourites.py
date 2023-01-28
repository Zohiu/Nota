import Functions
import discord
import json
import os

fileDir = os.path.join(os.getcwd(), "Files")

async def run(message, bot, msglst, id):

    premium = await Functions.get_premium_status(message)
    if premium == "ultra":
        if len(msglst) < 2:
            msglst.append("None")

        if msglst[1] == "add":
            with open(os.path.join(fileDir, '{}.json'.format(id)), "r") as file:
                s = json.loads(file.read())

            already_there = False
            for file in s["favourites"]:
                if msglst[2] == file:
                    already_there = True

            if not already_there:
                found = False
                for file in s["files"]:
                    if msglst[2] == file["name"]:
                        found = True
                        break

                if found:
                    count = 1
                    for file in s["favourites"]:
                        count += 1
                    if count < 10:
                        s["favourites"].append(msglst[2])
                        with open(os.path.join(fileDir, '{}.json'.format(id)), "w") as file:
                            file.write(json.dumps(s))

                        await Functions.embed(message, "<:nota_success:796499295980617739> " + msglst[2] + " has been added to your favourites!")
                    else:
                        await Functions.embed(message, "<:nota_error:796499987949027349> You have reached the favourite file limit.")
                else:
                    await Functions.embed(message, "<:nota_error:796499987949027349> This file does not exist.")
            else:
                await Functions.embed(message, "<:nota_error:796499987949027349> You already added that file.")

        elif msglst[1] == "remove":
            with open(os.path.join(fileDir, '{}.json'.format(id)), "r") as file:
                s = json.loads(file.read())

            found = False
            for file in s["favourites"]:
                if msglst[2] == file:
                    found = True
                    break

            if found:
                s["favourites"].remove(msglst[2])
                with open(os.path.join(fileDir, '{}.json'.format(id)), "w") as file:
                    file.write(json.dumps(s))

                await Functions.embed(message, "<:nota_success:796499295980617739> " + msglst[2] + " has been removed from your favourites!")

            else:
                await Functions.embed(message, "<:nota_error:796499987949027349> This file is not in your favourites.")

        else:
            with open(os.path.join(fileDir, '{}.json'.format(id)), "r") as file:
                s = json.loads(file.read())

            if str(message.channel.type) == "private":
                id = os.path.join(str(message.author.id), str(message.author.id))
            else:
                id = os.path.join(str(message.guild.id), str(message.guild.id))

            file = open(os.path.join(fileDir, '{}.json'.format(id)), "r")
            s = json.loads(file.read())
            file.close()

            color = s["settings"]["color"]
            embed = discord.Embed(title="Favourites:", description="*To open a file, click the reaction with the number of the file. You can also react to any message from Nota with the correct number to open that file.*\n\n**Your favourites:**", colour=discord.Color(value=int(color, 16)))

            count = 0
            for file in s["favourites"]:
                count += 1
                embed.add_field(name=file, value="`Num. " + str(count) + "`", inline=True)

            if count == 0:
                embed.add_field(name="You do not have favourites.", value="\u200b", inline=True)

            msg = await message.channel.send(embed=embed)

            for i in range(count):
                if i == 0:
                    await msg.add_reaction("1️⃣")
                if i == 1:
                    await msg.add_reaction("2️⃣")
                if i == 2:
                    await msg.add_reaction("3️⃣")
                if i == 3:
                    await msg.add_reaction("4️⃣")
                if i == 4:
                    await msg.add_reaction("5️⃣")
                if i == 5:
                    await msg.add_reaction("6️⃣")
                if i == 6:
                    await msg.add_reaction("7️⃣")
                if i == 7:
                    await msg.add_reaction("8️⃣")
                if i == 8:
                    await msg.add_reaction("9️⃣")


    await Functions.bot_used(message, "favourites", message.channel.type)