import Functions


async def run(message, bot):
    latency = str(round(bot.latency * 1000))
    await Functions.embed(message, "Nota's ping:", latency + " ms")
    await Functions.bot_used(message, "ping", message.channel.type)