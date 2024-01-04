from discord_components import DiscordComponents, Button, ButtonStyle
from discord.abc import PrivateChannel
from discord.ext import commands, tasks
from Modules.colors import Colors
import datetime
import discord
import asyncio
import shutil
import json
import time
import dbl
import os


class TopGG(commands.Cog):
    def __init__(self, bot_in):
        self.bot = bot_in
        self.token = json.loads(open("settings.json", "r").read())["top.gg"]["token"]
        self.dblpy = dbl.DBLClient(self.bot, self.token)
        self.update_stats.start()

    def cog_unload(self):
        self.update_stats.cancel()

    @tasks.loop(minutes=30)
    async def update_stats(self):
        await self.bot.wait_until_ready()
        try:
            server_count = len(self.bot.guilds)
            # await self.dblpy.post_guild_count(server_count)
            print(Colors.BLUE + '[top.gg] Posted server count ({})'.format(server_count) + Colors.RESET)
        except Exception as e:
            print(
                Colors.BLUE + '[top.gg] Failed to post server count\n{}: {}'.format(type(e).__name__, e) + Colors.RESET)


class Bot:
    TOKEN = json.loads(open("settings.json", "r").read())["bot"]["token"]
    BOT = commands.Bot(command_prefix="-", help_command=None)
    STARTUP_TIME = time.time()
    COMMANDS = []
    ENABLED = []
    BUTTON_LOOKUP = []
    BOT.remove_command("help")

    @staticmethod
    def getBot():
        return Bot.BOT

    @staticmethod
    def getStartupTime():
        return Bot.STARTUP_TIME

    @staticmethod
    def addButtonLookup(button):
        # "button" should look like: {"id": "custom id", "func": func}
        Bot.BUTTON_LOOKUP.append(button)

    @staticmethod
    def command(f):
        if not f.__name__ in Bot.ENABLED:
            Bot.COMMANDS.append({"name": f.__name__, "func": f})
            Bot.ENABLED.append(f.__name__)
            print(Colors.BLUE + '[Debug] Command "' + Colors.CYAN + f.__name__[0].upper() + f.__name__[
                                                                                            1:] + Colors.BLUE + '" has been enabled' + Colors.RESET)

        def wrapper(message):
            result = asyncio.run(f(message))
            return result

        return wrapper

    @staticmethod
    @BOT.event
    async def on_ready():
        DiscordComponents(Bot.BOT)
        Bot.getBot().add_cog(TopGG(Bot.getBot()))
        print(Colors.BLUE + "[Debug] Nota has been started and is online.\n" + Colors.RESET)

    @staticmethod
    @BOT.event
    async def on_guild_join(guild):
        print(Colors.GREEN + "[Bot] Nota joined a guild. Current number:" + Colors.CYAN,
              len(Bot.getBot().guilds) + Colors.RESET)

    @staticmethod
    @BOT.event
    async def on_guild_remove(guild):
        print(Colors.GREEN + "[Bot] Nota left a guild. Current number:" + Colors.CYAN,
              len(Bot.getBot().guilds) + Colors.RESET)
        fileDir = os.path.join(os.getcwd(), "Data/Files/{}".format(guild.id))
        shutil.rmtree(fileDir, ignore_errors=True)

    @staticmethod
    @BOT.event
    async def on_button_click(interaction):
        print(Colors.GREEN + "[Bot] A button has been pressed:",
              Colors.CYAN + interaction.component.id, Colors.RESET)
        for i in Bot.BUTTON_LOOKUP:
            if interaction.component.id == i["id"]:
                await i["func"](interaction)
                break

    @staticmethod
    @BOT.event
    async def on_message(message):
        if isinstance(message.channel, PrivateChannel):
            session = {"id": message.author.id, "is_private": True}
        else:
            try:
                session = {"id": message.guild.id, "is_private": False}
            except AttributeError:
                return

        fileDir = os.path.join(os.getcwd(), "Data/Files/{}".format(session["id"]))

        if not os.path.exists(fileDir):
            os.mkdir(fileDir)

        if not os.path.exists((os.path.join(fileDir, 'data.json'))):
            open(os.path.join(fileDir, 'settings.json'), "w+").write(
                json.dumps(
                    {"prefix": "-", "color": "68C60E", "read_footer": True, "show_ads": True,
                     "show_favourites": True}
                ))

        if not os.path.exists((os.path.join(fileDir, 'files.json'))):
            open(os.path.join(fileDir, 'files.json'), "w+").write(
                json.dumps(
                    {"files": []}
                ))

        if not os.path.exists((os.path.join(fileDir, 'stats.json'))):
            open(os.path.join(fileDir, 'stats.json'), "w+").write(
                json.dumps(
                    {"stats": []}
                ))

        if not os.path.exists((os.path.join(fileDir, 'favourites.json'))):
            open(os.path.join(fileDir, 'favourites.json'), "w+").write(
                json.dumps(
                    {"favourites": []}
                ))

        with open(os.path.join(fileDir, 'settings.json'), "r") as file:
            settings = json.loads(file.read())
            file.close()

        msglst = message.content.split(" ")

        for i in Bot.COMMANDS:
            if msglst[0] == settings["prefix"] + i["name"]:

                # Executing the actually command's function:
                await i["func"](message, Bot.getBot(), fileDir, session, Bot.getStartupTime())

                with open("Data/Statistics/botstats.json", "r") as stats:
                    stats = json.loads(stats.read())

                dt = datetime.datetime.today()
                stats["totaluses"] += 1
                stats["monthlyuses"]["current"]["amount"] += 1
                stats["dailyuses"]["current"]["amount"] += 1

                if dt.month != stats["monthlyuses"]["current"]["month"]:
                    stats["monthlyuses"]["old"].append(
                        {"year": dt.year,
                         "month": dt.month,
                         "amount": stats["monthlyuses"]["current"]["amount"]
                         }
                    )

                    stats["monthlyuses"]["current"]["month"] = dt.month
                    stats["monthlyuses"]["current"]["amount"] = 0

                if dt.day != stats["dailyuses"]["current"]["day"]:
                    stats["dailyuses"]["old"].append(
                        {"year": dt.year,
                         "month": dt.month,
                         "day": dt.day,
                         "amount": stats["dailyuses"]["current"]["amount"]
                         }
                    )

                    stats["dailyuses"]["current"]["day"] = dt.day
                    stats["dailyuses"]["current"]["amount"] = 0

                open("Data/Statistics/botstats.json", "w").write(json.dumps(stats))
                print(Colors.GREEN + "[Bot] A command has been executed",
                      Colors.BLUE + "#" + str(stats["totaluses"]) + ":",
                      Colors.CYAN + i["name"], Colors.RESET)
                break
