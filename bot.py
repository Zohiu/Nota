version = "4.0"
print("        _____________________________________________________ \n"
      "       /       ***************************************       \ \n"
      "      /        *  |\   |  |----|  ---|---    /-\     *        \ \n"
      "     /         *  | \  |  |    |     |      /   \    *         \ \n"
      "    /          *  |  \ |  |    |     |     /-----\   *          \ \n"
      "   /           *  |   \|  |----|     |    /       \  *           \ \n"
      "  /            ***************************************            \ \n"
      " /-----------------------------------------------------------------\ \n"
      " |              Version : "+version+"  |           REWRITE!!               | \n"
      " |-----------------------------------------------------------------| \n"
      " | This is the Nota bot it notes the notes. This is the best Bot!! | \n"
      " \-----------------------------------------------------------------/ \n"
      "  \                         code by Fguzy                         / \n"
      "   --------------------------------------------------------------- \n"
      )


# Importing the packages
print("\nImporting packages and setting variables...")
from Modules.Other import calc, embed, guilds, ping, timer, uptime, users, speed
from Modules.Settings import setprefix, setcolor, resetcolor
from Modules.Files import save, read, delete, files
from discord.ext.commands import CommandNotFound
from Modules import help, stats, premium
from discord.ext import commands
import discord
import shutil
import time
import os


# Defining the Vars
TOKEN = open("bot.token", "r").read()
bot = commands.Bot("-")
dirpath = os.getcwd()
location = dirpath
files_in_dir = []
fileDir = os.path.dirname(os.path.realpath('__file__'))
start_time = time.time()
allcmds = ["help", "setprefix", "setcolor", "stats", "timer", "remind", "save", "read", "delete", "files",
                   "share", "privatesave", "privateread", "privatedelete", "privatefiles", "calc", "ping", "embed",
                   "guilds", "premium", "uptime", "speed"]

# Removing normal help command
bot.remove_command("help")

print("[ OK ] All packages loaded and variables set.\n")
print("Nota is loading...")

class Events:

    @bot.event
    async def on_guild_join(guild):
        print("The bot joined a guild. Current number:", len(bot.guilds))
        os.mkdir(os.path.join(fileDir, str(guild.id)))
        os.mkdir(os.path.join(fileDir, '{}/settings'.format(guild.id)))
        os.mkdir(os.path.join(fileDir, '{}/stats'.format(guild.id)))

    @bot.event
    async def on_guild_remove(guild):
        print("The bot left a guild. Current number:", len(bot.guilds))
        shutil.rmtree(os.path.join(fileDir, str(guild.id)), ignore_errors=True)

    @bot.event
    async def on_ready():
        print("[ OK ] Nota is online.")
        print()
        activity = discord.Game(name="'What is my nota prefix?'")
        await bot.change_presence(status=discord.Status.online, activity=activity)

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, CommandNotFound):
            return
        raise error

class Commands:

    @bot.event
    async def on_message(message):
        if message.author.id == bot.user.id:
            return

        if str(message.channel.type) == "private":
            if not os.path.exists(os.path.join(fileDir, str(message.author.id))):
                os.mkdir(os.path.join(fileDir, str(message.author.id)))
                os.mkdir(os.path.join(fileDir, '{}/settings'.format(message.author.id)))
                os.mkdir(os.path.join(fileDir, '{}/stats'.format(message.author.id)))
                open(os.path.join(fileDir, '{}/user.files'.format(message.author.id)), "w+")
                print("The bot made a private directory.")
            if not os.path.exists((os.path.join(fileDir, '{}/settings'.format(message.author.id)))):
                os.mkdir(os.path.join(fileDir, '{}/settings'.format(message.author.id)))
            if not os.path.exists((os.path.join(fileDir, '{}/stats'.format(message.author.id)))):
                os.mkdir(os.path.join(fileDir, '{}/stats'.format(message.author.id)))
            if not os.path.exists((os.path.join(fileDir, '{}/settings/user.color'.format(message.author.id)))):
                open((os.path.join(fileDir,  '{}/settings/user.color'.format(message.author.id))), "w+").write("34B713")
            open(os.path.join(fileDir, '{}/private.info'.format(message.author.id)), "w+")
            if not os.path.exists((os.path.join(fileDir, '{}/user.list'.format(message.author.id)))):
                open((os.path.join(fileDir, '{}/user.list'.format(message.author.id))), "w+")

        else:
            if not os.path.exists(os.path.join(fileDir, str(message.guild.id))):
                os.mkdir(os.path.join(fileDir, str(message.guild.id)))
                os.mkdir(os.path.join(fileDir, '{}/settings'.format(message.guild.id)))
                os.mkdir(os.path.join(fileDir, '{}/stats'.format(message.guild.id)))
                open((os.path.join(fileDir, '{}/dc.files'.format(message.guild.id))), "w+")
                print("The bot made a guild directory.")
            if not os.path.exists((os.path.join(fileDir, '{}/settings'.format(message.guild.id)))):
                os.mkdir(os.path.join(fileDir, '{}/settings'.format(message.guild.id)))
            if not os.path.exists((os.path.join(fileDir, '{}/stats'.format(message.guild.id)))):
                os.mkdir(os.path.join(fileDir, '{}/stats'.format(message.guild.id)))
            if not os.path.exists((os.path.join(fileDir, '{}/settings/dc.color'.format(message.guild.id)))):
                open((os.path.join(fileDir,  '{}/settings/dc.color'.format(message.guild.id))), "w+").write("34B713")
            if not os.path.exists((os.path.join(fileDir, '{}/dc.list'.format(message.guild.id)))):
                open((os.path.join(fileDir, '{}/dc.list'.format(message.guild.id))), "w+")

        from Functions import Functions
        msglst = await Functions.input_handler(message.content)
        prefix = await Functions.get_prefix(message)

        if not msglst[0].startswith(prefix):
            return

        if message.content.lower() == "what is my nota prefix?":
            await Functions.embed(message, "Your Prefix is:", prefix)
            print("OOF! Someone forgot their prefix.")

        if message.content.lower() == "will nota kill us all?":
            await Functions.embed(message, "Yes.", "I will.")
            print("NOTA WILL KILL EVERYONE!!!")

        if msglst[0] == prefix + "help":
            await help.run(message, prefix, msglst, version)
            print("The bot was used.")

        # SETTINGS
        elif msglst[0] == prefix + "setprefix":
            await setprefix.run(message, prefix, msglst)

        elif msglst[0] == prefix + "setcolor": # PREMIUM
            await setcolor.run(message, prefix, msglst)

        elif msglst[0] == prefix + "resetcolor": # PREMIUM
            await resetcolor.run(message, prefix, msglst)

        # STATS
        elif msglst[0] == prefix + "stats" or msglst[0] == prefix + "privatestats":
            await stats.run(message, prefix, msglst, allcmds)

        # FILES
        elif msglst[0] == prefix + "save" or msglst[0] == prefix + "privatesave":
            await save.run(message, prefix, msglst)

        elif msglst[0] == prefix + "read" or msglst[0] == prefix + "privateread":
            await read.run(message, prefix, msglst)

        elif msglst[0] == prefix + "delete" or msglst[0] == prefix + "privatedelete":
            await delete.run(message, prefix, msglst)

        elif msglst[0] == prefix + "files" or msglst[0] == prefix + "privatefiles":
            await files.run(message, prefix, msglst)

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

        elif msglst[0] == prefix + "users":
            await users.run(message)

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

print("[ OK ] Nota was loaded into memory.\n")
print("Nota is starting... ")

bot.run(TOKEN)