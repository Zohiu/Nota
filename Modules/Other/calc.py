import Functions


async def run(message, msglst):
    premium = await Functions.get_premium_status(message)

    if premium == "default" or premium == "pro" or premium == "ultra":
        try:
            await Functions.embed(message, "Result:", eval(msglst[1]))
        except ZeroDivisionError as e:
            await Functions.embed(message, "Result:", str(e))
        except SyntaxError as e:
            await Functions.embed(message, "Result:", str(e))
        except NameError as e:
            await Functions.embed(message, "Result:", str(e))

        await Functions.bot_used(message, "calc", message.channel.type)
    else:
        await Functions.embed(message, "<:nota_error:796499987949027349> You need at least premium default to use this command!")