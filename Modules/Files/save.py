from Modules import encryptor
import Functions
import datetime
import json
import os

fileDir = os.path.join(os.getcwd(), "Files")

async def run(message, prefix, msglst, id):
    if len(msglst) > 5:
        await Functions.embed(message, "Error!", "That is not a valid argument.")
        return

    premium = await Functions.get_premium_status(message)
    allowed = True
    rlallowed = True

    files = 1
    counter = 0

    rlfiles = counter

    if premium == "none":
        if files >= 10:
            allowed = False
        if rlfiles >= 0:
            rlallowed = False
    elif premium == "default":
        if files >= 25:
            allowed = False
        if rlfiles >= 5:
            rlallowed = False
    elif premium == "pro":
        if files >= 50:
            allowed = False
        if rlfiles >= 15:
            rlallowed = False
    elif premium == "ultra":
        if files >= float('inf'):
            allowed = False
        if rlfiles >= 25:
            rlallowed = False

    done = False

    if allowed:
        if msglst[1] == "text":
            encrypted_text = encryptor.encrypt(msglst[3])

            done = True
            file = open(os.path.join(fileDir, '{}.json'.format(id)), "r")
            s = json.loads(file.read())
            file.close()
            newfile = {"name": msglst[2], "content": encrypted_text, "author_name": str(message.author), "author_id": str(message.author.id), "type": "text", "save_time": str(datetime.datetime.now())}
            already_used = False
            already_different = False
            for i in s["files"]:
                if i["name"] == newfile["name"]:
                    already_used = True
                if i["name"] == newfile["name"] and not i["type"] == "text":
                    already_different = True

            if already_different:
                await Functions.embed(message, "Error!", "A file with this name already exists!")

            elif not already_used:
                s["files"].append(newfile)
                open(os.path.join(fileDir, '{}.json'.format(id)), "w").write(json.dumps(s))
                await Functions.embed(message, "Successfully saved!", "'" + msglst[3] + "' was saved in '" + msglst[2] + "'")

            elif already_used:
                for i in s["files"]:
                    if i["name"] == newfile["name"]:
                        content = encryptor.decrypt(i["content"])
                        s["files"].remove(i)

                newfile = {"name": msglst[2], "content": content + encrypted_text, "author_name": str(message.author), "author_id": str(message.author.id), "type": "text", "save_time": str(datetime.datetime.now())}
                s["files"].append(newfile)
                open(os.path.join(fileDir, '{}.json'.format(id)), "w").write(json.dumps(s))
                await Functions.embed(message, "Successfully saved!", "The previous text has been overwritten.")
            del file, s, newfile, already_used, already_different

        elif msglst[1] == "raw":
            encrypted_text = encryptor.encrypt(msglst[3])
            done = True
            file = open(os.path.join(fileDir, '{}.json'.format(id)), "r")
            s = json.loads(file.read())
            file.close()
            newfile = {"name": msglst[2], "content": encrypted_text, "author_name": str(message.author),
                       "author_id": str(message.author.id), "type": "raw", "save_time": str(datetime.datetime.now())}
            already_used = False
            already_different = False
            for i in s["files"]:
                if i["name"] == newfile["name"]:
                    already_used = True
                if i["name"] == newfile["name"] and not i["type"] == "raw":
                    already_different = True

            if already_different:
                await Functions.embed(message, "Error!", "A file with this name already exists!")

            elif not already_used:
                s["files"].append(newfile)
                open(os.path.join(fileDir, '{}.json'.format(id)), "w").write(json.dumps(s))
                await Functions.embed(message, "Successfully saved!",
                                      "'" + msglst[3] + "' was saved in '" + msglst[2] + "'")

            elif already_used:
                for i in s["files"]:
                    if i["name"] == newfile["name"]:
                        content = encryptor.decrypt(i["content"])
                        s["files"].remove(i)

                newfile = {"name": msglst[2], "content": encryptor.encrypt(content + msglst[3]), "author_name": str(message.author),
                           "author_id": str(message.author.id), "type": "raw", "save_time": str(datetime.datetime.now())}
                s["files"].append(newfile)
                open(os.path.join(fileDir, '{}.json'.format(id)), "w").write(json.dumps(s))
                await Functions.embed(message, "Successfully saved!", "The previous text has been overwritten.")

            del file, s, newfile, already_used, already_different

    if rlallowed and not done:
        done = True
        if msglst[1] == "file":
            if rlallowed:
                try:
                    if message.attachments[0].size < 8000000:
                        if str(message.channel.type) == "private":
                            id2 = str(message.author.id)
                        else:
                            id2 = str(message.guild.id)

                        await message.attachments[0].save(os.path.join(fileDir, '{}/{}'.format(id2, msglst[2] + "." + msglst[3])))

                        if not len(msglst) >= 6:
                            print(msglst)

                        file = open(os.path.join(fileDir, '{}.json'.format(id)), "r")
                        s = json.loads(file.read())
                        file.close()
                        if len(msglst) <= 4:
                            newfile = {"name": msglst[2], "content": "", "author_name": str(message.author),
                                       "author_id": str(message.author.id), "type": "filetext", "save_time": str(datetime.datetime.now())}
                        else:
                            newfile = {"name": msglst[2], "content": msglst[4], "author_name": str(message.author),
                                       "author_id": str(message.author.id), "type": "filetext", "save_time": str(datetime.datetime.now())}

                        already_used = False
                        already_different = False
                        for i in s["files"]:
                            if i["name"] == newfile["name"]:
                                already_used = True
                            if i["name"] == newfile["name"] and not i["type"] == "text":
                                already_different = True

                        if not already_used:
                            s["files"].append(newfile)
                            open(os.path.join(fileDir, '{}.json'.format(id)), "w").write(json.dumps(s))


                        elif already_used:
                            for i in s["files"]:
                                if i["name"] == newfile["name"]:
                                    content = i["content"]
                                    s["files"].remove(i)

                            newfile = {"name": msglst[2], "content": content + msglst[4],
                                       "author_name": str(message.author), "author_id": str(message.author.id),
                                       "type": "filetext", "save_time": str(datetime.datetime.now())}
                            s["files"].append(newfile)
                            open(os.path.join(fileDir, '{}.json'.format(id)), "w").write(json.dumps(s))

                        await Functions.embed(message, "Success!", "The file was saved as '" + msglst[2] + "'. type '" + prefix + "read " + msglst[2] + "' to see your saved data.")

                        del already_used, already_different, s, newfile, id2

                    else:
                        await Functions.embed(message, "Error!", "This file is too big! Max: 8mb")
                except IndexError as e:
                    await Functions.embed(message, "Error!", "There is no attachment.")
            else:
                await Functions.embed(message, "Error!",
                                      "You have reached your file limit! consider upgrading your premium status.")

    elif not done:
        await Functions.embed(message, "Error!", "You have reached your file limit! consider upgrading your premium status.")

    del premium, allowed, rlallowed, files, counter, rlfiles, done

    await Functions.bot_used(message, "save", message.channel.type)