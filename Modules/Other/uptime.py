import Functions
import datetime

async def run(message, start_time, time):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    await Functions.embed(message, "Time since the last restart:", text)
    await Functions.bot_used(message, "uptime", message.channel.type)