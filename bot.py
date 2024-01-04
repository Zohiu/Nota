from datetime import datetime
from discord import Bot, Embed, Color
from discord.commands import Option
from discord.utils import basic_autocomplete
import data

from math import ceil

# The pycord Bot object
bot = Bot(debug_guilds = [744589923788652565])
color = Color(value=int("db48cd", 16))
time_format = "%d.%m.%Y %H:%M:%S"
error_emoji = "<:error_cross:925779010313658429>"
success_emoji = "<:success_check:925779052504154142>"

@bot.slash_command(name="save", description = "Saves a note")
async def save(ctx, name: Option(str, "The note's name"), content: Option(str, "The note's content"), attachment: Option(str, "Attached files", required = False, default = '')):
    # Name length checking
    if len(name) > 64:
        await ctx.respond(embed=Embed(description = f"{error_emoji} That name is too long! It can only be 64 characters in length.", color = color))
        return
    
    # Content length checking
    elif len(content) > 5000:
        await ctx.respond(embed=Embed(description = f"{error_emoji} That content is too long! It can only be 5000 characters in length.", color = color))
        return
    
    # File already exists checking
    files = await data.get_from_table(ctx.author.id, "files")
    if files is not None:
        for file in files:
            # If the file has been found
            if list(file.keys())[0] == name:
                await ctx.respond(embed=Embed(description = f"{error_emoji} That file name already exists!", color = color))
                return
    
    # If the file is valid, save it.
    attachments = None
    time = str(datetime.now().strftime(time_format))
    save = await data.set_for_table(
        ctx.author.id, "files", {f"{name}": f"{content}", "attachments": attachments, "author": ctx.author.id, "times_opened": 0,
                                 "created_at": time, "last_accessed": time, "last_modified": time}
    )
    
    # If the response is True, it worked. Else it returned an error
    if save:
        await ctx.respond(embed=Embed(description = f"{success_emoji} The file has been saved!", color = color))
    else:
        await ctx.respond(embed=Embed(description = f"{error_emoji} {save}!", color = color))


@bot.slash_command(description = "Shows you the content of a note")
async def read(ctx, name: Option(str, "The name of the note you want to show", autocomplete=basic_autocomplete(["Yes"]))):
    # Get all the users files
    files = await data.get_from_table(ctx.author.id, "files")
    
    # Loop and check for correct name
    for file in files:
        # If the file has been found
        if list(file.keys())[0] == name:
            # Update the file stats
            file["last_accessed"] = str(datetime.now().strftime(time_format))
            file["times_opened"] += 1
            await data.set_for_table(ctx.author.id, "files", file)
            
            # Send the response
            embed = Embed(title = list(file.keys())[0], description = list(file.values())[0], color = color)
            embed.set_footer(text = f'Created at {file["created_at"]} | Opened {file["times_opened"]} times')
            await ctx.respond(embed = embed)
            return
    
    # If it hasn't returned yet, the file doesn't exist.
    await ctx.respond(embed=Embed(description = f"{error_emoji} That file doesn't exist!", color = color))


@bot.slash_command(description = "Shows you a list of all notes")
async def files(ctx):
    # Get all the users files
    files = await data.get_from_table(ctx.author.id, "files")
    
    # If there aren't any files, return
    if files is None:
        await ctx.respond(embed = Embed(description = f"{error_emoji} You don't have any files.", color = color))
        return
    
    
    # Add everything to one list
    all_files = []
    for file in files:
        all_files.append(f'**{list(file.keys())[0]}**\n'
                      f' - Created on: {file["created_at"]}\n'
                      f' - Opened {file["times_opened"]} times\n'
                      f' - Last modification: {file["last_modified"]}\n'
                      f' - Last accessed: {file["last_accessed"]}\n')
    
    # Split the list into equal parts of 5
    all_fields = [all_files[x:x + 5] for x in range(0, len(all_files), 5)]
    
    # Set the description to the first field
    realfield = ""
    for subfield in all_fields[0]: realfield += subfield
    
    embed = Embed(title = "All files", description = realfield, color = color)
    
    # Add all the other fields
    for field in all_fields[1:]:
        realfield = ""
        for subfield in field: realfield += subfield
        embed.add_field(name = "\u200b", value = realfield, inline = False)
        
    
    # Send the response
    await ctx.respond(embed = embed)


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

print("running now")
bot.run("NjgxNTEwNDY0MzkxMzQ4MzA0.XlPgFA.fxsOMSi6Ojie5DZ0LT8B7mPSFi8")
