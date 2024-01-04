from discord.ext import commands
from discord.abc import PrivateChannel
from discord import errors
import traceback
import discord
import shutil
import json
import time
import os

class Functions:
    async def input_handler(message_content):
        if len(message_content) < 1:
            return [None]
        
        current_string = ""
        in_quotation = False
        msglst = []
        for i in message_content:
            if i == '"' or i == '“' or i == '”':
                i = ""
                if in_quotation:
                    in_quotation = False
                    msglst.append(current_string)
                    current_string = ""
                
                elif not in_quotation:
                    in_quotation = True
            
            if i == " " and not in_quotation:
                i = ""
                msglst.append(current_string)
                current_string = ""
            
            current_string += i
        msglst.append(current_string)
        
        for i in msglst:
            if i == "":
                msglst.remove(i)
        
        return msglst

    async def get_prefix(message):
        if isinstance(message.channel, PrivateChannel):
            file = open(os.path.join(fileDir, '{}/{}.json'.format(str(message.author.id), str(message.author.id))), "r")
            s = json.loads(file.read())
            file.close()
            return s["settings"]["prefix"]
        else:
            file = open(os.path.join(fileDir, '{}/{}.json'.format(str(message.guild.id), str(message.guild.id))), "r")
            s = json.loads(file.read())
            file.close()
            return s["settings"]["prefix"]


if __name__ == '__main__':
    bot = commands.Bot("longprefixjoi098n2zxß3r")
    bot_updater = bot
    files_in_dir = []
    fileDir = os.path.join(os.getcwd(), "Files")
    start_time = time.time()
    
    bot.remove_command("help")
    
    
    @bot.event
    async def on_guild_join(guild):
        await bot.leave_guild(guild)
        print("[Guilds] The bot joined a guild. Current number:", len(bot.guilds))
    
    @bot.event
    async def on_guild_remove(guild):
        print("[Guilds] The bot left a guild. Current number:", len(bot.guilds))
        shutil.rmtree(os.path.join(fileDir, str(guild.id)), ignore_errors = True)
    
    @bot.event
    async def on_ready():
        print("[Debug] Nota is online.")
        print()

    #with open("Data/totaluses.dat", "r") as file:
    #    fread = file.read()
    #    with open("Data/totaluses.dat", "w") as file2:
    #        file2.write(str(int(fread) + 1))
    
    @bot.event
    async def on_message(message):
        if message.author.id == bot.user.id:
            return
        
        prefix = await Functions.get_prefix(message)
        msglst = await Functions.input_handler(message.content)
        
        
        try:
            print("[Bot] Nota has been used.")
            if isinstance(message.channel, PrivateChannel):
                current_id = os.path.join(str(message.author.id), str(message.author.id))
            else:
                current_id = os.path.join(str(message.guild.id), str(message.guild.id))
            
            if str(msglst[0]).startswith(prefix):
                current_embed = discord.Embed(
                    title = "Nota has ended.",
                    description =
"""
**Why?**

Nota was created on `January 25th 2020`. The last major update was on `December 24th 2020`. That's almost exactly **one** year
of updates. I made some *small* patches after that to fix bugs but never continued to work on it

I started with Nota when I was still pretty new to programming. My code has gotten *really* messy and I'm not too happy with it.
But that's not a problem, right? I don't have to change much about the bot. It's just notes.

**Wrong!** Discord launched slash commands and requires everyone to switch. For me this would mean:

```
1: I redo everything from the start
2: I make it even more messy and impossible to work with
3: I stop
```

I could already drop the second idea because it's terrible. That only leaves two things I could do.

Long story short, making a note bot is really boring and I don't want to do it all again.
I would also have to use a fully new database solution as my current one is just terrible.

On top of that, I have started working on a lot of other projects that are way more fun to me.
That's why I picked option three. **I stop**.

**What happens now?**

I put everything I have of Nota up on github (Except user data of course). If you feel like using it, go ahead:
https://github.com/

About the data:
**You have time until <timecode> to execute the command "dump". It will provide you with a download of all your files.**
After the deadline, I will delete **all** remaining user data.

**Advertising **

Leaving Nota behind doesn't mean that I'll *poof* :ghost: and be gone forever. I will be working on new stuff in the future.
~~Maybe even Nota 2~~ I'll *almost certainly* come back to Discord bot development soon after the full death of Nota.

After all the time and resources I spent on keeping the bot alive, I deserve to be able to advertise.
I have a YouTube channel on which I make music: https://www.youtube.com/channel/UCMiR4h60k6DJPrWgvTY6soQ
My music is also on Spotify: https://open.spotify.com/artist/79sP0BbLIwBFAa5lxoBxYv?si=oqDaCi46S4eax5OPKAwlVw

But anyways, I invite everyone to join my Server and follow me to my future projects!

**Future projects**

```Vulria goes here.```

**It's been a great time**

Nota has been a motivation for me to learn programming and I've come a long way ever since.
While it might not be *among us* anymore, Nota had a big influence on my life and probably some Discord servers.
There were a lot of challenges and hours spent converting between databases, but now I'm here, ready for a new chapter.

Have a nice day!

`Start reading from the top, please.`
""",

                    colour = discord.Color(value = int("ff0066", 16)))
                
                await message.channel.send(embed = current_embed)
            
        except Exception as e:
            stringsend = f"There has been an error during execution:\n" \
                         f"```" \
                         f"{traceback.format_exc()}" \
                         f"```" \
                         f"Please report this error to the developer."
            print(e)
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
    
    bot.run("NjgxNTEwNDY0MzkxMzQ4MzA0.GPaI5h.G3PVf236mzGkwBh9NJcOv0X5M83DFRKM8G0Ix8")