import Functions
import discord
import json
import os

fileDir = os.path.join(os.getcwd(), "Files")

async def run(message, prefix, msglst, version):
    if str(message.channel.type) == "private":
        id = os.path.join(str(message.author.id), str(message.author.id))
    else:
        id = os.path.join(str(message.guild.id), str(message.guild.id))

    file = open(os.path.join(fileDir, '{}.json'.format(id)), "r")
    s = json.loads(file.read())
    file.close()

    color = s["settings"]["color"]

    embed = discord.Embed(title="Help:", description="", colour=discord.Color(value=int(color, 16)))

    if os.path.exists(os.path.join(fileDir, '{}/settings/user.color'.format(message.author.id))):
        color = open(
            os.path.join(fileDir, '{}/settings/user.color'.format(message.author.id, message.author.id)),
            "r").read()
        embed = discord.Embed(title="Help:", description="",
                              colour=discord.Color(value=int(color, 16)))

    if len(msglst) > 1:
        if msglst[1] == "files":
            embed.add_field(name="\u200b",
                            value="You can use all of these commands with your private files from DM on servers! just add A `private` in front of the command. Like: `privatesave` or `privateread`.",
                            inline=False)
            embed.add_field(name="\u200b\n------ File Commands ------", value="\u200b", inline=False)
            embed.add_field(name="Saving normal text:", value="```" + prefix + "save text <name> <content>```",
                            inline=False)
            embed.add_field(name="Saving raw text:", value="```" + prefix + "save raw <name> <content>```",
                            inline=False)
            embed.add_field(name="Saving attachments:\n`You need to attach a file. The message is optional.`",
                            value="```" + prefix + "save file <name> <file type> [message]```\n",
                            inline=False)
            embed.add_field(name="Editing files:",
                            value="`Add text to a file:`\n```" + prefix + "save edit add <name> <text>```\n" +
                                  "`Add a line to a file:`\n```" + prefix + "save edit addline <name> <text>```\n" +
                                  "`Overwrite a file:`\n```" + prefix + "save edit set <name> <new content>```\n" +
                                  "`Overwrite a line from a file:`\n```" + prefix + "save edit setline <name> <line> <new content>```\n" +
                                  "`Remove text from a file:`\n```" + prefix + "save edit remove <name> <text>```\n" +
                                  "`Remove a line from a file:`\n```" + prefix + "save edit removeline <name> <line> <new content>```\n",
                            inline=False)

            embed.add_field(name="Saving favourites (quick access):",
                            value="`Showing your favourites:`\n```" + prefix + "favourites```\n" +
                                  "`Adding favourites:`\n```" + prefix + "favourites add <name>```\n" +
                                  "`Removing favourites:`\n```" + prefix + "favourites remove <name>```\n",
                            inline=False)

            embed.add_field(name="Reading files:", value="```" + prefix + "read <name>```", inline=False)

            embed.add_field(name="Deleting files:", value="```" + prefix + "delete <name>```", inline=False)

            embed.add_field(name="Listing all files:", value="```" + prefix + "files```", inline=False)

        elif msglst[1] == "other":
            embed.add_field(name="\u200b\n------ Other Commands ------", value="\u200b", inline=False)
            embed.add_field(name="Setting the prefix:", value="```" + prefix + "setprefix <new prefix>```",
                            inline=False)
            embed.add_field(name="Creating timers (Keep in mind that this won't be exact!)",
                            value="```" + prefix + "timer <seconds>```", inline=False)
            embed.add_field(name="Solving math problems:", value="```" + prefix + "calc <problem>```", inline=False)
            embed.add_field(name="Making simple custom embeds", value="```" + prefix + "embed <title> <content>```",
                            inline=False)
            embed.add_field(name="Showing your  stats", value="```" + prefix + "stats```", inline=False)
            embed.add_field(name="Showing Nota's stats", value="```" + prefix + "botstats```", inline=False)

        elif msglst[1] == "premium":
            embed.add_field(name="\u200b\n------ Premium Commands ------", value="\u200b", inline=False)
            embed.add_field(name="Setting the embed color:", value="```" + prefix + "setcolor <color hex>```",
                            inline=False)
            embed.add_field(name="Resetting the embed color:", value="```" + prefix + "resetcolor```",
                            inline=False)
            embed.add_field(name="Toggling the info footer:", value="```" + prefix + "togglefooter```",
                            inline=False)
            embed.add_field(name="Toggling the advertisements:", value="```" + prefix + "toggleads```",
                            inline=False)
            embed.add_field(name="Toggling the favourites dock:", value="```" + prefix + "togglefavourites```",
                            inline=False)
            embed.add_field(name="Showing the premium status:", value="```" + prefix + "premium```", inline=False)

        else:
            embed.add_field(name="\u200b\n------ Error ------\n\u200b",
                            value="```This help page does not exist!```", inline=False)


    else:
        embed.add_field(name="Help for file features:", value="```-help files```")
        embed.add_field(name="Help for premium features:", value="```-help premium```")
        embed.add_field(name="Help for other features:", value="```-help other```\u200b")

        embed.add_field(name="You have ideas or questions?",
                        value="[Join the support server!](https://discord.gg/yf3jehq4sn)", inline=True)
        embed.add_field(name="You want private files?", value="Use Nota in private chat!", inline=True)

    embed.add_field(name="\u200b\nFAQ:",
                    value="**How do I put more than one word at once into a file?**\nJust use quotation marks like this:\n" + '`-save text "File name" "File content"`\n\n' +
                    "**What does <> and [] mean?**\nIf an argument is surrounded by `<>`, it is required to use that argument.\nIf an argument is surrounded by `[]`, it is not required to use that argument",
                    inline=False)

    embed.add_field(name="\u200b\nExtra info:",
                    value="`Current prefix: " + prefix + "`",
                    inline=False)

    embed.add_field(name="If you like the bot please vote for it on top.gg.",
                    value="https://top.gg/bot/670754613820915714/vote", inline=False)
    embed.add_field(name="You want to know more about privacy?", value="Type: " + "`" + prefix + "privacy`",
                    inline=True)

    embed.set_footer(text="© 2020 Nota " + version + " | A bot by Fguzy#5577.")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/673373031405453322/725093465704104016/Nota_logo_3_2.png?size=2048")
    embed.set_author(name="Nota Bot help",
                     icon_url="https://cdn.discordapp.com/attachments/673373031405453322/725088685065896007/Nota_icon_3.png?size=2048")

    await message.channel.send(embed=embed)
    await Functions.bot_used(message, "help", message.channel.type)