import Functions
import os

async def run(message):
    if open(os.path.join(os.getcwd(), "premium_manipulation"), "r").read() == "":
        if str(message.channel.type) == "private":
            premium = await Functions.get_premium_status(message)

            if premium == "none":
                await Functions.embed(message, "User premium status:", "This user does not have Nota premium.")
            else:
                await Functions.embed(message, "User premium status:", "This user has Nota premium " + premium)

            await Functions.bot_used(message, "premium", message.channel.type)
        else:
            premium = await Functions.get_premium_status(message)

            if premium == "none":
                await Functions.embed(message, "Server premium status:", "This server does not have Nota premium.")
            else:
                await Functions.embed(message, "Server premium status:", "This server has Nota premium " + premium + " through the owner's membership")
    else:
        await Functions.embed(message, "It's your lucky day!", "The owner has temporarily given everyone Nota premium " + open(os.path.join(os.getcwd(), "premium_manipulation"), "r").read() + "!")

        await Functions.bot_used(message, "premium", message.channel.type)