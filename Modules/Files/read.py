from Modules import encryptor
import Functions
import discord
import json
import os

fileDir = os.path.join(os.getcwd(), "Files")

async def run(message, prefix, msglst, id):
    file = open(os.path.join(fileDir, '{}.json'.format(id)), "r")
    s = json.loads(file.read())
    file.close()

    type = "text"

    existing = False
    for i in s["files"]:
        if i["name"] == msglst[1]:
            existing = True
            name = i["name"]
            content = i["content"]
            footer = i["author_name"] + " | " + i["save_time"].split(".")[0]
            type = i["type"]

    executed = False


    if existing:
        if type == "text":
            executed = True
            await Functions.embed(message, name, encryptor.decrypt(content), footer)
        elif type == "raw":
            executed = True
            await message.channel.send(encryptor.decrypt(content))

    if type == "filetext":
        executed = True
        repeat = False
        done = False
        for d in os.walk(os.path.join(fileDir, str(message.guild.id))):
            for f in d:
                for string in f:
                    if len(string.split(".")) > 1 and not "json" in string:
                        if string.split(".")[0] == msglst[1]:
                            if not repeat:
                                if str(message.channel.type) == "private":
                                    id2 = str(message.author.id)
                                else:
                                    id2 = str(message.guild.id)

                                done = True
                                fileformat = string.split(".")[-1]
                                open(os.path.join(fileDir, "{}/{}".format(id2, string)))
                                file = discord.File(os.path.join(fileDir, "{}/{}".format(str(message.guild.id), string)), filename=msglst[1] + "." + str(fileformat), spoiler=False)
                                try:
                                    msg = content
                                    repeat = True
                                except:
                                    msg = " "
                                await message.channel.send(content=msg, file=file)
                                del fileformat, file, msg
                            else:
                                return
        if not done:
            await Functions.embed(message, "Error", "There is no such file called '" + msglst[1] + "'.")

    if not executed:
        await Functions.embed(message, "Error", "There is no such file called '" + msglst[1] + "'.")

    del existing, content, footer, type, executed, s

    await Functions.bot_used(message, "save", message.channel.type)