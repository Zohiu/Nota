# /--------------------------\
# |  Nota bot code by Fguzy  |
# |--------------------------|
# |Version : 2.1  TWO!!!!!   |
# \--------------------------/

# Importing the packages
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

class Functions:
    async def embed(ctx, title, describtion):
        embed = discord.Embed(
            title=title,
            description=describtion,
            colour=0x34b713
        )
        embed.set_footer(text="Subscribe to the maker, Fguzy on YouTube: shorturl.at/mFJK8")
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


class Commands:
    @bot.command()
    async def help(ctx):
        if await Functions.check_perm(ctx):
            embed = discord.Embed(
                title="Commands:",
                description="Prefix : -",
                colour=0x34b713
            )

            embed.set_footer(text="Â© 2020 Nota, A bot by Fguzy#5577.")
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/670754613820915714/80e64cfc835ef73bef45ca6152b6da7e.png?size=2048")
            embed.set_author(name="Nota Bot help", icon_url="https://cdn.discordapp.com/avatars/670754613820915714/80e64cfc835ef73bef45ca6152b6da7e.png?size=2048")
            embed.add_field(name="Nota Bot help", value="-help", inline=False)
            embed.add_field(name="Save something. (dont forget the '')", value="-save {'TO BE SAVED'} {'FILENAME'}", inline=False)
            embed.add_field(name="Show you a saved text.", value="-read {'FILENAME'}", inline=False)
            embed.add_field(name="Delete a file", value="-delete {'FILENAME'}", inline=False)
            embed.add_field(name="Share a File. (how to get the guild id: Server settings -> Widget -> Server id)", value="-share {'SAVE FILE'} {GUILD ID OF THE RECEIVING SERVER}", inline=False)
            embed.add_field(name="enable the permissions", value="-enableperms", inline=False)
            embed.add_field(name="disable the permissions", value="-disableperms", inline=False)
            embed.add_field(name="Lists all files", value="-list", inline=False)
            embed.add_field(name="Show the amount of servers where the bot is online", value="-guilds", inline=False)
            embed.add_field(name="Show the Bots ping", value="-ping", inline=False)
            embed.add_field(name="Shows the invite link.", value="-invite", inline=False)
            embed.add_field(name="If you like the bot please vote for it on top.gg.", value="https://top.gg/bot/670754613820915714/vote", inline=False)
            embed.add_field(name="Support me, the maker by subscribing to me on youtube.", value="https://www.youtube.com/channel/UCMiR4h60k6DJPrWgvTY6soQ", inline=False)
            await ctx.send(embed=embed)


    @bot.command()
    async def save(ctx, content, name):
        if await Functions.check_perm(ctx):
            try:
                file = open(os.path.join(fileDir,'{}/{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, name)), "a+")
                file.write(content)
                file.close()
            except:
                os.mkdir(os.path.join(fileDir, '{}'.format(ctx.guild.id)))
                file = open(os.path.join(fileDir, '{}/{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, name)), "a+")
                file.write(content)
                file.close()

            await Functions.embed(ctx, "Successfully saved!", "'" + content + "' was saved in '" + name + "' type '-read " + name + "' to see your saved data")

            dclistfile = os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id))
            open(dclistfile, "a+")

            found = False
            with open(dclistfile) as f:
                if '"' + name + '"' in f.read():
                    found = True
        
            if found == False:
                dclist = open(dclistfile, "a")
                name = '"' + name + '"' +"\n"
                dclist.write(name)
                dclist.close

        else:
            await Functions.embed(ctx, "Error!", "You do not have the permission to use this command.")

    @bot.command()
    async def read(ctx, name):
        if await Functions.check_perm(ctx):
            try:
                filename = os.path.join(fileDir, '{}/{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, name))
                file = open(filename, "r")

                await Functions.embed(ctx, name, file.read())

                file.close()
            except:
                await Functions.embed(ctx, "Error", "There is no such file called '" + name + "'")
        else:
            await Functions.embed(ctx, "Error!", "You do not have the permission to use this command.")

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
                await Functions.embed(ctx, "Error", "There is no such file called '" + name + "'")
        else:
            await Functions.embed(ctx, "Error!", "You do not have the permission to use this command.")

    @bot.command(pass_context=True)
    async def ping(ctx):
        if await Functions.check_perm(ctx):
            before = time.monotonic()
            message = await ctx.send("Pong!")
            ping = (time.monotonic() - before) * 1000
            await message.edit(content=f"Pong!  `{int(ping)}ms`")


    @bot.command()
    async def list(ctx):
        if await Functions.check_perm(ctx):
            embed = discord.Embed(
                title = "All saved files on this server:",
                description = "",
                colour = 0x34b713
            )

            with open (os.path.join(fileDir, '{}/{}.dclist'.format(ctx.guild.id, ctx.guild.id)), "r") as file:
                for line in file:
                    embed.add_field(name="File:", value=line.strip(), inline=False)
            await ctx.send(embed=embed)


    @bot.command(pass_context=True)
    async def guilds(ctx):
        if await Functions.check_perm(ctx):
            await Functions.embed(ctx, "This bot is on this many servers:", len(bot.guilds))


    @bot.command(pass_context=True)
    async def share(ctx, file, share):
        if await Functions.check_perm(ctx):
            try:
                savefile = open(os.path.join(fileDir, '{}/{}.{}.dcsave'.format(ctx.guild.id, ctx.guild.id, file)) , "r")

                sharesavefile = open(os.path.join(fileDir, '{}/{}.{}.dcsave'.format(share, share, file)), "a")
                sharelistfile = open(os.path.join(fileDir, '{}/{}.dclist'.format(share, share)), "a")
            
                sharesavefile.write(savefile.read())
                sharelistfile.write('"' + file + '"')
                sharelistfile.close()
                sharesavefile.close()
                savefile.close()

                await Functions.embed(ctx, "Yay!", "Successfully shared '" + file + "' to '" + share + "'")

            except:
                await Functions.embed(ctx, "Error!", "A problem occured while trying to share '" + file + "' to '" + share + ". does the file exist? Have you entered a valid guild id?")

    @bot.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def enableperms(ctx):
        await ctx.guild.create_role(name="Nota perms")
        open(os.path.join(fileDir, '{}/{}.dcperms'.format(ctx.guild.id, ctx.guild.id)), "w+")
        await Functions.embed(ctx, "Yay!", "Perms enabled. ONLY people with the 'Nota perms' role can use the bot. Administrators can always type '-disableperms' to disable the perms.")

    @bot.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def disableperms(ctx):
        try:
            open(os.path.join(fileDir, '{}/{}.dcperms'.format(ctx.guild.id, ctx.guild.id)), "a+")
            role = discord.utils.get(ctx.guild.roles, name="Nota perms")
            if role:
                try:
                    os.remove(os.path.join(fileDir, '{}/{}.dcperms'.format(ctx.guild.id, ctx.guild.id)))
                    await Functions.embed(ctx, "Perms Disabled.", "The Perm role has been deleted and everyone can use the bot now. You can now delete the 'Nota perms role. You don't have to keep it.'")
                except discord.Forbidden:
                    await Functions.embed(ctx, "Error!", "No Permission to delete the 'Nota perms' role. Please move the 'Nota' role over the 'Nota perms' role and try again.")
            else:
                await bot.say("The role doesn't exist!")
        except:
            await Functions.embed(ctx, "Error!", "Perms are already disabled. type '-enableperms' to enable perms.")
            
    @bot.command()
    async def invite(ctx):
        await Functions.embed(ctx, "Invite Link:", "https://discordapp.com/oauth2/authorize?client_id=670754613820915714&permissions=268439552&scope=bot")

print("The Bot has started.")
bot.run(TOKEN)