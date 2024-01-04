import Functions


async def run(message, prefix, msglst):
    premium = await Functions.get_premium_status(message)

    if premium == "pro" or premium == "ultra":
        try:
            await Functions.embed(message, msglst[1], msglst[2])
        except:
            await Functions.embed(message, "<:nota_error:796499987949027349> Usage: '" + prefix + "embed <title> <content>'")
        await Functions.bot_used(message, "embed", message.channel.type)

    else:
        await Functions.embed(message, "<:nota_error:796499987949027349> You need at least premium pro to use this command!")