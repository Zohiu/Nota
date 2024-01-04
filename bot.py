if __name__ == '__main__':
    from Modules.Settings import setprefix, setcolor, resetcolor, togglefooter, toggleads, togglefavourites
    from Modules.Files import save, read, delete, files, favourites
    from Modules.Other import calc, embed, timer, stats, premium
    from discord.ext.commands import CommandNotFound
    from Modules import help, privacy, botstats
    from discord.ext import commands, tasks
    from discord.abc import PrivateChannel
    from Modules.Admin import broadcast
    from discord import errors
    from nota import version
    import Functions
    import shutil
    import json
    import time
    import dbl
    import os

    TOKEN = open("bot.token", "r").read()
    bot = commands.Bot("-")
    bot_updater = bot
    files_in_dir = []
    fileDir = os.path.join(os.getcwd(), "Files")
    start_time = time.time()

    bot.remove_command("help")


    class TopGG(commands.Cog):
        def __init__(self, bot_in):
            self.bot = bot_in
            self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY3MDc1NDYxMzgyMDkxNTcxNCIsImJvdCI6dHJ1ZSwiaWF0IjoxNjA3NDMwODA1fQ.7QZw6KUpNc-EyPnhRbYK1tfoMQNJTqzh--I-L9dj2Rk'  # set this to your DBL token
            self.dblpy = dbl.DBLClient(self.bot, self.token)
            self.update_stats.start()
            

        def cog_unload(self):
            self.update_stats.cancel()

        @tasks.loop(minutes=30)
        async def update_stats(self):
            await self.bot.wait_until_ready()
            
            try:
                server_count = len(self.bot.guilds)
                await self.dblpy.post_guild_count(server_count)
                print('[top.gg] Posted server count ({})'.format(server_count))
            except Exception as e:
                print('[top.gg] Failed to post server count\n{}: {}'.format(type(e).__name__, e))
            await Functions.update_status(bot)


    @bot.event
    async def on_guild_join(guild):
        print("[Guilds] The bot joined a guild. Current number:", len(bot.guilds))


    @bot.event
    async def on_guild_remove(guild):
        print("[Guilds] The bot left a guild. Current number:", len(bot.guilds))
        shutil.rmtree(os.path.join(fileDir, str(guild.id)), ignore_errors=True)


    @bot.event
    async def on_ready():
        bot.add_cog(TopGG(bot))
        print("[Debug] Nota is online.")
        print()
        await Functions.update_status(bot)


    @bot.event
    async def on_reaction_add(reaction, user):
        if user.id == bot.user.id:
            return

        if reaction.message.author.id == bot.user.id:
            emoji_list = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]

            for i in emoji_list:
                if reaction.emoji == i:
                    if str(reaction.message.channel.type) == "private":
                        current_id = os.path.join(str(reaction.message.author.id), str(reaction.message.author.id))
                    else:
                        current_id = os.path.join(str(reaction.message.guild.id), str(reaction.message.guild.id))

                    with open(os.path.join(fileDir, '{}.json'.format(current_id)), "r") as file:
                        s = json.loads(file.read())

                    await reaction.message.delete()
                    await read.run(reaction.message, "-", ["-read", s["favourites"][emoji_list.index(i)]], current_id)

                    return


    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, CommandNotFound):
            return ctx
        raise error


    @bot.event
    async def on_message(message):
        if message.author.id == bot.user.id:
            return

        try:
            prefix = await Functions.get_prefix(message)
        except FileNotFoundError:
            prefix = "-"
        except json.JSONDecodeError:
            if isinstance(message.channel, PrivateChannel):
                current_id = os.path.join(str(message.author.id), str(message.author.id))
                open(os.path.join(fileDir, '{}.json'.format(current_id)), "w+").write(
                    json.dumps({"files": [], "settings": {"prefix": "-", "color": "68C60E", "read_footer": True, "show_ads": True, "show_favourites": True}, "stats": [], "favourites": []}))
            else:
                current_id = os.path.join(str(message.guild.id), str(message.guild.id))
                open(os.path.join(fileDir, '{}.json'.format(current_id)), "w+").write(
                    json.dumps({"files": [], "settings": {"prefix": "-", "color": "68C60E", "read_footer": True, "show_ads": True, "show_favourites": True}, "stats": [], "favourites": []}))
            await message.channel.send(
                "Sorry, but there was a major error with your saved files. All of your files and settings had to be reset. Please join the support server and report exactly what happened leading up to this error. Thanks!\nhttps://discord.gg/yf3jehq4sn")
            print("[Error] Save file reset! User: " + message.author.name)
            return

        if message.content.lower() == "will nota kill us all?":
            await Functions.embed(message, "Yes.", "I will.")
            print("[Secret] NOTA WILL KILL EVERYONE!!!")
            return

        msglst = await Functions.input_handler(message.content)

        try:
            if not msglst[0].startswith(prefix):
                return
        except AttributeError:
            return

        try:
            print("[Bot] Nota has been used.")
            with open("Data/totaluses.dat", "r") as file:
                fread = file.read()
                with open("Data/totaluses.dat", "w") as file2:
                    file2.write(str(int(fread) + 1))

            if isinstance(message.channel, PrivateChannel):
                current_id = os.path.join(str(message.author.id), str(message.author.id))
                if not os.path.exists(os.path.join(fileDir, str(message.author.id))):
                    os.mkdir(os.path.join(fileDir, str(message.author.id)))
                if not os.path.exists((os.path.join(fileDir, '{}.json'.format(current_id)))):
                    open(os.path.join(fileDir, '{}.json'.format(current_id)), "w+").write(
                        json.dumps({"files": [], "settings": {"prefix": "-", "color": "68C60E", "read_footer": True, "show_ads": True, "show_favourites": True}, "stats": [], "favourites": []}))
            else:
                current_id = os.path.join(str(message.guild.id), str(message.guild.id))
                if not os.path.exists(os.path.join(fileDir, str(message.guild.id))):
                    os.mkdir(os.path.join(fileDir, str(message.guild.id)))
                if not os.path.exists((os.path.join(fileDir, '{}.json'.format(current_id)))):
                    open(os.path.join(fileDir, '{}.json'.format(current_id)), "w+").write(
                        json.dumps({"files": [], "settings": {"prefix": "-", "color": "68C60E", "read_footer": True, "show_ads": True, "show_favourites": True}, "stats": [], "favourites": []}))

            usrpremium = True
            with open(os.path.join(os.getcwd(), "premium.users"), "r") as f:
                for line in f.readlines():
                    lsplit = line.split("#")
                    if str(message.author.id) in lsplit[0]:
                        usrpremium = True

            if msglst[0] == prefix + "help":
                await help.run(message, prefix, msglst, version)

            elif msglst[0] == prefix + "privacy":
                await privacy.run(message, prefix, msglst, version)

            # ADMIN
            elif msglst[0] == prefix + "broadcast":
                if str(message.author.id) == "485441972111147010":
                    await broadcast.run(message, prefix, msglst, current_id, bot)
                else:
                    await Functions.embed(message, "Error!", "You do not have the permission to use this command!")

            # SETTINGS
            elif msglst[0] == prefix + "setprefix":
                await setprefix.run(message, prefix, msglst, current_id)

            elif msglst[0] == prefix + "setcolor":  # PREMIUM
                await setcolor.run(message, prefix, msglst, current_id)

            elif msglst[0] == prefix + "resetcolor":  # PREMIUM
                await resetcolor.run(message, prefix, msglst, current_id)

            elif msglst[0] == prefix + "togglefooter":  # PREMIUM
                await togglefooter.run(message, prefix, msglst, current_id)

            elif msglst[0] == prefix + "toggleads":  # PREMIUM
                await toggleads.run(message, prefix, msglst, current_id)

            elif msglst[0] == prefix + "togglefavourites":  # PREMIUM
                await togglefavourites.run(message, prefix, msglst, current_id)

            # STATS
            elif msglst[0] == prefix + "stats" or msglst[0] == prefix + "privatestats":
                if isinstance(message.channel, PrivateChannel):
                    await stats.run(message, prefix, msglst, os.path.join(str(message.author.id), str(message.author.id)))
                elif msglst[0] == prefix + "privatestats" and usrpremium:
                    await stats.run(message, prefix, msglst, os.path.join(str(message.author.id), str(message.author.id)))
                else:
                    await stats.run(message, prefix, msglst, current_id)

            # FILES
            elif msglst[0] == prefix + "save" or msglst[0] == prefix + "privatesave":
                if isinstance(message.channel, PrivateChannel):
                    await save.run(message, prefix, msglst, os.path.join(str(message.author.id), str(message.author.id)))
                elif msglst[0] == prefix + "privatesave" and usrpremium:
                    await save.run(message, prefix, msglst, os.path.join(str(message.author.id), str(message.author.id)))
                else:
                    await save.run(message, prefix, msglst, current_id)

            elif msglst[0] == prefix + "read" or msglst[0] == prefix + "privateread":
                if isinstance(message.channel, PrivateChannel):
                    await read.run(message, prefix, msglst, os.path.join(str(message.author.id), str(message.author.id)))
                elif msglst[0] == prefix + "privateread" and usrpremium:
                    await read.run(message, prefix, msglst, os.path.join(str(message.author.id), str(message.author.id)))
                else:
                    await read.run(message, prefix, msglst, current_id)

            elif msglst[0] == prefix + "delete" or msglst[0] == prefix + "privatedelete":
                if isinstance(message.channel, PrivateChannel):
                    await delete.run(message, prefix, msglst, os.path.join(str(message.author.id), str(message.author.id)))
                elif msglst[0] == prefix + "privatedelete" and usrpremium:
                    await delete.run(message, prefix, msglst, os.path.join(str(message.author.id), str(message.author.id)))
                else:
                    await delete.run(message, prefix, msglst, current_id)

            elif msglst[0] == prefix + "files" or msglst[0] == prefix + "privatefiles":
                if isinstance(message.channel, PrivateChannel):
                    await files.run(message, prefix, msglst, os.path.join(str(message.author.id), str(message.author.id)))
                elif msglst[0] == prefix + "privatefiles" and usrpremium:
                    await files.run(message, prefix, msglst, os.path.join(str(message.author.id), str(message.author.id)))
                else:
                    await files.run(message, prefix, msglst, current_id)

            elif msglst[0] == prefix + "favourites":
                await favourites.run(message, bot, msglst, current_id)

            # OTHER
            elif msglst[0] == prefix + "timer":
                await timer.run(message, prefix, msglst)

            elif msglst[0] == prefix + "calc":
                await calc.run(message, msglst)

            elif msglst[0] == prefix + "embed":
                await embed.run(message, prefix, msglst)

            elif msglst[0] == prefix + "botstats":
                await botstats.run(message, bot, start_time, time, current_id)

            # Premium
            elif msglst[0] == prefix + "premium":
                await premium.run(message)

            else:
                if msglst[0].startswith(prefix):
                    await Functions.embed(message, "<:nota_error:796499987949027349> That's not a command. type '" + prefix + "help' to find out hot the bot works!")

        except errors.Forbidden as e:
            stringsend = "I am missing some permissions here. Please make sure that I have all of the ones below:"
            stringsend += "\n- Manage Messages"
            stringsend += "\n- Embed Links"
            stringsend += "\n- Attach Files"
            stringsend += "\n- Read Message History"
            stringsend += "\n- Use External Emojis"
            stringsend += "\n\nIf you have any more problems, join the support server. (link on Nota's top.gg page)"
            print("[Error] Someone didn't give Nota permissions: " +
                  str(e).split("(")[1].split(")")[0].split(":")[
                      1].strip(" "))
            try:
                await message.channel.send(stringsend)
            except errors.Forbidden:
                print("[Error] ...and the Bot couldn't even tell them...")
            return
        except UnicodeDecodeError as e:
            print("[Error] " + str(e))

        except json.JSONDecodeError as e:
            print("[Error] " + str(e))

        # except Exception as e:
        #   print("Error: " + str(e))

        await bot.process_commands(message)


    bot.run(TOKEN)
