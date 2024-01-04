from discord_components import Button, ButtonStyle, Select, SelectOption
import discord
import json


def initialize(notabot):
    async def left(interaction):
        channel = await notabot.BOT.fetch_channel(interaction.channel_id)
        message = await channel.fetch_message(interaction.raw_data["message"]["id"])
        print(interaction.raw_data)
        # if I can use raw data to get old embed, I can send hidden info somehow
        # Or I am big brain and have the title always be the note title or the status. Then I get info everywhere.

        await message.delete()

        buttons = [[
            Button(
                style=ButtonStyle.blue,
                label="left 1",
                custom_id="left"
            ),
            Button(
                style=ButtonStyle.blue,
                label="right 1",
                custom_id="right"
            ),
        ]]

        await channel.send(embed=discord.Embed(
            description="left page right heeere",
            colour=discord.Color(value=int("00ff12", 16))),
            components=buttons)

    async def right(interaction):
        channel = await notabot.BOT.fetch_channel(interaction.channel_id)
        message = await channel.fetch_message(interaction.raw_data["message"]["id"])

        await message.delete()

        buttons = [[
            Button(
                style=ButtonStyle.blue,
                label="left",
                custom_id="left"
            ),
            Button(
                style=ButtonStyle.blue,
                label="right",
                custom_id="right"
            ),
        ]]

        await channel.send(embed=discord.Embed(
            description="right page right heeere",
            colour=discord.Color(value=int("00ff12", 16))),
            components=buttons)

    notabot.addButtonLookup({"id": "left", "func": left})
    notabot.addButtonLookup({"id": "right", "func": right})

    @notabot.command
    async def test(message, *args):
        bot = args[0]
        session_dir = args[1]
        session = args[2]

        with open(session_dir + "/" + 'settings.json', "r") as s:
            settings = json.loads(s.read())

        description = "main menu"

        buttons = [[
            Button(
                style=ButtonStyle.blue,
                label="left",
                custom_id="left"
            ),
            Button(
                style=ButtonStyle.blue,
                label="right",
                custom_id="right"
            ),
        ],
            Select(placeholder="This exists.", id="testid", options=[
                SelectOption(label="Well It dont work rn.", value="optval"),
                SelectOption(label="1Well It dont work rn.", value="optveeal"),
            ]),
        ]

        await message.channel.send(embed=discord.Embed(
            description=description,
            colour=discord.Color(value=int(settings["color"], 16))),
            components=buttons
        )
