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


    privacy_text =  "\n**What data does Nota collect?**\n"\
                    "The only things that Nota store are your notes and settings, the author's username and ID and the guild ID.\n"\
                    \
                    "\n**Why does Nota need that data?**\n"\
                    "The notes and settings are saved because that's what makes Nota possible.\n"\
                    "The username and ID are saved to identify what note is made by which user.\n"\
                    "The guild ID is saved to identify what guild a note belongs to.\n" \
                    \
                    "\n**How do I use that data?**\n"\
                    "The guild ID is used to safely store messages so no other guild can access them.\n"\
                    "The usernames and IDs are used to show who the message belongs to.\n"\
                    "The notes and settings are saved to make nota work.\n" \
                     \
                    "\n**Who do I share that data with?**\n"\
                    "The data is not shared with anyone.\n"\
                    "Only the owner is able to access any saved data.\n" \
                     \
                    "\n**How can I contact the owner?**\n"\
                    "You can join the support server at any time and message the owner.\n"\
                    "The link is found in the help menu.\n" \
                     \
                    "\n**How can I remove all of my data?**\n"\
                    "While Nota is online and you remove the bot from you server, all of your data is removed.\n"\
                    "If you remove the bot while it's offline or you want to remove your private data, contact the owner.\n"\


    embed = discord.Embed(title="Nota Privacy Policy:", description=privacy_text, colour=discord.Color(value=int(color, 16)))

    if os.path.exists(os.path.join(fileDir, '{}/settings/user.color'.format(message.author.id))):
        color = open(
            os.path.join(fileDir, '{}/settings/user.color'.format(message.author.id, message.author.id)),
            "r").read()
        embed = discord.Embed(title="Nota Privacy Policy:", description=privacy_text,
                              colour=discord.Color(value=int(color, 16)))


    embed.set_footer(text="© 2020 Nota " + version + " | A bot by Fguzy#5577.")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/673373031405453322/725093465704104016/Nota_logo_3_2.png?size=2048")

    await message.channel.send(embed=embed)
    await Functions.bot_used(message, "privacy", message.channel.type)