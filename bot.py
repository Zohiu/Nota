if __name__ == '__main__':
    from Modules.Settings import setprefix, setcolor, resetcolor, togglefooter, toggleads, togglefavourites
    from Modules.Other import calc, embed, guilds, ping, timer, uptime, total, speed
    from Modules.Files import save, read, delete, files, favourites
    from Modules import help, stats, premium, privacy
    from discord.ext.commands import CommandNotFound
    from discord.ext import commands, tasks
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
    dirpath = os.path.join(os.getcwd(), "Files")
    location = dirpath
    files_in_dir = []
    fileDir = os.path.join(os.getcwd(), "Files")
    start_time = time.time()
    allcmds = ["help", "setprefix", "setcolor", "stats", "timer", "save", "read", "delete", "files",
                       "share", "privatesave", "privateread", "privatedelete", "privatefiles", "calc", "ping", "embed",
                       "guilds", "premium", "uptime", "speed"]

    bot.remove_command("help")


    class TopGG(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
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
                print('Posted server count ({})'.format(server_count))
            except Exception as e:
                print('Failed to post server count\n{}: {}'.format(type(e).__name__, e))

    class Events:
        @bot.event
        async def on_guild_join(guild):
            print("The bot joined a guild. Current number:", len(bot.guilds))
            await Functions.update_status(bot)

        @bot.event
        async def on_guild_remove(guild):
            print("The bot left a guild. Current number:", len(bot.guilds))
            shutil.rmtree(os.path.join(fileDir, str(guild.id)), ignore_errors=True)
            await Functions.update_status(bot)

        @bot.event
        async def on_ready():
            bot.add_cog(TopGG(bot))
            print("\nNota is online.\n")
            print()
            await Functions.update_status(bot)

        @bot.event
        async def on_reaction_add(reaction, user):
            if not user.id == bot.user.id:
                if reaction.message.author.id == bot.user.id:
                    if str(reaction.message.channel.type) == "private":
                        id = os.path.join(str(reaction.message.author.id), str(reaction.message.author.id))
                    else:
                        id = os.path.join(str(reaction.message.guild.id), str(reaction.message.guild.id))

                    if reaction.emoji == "1??":
                        await reaction.message.remove_reaction("1??", user)
                        with open(os.path.join(fileDir, '{}.json'.format(id)), "r") as file:
                            s = json.loads(file.read())
                        await read.run(reaction.message, "-", ["-read", s["favourites"][0]], id)

                    elif reaction.emoji == "2??":
                        await reaction.message.remove_reaction("2??", user)
                        with open(os.path.join(fileDir, '{}.json'.format(id)), "r") as file:
                            s = json.loads(file.read())
                        await read.run(reaction.message, "-", ["-read", s["favourites"][1]], id)

                    elif reaction.emoji == "3??":
                        await reaction.message.remove_reaction("3??", user)
                        with open(os.path.join(fileDir, '{}.json'.format(id)), "r") as file:
                            s = json.loads(file.read())
                        await read.run(reaction.message, "-", ["-read", s["favourites"][2]], id)

                    elif reaction.emoji == "4??":
                        await reaction.message.remove_reaction("4??", user)
                        with open(os.path.join(fileDir, '{}.json'.format(id)), "r") as file:
                            s = json.loads(file.read())
                        await read.run(reaction.message, "-", ["-read", s["favourites"][3]], id)

                    elif reaction.emoji == "5??":
                        await reaction.message.remove_reaction("5??", user)
                        with open(os.path.join(fileDir, '{}.json'.format(id)), "r") as file:
                            s = json.loads(file.read())
                        await read.run(reaction.message, "-", ["-read", s["favourites"][4]], id)

                    elif reaction.emoji == "6??":
                        await reaction.message.remove_reaction("6??", user)
                        with open(os.path.join(fileDir, '{}.json'.format(id)), "r") as file:
                            s = json.loads(file.read())
                        await read.run(reaction.message, "-", ["-read", s["favourites"][5]], id)

                    elif reaction.emoji == "7??":
                        await reaction.message.remove_reaction("7??", user)
                        with open(os.path.join(fileDir, '{}.json'.format(id)), "r") as file:
                            s = json.loads(file.read())
                        await read.run(reaction.message, "-", ["-read", s["favourites"][6]], id)

                    elif reaction.emoji == "8??":
                        await reaction.message.remove_reaction("8??", user)
                        with open(os.path.join(fileDir, '{}.json'.format(id)), "r") as file:
                            s = json.loads(file.read())
                        await read.run(reaction.message, "-", ["-read", s["favourites"][7]], id)

                    elif reaction.emoji == "9??":
                        await reaction.message.remove_reaction("9??", user)
                        with open(os.path.join(fileDir, '{}.json'.format(id)), "r") as file:
                            s = json.loads(file.read())
                        await read.run(reaction.message, "-", ["-read", s["favourites"][8]], id)


        @bot.event
        async def on_command_error(ctx, error):
            if isinstance(error, CommandNotFound):
                return
            raise error

    class Commands:
        @bot.event
        async def on_message(message):
            try:
                if str(message.channel.type) == "private":
                    id = os.path.join(str(message.author.id), str(message.author.id))
                    if not os.path.exists(os.path.join(fileDir, str(message.author.id))):
                        os.mkdir(os.path.join(fileDir, str(message.author.id)))
                    if not os.path.exists((os.path.join(fileDir, '{}.json'.format(id)))):
                        open(os.path.join(fileDir, '{}.json'.format(id)), "w+").write(json.dumps({"files": [], "settings": {"prefix": "-", "color": "68C60E", "read_footer": True, "show_ads": True, "show_favourites": True},"stats": [], "favourites": []}))
                else:
                    id = os.path.join(str(message.guild.id), str(message.guild.id))
                    if not os.path.exists(os.path.join(fileDir, str(message.guild.id))):
                        os.mkdir(os.path.join(fileDir, str(message.guild.id)))
                    if not os.path.exists((os.path.join(fileDir, '{}.json'.format(id)))):
                        open(os.path.join(fileDir, '{}.json'.format(id)), "w+").write(json.dumps({"files": [], "settings": {"prefix": "-", "color": "68C60E", "read_footer": True, "show_ads": True, "show_favourites": True},"stats": [], "favourites": []}))

                global bot_updater
                bot_updater = bot
                if message.author.id == bot.user.id:
                    return

                import Functions
                msglst = await Functions.input_handler(message.content)

                try:
                    prefix = await Functions.get_prefix(message)
                except FileNotFoundError:
                    prefix = "-"

                if message.content.lower() == "what is my nota prefix?":
                    await Functions.embed(message, "Your Prefix is:", prefix)
                    print("OOF! Someone forgot their prefix.")

                if message.content.lower() == "will nota kill us all?":
                    await Functions.embed(message, "Yes.", "I will.")
                    print("NOTA WILL KILL EVERYONE!!!")

                if not msglst[0].startswith(prefix):
                    return

                else:
                    print("The bot was used.")

                    await Functions.update_status(bot)

                    usrpremium = False
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
                            await broadcast.run(message, prefix, msglst, id, bot)
                        else:
                            await Functions.embed(message, "Error!", "You do not have the permission to use this command!")

                    # SETTINGS
                    elif msglst[0] == prefix + "setprefix":
                        await setprefix.run(message, prefix, msglst, id)

                    elif msglst[0] == prefix + "setcolor": # PREMIUM
                        await setcolor.run(message, prefix, msglst, id)

                    elif msglst[0] == prefix + "resetcolor": # PREMIUM
                        await resetcolor.run(message, prefix, msglst, id)

                    elif msglst[0] == prefix + "togglefooter": # PREMIUM
                        await togglefooter.run(message, prefix, msglst, id)

                    elif msglst[0] == prefix + "toggleads": # PREMIUM
                        await toggleads.run(message, prefix, msglst, id)

                    elif msglst[0] == prefix + "togglefavourites": # PREMIUM
                        await togglefavourites.run(message, prefix, msglst, id)

                    # STATS
                    elif msglst[0] == prefix + "stats" or msglst[0] == prefix + "privatestats":
                        if str(message.channel.type) == "private":
                            await stats.run(message, prefix, msglst, id)
                        elif msglst[0] == prefix + "privatestats" and usrpremium:
                            await stats.run(message, prefix, msglst, id)
                        else:
                            await stats.run(message, prefix, msglst, id)

                    # FILES
                    elif msglst[0] == prefix + "save" or msglst[0] == prefix + "privatesave":
                        if str(message.channel.type) == "private":
                            await save.run(message, prefix, msglst, id)
                        elif msglst[0] == prefix + "privatesave" and usrpremium:
                            await save.run(message, prefix, msglst, id)
                        else:
                            await save.run(message, prefix, msglst, id)

                    elif msglst[0] == prefix + "read" or msglst[0] == prefix + "privateread":
                        if str(message.channel.type) == "private":
                            await read.run(message, prefix, msglst, id)
                        elif msglst[0] == prefix + "privateread" and usrpremium:
                            await read.run(message, prefix, msglst, id)
                        else:
                            await read.run(message, prefix, msglst, id)

                    elif msglst[0] == prefix + "delete" or msglst[0] == prefix + "privatedelete":
                        if str(message.channel.type) == "private":
                            await delete.run(message, prefix, msglst, id)
                        elif msglst[0] == prefix + "privateread" and usrpremium:
                            await delete.run(message, prefix, msglst, id)
                        else:
                            await delete.run(message, prefix, msglst, id)

                    elif msglst[0] == prefix + "files" or msglst[0] == prefix + "privatefiles":
                        if str(message.channel.type) == "private":
                            await files.run(message, prefix, msglst, id)
                        elif msglst[0] == prefix + "privateread" and usrpremium:
                            await files.run(message, prefix, msglst, id)
                        else:
                            await files.run(message, prefix, msglst, id)

                    elif msglst[0] == prefix + "favourites":
                        await favourites.run(message, bot, msglst, id)

                    # OTHER
                    elif msglst[0] == prefix + "timer":
                        await timer.run(message, prefix, msglst)

                    elif msglst[0] == prefix + "calc":
                        await calc.run(message, msglst)

                    elif msglst[0] == prefix + "ping":
                        await ping.run(message, bot)

                    elif msglst[0] == prefix + "embed":
                        await embed.run(message, prefix, msglst)

                    elif msglst[0] == prefix + "guilds":
                        await guilds.run(message, bot)

                    elif msglst[0] == prefix + "total":
                        await total.run(message, bot)

                    elif msglst[0] == prefix + "uptime":
                        await uptime.run(message, start_time, time)

                    elif msglst[0] == prefix + "speed":
                        await speed.run(message)

                    # Premium
                    elif msglst[0] == prefix + "premium":
                        await premium.run(message)

                    else:
                        if msglst[0].startswith(prefix):
                            await Functions.embed(message, "Error!", "That's not a command. type '" + prefix + "help' to find out hot the bot works! If this prefix is used by another bot then maybe consider changing it.")

                await bot.process_commands(message)

            except errors.Forbidden:
                print("Someone tried to use the bot in a channel where it doesn't have permissions.")
            except UnicodeDecodeError:
                print("There was an error while trying to decode unicode.")
            except Exception as e:
                return
                #print("Error: " + str(e))

    bot.run(TOKEN)