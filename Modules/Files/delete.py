import Functions
import json
import os

fileDir = os.path.join(os.getcwd(), "Files")


async def run(message, prefix, msglst, id):
    file = open(os.path.join(fileDir, '{}.json'.format(id)), "r")
    s = json.loads(file.read())
    file.close()

    found = False
    for i in s["files"]:
        if i["name"] == msglst[1]:
            s["files"].remove(i)
            for file in s["favourites"]:
                if msglst[1] == file:
                    s["favourites"].remove(msglst[1])
            found = True
    if found:
        open(os.path.join(fileDir, '{}.json'.format(id)), "w").write(json.dumps(s))
        await Functions.embed(message, "<:nota_success:796499295980617739> The file has been deleted.")

    elif not found:
        done = False
        for d in os.walk(id):
            for f in d:
                for string in f:
                    if len(string.split(".")) > 1 and not "json" in string:
                        if string.split(".")[0] == msglst[1]:
                            os.remove(os.path.join(id, string))

                            if os.path.exists(os.path.join(id, string)):
                                os.remove(os.path.join(id, string))

                            await Functions.embed(message,
                                                  "<:nota_success:796499295980617739> The file has been deleted.")
                            done = True

                            file = os.path.join(fileDir, '{}/dc.list'.format(message.guild.id))
                            tostrip = '"' + msglst[1] + '" (file)'

                            with open(file, "r") as fl:
                                lines = fl.readlines()

                            with open(file, "w") as fl:
                                for line in lines:
                                    if line.strip("\n") != tostrip:
                                        fl.write(line)
        if not done:
            msglst += " "
            await Functions.embed(message,
                                  "<:nota_error:796499987949027349> There is no such file called '" + msglst[1] + "'.")

    await Functions.bot_used(message, "delete", message.channel.type)
