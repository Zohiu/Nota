print("                                                                     ")
print("        _____________________________________________________        ")
print("       /       ***************************************       \       ")
print("      /        *  |\   |  |----|  ---|---    /-\     *        \      ")
print("     /         *  | \  |  |    |     |      /   \    *         \     ")
print("    /          *  |  \ |  |    |     |     /-----\   *          \    ")
print("   /           *  |   \|  |----|     |    /       \  *           \   ")
print("  /            ***************************************            \  ")
print(" /-----------------------------------------------------------------\ ")
print(" |              Version : 3.0  |           REWRITE!!               | ")
print(" |-----------------------------------------------------------------| ")
print(" | Well rewrites take long at least there are more things possible | ")
print(" \-----------------------------------------------------------------/ ")
print("  \                       code by Fguzy                           /  ")
print("   ---------------------------------------------------------------   ")
print("                                                                     ")


# Importing the packages
print("Importing packages and setting variables...")
import os
import discord
import datetime
import asyncio
from discord.ext import commands
from discord.ext.commands import CommandNotFound

# Defining the Vars
TOKEN = open("bot.token", "r").read()
prefix = "-"
bot = commands.Bot(prefix)
dirpath = os.getcwd()
location = dirpath
files_in_dir = []
fileDir = os.path.dirname(os.path.realpath('__file__'))
vc = None

# Removing normal help command
bot.remove_command("help")

print("[ OK ] All packages loaded and variables set.")
print()
print("Nota is loading...")

class Functions:

    async def embed(msg, title, describtion):

        try:
            color = open(os.path.join(fileDir, '{}/settings/{}.dccolor'.format(msg.guild.id, msg.guild.id)), "r").read()
            embed = discord.Embed(title=title, description=describtion, colour=discord.Color(value=int(color, 16)))
        except:
            try:
                color = open(os.path.join(fileDir, '{}/settings/{}.usercolor'.format(msg.author.id, msg.author.id)), "r").read()
                embed = discord.Embed(title=title, description=describtion, colour=discord.Color(value=int(color, 16)))
            except:
                embed = discord.Embed(title=title, description=describtion, colour=0x34b713)

        await msg.channel.send(embed=embed)

    async def get_prefix(message):
        try:
            return open(os.path.join(fileDir, '{}/settings/{}.dcprefix'.format(message.guild.id, message.guild.id)), "r").read()
        except:
            try:
                return open(os.path.join(fileDir, '{}/settings/{}.dcprefix'.format(message.author.id, message.author.id)), "r").read()
            except:
                return "-"

    async def check_perm(ctx):
        try:
            open(os.path.join(fileDir, '{}/{}.dcperms'.format(ctx.guild.id, ctx.guild.id)), "r").read()
            if "Nota perms" in str(ctx.message.author.roles):
                access = True
            else:
                access = False
        except:
            access = True

        return  access

    async def check_userperm(ctx, name):
        try:
            test = open(os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id)))
            lines = test.readlines()
            for line in lines:
                if '"' + name + '"' in line:
                    string = line.replace('"' + name + '"' + ' Owner: ', "")
                    if string.endswith("\n"):
                        string = string[:-1]

            if '"' + name + '"' in open(os.path.join(fileDir, '{}/{}.{}.dcuser'.format(ctx.guild.id, ctx.guild.id, ctx.message.author)), "r").read():
                access = True
            else:
                access = False
        except:
            access = False

        return  access

    async def bot_used(message, command, ChannelTypePrivate):

        if str(ChannelTypePrivate) == "private":
            try:
                totalusesR = open(os.path.join(fileDir, '{}/stats/{}.usertotaluses'.format(message.author.id, message.author.id)), "r").read()
                totalusesW = open(os.path.join(fileDir, '{}/stats/{}.usertotaluses'.format(message.author.id, message.author.id)), "w")
                totalusesW.write(str(int(totalusesR) + 1))
            except:
                try:
                    os.mkdir(os.path.join(fileDir, '{}/stats'.format(message.author.id)))
                    totalusesW = open(os.path.join(fileDir, '{}/stats/{}.usertotaluses'.format(message.author.id, message.author.id)), "w")
                    totalusesW.write("1")
                except:
                    os.mkdir(os.path.join(fileDir, '{}'.format(message.author.id)))
                    os.mkdir(os.path.join(fileDir, '{}/stats'.format(message.author.id)))
                    totalusesW = open(os.path.join(fileDir, '{}/stats/{}.usertotaluses'.format(message.author.id, message.author.id)), "w")
                    totalusesW.write("1")

        else:
            try:
                totalusesR = open(os.path.join(fileDir, '{}/stats/{}.dctotaluses'.format(message.guild.id, message.guild.id)), "r").read()
                totalusesW = open(os.path.join(fileDir, '{}/stats/{}.dctotaluses'.format(message.guild.id, message.guild.id)), "w")
                totalusesW.write(str(int(totalusesR) + 1))
            except:
                try:
                    os.mkdir(os.path.join(fileDir, '{}/stats'.format(message.guild.id)))
                    totalusesW = open(os.path.join(fileDir, '{}/stats/{}.dctotaluses'.format(message.guild.id, message.guild.id)), "w")
                    totalusesW.write("1")
                except:
                    os.mkdir(os.path.join(fileDir, '{}'.format(message.guild.id)))
                    os.mkdir(os.path.join(fileDir, '{}/stats'.format(message.guild.id)))
                    totalusesW = open(os.path.join(fileDir, '{}/stats/{}.dctotaluses'.format(message.guild.id, message.guild.id)), "w")
                    totalusesW.write("1")

        if str(ChannelTypePrivate) == "private":
            try:
                usesR = open(os.path.join(fileDir, '{}/stats/{}.user{}uses'.format(message.author.id, message.author.id, command)), "r").read()
                usesW = open(os.path.join(fileDir, '{}/stats/{}.user{}uses'.format(message.author.id, message.author.id, command)), "w")
                usesW.write(str(int(usesR) + 1))
            except:
                usesW = open(os.path.join(fileDir, '{}/stats/{}.user{}uses'.format(message.author.id, message.author.id, command)), "w")
                usesW.write("1")

        else:
            try:
                usesR = open(os.path.join(fileDir, '{}/stats/{}.dc{}uses'.format(message.guild.id, message.guild.id, command)), "r").read()
                usesW = open(os.path.join(fileDir, '{}/stats/{}.dc{}uses'.format(message.guild.id, message.guild.id, command)), "w")
                usesW.write(str(int(usesR) + 1))
            except:
                usesW = open(os.path.join(fileDir, '{}/stats/{}.dc{}uses'.format(message.guild.id, message.guild.id, command)), "w")
                usesW.write("1")

class Events:

    @bot.event
    async def on_ready():
        print("[ OK ] Nota is online.")
        print()
        activity = discord.Game(name="'What is my nota prefix?'")
        await bot.change_presence(status=discord.Status.online, activity=activity)

    @bot.event
    async def on_reminder(channel_id, author_id, text):
        channel = bot.get_channel(channel_id)
        embed = discord.Embed(title="You set a reminder to:", description=text, colour=0x34b713)
        await channel.send("<@{0}>".format(author_id), embed=embed)

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, CommandNotFound):
            return
        raise error

class Commands:

    @bot.event
    async def on_message(message):
        msglst = str(message.content).split()
        prefix = await Functions.get_prefix(message)

        if message.content == "What is my nota prefix?":
            await Functions.embed(message, "Your Prefix is:", prefix)
            print("OOF! Someone forgot their prefix.")

        if message.content.lower() == "will nota kill us all?":
            await Functions.embed(message, "Yes.", "I will.")
            print("NOTA WILL KILL EVERYONE!!!")

        allcmds = ["help", "changeprefix", "changecolor", "stats", "timer", "remind", "save", "read", "delete", "files", "share", "privatesave", "privateread", "privatedelete", "privatefiles", "calc", "ping", "embed", "guilds", "certificate"]

        try:
            if msglst[0] == prefix + "help":
                    if 1 == 1:

                        try:
                            color = open(os.path.join(fileDir, '{}/settings/{}.dccolor'.format(message.guild.id, message.guild.id)), "r").read()
                            embed = discord.Embed(title="Commands:", description="Prefix : -", colour=discord.Color(value=int(color, 16)))
                        except:
                            try:
                                color = open(os.path.join(fileDir, '{}/settings/{}.usercolor'.format(message.author.id, message.author.id)), "r").read()
                                embed = discord.Embed(title="Commands:", description="Prefix : -", colour=discord.Color(value=int(color, 16)))
                            except:
                                embed = discord.Embed(title="Commands:", description="Prefix : -", colour=0x34b713)

                        embed.add_field(name="----------------------------------------------------------------",
                                        value="--------------------------------------------------------------",
                                        inline=False)

                        embed.set_footer(text="© 2020 Nota 3.0 | REWRITE!!, A bot by Fguzy#5577.")
                        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/673373031405453322/725093465704104016/Nota_logo_3_2.png?size=2048")
                        embed.set_author(name="Nota Bot help", icon_url="https://cdn.discordapp.com/attachments/673373031405453322/725088685065896007/Nota_icon_3.png?size=2048")


                        try:
                            if msglst[1] == "save":
                                embed.add_field(name="------ Save Commands ------", value="Help for saving files:" , inline=False)
                                embed.add_field(name="Saving normal files:", value="`" + prefix + "save text <name> <content>`" , inline=False)
                                embed.add_field(name="Saving picture files:", value="`" + prefix + "save pic <name> <content>`" , inline=False)
                                embed.add_field(name="Saving real files:",
                                                value="`" + prefix + "save file <name> <filetype>`\n" +
                                                "`You need to attach a file.`",
                                                inline=False)
                                embed.add_field(name="Saving list files:",
                                                value="Making lists:\n`" + prefix + "save list make <name>`\n" +
                                                "Adding content to lists:\n`" + prefix + "save list add <name> <content>`\n" +
                                                "Changing lines from lists:\n`" + prefix + "save list change <name> <line> <new content>`\n" +
                                                "Removing lines from lists:\n`" + prefix + "save list remove <name> <line>`\n",
                                                inline=False)

                            elif msglst[1] == "read":
                                embed.add_field(name="------ Read Commands ------", value="Help for reading / showing files:", inline=False)
                                embed.add_field(name="Read files:",  value="`" + prefix + "read <name>`", inline=False)

                            elif msglst[1] == "delete":
                                embed.add_field(name="------ Delete Commands ------", value="Help for deleting files:", inline=False)
                                embed.add_field(name="Delete files:", value="`" + prefix + "delete <name>`", inline=False)

                            elif msglst[1] == "listing":
                                embed.add_field(name="------ Listing Commands ------", value="Help for listing all files:", inline=False)
                                embed.add_field(name="Listing files:", value="`" + prefix + "files`", inline=False)

                            elif msglst[1] == "other":
                                embed.add_field(name="------ Other Commands ------", value="Help for other stuffs:", inline=False)
                                embed.add_field(name="Changing the prefix:", value="`" + prefix + "setprefix <new prefix>`", inline=False)
                                embed.add_field(name="Solving math problems:", value="`" + prefix + "calc <problem>`", inline=False)
                                embed.add_field(name="Showing the ping of the bot:", value="`" + prefix + "ping`", inline=False)
                                embed.add_field(name="Showning the amount of servers the bot is in", value="`" + prefix + "guilds`", inline=False)
                                embed.add_field(name="Making custom embeds", value="`" + prefix + "embed <title> <content>`", inline=False)
                                embed.add_field(name="Showing stats", value="`" + prefix + "stats`", inline=False)

                            elif msglst[1] == "timer":
                                embed.add_field(name="------ Timer Commands ------", value="Help for timers:", inline=False)
                                embed.add_field(name="Creating timers", value="`" + prefix + "timer <seconds>`", inline=False)

                            elif msglst[1] == "premium":
                                embed.add_field(name="------ Premium Commands ------", value="Help for premium features:", inline=False)
                                embed.add_field(name="Changing the embed color:", value="`" + prefix + "setcolor <color hex>`", inline=False)
                                embed.add_field(name="Showing the premium status:", value="`" + prefix + "certificate`", inline=False)

                            else:
                                embed.add_field(name="Error!!!",
                                                value="This help page does not exist!", inline=False)


                        except:
                            embed.add_field(name="Help for saving files:", value=prefix + "help save", inline=False)
                            embed.add_field(name="Help for reading / showing files:", value=prefix + "help read", inline=False)
                            embed.add_field(name="Help for deleting files:", value=prefix + "help delete", inline=False)
                            embed.add_field(name="Help for listing all files / listing your perms:", value=prefix + "help listing", inline=False)
                            embed.add_field(name="Help for premium features:", value=prefix + "help premium", inline=False)
                            embed.add_field(name="Help for other stuffs:", value=prefix + "help other", inline=False)
                            embed.add_field(name="Help for timers:", value=prefix + "help timer", inline=False)

                        embed.add_field(name="----------------------------------------------------------------", value="--------------------------------------------------------------", inline=False)
                        embed.add_field(name="If you like the bot please vote for it on top.gg.", value="https://top.gg/bot/670754613820915714/vote", inline=False)
                        embed.add_field(name="Support me, the maker by subscribing to me on youtube.", value="https://www.youtube.com/channel/UCMiR4h60k6DJPrWgvTY6soQ", inline=False)

                        await message.channel.send(embed=embed)
                        print("The bot was used.")
                        await Functions.bot_used(message, "help", message.channel.type)

            # SETTINGS
            elif msglst[0] == prefix + "setprefix":
                try:
                    if str(message.channel.type) == "private":
                        try:
                            open(os.path.join(fileDir, '{}/settings/{}.userprefix'.format(message.author.id , message.author.id)), "w").write(msglst[1])
                            await Functions.embed(message, "Prefix changed!", "New prefix: " + msglst[1])
                            print("The bot was used.")
                            await Functions.bot_used(message, "changeprefix", message.channel.type)

                        except IndexError:
                            await Functions.embed(message, "Error!", "You have to enter a prefix.\nUsage: changeprefix <prefix>")

                        except FileNotFoundError:
                            try:
                                os.mkdir(os.path.join(fileDir, '{}/settings'.format(message.author.id)))
                                open(os.path.join(fileDir, '{}/settings/{}.userprefix'.format(message.author.id, message.author.id)), "w").write(msglst[1])
                                await Functions.embed(message, "Prefix changed!", "New prefix: " + msglst[1])
                                print("The bot was used.")
                                await Functions.bot_used(message, "changeprefix", message.channel.type)
                            except:
                                os.mkdir(os.path.join(fileDir, '{}'.format(message.author.id)))
                                os.mkdir(os.path.join(fileDir, '{}/settings'.format(message.author.id)))
                                open(os.path.join(fileDir, '{}/settings/{}.userprefix'.format(message.author.id,  message.author.id)), "w").write(msglst[1])
                                await Functions.embed(message, "Prefix changed!", "New prefix: " + msglst[1])
                                print("The bot was used.")
                                await Functions.bot_used(message, "changeprefix", message.channel.type)

                    else:
                        try:
                            open(os.path.join(fileDir, '{}/settings/{}.dcprefix'.format(message.guild.id, message.guild.id)), "w").write(msglst[1])
                            await Functions.embed(message, "Prefix changed!", "New prefix: " + msglst[1])
                            print("The bot was used.")
                            await Functions.bot_used(message, "changeprefix", message.channel.type)

                        except IndexError:
                            await Functions.embed(message, "Error!", "You have to enter a prefix.\nUsage: changeprefix <prefix>")

                        except FileNotFoundError:
                            try:
                                os.mkdir(os.path.join(fileDir, '{}/settings'.format(message.guild.id)))
                                open(os.path.join(fileDir, '{}/settings/{}.dcprefix'.format(message.guild.id, message.guild.id)), "w").write(msglst[1])
                                await Functions.embed(message, "Prefix changed!", "New prefix: " + msglst[1])
                                print("The bot was used.")
                                await Functions.bot_used(message, "changeprefix", message.channel.type)
                            except:
                                os.mkdir(os.path.join(fileDir, '{}'.format(message.guild.id)))
                                os.mkdir(os.path.join(fileDir, '{}/settings'.format(message.guild.id)))
                                open(os.path.join(fileDir, '{}/settings/{}.dcprefix'.format(message.guild.id, message.guild.id)), "w").write(msglst[1])
                                await Functions.embed(message, "Prefix changed!", "New prefix: " + msglst[1])
                                print("The bot was used.")
                                await Functions.bot_used(message, "changeprefix", message.channel.type)
                except:
                    await Functions.embed(message, "Error!", "Usage: '" + prefix + "changeprefix <prefix>'") # #

            elif msglst[0] == prefix + "setcolor": # PREMIUM
                try:
                    if str(message.channel.type) == "private":
                        file = open("premium.users", "r")
                        certificate = False
                        for line in file.readlines():
                            if str(message.author.id) in str(line):
                                certificate = True
                        if certificate:
                            try:
                                embed = discord.Embed(
                                    title="title",
                                    description="describtion",
                                    colour=discord.Color(value=int(msglst[1].replace('#', ''), 16))
                                )
                                try:
                                    open(os.path.join(fileDir, '{}/settings/{}.usercolor'.format(message.author.id, message.author.id)), "w").write(msglst[1].replace("#", ""))
                                    await Functions.embed(message, "Color changed!", "New color: " + msglst[1])
                                    print("The bot was used.")
                                    await Functions.bot_used(message, "changecolor", message.channel.type)
                                except:
                                    try:
                                        os.mkdir(os.path.join(fileDir, '{}/settings'.format(message.author.id)))
                                        open(os.path.join(fileDir, '{}/settings/{}.usercolor'.format(message.author.id, message.author.id)), "w").write(msglst[1].replace("#", ""))
                                        await Functions.embed(message, "Color changed!", "New color: " + msglst[1])
                                        print("The bot was used.")
                                        await Functions.bot_used(message, "changecolor", message.channel.type)
                                    except:
                                        os.mkdir(os.path.join(fileDir, '{}'.format(message.author.id)))
                                        os.mkdir(os.path.join(fileDir, '{}/settings'.format(message.author.id)))
                                        open(os.path.join(fileDir, '{}/settings/{}.usercolor'.format(message.author.id, message.author.id)), "w").write(msglst[1].replace("#", ""))
                                        await Functions.embed(message, "Color changed!", "New color: " + msglst[1])
                                        print("The bot was used.")
                                        await Functions.bot_used(message, "changecolor", message.channel.type)

                            except:
                                await Functions.embed(message, "Error!", "You have to use a hex color. You can generate hex colors here: https://www.rapidtables.com/convert/color/rgb-to-hex.html\nUsage: changecolor <colorhex>")
                        else:
                            await Functions.embed(message, "Premium required!", "To use this command you need Nota Premium! Join the support server for mor info.")
                    else:
                        file = open("premium.guilds", "r")
                        certificate = False
                        for line in file.readlines():
                            if str(message.guild.id) in str(line):
                                certificate = True
                        if certificate:
                            try:
                                embed = discord.Embed(
                                    title="title",
                                    description="describtion",
                                    colour=discord.Color(value=int(msglst[1].replace('#', ''), 16))
                                )
                                try:
                                    open(os.path.join(fileDir, '{}/settings/{}.dccolor'.format(message.guild.id, message.guild.id)), "w").write(msglst[1].replace("#", ""))
                                    await Functions.embed(message, "Color changed!", "New color: " + msglst[1])
                                    print("The bot was used.")
                                    await Functions.bot_used(message, "changecolor", message.channel.type)
                                except:
                                    try:
                                        os.mkdir(os.path.join(fileDir, '{}/settings'.format(message.guild.id)))
                                        open(os.path.join(fileDir, '{}/settings/{}.dccolor'.format(message.guild.id, message.guild.id)), "w").write(msglst[1].replace("#", ""))
                                        await Functions.embed(message, "Color changed!", "New color: " + msglst[1])
                                        print("The bot was used.")
                                        await Functions.bot_used(message, "changecolor", message.channel.type)

                                    except:
                                        os.mkdir(os.path.join(fileDir, '{}'.format(message.guild.id)))
                                        os.mkdir(os.path.join(fileDir, '{}/settings'.format(message.guild.id)))
                                        open(os.path.join(fileDir, '{}/settings/{}.dccolor'.format(message.guild.id, message.guild.id)), "w").write(msglst[1].replace("#", ""))
                                        await Functions.embed(message, "Color changed!", "New color: " + msglst[1])
                                        print("The bot was used.")
                                        await Functions.bot_used(message, "changecolor", message.channel.type)
                            except:
                                await Functions.embed(message, "Error!", "You have to use a hex color. You can generate hex colors here: https://www.rapidtables.com/convert/color/rgb-to-hex.html\nUsage: changecolor <colorhex>")
                        else:
                            await Functions.embed(message, "Premium required!", "To use this command you need Nota Premium! Join the support server for mor info.")
                except:
                    await Functions.embed(message, "Error!", "type '" + prefix + "help' to find out how the bot works!")

            # STATS
            elif msglst[0] == prefix + "stats":
                try:
                    if str(message.channel.type) == "private":
                        await Functions.bot_used(message, "stats", message.channel.type)

                        prnt = ""
                        for string in allcmds:
                            try:
                                prnt += string + " uses: " + open(os.path.join(fileDir, '{}/stats/{}.user{}uses'.format(message.author.id, message.author.id, string)), "r").read() + "\n"
                            except:
                                continue


                        await Functions.embed(message, "Your stats:", prnt)
                        print("The bot was used in private.")

                    else:
                        await Functions.bot_used(message, "stats", message.channel.type)

                        prnt = ""
                        for string in allcmds:
                            try:
                                prnt += string + " uses: " + open(os.path.join(fileDir, '{}/stats/{}.dc{}uses'.format(
                                    message.guild.id, message.guild.id, string)), "r").read() + "\n"
                            except:
                                continue

                        await Functions.embed(message, "This servers stats:", prnt)

                        print("The bot was used.")
                except:
                    await Functions.embed(message, "Error!", "Usage: '" + prefix + "stats'")

            # TIMERS 'TIMER AOKNIMSIDNAKOSD
            elif msglst[0] == prefix + "timer":
                try:
                    if str(message.channel.type) == "private":
                        timerGoing = True
                        counter = int(msglst[1])

                        try:
                            color = open(os.path.join(fileDir, '{}/settings/{}.dccolor'.format(message.guild.id, message.guild.id)), "r").read()
                            embed = discord.Embed(title="Timer:", description=str(counter), colour=discord.Color(value=int(color, 16)))
                        except:
                            try:
                                color = open(os.path.join(fileDir, '{}/settings/{}.usercolor'.format(message.author.id, message.author.id)), "r").read()
                                embed = discord.Embed(title="Timer:", description=str(counter), colour=discord.Color(value=int(color, 16)))
                            except:
                                embed = discord.Embed(title="Timer:", description=str(counter), colour=0x34b713)

                        msg = await message.channel.send(embed=embed)

                        while timerGoing:
                            try:
                                color = open(os.path.join(fileDir, '{}/settings/{}.dccolor'.format(message.guild.id,
                                                                                                   message.guild.id)),
                                             "r").read()
                                embed = discord.Embed(title="Timer:", description=str(counter),
                                                      colour=discord.Color(value=int(color, 16)))
                            except:
                                try:
                                    color = open(os.path.join(fileDir,
                                                              '{}/settings/{}.usercolor'.format(message.author.id,
                                                                                                message.author.id)),
                                                 "r").read()
                                    embed = discord.Embed(title="Timer:", description=str(counter),
                                                          colour=discord.Color(value=int(color, 16)))
                                except:
                                    embed = discord.Embed(title="Timer:", description=str(counter), colour=0x34b713)

                                await msg.delete()
                                msg = await message.channel.send(embed=embed)

                            counter -= 1

                            if counter == 0:
                                timerGoing = False

                            await asyncio.sleep(1)

                        try:
                            color = open(os.path.join(fileDir, '{}/settings/{}.dccolor'.format(message.guild.id,
                                                                                               message.guild.id)),
                                         "r").read()
                            embed = discord.Embed(title="Timer:", description="Time is up!",
                                                  colour=discord.Color(value=int(color, 16)))
                        except:
                            try:
                                color = open(os.path.join(fileDir,
                                                          '{}/settings/{}.usercolor'.format(message.author.id,
                                                                                            message.author.id)),
                                             "r").read()
                                embed = discord.Embed(title="Timer:", description="Time is up!",
                                                      colour=discord.Color(value=int(color, 16)))
                            except:
                                embed = discord.Embed(title="Timer:", description="Time is up!", colour=0x34b713)


                        await msg.delete()
                        msg = await message.channel.send(embed=embed)

                        await Functions.bot_used(message, "timer", message.channel.type)
                        print("The bot was used in private.")
                    else:
                        timerGoing = True
                        counter = int(msglst[1])

                        try:
                            color = open(os.path.join(fileDir, '{}/settings/{}.dccolor'.format(message.guild.id,
                                                                                               message.guild.id)),
                                         "r").read()
                            embed = discord.Embed(title="Timer:", description=str(counter),
                                                  colour=discord.Color(value=int(color, 16)))
                        except:
                            try:
                                color = open(os.path.join(fileDir, '{}/settings/{}.usercolor'.format(message.author.id,
                                                                                                     message.author.id)),
                                             "r").read()
                                embed = discord.Embed(title="Timer:", description=str(counter),
                                                      colour=discord.Color(value=int(color, 16)))
                            except:
                                embed = discord.Embed(title="Timer:", description=str(counter), colour=0x34b713)

                        msg = await message.channel.send(embed=embed)

                        while timerGoing:
                            try:
                                color = open(os.path.join(fileDir, '{}/settings/{}.dccolor'.format(message.guild.id,
                                                                                                   message.guild.id)),
                                             "r").read()
                                embed = discord.Embed(title="Timer:", description=str(counter),
                                                      colour=discord.Color(value=int(color, 16)))
                            except:
                                try:
                                    color = open(os.path.join(fileDir,
                                                              '{}/settings/{}.usercolor'.format(message.author.id,
                                                                                                message.author.id)),
                                                 "r").read()
                                    embed = discord.Embed(title="Timer:", description=str(counter),
                                                          colour=discord.Color(value=int(color, 16)))
                                except:
                                    embed = discord.Embed(title="Timer:", description=str(counter), colour=0x34b713)

                            await msg.delete()
                            msg = await message.channel.send(embed=embed)

                            counter -= 1

                            if counter == 0:
                                timerGoing = False

                            await asyncio.sleep(1)

                        try:
                            color = open(os.path.join(fileDir, '{}/settings/{}.dccolor'.format(message.guild.id,
                                                                                               message.guild.id)),
                                         "r").read()
                            embed = discord.Embed(title="Timer:", description="Time is up!",
                                                  colour=discord.Color(value=int(color, 16)))
                        except:
                            embed = discord.Embed(title="Timer:", description="Time is up!", colour=0x34b713)

                        await msg.delete()
                        msg = await message.channel.send(embed=embed)

                        await Functions.bot_used(message, "timer", message.channel.type)
                        print("The bot was used.")
                except:
                    await Functions.embed(message, "Error!", "Usage: '" + prefix + "timer <seconds>'")

            # FILES
            elif msglst[0] == prefix + "save":
                try:
                    if str(message.channel.type) == "private":
                        if msglst[1] == "text":
                            try:
                                file = open(os.path.join(fileDir,
                                                         '{}/{}.{}.usersave'.format(message.author.id, message.author.id,
                                                                                  msglst[2])), "a+")
                                file.write(msglst[3])
                                file.close()
                            except:
                                os.mkdir(os.path.join(fileDir, '{}'.format(message.author.id)))
                                file = open(os.path.join(fileDir,
                                                         '{}/{}.{}.usersave'.format(message.author.id, message.author.id,
                                                                                  msglst[2])), "a+")
                                file.write(msglst[3])
                                file.close()

                            await Functions.embed(message, "Successfully saved!",
                                                  "'" + msglst[3] + "' was saved in '" + msglst[2] + "' type '" + prefix + "'read " +
                                                  msglst[2] + "' to see your saved data")

                            dclistfile = os.path.join(fileDir,
                                                      '{}/{}.userlist'.format(message.author.id, message.author.id))
                            open(dclistfile, "a+")

                            found = False
                            with open(dclistfile) as f:
                                if '"' + msglst[2] + '"' in f.read():
                                    found = True

                            if found == False:
                                dclist = open(dclistfile, "a")
                                name = '"' + msglst[2] + '"' + "\n"
                                dclist.write(name)
                                dclist.close()

                        if msglst[1] == "pic":
                            try:
                                file = open(os.path.join(fileDir, '{}/{}.{}.usersavepic'.format(message.author.id, message.author.id, msglst[2])), "a+")
                                file.write(msglst[3])
                                file.close()
                            except:
                                os.mkdir(os.path.join(fileDir, '{}'.format(message.author.id)))
                                file = open(os.path.join(fileDir, '{}/{}.{}.usersavepic'.format(message.author.id, message.author.id, msglst[2])), "a+")
                                file.write(msglst[3])
                                file.close()

                            await Functions.embed(message, "Successfully saved!", "'" + msglst[3] + "' was saved in '" + msglst[2] + "' type '" + prefix + "'read " + msglst[2] + "' to see your saved data")

                            dclistfile = os.path.join(fileDir, '{}/{}.userlist'.format(message.author.id, message.author.id))
                            open(dclistfile, "a+")

                            found = False
                            with open(dclistfile) as f:
                                if '"' + msglst[2] + '" (pic)' in f.read():
                                    found = True

                            if found == False:
                                dclist = open(dclistfile, "a")
                                name = '"' + msglst[2] + '" (pic)' + "\n"
                                dclist.write(name)
                                dclist.close()

                        if msglst[1] == "list":
                            name = str(msglst[3])
                            if msglst[2] == 'make':
                                try:
                                    file = open(os.path.join(fileDir,
                                                             '{}/{}.{}.usersave'.format(message.author.id, message.author.id, name)),
                                                "a+")
                                    file.write("")
                                    file.close()

                                    dclistfile = os.path.join(fileDir,
                                                              '{}/{}.userlist'.format(message.author.id, message.author.id))
                                    open(dclistfile, "a+")

                                    found = False
                                    with open(dclistfile) as f:
                                        if '"' + name + '"' in f.read():
                                            found = True

                                    if found == False:
                                        dclist = open(dclistfile, "a")
                                        name2 = '"' + name + '"' + "\n"
                                        dclist.write(name2)
                                        dclist.close

                                except:
                                    await Functions.embed(message, "Error!",
                                                          "uh oh! this error is fatal! join the support server and tell Fguzy#5577 aka the bot owner about this!")

                                await Functions.embed(message, "List made: '" + name + "'",
                                                      "type '" + prefix + "save list add " + name + " <content>' to add a line")

                            elif msglst[2] == 'add':
                                try:
                                    file = open(os.path.join(fileDir,
                                                             '{}/{}.{}.usersave'.format(message.author.id, message.author.id, name)),
                                                "r")
                                    file.close()
                                    file = open(os.path.join(fileDir,
                                                             '{}/{}.{}.usersave'.format(message.author.id, message.author.id, name)),
                                                "a+")
                                    if file.readlines() == 0:
                                        file.write(msglst[4] + "\n")
                                    else:
                                        file.write("\n" + msglst[4])

                                    file.close()
                                except:
                                    await Functions.embed(message, "Error!", "This file does not exist.")

                                await Functions.embed(message, "Successfully added point!", "'" + msglst[4] + "' was saved in '" + name + "' type '" + prefix + "read' " + name + "' to see your saved list")

                            elif msglst[2] == 'change':
                                try:
                                    file = open(os.path.join(fileDir,
                                                             '{}/{}.{}.usersave'.format(message.author.id, message.author.id, name)),
                                                "r")
                                    lines = file.readlines()
                                    file.close()

                                    lines = open(os.path.join(fileDir,
                                                              '{}/{}.{}.usersave'.format(message.author.id, message.author.id, name)),
                                                 "r").read().splitlines()
                                    lines[int(msglst[4])] = msglst[5]
                                    open(os.path.join(fileDir, '{}/{}.{}.usersave'.format(message.author.id, message.author.id, name)),
                                         'w').write('\n'.join(lines))

                                    await Functions.embed(message, "Successfully changed!",
                                                          "line '" + msglst[4] + "' was changed to '" + msglst[5])
                                except:
                                    await Functions.embed(message, "Error!", "This file or line does not exist.")

                            elif msglst[2] == 'remove':
                                try:
                                    a_file = open(os.path.join(fileDir,
                                                               '{}/{}.{}.usersave'.format(message.author.id, message.author.id, name)),
                                                  "r")
                                    lines = a_file.readlines()
                                    a_file.close()
                                    del lines[int(msglst[4])]
                                    new_file = open(os.path.join(fileDir,
                                                                 '{}/{}.{}.usersave'.format(message.author.id, message.author.id, name)),
                                                    "w+")
                                    for line in lines:
                                        new_file.write(line)
                                    new_file.close()

                                    await Functions.embed(message, "Successfully deleted!", "line was deleted.")
                                except:
                                    await Functions.embed(message, "Error!", "This file or line does not exist.")
                            else:
                                await Functions.embed(message, "Error!",
                                                      "Use 'make', 'add', 'change' or 'remove'. For help type '" + prefix + "help'")

                        if msglst[1] == "file":
                            try:
                                file = open("premium.users", "r")
                                certificate = False
                                premium = False
                                for line in file.readlines():
                                    if str(message.author.id) in str(line):
                                        premium = True

                                counter = 0

                                full = True
                                available = False

                                try:
                                    file = open(os.path.join(fileDir,
                                                             '{}/{}.userlist'.format(message.author.id, message.author.id)),
                                                "r")
                                    lines = file.readlines()

                                    for line in lines:
                                        if '" (file)' in line:
                                            counter += 1
                                            print(counter)
                                            print(line)

                                    if premium:
                                        if counter < 25:
                                            available = True
                                        else:
                                            available = False
                                            full = True
                                    else:
                                        if counter < 10:
                                            available = True
                                        else:
                                            available = False
                                            full = True
                                except:
                                    available = False

                                if message.attachments[0].size < 8000000 and available:
                                    await message.attachments[0].save(os.path.join(fileDir, '{}/{}.{}.{}'.format(message.author.id, message.author.id, msglst[2], msglst[3])))

                                    dclistfile = os.path.join(fileDir,
                                                              '{}/{}.userlist'.format(message.author.id, message.author.id))
                                    open(dclistfile, "a+")

                                    found = False
                                    with open(dclistfile) as f:
                                        if '"' + msglst[2] + '" (file)' in f.read():
                                            found = True

                                    if found == False:
                                        dclist = open(dclistfile, "a")
                                        name = '"' + msglst[2] + '" (file)\n'
                                        dclist.write(name)
                                        dclist.close()

                                    await Functions.embed(message, "Success!", "The file was saved as '" + msglst[2] + "'. type '" + prefix + "read " + msglst[2] + "' to see your saved data.")

                                else:
                                    if full:
                                        await Functions.embed(message, "Error!", "You have reached your file limit!")
                                    else:
                                        await Functions.embed(message, "Error!", "This file is too big! Max: 8mb")

                            except:
                                try:
                                    os.mkdir(os.path.join(fileDir, '{}'.format(message.author.id)))
                                    await message.attachments[0].save(os.path.join(fileDir, '{}/{}.{}.{}'.format(message.author.id, message.author.id, msglst[2], msglst[3])))

                                    dclistfile = os.path.join(fileDir,
                                                              '{}/{}.userlist'.format(message.author.id, message.author.id))
                                    open(dclistfile, "a+")

                                    found = False
                                    with open(dclistfile) as f:
                                        if '"' + msglst[2] + '" (file)' in f.read():
                                            found = True

                                    if found == False:
                                        dclist = open(dclistfile, "a")
                                        name = '"' + msglst[2] + '" (file)\n'
                                        dclist.write(name)
                                        dclist.close()

                                    await Functions.embed(message, "Success!", "The file was saved as '" + msglst[2] + "'. type '" + prefix + "read " + msglst[2] + "' to see your saved data.")
                                except:
                                    await Functions.embed(message, "Error!", "Type '" + prefix + "help' to see how the command works!.")

                        await Functions.bot_used(message, "save", message.channel.type)
                        print("The bot was used in private.")

                    else:
                        if msglst[1] == "text":
                            try:
                                file = open(os.path.join(fileDir, '{}/{}.{}.dcsave'.format(message.guild.id, message.guild.id, msglst[2])), "a+")
                                file.write(msglst[3])
                                file.close()
                            except:
                                os.mkdir(os.path.join(fileDir, '{}'.format(message.guild.id)))
                                file = open(os.path.join(fileDir, '{}/{}.{}.dcsave'.format(message.guild.id, message.guild.id, msglst[2])), "a+")
                                file.write(msglst[3])
                                file.close()

                            await Functions.embed(message, "Successfully saved!", "'" + msglst[3] + "' was saved in '" + msglst[2] + "' type '" + prefix + "read' " + msglst[2] + "' to see your saved data")

                            dclistfile = os.path.join(fileDir, '{}/{}.dclist'.format(message.guild.id, message.guild.id))
                            open(dclistfile, "a+")

                            found = False
                            with open(dclistfile) as f:
                                if '"' + msglst[2] + '" Author: ' + str(message.author) in f.read():
                                    found = True

                            if found == False:
                                dclist = open(dclistfile, "a")
                                name = '"' + msglst[2] + '" Author: ' + str(message.author) + "\n"
                                dclist.write(name)
                                dclist.close()

                        if msglst[1] == "pic":
                            try:
                                file = open(os.path.join(fileDir, '{}/{}.{}.dcsavepic'.format(message.guild.id, message.guild.id, msglst[2])), "a+")
                                file.write(msglst[3])
                                file.close()
                            except:
                                os.mkdir(os.path.join(fileDir, '{}'.format(message.guild.id)))
                                file = open(os.path.join(fileDir, '{}/{}.{}.dcsavepic'.format(message.guild.id, message.guild.id, msglst[2])), "a+")
                                file.write(msglst[3])
                                file.close()

                            await Functions.embed(message, "Successfully saved!", "'" + msglst[3] + "' was saved in '" + msglst[2] + "' type '" + prefix + "read' " + msglst[2] + "' to see your saved data")

                            dclistfile = os.path.join(fileDir, '{}/{}.dclist'.format(message.guild.id, message.guild.id))
                            open(dclistfile, "a+")

                            found = False
                            with open(dclistfile) as f:
                                if '"' + msglst[2] + '" (pic) Author: ' + str(message.author) in f.read():
                                    found = True

                            if found == False:
                                dclist = open(dclistfile, "a")
                                name = '"' + msglst[2] + '" (pic) Author: ' + str(message.author) + "\n"
                                dclist.write(name)
                                dclist.close()

                        if msglst[1] == "list":
                            name = str(msglst[3])
                            if msglst[2] == 'make':
                                try:
                                    file = open(os.path.join(fileDir,
                                                             '{}/{}.{}.dcsave'.format(message.guild.id, message.guild.id, name)),
                                                "a+")
                                    file.write("")
                                    file.close()

                                    dclistfile = os.path.join(fileDir,
                                                              '{}/{}.dclist'.format(message.guild.id, message.guild.id))
                                    open(dclistfile, "a+")

                                    found = False
                                    with open(dclistfile) as f:
                                        if '"' + name + '"' in f.read():
                                            found = True

                                    if found == False:
                                        dclist = open(dclistfile, "a")
                                        name2 = '"' + name + '" Author: ' + str(message.author) + "\n"
                                        dclist.write(name2)
                                        dclist.close

                                except:
                                    await Functions.embed(message, "Error!",
                                                          "uh oh! this error is fatal! join the support server and tell Fguzy#5577 aka the bot owner about this!")

                                await Functions.embed(message, "List made: '" + name + "'",
                                                      "type '" + prefix + "list add " + name + " <content>' to add a line")

                            elif msglst[2] == 'add':
                                try:
                                    file = open(os.path.join(fileDir,
                                                             '{}/{}.{}.dcsave'.format(message.guild.id, message.guild.id, name)),
                                                "r")
                                    file.close()
                                    file = open(os.path.join(fileDir,
                                                             '{}/{}.{}.dcsave'.format(message.guild.id, message.guild.id, name)),
                                                "a+")
                                    if file.readlines() == 0:
                                        file.write(msglst[4] + "\n")
                                    else:
                                        file.write("\n" + msglst[4])

                                    file.close()
                                except:
                                    await Functions.embed(message, "Error!", "This file does not exist.")

                                await Functions.embed(message, "Successfully added point!", "'" + msglst[4] + "' was saved in '" + name + "' type '" + prefix + "read' " + name + "' to see your saved list")

                            elif msglst[2] == 'change':
                                try:
                                    file = open(os.path.join(fileDir,
                                                             '{}/{}.{}.dcsave'.format(message.guild.id, message.guild.id, name)),
                                                "r")
                                    lines = file.readlines()
                                    file.close()

                                    lines = open(os.path.join(fileDir,
                                                              '{}/{}.{}.dcsave'.format(message.guild.id, message.guild.id, name)),
                                                 "r").read().splitlines()
                                    lines[int(msglst[4])] = msglst[5]
                                    open(os.path.join(fileDir, '{}/{}.{}.dcsave'.format(message.guild.id, message.guild.id, name)),
                                         'w').write('\n'.join(lines))

                                    await Functions.embed(message, "Successfully changed!",
                                                          "line '" + msglst[4] + "' was changed to '" + msglst[5])
                                except:
                                    await Functions.embed(message, "Error!", "This file or line does not exist.")

                            elif msglst[2] == 'remove':
                                try:
                                    a_file = open(os.path.join(fileDir,
                                                               '{}/{}.{}.dcsave'.format(message.guild.id, message.guild.id, name)),
                                                  "r")
                                    lines = a_file.readlines()
                                    a_file.close()
                                    del lines[int(msglst[4])]
                                    new_file = open(os.path.join(fileDir,
                                                                 '{}/{}.{}.dcsave'.format(message.guild.id, message.guild.id, name)),
                                                    "w+")
                                    for line in lines:
                                        new_file.write(line)
                                    new_file.close()

                                    await Functions.embed(message, "Successfully deleted!", "line was deleted.")
                                except:
                                    await Functions.embed(message, "Error!", "This file or line does not exist.")
                            else:
                                await Functions.embed(message, "Error!",
                                                      "Use 'make', 'add', 'change' or 'remove'. For help type '" + prefix + "help'")

                        if msglst[1] == "file":
                            try:
                                file = open("premium.guilds", "r")
                                certificate = False
                                premium = False
                                for line in file.readlines():
                                    if str(message.guild.id) in str(line):
                                        premium = True

                                counter = 0

                                full = True
                                available = False

                                try:
                                    file = open(os.path.join(fileDir, '{}/{}.dclist'.format(message.guild.id, message.guild.id)), "r")
                                    lines = file.readlines()

                                    for line in lines:
                                        if '" (file)' in line:
                                            counter += 1

                                    if premium:
                                        if counter < 25:
                                            available = True
                                        else:
                                            available = False
                                            full = True
                                    else:
                                        if counter < 10:
                                            available = True
                                        else:
                                            available = False
                                            full = True
                                except:
                                    available = False

                                if message.attachments[0].size < 8000000 and available:
                                    await message.attachments[0].save(os.path.join(fileDir, '{}/{}.{}.{}'.format(message.guild.id, message.guild.id, msglst[2], msglst[3])))

                                    dclistfile = os.path.join(fileDir,
                                                              '{}/{}.dclist'.format(message.guild.id, message.guild.id))
                                    open(dclistfile, "a+")

                                    found = False
                                    with open(dclistfile) as f:
                                        if '"' + msglst[2] + '" (file) Author: ' + str(message.author) in f.read():
                                            found = True

                                    if found == False:
                                        dclist = open(dclistfile, "a")
                                        name = '"' + msglst[2] + '" (file) Author: ' + str(message.author) + "\n"
                                        dclist.write(name)
                                        dclist.close()

                                    await Functions.embed(message, "Success!", "The file was saved as '" + msglst[2] + "'. type '" + prefix + "read " + msglst[2] + "' to see your saved data.")

                                else:
                                    if full:
                                        await Functions.embed(message, "Error!", "You have reached your file limit!")
                                    else:
                                        await Functions.embed(message, "Error!", "This file is too big! Max: 8mb")

                            except:
                                try:
                                    os.mkdir(os.path.join(fileDir, '{}'.format(message.guild.id)))
                                    await message.attachments[0].save(os.path.join(fileDir, '{}/{}.{}.{}'.format(message.guild.id, message.guild.id, msglst[2], msglst[3])))

                                    dclistfile = os.path.join(fileDir,
                                                              '{}/{}.dclist'.format(message.guild.id, message.guild.id))
                                    open(dclistfile, "a+")

                                    found = False
                                    with open(dclistfile) as f:
                                        if '"' + msglst[2] + '" (file) Author: ' + str(message.author) in f.read():
                                            found = True

                                    if found == False:
                                        dclist = open(dclistfile, "a")
                                        name = '"' + msglst[2] + '" (file) Author: ' + str(message.author) + "\n"
                                        dclist.write(name)
                                        dclist.close()

                                    await Functions.embed(message, "Success!", "The file was saved as '" + msglst[2] + "'. type '" + prefix + "read " + msglst[2] + "' to see your saved data.")
                                except:
                                    await Functions.embed(message, "Error!", "Type '" + prefix + "help' to see how the command works!.")

                        await Functions.bot_used(message, "save", message.channel.type)
                        print("The bot was used.")

                except:
                    await Functions.embed(message, "Error!", "Type: '" + prefix + "help save'")

            elif msglst[0] == prefix + "read":
                if str(message.channel.type) == "private":
                    try:
                        try:
                            filename = os.path.join(fileDir, '{}/{}.{}.usersave'.format(message.author.id, message.author.id, msglst[1]))
                            file = open(filename, "r")

                            await Functions.embed(message, msglst[1], file.read())

                            file.close()
                        except:
                            try:
                                filename = os.path.join(fileDir, '{}/{}.{}.usersavepic'.format(message.author.id, message.author.id, msglst[1]))
                                file = open(filename, "r")

                                await message.channel.send(file.read())

                                file.close()
                            except:
                                try:
                                    for d in os.walk(os.path.join(fileDir, str(message.author.id))):
                                        for f in d:
                                            for string in f:
                                                if str(message.author.id) in string and msglst[1] in string and not "usersave" in string and not "usersavepic" in string:
                                                    fileformat = string.split(".")[-1]
                                                    open(os.path.join(fileDir, "{}/{}".format(str(message.author.id), string)))
                                                    file = discord.File(os.path.join(fileDir, "{}/{}".format(str(message.author.id), string)), filename = msglst[1] + ".{}".format(fileformat), spoiler=False)
                                                    await message.channel.send(file = file)
                                except:
                                    await Functions.embed(message, "Error!", "That file does not exist!")
                    except:
                        await Functions.embed(message, "Error!", "That file does not exist!")

                    print("The bot was used in private.")
                    await Functions.bot_used(message, "read", message.channel.type)

                else:
                    try:
                        try:
                            filename = os.path.join(fileDir, '{}/{}.{}.dcsave'.format(message.guild.id, message.guild.id, msglst[1]))
                            file = open(filename, "r")

                            await Functions.embed(message, msglst[1], file.read())

                            file.close()
                        except:
                            try:
                                filename = os.path.join(fileDir, '{}/{}.{}.dcsavepic'.format(message.guild.id,
                                                                                               message.guild.id,
                                                                                               msglst[1]))
                                file = open(filename, "r")

                                await message.channel.send(file.read())

                                file.close()
                            except:
                                try:
                                    for d in os.walk(os.path.join(fileDir, str(message.guild.id))):
                                        for f in d:
                                            for string in f:
                                                if str(message.guild.id) in string and msglst[1] in string and not "dcsave" in string and not "dcsavepic" in string:
                                                    fileformat = string.split(".")[-1]
                                                    open(os.path.join(fileDir, "{}/{}".format(str(message.guild.id), string)))
                                                    file = discord.File(os.path.join(fileDir, "{}/{}".format(str(message.guild.id), string)), filename = msglst[1] + ".{}".format(fileformat), spoiler=False)
                                                    await message.channel.send(file = file)
                                except:
                                    await Functions.embed(message, "Error!", "That file does not exist!")
                    except:
                        await Functions.embed(message, "Error!", "That file does not exist!")

                    print("The bot was used.")
                    await Functions.bot_used(message, "save", message.channel.type)

            elif msglst[0] == prefix + "delete":
                if str(message.channel.type) == "private":
                    try:
                        try:
                            os.remove(os.path.join(fileDir, '{}/{}.{}.usersave'.format(message.author.id, message.author.id,
                                                                                     msglst[1])))

                            await Functions.embed(message, "'" + msglst[1] + "' has been deleted.",
                                                  "This action can't be undone.")

                            file = os.path.join(fileDir, '{}/{}.userlist'.format(message.author.id, message.author.id))
                            tostrip = '"' + msglst[1] + '"'

                            with open(file, "r") as f:
                                lines = f.readlines()

                            with open(file, "w") as f:
                                for line in lines:
                                    if line.strip("\n") != tostrip:
                                        f.write(line)
                        except:
                            try:
                                os.remove(os.path.join(fileDir,
                                                       '{}/{}.{}.usersavepic'.format(message.author.id, message.author.id,
                                                                                   msglst[1])))

                                await Functions.embed(message, "'" + msglst[1] + "' has been deleted.",
                                                      "This action can't be undone.")

                                file = os.path.join(fileDir, '{}/{}.userlist'.format(message.author.id, message.author.id))
                                tostrip = '"' + msglst[1] + '" (pic)'

                                with open(file, "r") as f:
                                    lines = f.readlines()

                                with open(file, "w") as f:
                                    for line in lines:
                                        if line.strip("\n") != tostrip:
                                            f.write(line)
                            except:
                                try:
                                    for d in os.walk(os.path.join(fileDir, str(message.author.id))):
                                        for f in d:
                                            for string in f:
                                                if str(message.author.id) in string and msglst[1] in string and not "usersave" in string and not "usersavepic" in string:
                                                    os.remove(os.path.join(fileDir, '{}/{}'.format(str(message.author.id), string)))

                                                    await Functions.embed(message,
                                                                          "'" + msglst[1] + "' has been deleted.",
                                                                          "This action can't be undone.")

                                                    file = os.path.join(fileDir, '{}/{}.userlist'.format(message.author.id,
                                                                                                       message.author.id))
                                                    tostrip = '"' + msglst[1] + '" (file)'

                                                    with open(file, "r") as fl:
                                                        lines = fl.readlines()

                                                    with open(file, "w") as fl:
                                                        for line in lines:
                                                            if line.strip("\n") != tostrip:
                                                                fl.write(line)
                                except:
                                    await Functions.embed(message, "Error", "There is no such file called '" + msglst[
                                        1] + "' or you don't have the permission.")
                    except:
                        await Functions.embed(message, "Error!", "Usage: '" + prefix + "delete <name>'")

                    print("The bot was used in private.")
                    await Functions.bot_used(message, "delete", message.channel.type)

                else:
                    try:
                        try:
                            os.remove(os.path.join(fileDir, '{}/{}.{}.dcsave'.format(message.guild.id, message.guild.id, msglst[1])))

                            await Functions.embed(message, "'" + msglst[1] + "' has been deleted.",
                                                  "This action can't be undone.")

                            file = os.path.join(fileDir, '{}/{}.dclist'.format(message.guild.id, message.guild.id))
                            tostrip = '"' + msglst[1] + '"'

                            with open(file, "r") as f:
                                lines = f.readlines()

                            with open(file, "w") as f:
                                for line in lines:
                                    if not tostrip in line:
                                        f.write(line)

                        except:
                            try:
                                os.remove(os.path.join(fileDir, '{}/{}.{}.dcsavepic'.format(message.guild.id, message.guild.id, msglst[1])))

                                await Functions.embed(message, "'" + msglst[1] + "' has been deleted.", "This action can't be undone.")

                                file = os.path.join(fileDir, '{}/{}.dclist'.format(message.guild.id, message.guild.id))
                                tostrip = '"' + msglst[1] + '" (pic) Author: ' + str(message.author)

                                with open(file, "r") as f:
                                    lines = f.readlines()

                                with open(file, "w") as f:
                                    for line in lines:
                                        if line.strip("\n") != tostrip:
                                            f.write(line)
                            except:
                                try:
                                    for d in os.walk(os.path.join(fileDir, str(message.guild.id))):
                                        for f in d:
                                            for string in f:
                                                if str(message.guild.id) in string and msglst[1] in string and not "dcsave" in string and not "dcsavepic" in string:
                                                    os.remove(os.path.join(fileDir, '{}/{}'.format(str(message.guild.id), string)))

                                                    await Functions.embed(message,
                                                                          "'" + msglst[1] + "' has been deleted.",
                                                                          "This action can't be undone.")

                                                    file = os.path.join(fileDir, '{}/{}.dclist'.format(message.guild.id,
                                                                                                       message.guild.id))
                                                    tostrip = '"' + msglst[1] + '" (file) Author: ' + str(message.author)

                                                    with open(file, "r") as fl:
                                                        lines = fl.readlines()

                                                    with open(file, "w") as fl:
                                                        for line in lines:
                                                            if line.strip("\n") != tostrip:
                                                                fl.write(line)
                                except:
                                    await Functions.embed(message, "Error",  "There is no such file called '" + msglst[1] + "' or you don't have the permission.")
                    except:
                        await Functions.embed(message, "Error!", "type '" + prefix + "help' to find out how the bot works!")
                    print("The bot was used.")
                    await Functions.bot_used(message, "delete", message.channel.type)

            elif msglst[0] == prefix + "files":
                if str(message.channel.type) == "private":
                    try:
                        file_lines_2 = ""
                        file_lines = []
                        counter = 0

                        try:
                            color = open(os.path.join(fileDir, '{}/settings/{}.dccolor'.format(message.guild.id, message.guild.id)), "r").read()
                            embed = discord.Embed(title="All files:", description="", colour=discord.Color(value=int(color, 16)))
                        except:
                            try:
                                color = open(os.path.join(fileDir, '{}/settings/{}.usercolor'.format(message.author.id, message.author.id)), "r").read()
                                embed = discord.Embed(title="All files:", description="", colour=discord.Color(value=int(color, 16)))
                            except:
                                embed = discord.Embed(title="All files:", description="", colour=0x34b713)

                        try:
                            with open(os.path.join(fileDir, '{}/{}.userlist'.format(message.author.id, message.author.id)),
                                      "r") as file:

                                for line in file:
                                    file_lines.append(line + "\n")
                                    counter += 1

                                    if counter == 24:
                                        for thing in file_lines:
                                            file_lines_2 = str(file_lines_2) + str(thing)

                                        embed.add_field(name="Chunk of files:", value=file_lines_2, inline=False)
                                        file_lines = []
                                        file_lines_2 = []
                                        counter = 0

                                for thing in file_lines:
                                    file_lines_2 = str(file_lines_2) + str(thing)

                                embed.add_field(name="Chunk of files:", value=file_lines_2, inline=False)
                                file_lines = []
                                file_lines_2 = []

                            await message.channel.send(embed=embed)
                        except:
                            await Functions.embed(message, "All saved files:",
                                                  "There are no files saved.")
                    except:
                        await Functions.embed(message, "Error!", "Usage: '" + prefix + "files'")

                    print("The bot was used in private.")
                    await Functions.bot_used(message, "files", message.channel.type)

                else:
                    try:
                        file_lines_2 = ""
                        file_lines = []
                        counter = 0
                        try:
                            color = open(os.path.join(fileDir, '{}/settings/{}.dccolor'.format(message.guild.id,
                                                                                               message.guild.id)),
                                         "r").read()
                            embed = discord.Embed(title="All files on this server:", description="",
                                                  colour=discord.Color(value=int(color, 16)))
                        except:
                            try:
                                color = open(os.path.join(fileDir, '{}/settings/{}.usercolor'.format(message.author.id,
                                                                                                     message.author.id)),
                                             "r").read()
                                embed = discord.Embed(title="All files on this server:", description="",
                                                      colour=discord.Color(value=int(color, 16)))
                            except:
                                embed = discord.Embed(title="All files on this server:", description="", colour=0x34b713)

                        try:
                            with open(os.path.join(fileDir, '{}/{}.dclist'.format(message.guild.id, message.guild.id)),  "r") as file:

                                for line in file:
                                    file_lines.append(line + "\n")
                                    counter += 1

                                    if counter == 24:
                                        for thing in file_lines:
                                            file_lines_2 = str(file_lines_2) + str(thing)

                                        embed.add_field(name="Chunk of files:", value=file_lines_2, inline=False)
                                        file_lines = []
                                        file_lines_2 = []
                                        counter = 0

                                for thing in file_lines:
                                    file_lines_2 = str(file_lines_2) + str(thing)

                                embed.add_field(name="Chunk of files:", value=file_lines_2, inline=False)
                                file_lines = []
                                file_lines_2 = []

                            await message.channel.send(embed=embed)
                        except:
                            await Functions.embed(message, "All saved files on this server:", "There are no files saved on this server.")
                    except:
                        await Functions.embed(message, "Error!", "That file does not exist!")

                    print("The bot was used.")
                    await Functions.bot_used(message, "files", message.channel.type)

            elif msglst[0] == prefix + "share":
                if str(message.channel.type) == "private":
                    file = msglst[1]
                    share = msglst[2]
                    if len(msglst[2]) == 18:
                        try:
                            savefile = open(os.path.join(fileDir,
                                                         '{}/{}.{}.dcsave'.format(message.author.id, message.author.id,
                                                                                  file)), "r")

                            sharesavefile = open(os.path.join(fileDir, '{}/{}.{}.dcsave'.format(share, share,
                                                                                                file)), "a+")
                            sharelistfile = open(os.path.join(fileDir, '{}/{}.dclist'.format(share, share)), "a+")

                            sharesavefile.write(savefile.read())
                            sharelistfile.write('"' + file + '" Author: ' + str(message.author))
                            sharelistfile.close()
                            sharesavefile.close()
                            savefile.close()

                            await Functions.embed(message, "Yay!",
                                                  "Successfully shared '" + file + "' to '" + share + "'")

                        except:
                            try:
                                savefile = open(os.path.join(fileDir,
                                                             '{}/{}.{}.dcsavepic'.format(message.author.id,
                                                                                         message.author.id, file)),
                                                "r")

                                sharesavefile = open(os.path.join(fileDir, '{}/{}.{}.dcsavepic'.format(share, share,
                                                                                                       file)), "a+")
                                sharelistfile = open(os.path.join(fileDir, '{}/{}.dclist'.format(share, share)), "a+")

                                sharesavefile.write(savefile.read())
                                sharelistfile.write('"' + file + '" (pic) Author: ' + str(message.author))
                                sharelistfile.close()
                                sharesavefile.close()
                                savefile.close()

                                await Functions.embed(message, "Yay!",
                                                      "Successfully shared '" + file + "' to '" + share + "'")

                            except:
                                await Functions.embed(message, "Error!",
                                                      "A problem occured while trying to share '" + file + "' to '" + share + ". does the file exist? Have you entered a valid user id? Does that user use Nota?")
                    else:
                        await Functions.embed(message, "Error!",
                                              "A problem occured while trying to share '" + file + "' to '" + share + ". Have you entered a valid user id? Does that user use Nota?")

                    print("The bot was used in private.")
                    await Functions.bot_used(message, "share", message.channel.type)

                else:
                    file = msglst[1]
                    share = msglst[2]
                    if len(msglst[2]) == 18:
                        try:
                            savefile = open(os.path.join(fileDir,
                                                         '{}/{}.{}.dcsave'.format(message.guild.id, message.guild.id, file)), "r")

                            sharesavefile = open(os.path.join(fileDir, '{}/{}.{}.dcsave'.format(share, share,
                                                                                                   file)), "a+")
                            sharelistfile = open(os.path.join(fileDir, '{}/{}.dclist'.format(share, share)), "a+")

                            sharesavefile.write(savefile.read())
                            sharelistfile.write('"' + file + '" Author: ' + str(message.author))
                            sharelistfile.close()
                            sharesavefile.close()
                            savefile.close()

                            await Functions.embed(message, "Yay!", "Successfully shared '" + file + "' to '" + share + "'")

                        except:
                            try:
                                savefile = open(os.path.join(fileDir,
                                                             '{}/{}.{}.dcsavepic'.format(message.guild.id, message.guild.id, file)),
                                                "r")

                                sharesavefile = open(os.path.join(fileDir, '{}/{}.{}.dcsavepic'.format(share, share,
                                                                                                       file)), "a+")
                                sharelistfile = open(os.path.join(fileDir, '{}/{}.dclist'.format(share, share)), "a+")

                                sharesavefile.write(savefile.read())
                                sharelistfile.write('"' + file + '" (pic) Author: ' + str(message.author))
                                sharelistfile.close()
                                sharesavefile.close()
                                savefile.close()

                                await Functions.embed(message, "Yay!",
                                                      "Successfully shared '" + file + "' to '" + share + "'")

                            except:
                                await Functions.embed(message, "Error!",
                                                      "A problem occured while trying to share '" + file + "' to '" + share + ". does the file exist? Have you entered a valid guild id? Does that server use Nota?")
                    else:
                        await Functions.embed(message, "Error!",
                                              "A problem occured while trying to share '" + file + "' to '" + share + ". Have you entered a valid guild id? Does that server use Nota?")

                    print("The bot was used.")
                    await Functions.bot_used(message, "share", message.channel.type)

            # FILE PRIVATE (GUILD ONLY)
            elif msglst[0] == prefix + "privatesave":
                try:
                    if str(message.channel.type) == "private":
                        await Functions.embed(message, "Error!", "This command only works on servers.")

                    else:
                        if msglst[1] == "text":
                            try:
                                file = open(os.path.join(fileDir,
                                                         '{}/{}.{}.usersave'.format(message.author.id,
                                                                                    message.author.id,
                                                                                    msglst[2])), "a+")
                                file.write(msglst[3])
                                file.close()
                            except:
                                os.mkdir(os.path.join(fileDir, '{}'.format(message.author.id)))
                                file = open(os.path.join(fileDir,
                                                         '{}/{}.{}.usersave'.format(message.author.id,
                                                                                    message.author.id,
                                                                                    msglst[2])), "a+")
                                file.write(msglst[3])
                                file.close()

                            await Functions.embed(message, "Successfully saved!",
                                                  "'" + msglst[3] + "' was saved in '" + msglst[
                                                      2] + "' type '" + prefix + "'privateread " +
                                                  msglst[2] + "' to see your saved data")

                            dclistfile = os.path.join(fileDir,
                                                      '{}/{}.userlist'.format(message.author.id, message.author.id))
                            open(dclistfile, "a+")

                            found = False
                            with open(dclistfile) as f:
                                if '"' + msglst[2] + '"' in f.read():
                                    found = True

                            if found == False:
                                dclist = open(dclistfile, "a")
                                name = '"' + msglst[2] + '"' + "\n"
                                dclist.write(name)
                                dclist.close()

                        if msglst[1] == "pic":
                            try:
                                file = open(os.path.join(fileDir, '{}/{}.{}.usersavepic'.format(message.author.id,
                                                                                                message.author.id,
                                                                                                msglst[2])), "a+")
                                file.write(msglst[3])
                                file.close()
                            except:
                                os.mkdir(os.path.join(fileDir, '{}'.format(message.author.id)))
                                file = open(os.path.join(fileDir, '{}/{}.{}.usersavepic'.format(message.author.id,
                                                                                                message.author.id,
                                                                                                msglst[2])), "a+")
                                file.write(msglst[3])
                                file.close()

                            await Functions.embed(message, "Successfully saved!",
                                                  "'" + msglst[3] + "' was saved in '" + msglst[
                                                      2] + "' type '" + prefix + "'privateread " + msglst[
                                                      2] + "' to see your saved data")

                            dclistfile = os.path.join(fileDir,
                                                      '{}/{}.userlist'.format(message.author.id, message.author.id))
                            open(dclistfile, "a+")

                            found = False
                            with open(dclistfile) as f:
                                if '"' + msglst[2] + '" (pic)' in f.read():
                                    found = True

                            if found == False:
                                dclist = open(dclistfile, "a")
                                name = '"' + msglst[2] + '" (pic)' + "\n"
                                dclist.write(name)
                                dclist.close()

                        if msglst[1] == "list":
                            name = str(msglst[3])
                            if msglst[2] == 'make':
                                try:
                                    file = open(os.path.join(fileDir,
                                                             '{}/{}.{}.usersave'.format(message.author.id,
                                                                                        message.author.id, name)),
                                                "a+")
                                    file.write("")
                                    file.close()

                                    dclistfile = os.path.join(fileDir,
                                                              '{}/{}.userlist'.format(message.author.id,
                                                                                      message.author.id))
                                    open(dclistfile, "a+")

                                    found = False
                                    with open(dclistfile) as f:
                                        if '"' + name + '"' in f.read():
                                            found = True

                                    if found == False:
                                        dclist = open(dclistfile, "a")
                                        name2 = '"' + name + '"' + "\n"
                                        dclist.write(name2)
                                        dclist.close

                                except:
                                    await Functions.embed(message, "Error!",
                                                          "uh oh! this error is fatal! join the support server and tell Fguzy#5577 aka the bot owner about this!")

                                await Functions.embed(message, "List made: '" + name + "'",
                                                      "type '" + prefix + "save list add " + name + " <content>' to add a line")

                            elif msglst[2] == 'add':
                                try:
                                    file = open(os.path.join(fileDir,
                                                             '{}/{}.{}.usersave'.format(message.author.id,
                                                                                        message.author.id, name)),
                                                "r")
                                    file.close()
                                    file = open(os.path.join(fileDir,
                                                             '{}/{}.{}.usersave'.format(message.author.id,
                                                                                        message.author.id, name)),
                                                "a+")
                                    if file.readlines() == 0:
                                        file.write(msglst[4] + "\n")
                                    else:
                                        file.write("\n" + msglst[4])

                                    file.close()
                                except:
                                    await Functions.embed(message, "Error!", "This file does not exist.")

                                await Functions.embed(message, "Successfully added point!", "'" + msglst[
                                    4] + "' was saved in '" + name + "' type '" + prefix + "read' " + name + "' to see your saved list")

                            elif msglst[2] == 'change':
                                try:
                                    file = open(os.path.join(fileDir,
                                                             '{}/{}.{}.usersave'.format(message.author.id,
                                                                                        message.author.id, name)),
                                                "r")
                                    lines = file.readlines()
                                    file.close()

                                    lines = open(os.path.join(fileDir,
                                                              '{}/{}.{}.usersave'.format(message.author.id,
                                                                                         message.author.id, name)),
                                                 "r").read().splitlines()
                                    lines[int(msglst[4])] = msglst[5]
                                    open(os.path.join(fileDir,
                                                      '{}/{}.{}.usersave'.format(message.author.id, message.author.id,
                                                                                 name)),
                                         'w').write('\n'.join(lines))

                                    await Functions.embed(message, "Successfully changed!",
                                                          "line '" + msglst[4] + "' was changed to '" + msglst[5])
                                except:
                                    await Functions.embed(message, "Error!", "This file or line does not exist.")

                            elif msglst[2] == 'remove':
                                try:
                                    a_file = open(os.path.join(fileDir,
                                                               '{}/{}.{}.usersave'.format(message.author.id,
                                                                                          message.author.id, name)),
                                                  "r")
                                    lines = a_file.readlines()
                                    a_file.close()
                                    del lines[int(msglst[4])]
                                    new_file = open(os.path.join(fileDir,
                                                                 '{}/{}.{}.usersave'.format(message.author.id,
                                                                                            message.author.id, name)),
                                                    "w+")
                                    for line in lines:
                                        new_file.write(line)
                                    new_file.close()

                                    await Functions.embed(message, "Successfully deleted!", "line was deleted.")
                                except:
                                    await Functions.embed(message, "Error!", "This file or line does not exist.")
                            else:
                                await Functions.embed(message, "Error!",
                                                      "Use 'make', 'add', 'change' or 'remove'. For help type '" + prefix + "help'")

                        if msglst[1] == "file":
                            try:
                                file = open("premium.users", "r")
                                certificate = False
                                for line in file.readlines():
                                    if str(message.author.id) in str(line):
                                        premium = True

                                if message.attachments[0].size < 8388608:
                                    await message.attachments[0].save(os.path.join(fileDir, '{}/{}.{}.{}'.format(
                                        message.author.id, message.author.id, msglst[2], msglst[3])))

                                    dclistfile = os.path.join(fileDir,
                                                              '{}/{}.userlist'.format(message.author.id,
                                                                                      message.author.id))
                                    open(dclistfile, "a+")

                                    found = False
                                    with open(dclistfile) as f:
                                        if '"' + msglst[2] + '" (file)' in f.read():
                                            found = True

                                    if found == False:
                                        dclist = open(dclistfile, "a")
                                        name = '"' + msglst[2] + '" (file)\n'
                                        dclist.write(name)
                                        dclist.close()

                                    await Functions.embed(message, "Success!", "The file was saved as '" + msglst[
                                        2] + "'. type '" + prefix + "read " + msglst[2] + "' to see your saved data.")

                                elif message.attachments[0].size < 16777216 and premium:
                                    await message.attachments[0].save(os.path.join(fileDir, '{}/{}.{}.{}'.format(
                                        message.author.id, message.author.id, msglst[2], msglst[3])))

                                    dclistfile = os.path.join(fileDir,
                                                              '{}/{}.userlist'.format(message.author.id,
                                                                                      message.author.id))
                                    open(dclistfile, "a+")

                                    found = False
                                    with open(dclistfile) as f:
                                        if '"' + msglst[2] + '" (file)' in f.read():
                                            found = True

                                    if found == False:
                                        dclist = open(dclistfile, "a")
                                        name = '"' + msglst[2] + '" (file)\n'
                                        dclist.write(name)
                                        dclist.close()

                                    await Functions.embed(message, "Success!", "The file was saved as '" + msglst[
                                        2] + "'. type '" + prefix + "read " + msglst[2] + "' to see your saved data.")

                                else:
                                    await Functions.embed(message, "Error!", "This file is too big!")

                            except:
                                try:
                                    os.mkdir(os.path.join(fileDir, '{}'.format(message.author.id)))
                                    await message.attachments[0].save(os.path.join(fileDir, '{}/{}.{}.{}'.format(
                                        message.author.id, message.author.id, msglst[2], msglst[3])))

                                    dclistfile = os.path.join(fileDir,
                                                              '{}/{}.userlist'.format(message.author.id,
                                                                                      message.author.id))
                                    open(dclistfile, "a+")

                                    found = False
                                    with open(dclistfile) as f:
                                        if '"' + msglst[2] + '" (file)' in f.read():
                                            found = True

                                    if found == False:
                                        dclist = open(dclistfile, "a")
                                        name = '"' + msglst[2] + '" (file)\n'
                                        dclist.write(name)
                                        dclist.close()

                                    await Functions.embed(message, "Success!", "The file was saved as '" + msglst[
                                        2] + "'. type '" + prefix + "read " + msglst[2] + "' to see your saved data.")
                                except:
                                    await Functions.embed(message, "Error!",
                                                          "Type '" + prefix + "help' to see how the command works!.")

                        await Functions.bot_used(message, "privatesave", message.channel.type)
                        print("The bot was used.")

                except:
                    await Functions.embed(message, "Error!", "Type: '" + prefix + "help save'")

            elif msglst[0] == prefix + "privateread":
                if str(message.channel.type) == "private":
                    await Functions.embed(message, "Error!", "This command only works on servers.")

                else:
                    try:
                        try:
                            filename = os.path.join(fileDir,
                                                    '{}/{}.{}.usersave'.format(message.author.id, message.author.id,
                                                                               msglst[1]))
                            file = open(filename, "r")

                            await Functions.embed(message, msglst[1], file.read())

                            file.close()
                        except:
                            try:
                                filename = os.path.join(fileDir, '{}/{}.{}.usersavepic'.format(message.author.id,
                                                                                               message.author.id,
                                                                                               msglst[1]))
                                file = open(filename, "r")

                                await message.channel.send(file.read())

                                file.close()
                            except:
                                try:
                                    for d in os.walk(os.path.join(fileDir, str(message.author.id))):
                                        for f in d:
                                            for string in f:
                                                if str(message.author.id) in string and msglst[
                                                    1] in string and not "usersave" in string and not "usersavepic" in string:
                                                    fileformat = string.split(".")[-1]
                                                    open(os.path.join(fileDir,
                                                                      "{}/{}".format(str(message.author.id), string)))
                                                    file = discord.File(os.path.join(fileDir, "{}/{}".format(
                                                        str(message.author.id), string)),
                                                                        filename=msglst[1] + ".{}".format(fileformat),
                                                                        spoiler=False)
                                                    await message.channel.send(file=file)
                                except:
                                    await Functions.embed(message, "Error!", "That file does not exist!")
                    except:
                        await Functions.embed(message, "Error!", "That file does not exist!")

                    print("The bot was used.")
                    await Functions.bot_used(message, "privateread", message.channel.type)

            elif msglst[0] == prefix + "privatedelete":
                if str(message.channel.type) == "private":
                    await Functions.embed(message, "Error!", "This command only works on servers.")

                else:
                    try:
                        try:
                            os.remove(os.path.join(fileDir, '{}/{}.{}.usersave'.format(message.author.id, message.author.id, msglst[1])))

                            await Functions.embed(message, "'" + msglst[1] + "' has been deleted.",
                                                  "This action can't be undone.")

                            file = os.path.join(fileDir, '{}/{}.userlist'.format(message.author.id, message.author.id))
                            tostrip = '"' + msglst[1] + '"'

                            with open(file, "r") as f:
                                lines = f.readlines()

                            with open(file, "w") as f:
                                for line in lines:
                                    if not tostrip in line:
                                        f.write(line)

                        except:
                            try:
                                os.remove(os.path.join(fileDir,
                                                       '{}/{}.{}.usersavepic'.format(message.author.id,
                                                                                     message.author.id,
                                                                                     msglst[1])))

                                await Functions.embed(message, "'" + msglst[1] + "' has been deleted.",
                                                      "This action can't be undone.")

                                file = os.path.join(fileDir,
                                                    '{}/{}.userlist'.format(message.author.id, message.author.id))
                                tostrip = '"' + msglst[1] + '" (pic)'

                                with open(file, "r") as f:
                                    lines = f.readlines()

                                with open(file, "w") as f:
                                    for line in lines:
                                        if line.strip("\n") != tostrip:
                                            f.write(line)
                            except:
                                try:
                                    for d in os.walk(os.path.join(fileDir, str(message.author.id))):
                                        for f in d:
                                            for string in f:
                                                if str(message.author.id) in string and msglst[
                                                    1] in string and not "usersave" in string and not "usersavepic" in string:
                                                    os.remove(os.path.join(fileDir,
                                                                           '{}/{}'.format(str(message.author.id),
                                                                                          string)))

                                                    await Functions.embed(message,
                                                                          "'" + msglst[1] + "' has been deleted.",
                                                                          "This action can't be undone.")

                                                    file = os.path.join(fileDir,
                                                                        '{}/{}.userlist'.format(message.author.id,
                                                                                                message.author.id))
                                                    tostrip = '"' + msglst[1] + '" (file)'

                                                    with open(file, "r") as fl:
                                                        lines = fl.readlines()

                                                    with open(file, "w") as fl:
                                                        for line in lines:
                                                            if line.strip("\n") != tostrip:
                                                                fl.write(line)
                                except:
                                    await Functions.embed(message, "Error", "There is no such file called '" + msglst[
                                        1] + "' or you don't have the permission.")
                    except:
                        await Functions.embed(message, "Error!", "type '" + prefix + "help' to find out how the bot works!")
                    print("The bot was used.")
                    await Functions.bot_used(message, "privatedelete", message.channel.type)

            elif msglst[0] == prefix + "privatefiles":
                if str(message.channel.type) == "private":
                    await Functions.embed(message, "Error!", "This command only works on servers.")

                else:
                    try:
                        file_lines_2 = ""
                        file_lines = []
                        counter = 0
                        try:
                            color = open(
                                os.path.join(fileDir, '{}/{}.usercolor'.format(message.author.id, message.author.id)),
                                "r").read()
                            embed = discord.Embed(title="All files:", description="",
                                                  colour=discord.Color(value=int(color, 16)))
                        except:
                            embed = discord.Embed(title="All files:", description="", colour=0x34b713)

                        try:
                            with open(os.path.join(fileDir,
                                                   '{}/{}.userlist'.format(message.author.id, message.author.id)),
                                      "r") as file:

                                for line in file:
                                    file_lines.append(line + "\n")
                                    counter += 1

                                    if counter == 24:
                                        for thing in file_lines:
                                            file_lines_2 = str(file_lines_2) + str(thing)

                                        embed.add_field(name="Chunk of files:", value=file_lines_2, inline=False)
                                        file_lines = []
                                        file_lines_2 = []
                                        counter = 0

                                for thing in file_lines:
                                    file_lines_2 = str(file_lines_2) + str(thing)

                                embed.add_field(name="Chunk of files:", value=file_lines_2, inline=False)
                                file_lines = []
                                file_lines_2 = []

                            await message.channel.send(embed=embed)
                        except:
                            await Functions.embed(message, "All saved files:",
                                                  "There are no files saved.")
                    except:
                        await Functions.embed(message, "Error!", "Usage: '" + prefix + "files'")

                    print("The bot was used.")
                    await Functions.bot_used(message, "privatefiles", message.channel.type)

            # OTHER
            elif msglst[0] == prefix + "calc":
                try:
                    await Functions.embed(message, "Result:", eval(msglst[1]))
                except ZeroDivisionError:
                    await Functions.embed(message, "Result:", "ERROR! Division by zero is impossible!")
                except:
                    await Functions.embed(message, "Result:", "ERROR! You cant solve that!")

                if str(message.channel.type) == "private":
                    print("The bot was used in private.")
                else:
                    print("The bot was used.")

                await Functions.bot_used(message, "calc", message.channel.type)

            elif msglst[0] == prefix + "ping":
                latency = str(round(bot.latency * 1000))
                await Functions.embed(message, "Ping", latency + " ms")
                await Functions.bot_used(message, "ping", message.channel.type)

                if str(message.channel.type) == "private":
                    print("The bot was used in private.")
                else:
                    print("The bot was used.")

            elif msglst[0] == prefix + "embed":
                try:
                    await Functions.embed(message, msglst[1], msglst[2])
                except:
                    await Functions.embed(message, "Error!", "Usage: '" + prefix + "embed <title> <content>'")
                await Functions.bot_used(message, "embed", message.channel.type)

                if str(message.channel.type) == "private":
                    print("The bot was used in private.")
                else:
                    print("The bot was used.")

            elif msglst[0] == prefix + "guilds":
                numberofguilds = len(bot.guilds)
                await Functions.embed(message, "Nota is on this many servers:", str(numberofguilds))
                await Functions.bot_used(message, "guilds", message.channel.type)

                if str(message.channel.type) == "private":
                    print("The bot was used in private.")
                else:
                    print("The bot was used.")

            # CERTIFICATE
            elif msglst[0] == prefix + "certificate":
                if str(message.channel.type) == "private":
                    file = open("premium.users", "r")
                    certificate = False
                    for line in file.readlines():
                        if str(message.author.id) in str(line):
                            await Functions.embed(message, "Nota user certificate", "This user has Nota Premium.")
                            certificate = True

                    if certificate == False:
                        await Functions.embed(message, "Nota user certificate", "This user does not have Nota Premium.")

                    await Functions.bot_used(message, "certificate", message.channel.type)
                    print("The bot was used in private.")
                else:
                    file = open("premium.guilds", "r")
                    certificate = False
                    for line in file.readlines():
                        if str(message.guild.id) in str(line):
                            await Functions.embed(message, "Nota server certificate", "This server has Nota Premium.")
                            certificate = True

                    if certificate == False:
                        await Functions.embed(message, "Nota server certificate", "This server does not have Nota Premium.")

                    await Functions.bot_used(message, "certificate", message.channel.type)
                    print("The bot was used.")

            else:
                if msglst[0].startswith(prefix):
                    await Functions.embed(message, "Error!", "Thats not a command. type '" + prefix + "help' to find out hot the bot works! If this prefix is used by another bot then maybe consider changing it.")

        except IndexError:
            return

        except:
            await Functions.embed(message, "Error", "Type: '" + prefix + "help' to find out how the bot works.")

        await bot.process_commands(message)

print("[ OK ] Nota was loaded into memory.")
print()
print("Nota is starting... ")

bot.run(TOKEN)