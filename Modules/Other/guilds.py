import Functions


async def run(message, bot):
    numberofguilds = len(bot.guilds)
    await Functions.embed(message, "Nota is on this many servers:", str(numberofguilds))
    await Functions.bot_used(message, "guilds", message.channel.type)