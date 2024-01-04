# /--------------------------\
# |  Nota bot code by Fguzy  |
# |--------------------------|
# |Version : 1.6 share funct.|
# \--------------------------/

# Importing the packages
import os
import discord
from discord.ext import commands
import datetime
import time

# Defining the Vars
TOKEN = 'NjgxNTEwNDY0MzkxMzQ4MzA0.XlROUA.OZBHPEk8u5hQiMoEpR_OLYQ_0bk'
GUILD = discord.Guild
prefix = "-"
bot = commands.Bot(prefix)
dirpath = os.getcwd()
foldername = os.path.basename(dirpath)
location = dirpath
files_in_dir = []

# Removing normal help command
bot.remove_command("help")

async def save(guild, save, name):
    file = open("{}.dcsave".format(guild), "a+")
    file.write(save, name)
    file.close()

async def helptext(ctx):
    embed = discord.Embed(
        title = "Commands:",
        description = "Prefix : -",
        colour = 0x34b713
    )
    
    embed.set_footer(text="© 2020 Nota, A bot by Fguzy#5577.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/670754613820915714/80e64cfc835ef73bef45ca6152b6da7e.png?size=2048")
    embed.set_author(name="Nota Bot help" , icon_url="https://cdn.discordapp.com/avatars/670754613820915714/80e64cfc835ef73bef45ca6152b6da7e.png?size=2048")
    embed.add_field(name="Nota Bot help", value="-help", inline=False)
    embed.add_field(name="Save something. (dont forget the '')", value="-save {'TO BE SAVED'} {'FILENAME'}", inline=False)
    embed.add_field(name="Show you a saved text.", value="-read {'FILENAME'}", inline=False)
    embed.add_field(name="Delete a file", value="-delete {'FILENAME'}", inline=False)
    embed.add_field(name="Share a File. (how to get the guild id: Server settings -> Widget -> Server id)", value="-share {'SAVE FILE'} {GUILD ID OF THE RECEIVING SERVER}", inline=False)
    embed.add_field(name="Lists all files", value="-list", inline=False)
    embed.add_field(name="Show the amount of servers where the bot is online", value="-botservers", inline=False)
    embed.add_field(name="Show the Bots ping", value="-ping", inline=False)
    embed.add_field(name="If you like the bot please vote for it on top.gg.", value="https://top.gg/bot/670754613820915714/vote", inline=False)
    await ctx.send(embed=embed)

async def savetext(ctx, title, description):
    embed = discord.Embed(
        title = title,
        description = description,
        colour = 0x34b713
    )
    await ctx.send(embed=embed)
    
async def readtext(ctx, title, description):
    embed = discord.Embed(
        title = title,
        description = description,
        colour = 0x34b713
    )
    await ctx.send(embed=embed)

async def failreadtext(ctx, title, description):
    embed = discord.Embed(
        title = title,
        description = description,
        colour = 0x34b713
    )
    await ctx.send(embed=embed)
    
async def deletetext(ctx, title, description):
    embed = discord.Embed(
        title = title,
        description = description,
        colour = 0x34b713
    )
    await ctx.send(embed=embed)
    
async def remove_empty_lines(filename):
    if not os.path.isfile(filename):
        print("{} does not exist ".format(filename))
        return
    with open(filename) as filehandle:
        lines = filehandle.readlines()

    with open(filename, 'w') as filehandle:
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines)

# Commands
@bot.command()
async def help(ctx):
    await helptext(ctx)

@bot.command()
async def save(ctx, arg, arg2):
    global now
    text = "´" + arg + "´ was saved in ´" + arg2 + "´ type ´-read "+ arg2 + "´ to see your saved data"
    file = open("{}.{}.dcsave".format(ctx.guild.id, arg2), "a")
    file.write(arg)
    await savetext(ctx, "Successfully saved!", text)
    print("someone saved '" + arg + "' under the name '" + "{}.{}.dcsave".format(ctx.guild, arg2) + "'")
    file.close()
    file = open("{}.{}.dcsave".format(ctx.guild.id, arg2), "a")
    
    file = open("{}.logfile".format(datetime.datetime.now().date()), "a")
    file.write(now.strftime("%Y-%m-%d %H:%M:%S") + " | someone saved '" + arg + "' under the name '" + "{}.{}.dcsave".format(ctx.guild, arg2) + "'\n")
    file.close
    file = open("{}.dclist".format(ctx.guild.id), "a")
    file.close
    
    found = False
    with open("{}.dclist".format(ctx.guild.id)) as f:
        if '"' + arg2 + '"' in f.read():
            found = True
        
    if found == False:
        file = open("{}.dclist".format(ctx.guild.id), "a")
        arg2 = '"' + arg2 + '"' +"\n"
        file.write(arg2)
        print("saved", arg2, "in", str(ctx.guild.id) + ".dclist")
        file.close
    
@bot.command()
async def read(ctx, arg):
    global now
    try:
        file = open("{}.{}.dcsave".format(ctx.guild.id, arg), "r")
        await readtext(ctx, arg ,file.read())
        print("someone read '" + "{}.{}.dcsave".format(ctx.guild.id, arg) + "'")
        file.close()
        file = open("{}.logfile".format(datetime.datetime.now().date()), "a")
        file.write(now.strftime("%Y-%m-%d %H:%M:%S") + " | someone read '" + "{}.{}.dcsave".format(ctx.guild.id, arg) + "'\n")
        file.close
    except:
        await failreadtext(ctx, "Error!", "there is no such file called ´" + arg + "´.")

@bot.command()
async def delete(ctx, arg):
    global now
    text = "´" + arg + "´ has been deleted."
    os.remove("{}.{}.dcsave".format(ctx.guild.id, arg))
    await deletetext(ctx, text, "This action can't be undone")
    print("someon deleted '" + "{}.{}.dcsave".format(ctx.guild.id, arg) + "'")
    file = open("{}.logfile".format(datetime.datetime.now().date()), "a")
    file.write(now.strftime("%Y-%m-%d %H:%M:%S") + " | someone deleted '" + "{}.{}.dcsave".format(ctx.guild.id, arg) + "'\n")
    file.close
    
    file = "{}.dclist".format(ctx.guild.id)
    
    arg = '"' + arg + '"'
    
    f = open(file, 'r')
    a = [arg, arg, arg]
    lst = []
    for line in f:
        if arg in line:
            line = line.replace(arg,'')
    lst.append(line)
    f.close()
    f = open(file,'w')
    for line in lst:
        f.write(line)
    f.close()
    
    await remove_empty_lines(file)
    
@bot.command(pass_context=True)
async def ping(ctx):
    """ Pong! """
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")
    print(f'Ping {int(ping)}ms')
    
@bot.command()
async def list(ctx):
    global location
    global files_in_dir
    embed = discord.Embed(
        title = "All saved files on this server:",
        description = "",
        colour = 0x34b713
    )
    with open ("{}.dclist".format(ctx.guild.id), "r") as fileHandler:
    # Read each line in loop
        for line in fileHandler:
        # As each line (except last one) will contain new line character, so strip that
            print(line.strip())
            embed.add_field(name="File:", value=line.strip(), inline=False)
    await ctx.send(embed=embed)
    
@bot.command(pass_context=True)
async def botservers(ctx):
    embed = discord.Embed(
        title = "This bot is on this many servers:",
        description = len(bot.guilds),
        colour = 0x34b713
    )
    await ctx.send(embed=embed)  
    
@bot.command(pass_context=True)
async def share(ctx, arg, arg2):
    global now
    try:
        file = open("{}.{}.dcsave".format(ctx.guild.id, arg), "r")
        if len(arg2) == 18:
            file2 = open("{}.{}.dcsave".format(arg2, arg), "a")
            
        file2.write(file.read())
        file2.close()
        file.close()
        file = open("{}.logfile".format(datetime.datetime.now().date()), "a")
        file.write(now.strftime("%Y-%m-%d %H:%M:%S") + " | someone shared '" + "{}.{}.dcsave".format(ctx.guild.id, arg) + "'\n")
        file.close
        
        embed = discord.Embed(
            title = "Yay!",
            description = "Successfully shared '" + arg + "' to '" + arg2 + "'",
            colour = 0x34b713
        )
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(
            title = "Error!",
            description = "A problem occured while trying to share '" + arg + "' to '" + arg2 + "does the file exist? Have you entered a valid guild id?",
            colour = 0x34b713
        )
        await ctx.send(embed=embed)

print("the bot has started!")
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print("current directory is : " + dirpath)
print("Directory name is : " + foldername)
print("everything should work")

bot.run(TOKEN)