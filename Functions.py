import discord
import random
import json
import os

fileDir = os.path.join(os.getcwd(), "Files")

async def embed(message, title, describtion, *args):
    if str(message.channel.type) == "private":
        id = os.path.join(str(message.author.id), str(message.author.id))
    else:
        id = os.path.join(str(message.guild.id), str(message.guild.id))

    file = open(os.path.join(fileDir, '{}.json'.format(id)), "r")
    s = json.loads(file.read())
    file.close()

    if s["settings"]["show_ads"] == True and bool(random.getrandbits(1)) == True:
        describtion += "\n\nIn need of an invite manager bot? Click [here](https://nira.ferdi.xyz) to invite Nira! The cat that manages your invites, quick and easy to use."
        with open("Ads/Nira.dat", "r") as file:
            fread = file.read()
            with open("Ads/Nira.dat", "w") as file:
                file.write(str(int(fread) + 1))

    color = s["settings"]["color"]
    embed = discord.Embed(title=title, description=describtion, colour=discord.Color(value=int(color, 16)))

    if len(args) > 0:
        with open(os.path.join(fileDir, '{}.json'.format(id)), "r") as file:
            s = json.loads(file.read())

            if s["settings"]["read_footer"] == True:
                embed.set_footer(text="Author: " + str(args[0]))

    msg = await message.channel.send(embed=embed)

    if s["settings"]["show_favourites"] == True:
        count = 0
        for file in s["favourites"]:
            count += 1
            embed.add_field(name=file, value="`Num. " + str(count) + "`", inline=True)

        for i in range(count):
            if i == 0:
                await msg.add_reaction("1??")
            if i == 1:
                await msg.add_reaction("2??")
            if i == 2:
                await msg.add_reaction("3??")
            if i == 3:
                await msg.add_reaction("4??")
            if i == 4:
                await msg.add_reaction("5??")
            if i == 5:
                await msg.add_reaction("6??")
            if i == 6:
                await msg.add_reaction("7??")
            if i == 7:
                await msg.add_reaction("8??")
            if i == 8:
                await msg.add_reaction("9??")

    del s, color, embed, msg

async def get_premium_status(message):
    if open("premium_manipulation", "r").read() == "":
        if str(message.channel.type) == "private":
            with open(os.path.join(os.getcwd(), "premium.users"), "r") as f:
                for line in f.readlines():
                    lsplit = line.split("#")
                    if str(message.author.id) in lsplit[0]:
                        if "default" in lsplit[2]:
                            return "default"
                        elif "pro" in lsplit[2]:
                            return "pro"
                        elif "ultra" in lsplit[2]:
                            return "ultra"

        else:
            with open(os.path.join(os.getcwd(), "premium.users"), "r") as f:
                for line in f.readlines():
                    lsplit = line.split("#")
                    if str(message.guild.owner_id) in lsplit[0]:
                        if "default" in lsplit[2]:
                            return "default"
                        elif "pro" in lsplit[2]:
                            return "pro"
                        elif "ultra" in lsplit[2]:
                            return "ultra"

        return "none"

    else:
        return open("premium_manipulation", "r").read()

async def update_status(bot):
    from random import randint
    random = randint(1, 10)
    if random == 1:
        count = 0
        for dirpath, dirnames, filenames in os.walk(fileDir):
            for filename in [f for f in filenames if f == "private.info"]:
                count += 1
        activity = discord.Game(name=str(len(bot.guilds)) + " Servers!")
    elif random == 2:
        activity = discord.Game(name="This is Nota pun.")
    elif random == 3:
        activity = discord.Game(name="psst Fguzy is kinda sus..")
    elif random == 4:
        activity = discord.Game(name="hint: what is my nota prefix?")
    elif random == 5:
        activity = discord.Game(name="Made in Germany")
    elif random == 6:
        activity = discord.Game(name="-help")
    elif random == 7:
        activity = discord.Game(name="If you have any ideas, join the support server!")
    elif random == 8:
        activity = discord.Game(name="Fguzy is kinda sus..")
    elif random == 9:
        activity = discord.Game(name="To support nota you can donate.")
    elif random == 10:
        activity = discord.Game(name="https://donatebot.io/checkout/673372073242132480")

    await bot.change_presence(status=discord.Status.online, activity=activity)

async def get_prefix(message):
    if str(message.channel.type) == "private":
        file = open(os.path.join(fileDir, '{}/{}.json'.format(str(message.author.id), str(message.author.id))), "r")
        s = json.loads(file.read())
        file.close()
        return s["settings"]["prefix"]
    else:
        file = open(os.path.join(fileDir, '{}/{}.json'.format(str(message.guild.id), str(message.guild.id))), "r")
        s = json.loads(file.read())
        file.close()
        return s["settings"]["prefix"]

async def bot_used(message, command, ChannelTypePrivate):
    if str(message.channel.type) == "private":
        id = os.path.join(str(message.author.id), str(message.author.id))
    else:
        id = os.path.join(str(message.guild.id), str(message.guild.id))

    file = open(os.path.join(fileDir, '{}.json'.format(id)), "r")
    s = json.loads(file.read())
    file.close()
    already_used = False
    for i in s["stats"]:
        if i["name"] == command:
            already_used = True

    if not already_used:
        new = {"name": command, "value": 1}
        s["stats"].append(new)
        open(os.path.join(fileDir, '{}.json'.format(id)), "w").write(json.dumps(s))

    elif already_used:
        for i in s["stats"]:
            if i["name"] == command:
                value = i["value"]
                s["stats"].remove(i)

        new = {"name": command, "value": value + 1}
        s["stats"].append(new)
        open(os.path.join(fileDir, '{}.json'.format(id)), "w").write(json.dumps(s))

    del id, file, s, already_used, new

async def input_handler(message_content):
    rawlst = message_content.split(' ')
    msglst = []
    track = ""
    trackstart = False

    if message_content == None:
        del rawlst, msglst, track, trackstart
        return ["notAcommand"]
    else:
        for string in rawlst:
            try:
                if string[0] == '"' and string[-1] == '"':
                    msglst.append(string.strip('"'))

                elif string[0] == '"':
                    trackstart = True
                    track += string.strip('"') + " "

                elif string[-1] == '"':
                    msglst.append(track + string.strip('"'))
                    track = ""
                    trackstart = False

                elif trackstart:
                    track += string.strip('"') + " "

                elif not string == " ":
                    msglst.append(string.strip('"'))
            except:
                msglst.append(string.strip('"'))
        return msglst
        del rawlst, msglst, track, trackstart