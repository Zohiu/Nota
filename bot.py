print("                                                                     ")
print("        _____________________________________________________        ")
print("       /       ***************************************       \       ")
print("      /        *  |\   |  |----|  ---|---    /-\     *        \      ")
print("     /         *  | \  |  |    |     |      /   \    *         \     ")
print("    /          *  |  \ |  |    |     |     /-----\   *          \    ")
print("   /           *  |   \|  |----|     |    /       \  *           \   ")
print("  /            ***************************************            \  ")
print(" /-----------------------------------------------------------------\ ")
print(" |              Version : 2.3  |  The BOT REVOLUTION!              | ")
print(" |-----------------------------------------------------------------| ")
print(" | This bot has gotten too big. send help. this code is just giant | ")
print(" \-----------------------------------------------------------------/ ")
print("  \                       code by Fguzy                           /  ")
print("   ---------------------------------------------------------------   ")
print("                                                                     ")


# Importing the packages
print("Importing packages and setting variables...")
import os
import discord
from discord.ext import commands
import time

# Defining the Vars
TOKEN = 'NjcwNzU0NjEzODIwOTE1NzE0.XqiCgQ.y9dbMQiPjw8IfAJidFbbfYf1vZI'
prefix = "-"
bot = commands.Bot(prefix)
dirpath = os.getcwd()
location = dirpath
files_in_dir = []
fileDir = os.path.dirname(os.path.realpath('__file__'))

# Removing normal help command
bot.remove_command("help")

print("[ OK ] All packages loaded and variables set.")
print()
print("Nota is loading...")

class Functions:

    async def embed(ctx, title, describtion):
        embed = discord.Embed(
            title=title,
            description=describtion,
            colour=0x34b713
        )
        #embed.set_footer(text="WARNING! ALL FILES FROM THIS BOT WILL BE MOVED OVER TO ANOTHER ONE! THIS BOT WILL BE UPDATED TO FIX MANY ISSUES AND YOU HAVE TO COPY YOUR FILES OVER TO THIS BOT. (IF YOU DON'T WANT TO COPY ALL FILES, CONTACT FGUZY#5577 ON THE SUPPORT SERVER. HE WILL COPY ALL OF THEM IF THEY ARE MORE THAN 15)")
        await ctx.send(embed=embed)

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

class Events:

    @bot.event
    async def on_ready():
        print("[ OK ] Nota is online.")
        print()

class Commands:

    @bot.command()
    async def help(ctx, *args):
        if await Functions.check_perm(ctx):
            embed = discord.Embed(
                title="Commands:",
                description="Prefix : -",
                colour=0x34b713
            )

            embed.set_footer(text="© 2020 Nota version 2.3 | The BOT REVOLUTION!, A bot by Fguzy#5577.")
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/670754613820915714/80e64cfc835ef73bef45ca6152b6da7e.png?size=2048")
            embed.set_author(name="Nota Bot help", icon_url="https://cdn.discordapp.com/avatars/670754613820915714/80e64cfc835ef73bef45ca6152b6da7e.png?size=2048")

            embed.add_field(name="Nota Bot main help page", value="-help", inline=False)

            try:
                if args[0] == "save":
                    embed.add_field(name="--------------", value="------ Save Commands ------", inline=False)

                    embed.add_field(name="Save something that only you can read. (dont forget the '')", value="-save {'TO BE SAVED'} {'FILENAME'}", inline=False)
                    embed.add_field(name="Save something that everyone can read. (dont forget the '')", value="-saveglobal {'TO BE SAVED'} {'FILENAME'}", inline=False)
                    embed.add_field(name="Save images for yourself. (dont forget the '')", value="-savepic {IMAGE LINK} {'FILENAME'}",inline=False)
                    embed.add_field(name="Save global images. (dont forget the '')", value="-savepicglobal {IMAGE LINK} {'FILENAME'}", inline=False)
                    embed.add_field(name="Save lists for yourself. (dont forget the '')", value="-list {make/add/change/remove} {'FILENAME'} {LINE NUMBER} {'TO BE SAVED'}\n'Line number' and 'to be saved' only on 'change'/'remove' | when using 'add' skip 'line number' and only do 'to be saved.'|", inline=False)
                    embed.add_field(name="Save global lists. (dont forget the '')", value="-list {make/add/change/remove} {'FILENAME'} {LINE NUMBER} {'TO BE SAVED'}\n'Line number' and 'to be saved' only on 'change'/'remove' | when using 'add' skip 'line number' and only do 'to be saved.'|", inline=False)

                if args[0] == "read":
                    embed.add_field(name="--------------", value="------ Read Commands ------", inline=False)

                    embed.add_field(name="Shows you a saved text.", value="-read {'FILENAME'}", inline=False)
                    embed.add_field(name="Shows you whichever text you want. (admins only)", value="-amdinread {'FILENAME'}", inline=False)

                if args[0] == "delete":
                    embed.add_field(name="--------------", value="------ Delete Commands ------", inline=False)

                    embed.add_field(name="Delete a file", value="-delete {'FILENAME'}", inline=False)
                    embed.add_field(name="Delete whichever file you want. (admins only)", value="-admindelete {'FILENAME'}", inline=False)

                if args[0] == "perms":
                    embed.add_field(name="--------------", value="------ Permission Commands ------", inline=False)

                    embed.add_field(name="give a user the permission to read a file", value="-userperm {'SAVE FILE'} {USER} {ADD/DELETE}\nuse add to give someone the perms and delete to take them away.", inline=False)
                    embed.add_field(name="Share a File. (how to get the guild id: Server settings -> Widget -> Server id)", value="-share {'SAVE FILE'} {GUILD ID OF THE RECEIVING SERVER}", inline=False)
                    embed.add_field(name="Only people with the role can use the bot", value="-onlyrole", inline=False)
                    embed.add_field(name="Everyone can use the bot", value="-everyone", inline=False)

                if args[0] == "listing":
                    embed.add_field(name="--------------", value="------ Listing Commands ------", inline=False)

                    embed.add_field(name="Lists all files that you can access (max files that the bot can list: 625)", value="-files", inline=False)
                    embed.add_field(name="Lists all files (max files that the bot can list: 625, admin only)", value="-adminfiles", inline=False)
                    embed.add_field(name="Lists your perms.", value="-userperms", inline=False)

                if args[0] == "other":
                    embed.add_field(name="--------------", value="------ Other Commands ------", inline=False)

                    embed.add_field(name="Calculate anything you want!", value="-calc {'task'}", inline=False)
                    embed.add_field(name="Embed anything you want!", value="-embed {'TITLE'} {'TEXT'}", inline=False)
                    embed.add_field(name="Show the amount of servers where the bot is online", value="-guilds", inline=False)
                    embed.add_field(name="Show the Bots ping", value="-ping", inline=False)
                    embed.add_field(name="Shows the invite link.", value="-invite", inline=False)
                    embed.add_field(name="Shows your server certificate", value="-certificate", inline=False)

                if args[0] == "premium":
                    embed.add_field(name="--------------", value="------ Premium Commands ------", inline=False)


            except:
                embed.add_field(name="Help for saving files:", value="-help save", inline=False)
                embed.add_field(name="Help for reading / showing files:", value="-help read", inline=False)
                embed.add_field(name="Help for deleting files:", value="-help delete", inline=False)
                embed.add_field(name="Help for file / command permissions:", value="-help perms", inline=False)
                embed.add_field(name="Help for listing all files / listing your perms:", value="-help listing", inline=False)
                embed.add_field(name="Help for premium features:", value="-help premium", inline=False)
                embed.add_field(name="Help for other stuffs:", value="-help other", inline=False)

            embed.add_field(name="If you like the bot please vote for it on top.gg.", value="https://top.gg/bot/670754613820915714/vote", inline=False)
            embed.add_field(name="Support me, the maker by subscribing to me on youtube.", value="https://www.youtube.com/channel/UCMiR4h60k6DJPrWgvTY6soQ", inline=False)

            await ctx.send(embed=embed)

# SAVING
    @bot.command()
    async def savepic(ctx, content, name):
        if await Functions.check_perm(ctx):
            try:
                file = open(os.path.join(fileDir, '{}/{}.{}.{}.dcsavepic'.format(ctx.guild.id, ctx.guild.id, ctx.message.author,name)), "a+")
                file.write(content)
                file.close()
            except:
                os.mkdir(os.path.join(fileDir, '{}'.format(ctx.guild.id)))
                file = open(os.path.join(fileDir, '{}/{}.{}.{}.dcsavepic'.format(ctx.guild.id, ctx.guild.id, ctx.message.author,name)), "a+")
                file.write(content)
                file.close()

            await Functions.embed(ctx, "Successfully saved!", "'" + content + "' was saved in '" + name + "' type '-read " + name + "' to see your saved data")

            dclistfile = os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id))
            open(dclistfile, "a+")

            found = False
            with open(dclistfile) as f:
                if '"' + name + '" (pic) Author: ' + str(ctx.message.author) + "\n" in f.read():
                    found = True
        
            if found == False:
                dclist = open(dclistfile, "a")
                name = '"' + name + '" (pic) Author: ' + str(ctx.message.author) + "\n"
                dclist.write(name)
                dclist.close

        else:
            await Functions.embed(ctx, "Error!", "You do not have the permission to use this command.")

    @bot.command()
    async def savepicglobal(ctx, content, name):
        if await Functions.check_perm(ctx):
            try:
                file = open(os.path.join(fileDir, '{}/{}.{}.dcsavepicglobal'.format(ctx.guild.id, ctx.guild.id, name)), "a+")
                file.write(content)
                file.close()
            except:
                os.mkdir(os.path.join(fileDir, '{}'.format(ctx.guild.id)))
                file = open(os.path.join(fileDir, '{}/{}.{}.dcsavepicglobal'.format(ctx.guild.id, ctx.guild.id, name)), "a+")
                file.write(content)
                file.close()

            await Functions.embed(ctx, "Successfully saved!", "'" + content + "' was saved in '" + name + "' type '-read " + name + "' to see your saved data. This save is global. Everyone can se it.")

            dclistfile = os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id))
            open(dclistfile, "a+")

            found = False
            with open(dclistfile) as f:
                if '"' + name + '" (pic) Author: ' + str(ctx.message.author) in f.read():
                    found = True

            if found == False:
                dclist = open(dclistfile, "a")
                name = '"' + name + '" (pic) Author: ' + str(ctx.message.author) + "\n"
                dclist.write(name)
                dclist.close

        else:
            await Functions.embed(ctx, "Error!", "You do not have the permission to use this command.")

    @bot.command()
    async def list(ctx, para, name, *args):
        if await Functions.check_perm(ctx):

            if para == 'make':
                try:
                    file = open(os.path.join(fileDir, '{}/{}.{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, ctx.message.author, name)),"a+")
                    file.write("")
                    file.close()

                    dclistfile = os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id))
                    open(dclistfile, "a+")

                    found = False
                    with open(dclistfile) as f:
                        if '"' + name + '"' in f.read():
                            found = True

                    if found == False:
                        dclist = open(dclistfile, "a")
                        name2 = '"' + name + '" Owner: ' + str(ctx.message.author) + "\n"
                        dclist.write(name2)
                        dclist.close

                except:
                    await Functions.embed(ctx, "Error!", "uh oh! this error is fatal! join the support server and tell Fguzy#5577 aka the bot owner about this!")

                await Functions.embed(ctx, "List made: '" + name + "'", "type '-list add " + name + " {CONTENT}' to add a line")

            elif para == 'add':
                try:
                    file = open(os.path.join(fileDir, '{}/{}.{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, ctx.message.author, name)), "r")
                    file.close()
                    file = open(os.path.join(fileDir, '{}/{}.{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, ctx.message.author, name)), "a+")
                    if file.readlines() == 0:
                        file.write(args[0] + "\n")
                    else:
                        file.write("\n" + args[0])

                    file.close()
                except:
                    await Functions.embed(ctx, "Error!", "This file does not exist.")

                await Functions.embed(ctx, "Successfully added point!", "'" + args[0] + "' was saved in '" + name + "' type '-read " + name + "' to see your saved list")

            elif para == 'change':
                try:
                    file = open(os.path.join(fileDir, '{}/{}.{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, ctx.message.author, name)), "r")
                    lines = file.readlines()
                    file.close()

                    lines = open(os.path.join(fileDir, '{}/{}.{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, ctx.message.author, name)), "r").read().splitlines()
                    lines[int(args[0])] = args[1]
                    open(os.path.join(fileDir, '{}/{}.{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, ctx.message.author, name)), 'w').write('\n'.join(lines))

                    await Functions.embed(ctx, "Successfully changed!", "line '" + args[0] + "' was changed to '" + args[1])
                except:

                    await Functions.embed(ctx, "Error!", "This file or line does not exist.")

            elif para == 'remove':
                try:
                    a_file = open(os.path.join(fileDir, '{}/{}.{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, ctx.message.author, name)), "r")
                    lines = a_file.readlines()
                    a_file.close()
                    del lines[int(args[0])]
                    new_file = open(os.path.join(fileDir, '{}/{}.{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, ctx.message.author, name)), "w+")
                    for line in lines:
                        new_file.write(line)
                    new_file.close()

                    await Functions.embed(ctx, "Successfully deleted!", "line was deleted.")
                except:
                    await Functions.embed(ctx, "Error!", "This file or line does not exist.")
            else:
                await Functions.embed(ctx, "Error!", "Use 'make', 'add', 'change' or 'remove'. For help type '-help'")
        else:
            await Functions.embed(ctx, "Error!", "You do not have the permission to use this command.")

    @bot.command()
    async def listglobal(ctx, para, name, *args):
        if await Functions.check_perm(ctx):

            if para == 'make':
                try:
                    file = open(os.path.join(fileDir, '{}/{}.{}.dcsaveglobal'.format(ctx.guild.id, ctx.guild.id, name)), "a+")
                    file.write("")
                    file.close()

                    dclistfile = os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id))
                    open(dclistfile, "a+")

                    found = False
                    with open(dclistfile) as f:
                        if '"' + name + '"' in f.read():
                            found = True

                    if found == False:
                        dclist = open(dclistfile, "a")
                        name2 = '"' + name + '" Author: ' + str(ctx.message.author) + "\n"
                        dclist.write(name2)
                        dclist.close

                except:
                    await Functions.embed(ctx, "Error!", "uh oh! this error is fatal! join the support server and tell Fguzy#5577 aka the bot owner about this!")

                await Functions.embed(ctx, "List made: '" + name + "'", "type '-list add " + name + " {CONTENT}' to add a line")

            elif para == 'add':
                try:
                    file = open(os.path.join(fileDir, '{}/{}.{}.dcsaveglobal'.format(ctx.guild.id, ctx.guild.id, name)), "r")
                    file.close()
                    file = open(os.path.join(fileDir, '{}/{}.{}.dcsaveglobal'.format(ctx.guild.id, ctx.guild.id, name)), "a+")
                    if file.readlines() == 0:
                        file.write(args[0] + "\n")
                    else:
                        file.write("\n" + args[0])

                    file.close()
                except:
                    await Functions.embed(ctx, "Error!", "This file does not exist.")

                await Functions.embed(ctx, "Successfully added point!", "'" + args[0] + "' was saved in '" + name + "' type '-read " + name + "' to see your saved list")

            elif para == 'change':
                try:
                    file = open(os.path.join(fileDir, '{}/{}.{}.dcsaveglobal'.format(ctx.guild.id, ctx.guild.id, name)), "r")
                    lines = file.readlines()
                    file.close()

                    lines = open(os.path.join(fileDir, '{}/{}.{}.dcsaveglobal'.format(ctx.guild.id, ctx.guild.id, name)), "r").read().splitlines()
                    lines[int(args[0])] = args[1]
                    open(os.path.join(fileDir, '{}/{}.{}.dcsaveglobal'.format(ctx.guild.id, ctx.guild.id, name)), 'w').write('\n'.join(lines))

                    await Functions.embed(ctx, "Successfully changed!", "line '" + args[0] + "' was changed to '" + args[1])
                except:
                    await Functions.embed(ctx, "Error!", "This file or line does not exist.")

            elif para == 'remove':
                try:
                    a_file = open(os.path.join(fileDir, '{}/{}.{}.dcsaveglobal'.format(ctx.guild.id, ctx.guild.id, name)), "r")
                    lines = a_file.readlines()
                    a_file.close()
                    del lines[int(args[0])]
                    new_file = open(os.path.join(fileDir, '{}/{}.{}.dcsaveglobal'.format(ctx.guild.id, ctx.guild.id, name)), "w+")
                    for line in lines:
                        new_file.write(line)
                    new_file.close()

                    await Functions.embed(ctx, "Successfully deleted!", "line was deleted.")
                except:
                    await Functions.embed(ctx, "Error!", "This file or line does not exist.")
            else:
                await Functions.embed(ctx, "Error!", "Use 'make', 'add', 'change' or 'remove'. For help type '-help'")
        else:
            await Functions.embed(ctx, "Error!", "You do not have the permission to use this command.")

    @bot.command()
    async def save(ctx, content, name):
        if await Functions.check_perm(ctx):
            try:
                file = open(os.path.join(fileDir, '{}/{}.{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, ctx.message.author, name)), "a+")
                file.write(content)
                file.close()
            except:
                os.mkdir(os.path.join(fileDir, '{}'.format(ctx.guild.id)))
                file = open(os.path.join(fileDir, '{}/{}.{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, ctx.message.author, name)), "a+")
                file.write(content)
                file.close()

            await Functions.embed(ctx, "Successfully saved!", "'" + content + "' was saved in '" + name + "' type '-read " + name + "' to see your saved data")

            dclistfile = os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id))
            open(dclistfile, "a+")

            found = False
            with open(dclistfile) as f:
                if '"' + name + '" Owner: ' + str(ctx.message.author) in f.read():
                    found = True

            if found == False:
                dclist = open(dclistfile, "a")
                name = '"' + name + '" Owner: ' + str(ctx.message.author) + "\n"
                dclist.write(name)
                dclist.close

        else:
            await Functions.embed(ctx, "Error!", "You do not have the permission to use this command.")

    @bot.command()
    async def saveglobal(ctx, content, name):
        if await Functions.check_perm(ctx):
            try:
                file = open(os.path.join(fileDir, '{}/{}.{}.dcsaveglobal'.format(ctx.guild.id, ctx.guild.id, name)), "a+")
                file.write(content)
                file.close()
            except:
                os.mkdir(os.path.join(fileDir, '{}'.format(ctx.guild.id)))
                file = open(os.path.join(fileDir, '{}/{}.{}.dcsaveglobal'.format(ctx.guild.id, ctx.guild.id, name)), "a+")
                file.write(content)
                file.close()

            await Functions.embed(ctx, "Successfully saved!", "'" + content + "' was saved in '" + name + "' type '-read " + name + "' to see your saved data. This save is global. Everyone can se it.")

            dclistfile = os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id))
            open(dclistfile, "a+")

            found = False
            with open(dclistfile) as f:
                if '"' + name + '" Author: ' + str(ctx.message.author) in f.read():
                    found = True

            if found == False:
                dclist = open(dclistfile, "a")
                name = '"' + name + '" Author: ' + str(ctx.message.author) + "\n"
                dclist.write(name)
                dclist.close

        else:
            await Functions.embed(ctx, "Error!", "You do not have the permission to use this command.")

# READING
    @bot.command()
    async def read(ctx, name):
        if await Functions.check_perm(ctx):
            try:
                filename = os.path.join(fileDir, '{}/{}.{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, ctx.message.author, name))
                file = open(filename, "r")

                await Functions.embed(ctx, name, file.read())

                file.close()
            except:
                try:
                    filename = os.path.join(fileDir, '{}/{}.{}.{}.dcsavepic'.format(ctx.guild.id, ctx.guild.id, ctx.message.author, name))
                    file = open(filename, "r")

                    await ctx.send(file.read())

                    file.close()
                except:
                    try:
                        filename = os.path.join(fileDir, '{}/{}.{}.dcsavepicglobal'.format(ctx.guild.id, ctx.guild.id, name))
                        file = open(filename, "r")

                        await ctx.send(file.read())

                        file.close()
                    except:
                        try:
                            filename = os.path.join(fileDir, '{}/{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, name))
                            file = open(filename, "r")

                            embed = discord.Embed(
                                title=name,
                                description=file.read(),
                                colour=0x34b713
                            )
                            embed.set_footer(text="NOTE: This file is old. to be compatible with permissions, please make a new file containing the content of this file.")
                            await ctx.send(embed=embed)

                            file.close()
                        except:
                            try:
                                filename = os.path.join(fileDir, '{}/{}.{}.dcsaveglobal'.format(ctx.guild.id, ctx.guild.id, name))
                                file = open(filename, "r")

                                embed = discord.Embed(
                                    title=name,
                                    description=file.read(),
                                    colour=0x34b713
                                )
                                embed.set_footer(text="Global File")
                                await ctx.send(embed=embed)

                                file.close()
                            except:
                                try:
                                    if await Functions.check_userperm(ctx, name):
                                        test = open(os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id)))
                                        lines = test.readlines()
                                        for line in lines:
                                            if '"' + name + '"' in line:
                                                string = line.replace('"' + name + '"' + ' Owner: ', "")
                                                if string.endswith("\n"):
                                                    string = string[:-1]

                                        filename = os.path.join(fileDir, '{}/{}.{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, string, name))
                                        file = open(filename, "r")

                                        await Functions.embed(ctx, name, file.read())

                                        file.close()

                                    elif ctx.message.author.server_permissions.administrator:
                                        try:
                                            filename = os.path.join(fileDir, '{}/{}.{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, ctx.message.author, name))
                                            file = open(filename, "r")

                                            await Functions.embed(ctx, name, file.read())

                                            file.close()
                                        except:
                                            filename = os.path.join(fileDir, '{}/{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, name))
                                            file = open(filename, "r")

                                            embed = discord.Embed(
                                                title=name,
                                                description=file.read(),
                                                colour=0x34b713
                                            )
                                            embed.set_footer(text="NOTE: This file is old. to be compatible with permissions, please make a new file containing the content of this file.")
                                            await ctx.send(embed=embed)

                                            file.close()
                                    else:
                                        await Functions.embed(ctx, "Error", "There is no such file called '" + name + "' or you do not have the permission to read the file.")

                                except:
                                    await Functions.embed(ctx, "Error", "There is no such file called '" + name + "' or you do not have the permission to read the file.")



        else:
            await Functions.embed(ctx, "Error", "There is no such file called '" + name + "' or you do not have the permission to read the file.")

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def adminread(ctx, name):
        try:
            test = open(os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id)))
            lines = test.readlines()
            for line in lines:
                if '"' + name + '"' in line:
                    string = line.replace('"' + name + '"' + ' Owner: ', "")
                    if string.endswith("\n"):
                        string = string[:-1]

            filename = os.path.join(fileDir, '{}/{}.{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, string, name))
            file = open(filename, "r")

            await Functions.embed(ctx, name, file.read())

            file.close()
        except:
            try:
                for line in lines:
                    if '"' + name + '"' in line:
                        string = line.replace('"' + name + '"' + ' (pic) Owner: ', "")
                        if string.endswith("\n"):
                            string = string[:-1]

                filename = os.path.join(fileDir, '{}/{}.{}.{}.dcsavepic'.format(ctx.guild.id, ctx.guild.id, string, name))
                file = open(filename, "r")

                await ctx.send(file.read())

                file.close()
            except:
                try:

                    filename = os.path.join(fileDir, '{}/{}.{}.dcsavepicglobal'.format(ctx.guild.id, ctx.guild.id, name))
                    file = open(filename, "r")

                    await ctx.send(file.read())

                    file.close()
                except:
                    try:
                        filename = os.path.join(fileDir, '{}/{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, name))
                        file = open(filename, "r")

                        embed = discord.Embed(
                            title=name,
                            description=file.read(),
                            colour=0x34b713
                        )
                        embed.set_footer(text="NOTE: This file is old. to be compatible with permissions, please make a new file containing the content of this file.")
                        await ctx.send(embed=embed)

                        file.close()
                    except:
                        try:
                            filename = os.path.join(fileDir, '{}/{}.{}.dcsaveglobal'.format(ctx.guild.id, ctx.guild.id, name))
                            file = open(filename, "r")

                            embed = discord.Embed(
                                title=name,
                                description=file.read(),
                                colour=0x34b713
                            )
                            embed.set_footer(text="Global File")
                            await ctx.send(embed=embed)

                            file.close()
                        except:
                            await Functions.embed(ctx, "Error!", "This file does not exist.")

# DELETING
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def admindelete(ctx, name):
        try:
            test = open(os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id)))
            lines = test.readlines()
            for line in lines:
                if '"' + name + '"' in line:
                    string = line.replace('"' + name + '"' + ' Owner: ', "")
                    if string.endswith("\n"):
                        string = string[:-1]

            os.remove(os.path.join(fileDir, '{}/{}.{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, string, name)))

            await Functions.embed(ctx, "'" + name + "' has been deleted.", "This action can't be undone.")

            file = os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id))
            tostrip = '"' + name + '" Owner: ' + str(string)

            with open(file, "r") as f:
                lines = f.readlines()

            with open(file, "w") as f:
                for line in lines:
                    if line.strip("\n") != tostrip:
                        f.write(line)
        except:
            try:
                os.remove(os.path.join(fileDir, '{}/{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, string, name)))

                await Functions.embed(ctx, "'" + name + "' has been deleted.", "This action can't be undone.")

                file = os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id))
                tostrip = '"' + name + '"'

                with open(file, "r") as f:
                    lines = f.readlines()

                with open(file, "w") as f:
                    for line in lines:
                        if line.strip("\n") != tostrip:
                            f.write(line)
            except:
                try:
                    test = open(os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id)))
                    lines = test.readlines()
                    for line in lines:
                        if '"' + name + '"' in line:
                            string = line.replace('"' + name + '"' + ' (pic) Owner: ', "")
                            if string.endswith("\n"):
                                string = string[:-1]

                    os.remove(os.path.join(fileDir, '{}/{}.{}.dcsavepic'.format(ctx.guild.id, ctx.guild.id, name)))

                    await Functions.embed(ctx, "'" + name + "' has been deleted.", "This action can't be undone.")

                    file = os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id))
                    tostrip = '"' + name + '" (pic) Author: ' + string

                    with open(file, "r") as f:
                        lines = f.readlines()

                    with open(file, "w") as f:
                        for line in lines:
                            if line.strip("\n") != tostrip:
                                f.write(line)
                except:
                    try:
                        test = open(os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id)))
                        lines = test.readlines()
                        for line in lines:
                            if '"' + name + '"' in line:
                                string = line.replace('"' + name + '"' + ' (pic) Author: ', "")
                                if string.endswith("\n"):
                                    string = string[:-1]

                        os.remove(os.path.join(fileDir, '{}/{}.{}.dcsavepicglobal'.format(ctx.guild.id, ctx.guild.id, name)))

                        await Functions.embed(ctx, "'" + name + "' has been deleted.", "This action can't be undone.")

                        file = os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id))
                        tostrip = '"' + name + '" (pic) Author: ' + string

                        with open(file, "r") as f:
                            lines = f.readlines()

                        with open(file, "w") as f:
                            for line in lines:
                                if line.strip("\n") != tostrip:
                                    f.write(line)
                    except:
                        try:
                            os.remove(
                                os.path.join(fileDir, '{}/{}.{}.dcsaveglobal'.format(ctx.guild.id, ctx.guild.id, name)))

                            await Functions.embed(ctx, "'" + name + "' has been deleted.", "This action can't be undone.")

                            test = open(os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id)))
                            lines = test.readlines()
                            for line in lines:
                                if '"' + name + '"' in line:
                                    string = line.replace('"' + name + '"' + ' Author: ', "")
                                    if string.endswith("\n"):
                                        string = string[:-1]

                            file = os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id))
                            tostrip = '"' + name + '" Author: ' + str(string)

                            with open(file, "r") as f:
                                lines = f.readlines()

                            with open(file, "w") as f:
                                for line in lines:
                                    if line.strip("\n") != tostrip:
                                        f.write(line)
                        except:
                            await Functions.embed(ctx, "Error", "There is no such file called '" + name + "' or you don't have the permission.")

    @bot.command()
    async def delete(ctx, name):
        if await Functions.check_perm(ctx):
            try:
                os.remove(os.path.join(fileDir, '{}/{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, name)))

                await Functions.embed(ctx, "'" + name + "' has been deleted.", "This action can't be undone.")

                file = os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id))
                tostrip = '"' + name + '"'

                with open(file, "r") as f:
                    lines = f.readlines()

                with open(file, "w") as f:
                    for line in lines:
                        if line.strip("\n") != tostrip:
                            f.write(line)
            except:
                try:
                    os.remove(os.path.join(fileDir, '{}/{}.{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, ctx.message.author, name)))

                    await Functions.embed(ctx, "'" + name + "' has been deleted.", "This action can't be undone.")

                    file = os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id))
                    tostrip = '"' + name + '" Owner: ' + str(ctx.message.author)

                    with open(file, "r") as f:
                        lines = f.readlines()

                    with open(file, "w") as f:
                        for line in lines:
                            if line.strip("\n") != tostrip:
                                f.write(line)
                except:
                    try:
                        os.remove(os.path.join(fileDir, '{}/{}.{}.{}.dcsavepic'.format(ctx.guild.id, ctx.guild.id, ctx.message.author, name)))

                        await Functions.embed(ctx, "'" + name + "' has been deleted.", "This action can't be undone.")

                        file = os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id))
                        tostrip = '"' + name + '" (pic) Owner: ' + str(ctx.message.author)

                        with open(file, "r") as f:
                            lines = f.readlines()

                        with open(file, "w") as f:
                            for line in lines:
                                if line.strip("\n") != tostrip:
                                    f.write(line)
                    except:
                        try:
                            test = open(os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id)))
                            lines = test.readlines()
                            for line in lines:
                                if '"' + name + '"' in line:
                                    string = line.replace('"' + name + '"' + ' (pic) Author: ', "")
                                    if string.endswith("\n"):
                                        string = string[:-1]

                            os.remove(os.path.join(fileDir, '{}/{}.{}.dcsavepicglobal'.format(ctx.guild.id, ctx.guild.id, name)))

                            await Functions.embed(ctx, "'" + name + "' has been deleted.", "This action can't be undone.")

                            file = os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id))
                            tostrip = '"' + name + '" (pic) Author: ' + string

                            with open(file, "r") as f:
                                lines = f.readlines()

                            with open(file, "w") as f:
                                for line in lines:
                                    if line.strip("\n") != tostrip:
                                        f.write(line)
                        except:
                            try:
                                os.remove(os.path.join(fileDir, '{}/{}.{}.dcsaveglobal'.format(ctx.guild.id, ctx.guild.id, name)))

                                await Functions.embed(ctx, "'" + name + "' has been deleted.", "This action can't be undone.")

                                test = open(os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id)))
                                lines = test.readlines()
                                for line in lines:
                                    if '"' + name + '"' in line:
                                        string = line.replace('"' + name + '"' + ' Author: ', "")
                                        if string.endswith("\n"):
                                            string = string[:-1]

                                file = os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id))
                                tostrip = '"' + name + '" Author: ' + str(string)

                                with open(file, "r") as f:
                                    lines = f.readlines()

                                with open(file, "w") as f:
                                    for line in lines:
                                        if line.strip("\n") != tostrip:
                                            f.write(line)
                            except:
                                await Functions.embed(ctx, "Error", "There is no such file called '" + name + "' or you don't have the permission.")
        else:
            await Functions.embed(ctx, "Error!", "You do not have the permission to use this command.")

# LISTING
    @bot.command(pass_context=True)
    async def files(ctx):
        file_lines_2 = ""
        file_lines = []
        counter = 0
        if await Functions.check_perm(ctx):
            embed = discord.Embed(
                title="All files that you can read:",
                description="",
                colour=0x34b713
            )

            try:
                with open(os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id)), "r") as file:

                    for line in file:
                        if "Author" in line:
                            file_lines.append(line + "\n")
                            counter += 1
                        elif str(ctx.message.author) in line:
                            file_lines.append(line + "\n")
                            counter += 1

                        if counter == 24:
                            for thing in file_lines:
                                file_lines_2 = str(file_lines_2) + str(thing)

                            embed.add_field(name="25 files:", value=file_lines_2, inline=False)
                            file_lines = []
                            file_lines_2 = []
                            counter = 0

                    for thing in file_lines:
                        file_lines_2 = str(file_lines_2) + str(thing)

                    embed.add_field(name="the rest:", value=file_lines_2, inline=False)
                    file_lines = []
                    file_lines_2 = []

                await ctx.send(embed=embed)
            except:
                await Functions.embed(ctx, "All saved files on this server:",
                                      "There are no files saved on this server.")

    @bot.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def adminfiles(ctx):
        file_lines_2 = ""
        file_lines = []
        counter = 0
        if await Functions.check_perm(ctx):
            embed = discord.Embed(
                title="All saved files on this server:",
                description="",
                colour=0x34b713
            )

            try:
                with open(os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id)), "r") as file:

                    for line in file:
                        file_lines.append(line + "\n")
                        counter += 1
                        if counter == 24:
                            for thing in file_lines:
                                file_lines_2 = str(file_lines_2) + str(thing)

                            embed.add_field(name="25 files:", value=file_lines_2, inline=False)
                            file_lines = []
                            file_lines_2 = []
                            counter = 0

                    for thing in file_lines:
                        file_lines_2 = str(file_lines_2) + str(thing)

                    embed.add_field(name="the rest:", value=file_lines_2, inline=False)
                    file_lines = []
                    file_lines_2 = []

                await ctx.send(embed=embed)
            except:
                await Functions.embed(ctx, "All saved files on this server:",
                                      "There are no files saved on this server.")

# PERMS
    @bot.command(pass_context=True)
    async def userperm(ctx, file, user: discord.Member, add_delete):
        if add_delete == "add":
            try:
                open(os.path.join(fileDir, '{}/{}.{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, ctx.message.author, file)), "r")
                userfile = open(os.path.join(fileDir, '{}/{}.{}.dcuser'.format(ctx.guild.id, ctx.guild.id, user)), "a+")
                write = '"' + file + '"' + '\n'
                userfile.write(write)
                userfile.close()
                await Functions.embed(ctx, "Successfully set permissions.", "The user now has the permissions to view that file.")
            except:
                await Functions.embed(ctx, "Error!", "You don't own that file or it doesn't exist.")

        elif add_delete == "delete":
            try:
                open(os.path.join(fileDir, '{}/{}.{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, ctx.message.author, file)), "r")

                userfile = os.path.join(fileDir, '{}/{}.{}.dcuser'.format(ctx.guild.id, ctx.guild.id, user))

                fn = userfile
                f = open(fn)
                output = []
                str = '"' + file + '"'
                for line in f:
                    if not line.startswith(str):
                        output.append(line)
                f.close()
                f = open(fn, 'w')
                f.writelines(output)
                f.close()

                await Functions.embed(ctx, "Successfully deleted permissions.", "you deleted the permissions for this file for that user.")

            except:
                await Functions.embed(ctx, "Error!", "You don't own that file, it doesn't exist or the user doesn't have the permissions for it.")

        else:
            await Functions.embed(ctx, "Error!", "Use 'add' or 'delete'. For help type '-help'")

    @bot.command(pass_context=True)
    async def userperms(ctx, *args):
        if await Functions.check_perm(ctx):
            embed = discord.Embed(
                title="Your perms:",
                description="",
                colour=0x34b713
            )

            try:
                file = open(
                    os.path.join(fileDir, '{}/{}.{}.dcuser'.format(ctx.guild.id, ctx.guild.id, ctx.message.author)),
                    "r")
                embed.add_field(name="Files:", value=file.read(), inline=False)
                await ctx.send(embed=embed)

            except:
                await Functions.embed(ctx, "All saved files on this server:",
                                      "There are no files saved on this server.")

    @bot.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def onlyrole(ctx):
        await ctx.guild.create_role(name="Nota perms")
        open(os.path.join(fileDir, '{}/{}.dcperms'.format(ctx.guild.id, ctx.guild.id)), "w+")
        await Functions.embed(ctx, "Yay!",
                              "Perms enabled. ONLY people with the 'Nota perms' role can use the bot. Administrators can always type '-disableperms' to disable the perms.")

    @bot.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def everyone(ctx):
        try:
            open(os.path.join(fileDir, '{}/{}.dcperms'.format(ctx.guild.id, ctx.guild.id)), "a+")
            role = discord.utils.get(ctx.guild.roles, name="Nota perms")
            if role:
                try:
                    os.remove(os.path.join(fileDir, '{}/{}.dcperms'.format(ctx.guild.id, ctx.guild.id)))
                    await Functions.embed(ctx, "Perms Disabled.",
                                          "The Perms have been disabled and everyone can use the bot now. You can now delete the 'Nota perms role. You don't have to keep it.'")
                except discord.Forbidden:
                    await Functions.embed(ctx, "Error!",
                                          "No Permission to delete the 'Nota perms' role. Please move the 'Nota' role over the 'Nota perms' role and try again.")
            else:
                await bot.say("The role doesn't exist!")
        except:
            await Functions.embed(ctx, "Error!", "Perms are already disabled. type '-enableperms' to enable perms.")

# OTHER STUFF
    @bot.command(pass_context=True)
    async def calc(ctx, problem):
        try:
            await Functions.embed(ctx, "Result:", eval(problem))
        except ZeroDivisionError:
            await Functions.embed(ctx, "Result:", "ERROR! Division by zero is impossible!")
        except:
            await Functions.embed(ctx, "Result:", "ERROR! You cant solve that!")

    @bot.command(pass_context=True)
    async def ping(ctx):
        if await Functions.check_perm(ctx):
            before = time.monotonic()
            message = await ctx.send("Pong!")
            ping = (time.monotonic() - before) * 1000
            await message.edit(content=f"Pong!  `{int(ping)}ms`")

    @bot.command(pass_context=True)
    async def embed(ctx, title, text):
        await Functions.embed(ctx, title, text)

    @bot.command(pass_context=True)
    async def guilds(ctx):
        if await Functions.check_perm(ctx):
            await Functions.embed(ctx, "This bot is on this many servers:", len(bot.guilds))

    @bot.command(pass_context=True)
    async def share(ctx, file, share):
        if await Functions.check_perm(ctx):
            try:
                savefile = open(os.path.join(fileDir, '{}/{}.{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, ctx.message.author, file)), "r")

                sharesavefile = open(os.path.join(fileDir, '{}/{}.{}.{}.dcsave'.format(share, share, ctx.message.author,file)), "a")
                sharelistfile = open(os.path.join(fileDir, '{}/{}.dclist'.format(share, share)), "a")
            
                sharesavefile.write(savefile.read())
                sharelistfile.write('"' + file + '" Owner: ' + str(ctx.message.author))
                sharelistfile.close()
                sharesavefile.close()
                savefile.close()

                await Functions.embed(ctx, "Yay!", "Successfully shared '" + file + "' to '" + share + "'")

            except:
                try:
                    savefile = open(os.path.join(fileDir, '{}/{}.{}.{}.dcsavepic'.format(ctx.guild.id, ctx.guild.id, ctx.message.author, file)), "r")

                    sharesavefile = open(os.path.join(fileDir, '{}/{}.{}.{}.dcsave'.format(share, share, ctx.message.author, file)), "a")
                    sharelistfile = open(os.path.join(fileDir, '{}/{}.dclist'.format(share, share)), "a")

                    sharesavefile.write(savefile.read())
                    sharelistfile.write('"' + file + '" (pic) Owner: ' + str(ctx.message.author))
                    sharelistfile.close()
                    sharesavefile.close()
                    savefile.close()

                    await Functions.embed(ctx, "Yay!", "Successfully shared '" + file + "' to '" + share + "'")

                except:
                    await Functions.embed(ctx, "Error!", "A problem occured while trying to share '" + file + "' to '" + share + ". does the file exist? Have you entered a valid guild id?")
            
    @bot.command()
    async def invite(ctx):
        await Functions.embed(ctx, "Invite Link:", "https://discordapp.com/oauth2/authorize?client_id=670754613820915714&permissions=268439552&scope=bot")

# PREMIUM
    @bot.command(pass_context=True)
    async def certificate(ctx):
        if str(ctx.guild.id) == "693204864045416519":
            await Functions.embed(ctx, "Nota server certificate", "This server is officially backed by me, the developer (Fguzy#5577).")

        elif str(ctx.guild.id) == "483168202306748427":
            await Functions.embed(ctx, "Nota server certificate", "This server is officially backed by me, the developer (Fguzy#5577).")

        elif str(ctx.guild.id) == "673372073242132480":
            await Functions.embed(ctx, "Nota server certificate", "This server is officially backed by me, the developer (Fguzy#5577).")

        else:
            await Functions.embed(ctx, "Nota server certificate", "Sorry, this server doesn't seem to have a Nota certificate.")

print("[ OK ] Nota was loaded into memory.")
print()
print("Nota is starting... ")

bot.run(TOKEN)