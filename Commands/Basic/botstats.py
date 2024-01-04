from pathlib import Path
import datetime
import discord
import time
import json
import os

def initialize(notabot):
    @notabot.command
    async def botstats(message, *args):
        bot = args[0]
        session_dir = args[1]
        session = args[2]
        startup_time = args[3]

        file = open(os.path.join(session_dir, 'settings.json'), "r")
        settings = json.loads(file.read())
        file.close()

        color = settings["color"]

        files = folders = 0
        for _, dirnames, filenames in os.walk(os.getcwd() + "/Data/Files"):
            folders += len(dirnames)
            for i in filenames:
                if i == "files.json":
                    file = open(os.path.join(_, i), "r")
                    s = json.loads(file.read())
                    file.close()
                    files += len(s["files"])
                    break

        with open("Data/Statistics/botstats.json", "r") as file:
            totaluses = file.read()

        stats = open("Data/Statistics/botstats.json", "r").read()
        stats = json.loads(stats)

        # Usage data
        totaluses = stats["totaluses"]
        monthlyuses = stats["monthlyuses"]["current"]["amount"]
        dailyuses = stats["monthlyuses"]["current"]["amount"]

        # Uptime data
        current_time = time.time()
        difference = int(round(current_time - startup_time))
        text = str(datetime.timedelta(seconds=difference))

        used_space = round(sum(f.stat().st_size for f in Path(os.getcwd()).glob('**/*') if f.is_file()) / (1024 * 1024),
                           2)

        embed = discord.Embed(title="Nota's statistics\nPing: " + str(round(bot.latency * 1000)),
                              description="```Basics```",
                              colour=int(color, 16))

        embed.add_field(name="**Total guilds:** ", value=str(len(bot.guilds)), inline=True)
        embed.add_field(name="**Total userdata:** ", value=str(folders), inline=True)
        embed.add_field(name="**Total files:** ", value=str(files), inline=True)

        embed.add_field(name="\u200b\n", value="```Usage```", inline=False)

        embed.add_field(name="**Total uses:** ", value=str(totaluses), inline=True)
        embed.add_field(name="**Monthly uses:** ", value=str(monthlyuses), inline=True)
        embed.add_field(name="**Daily uses:** ", value=str(dailyuses), inline=True)

        embed.add_field(name="\u200b\n", value="```Other```", inline=False)

        embed.add_field(name="**Time since last restart:** ", value=str(text), inline=True)
        embed.add_field(name="**Total used space:** ", value=str(used_space) + " MB", inline=True)

        embed.set_footer(text=1 * "\u2800")

        await message.channel.send(embed=embed)