import Functions
import os

fileDir = os.path.join(os.getcwd(), "Files")

async def run(message, bot):
    files = folders = 0
    for _, dirnames, filenames in os.walk(fileDir):
        # ^ this idiom means "we won't be using this value"
        files += len(filenames)
        folders += len(dirnames)

    await Functions.embed(message, "Nota has data of this many servers and users saved:", str(folders))