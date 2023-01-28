from discord.abc import PrivateChannel
import discord
import json
import os

fileDir = os.path.join(os.getcwd(), "Files")


async def embed(message, *args):
    if str(message.channel.type) == "private":
        current_id = os.path.join(str(message.author.id), str(message.author.id))
    else:
        current_id = os.path.join(str(message.guild.id), str(message.guild.id))

    file = open(os.path.join(fileDir, '{}.json'.format(current_id)), "r")
    s = json.loads(file.read())
    file.close()

    if len(args) == 1:
        describtion = args[0]
        title = args[0]
    else:
        describtion = args[1]
        title = args[0]

    # if s["settings"]["show_ads"] == True and bool(random.getrandbits(1)) == True:
    #    describtion += "\n\nIn need of an invite manager bot? Click [here](https://nira.ferdi.xyz) to invite Nira! The cat that manages your invites, quick and easy to use."
    #    with open("Ads/Nira.dat", "r") as file:
    #        fread = file.read()
    #        with open("Ads/Nira.dat", "w") as file:
    #            file.write(str(int(fread) + 1))

    color = s["settings"]["color"]

    if len(args) == 1:
        current_embed = discord.Embed(description=describtion, colour=discord.Color(value=int(color, 16)))
    else:
        current_embed = discord.Embed(title=title, description=describtion, colour=discord.Color(value=int(color, 16)))

    if len(args) > 0:
        with open(os.path.join(fileDir, '{}.json'.format(current_id)), "r") as file:
            s = json.loads(file.read())

            try:
                if s["settings"]["read_footer"]:
                    current_embed.set_footer(text="Author: " + str(args[2]))
            except IndexError:
                pass

    msg = await message.channel.send(embed=current_embed)

    if s["settings"]["show_favourites"]:
        count = 0
        for file in s["favourites"]:
            count += 1
            current_embed.add_field(name=file, value="`Num. " + str(count) + "`", inline=True)

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

    del s, color, current_embed, msg


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
    activity = None
    if random == 1:
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
        activity = discord.Game(name="Join the support server if you have any problems!")
    elif random == 8:
        activity = discord.Game(name="Fguzy is kinda sus..")
    elif random == 9:
        activity = discord.Game(name="To support nota, you can donate.")
    elif random == 10:
        activity = discord.Game(name="https://donatebot.io/checkout/673372073242132480")

    await bot.change_presence(status=discord.Status.online, activity=activity)


async def get_prefix(message):
    if isinstance(message.channel, PrivateChannel):
        file = open(os.path.join(fileDir, '{}/{}.json'.format(str(message.author.id), str(message.author.id))), "r")
        s = json.loads(file.read())
        file.close()
        return s["settings"]["prefix"]
    else:
        file = open(os.path.join(fileDir, '{}/{}.json'.format(str(message.guild.id), str(message.guild.id))), "r")
        s = json.loads(file.read())
        file.close()
        return s["settings"]["prefix"]


async def bot_used(message, command, channeltype):
    if isinstance(message.channel, PrivateChannel):
        current_id = os.path.join(str(message.author.id), str(message.author.id))
    else:
        current_id = os.path.join(str(message.guild.id), str(message.guild.id))

    file = open(os.path.join(fileDir, '{}.json'.format(current_id)), "r")
    s = json.loads(file.read())
    file.close()
    already_used = False
    for i in s["stats"]:
        if i["name"] == command:
            already_used = True

    if not already_used:
        new = {"name": command, "value": 1}
        s["stats"].append(new)
        open(os.path.join(fileDir, '{}.json'.format(current_id)), "w").write(json.dumps(s))

    elif already_used:
        value = 0
        for i in s["stats"]:
            if i["name"] == command:
                value = i["value"]
                s["stats"].remove(i)

        new = {"name": command, "value": value + 1}
        s["stats"].append(new)
        open(os.path.join(fileDir, '{}.json'.format(current_id)), "w").write(json.dumps(s))

    del current_id, file, s, already_used, new
    return channeltype


async def input_handler(message_content):
    if len(message_content) < 1:
        return [None]

    current_string = ""
    in_quotation = False
    msglst = []
    for i in message_content:
        if i == '"' or i == '“' or i == '”':
            i = ""
            if in_quotation:
                in_quotation = False
                msglst.append(current_string)
                current_string = ""

            elif not in_quotation:
                in_quotation = True

        if i == " " and not in_quotation:
            i = ""
            msglst.append(current_string)
            current_string = ""

        current_string += i
    msglst.append(current_string)

    for i in msglst:
        if i == "":
            msglst.remove(i)

    return msglst
