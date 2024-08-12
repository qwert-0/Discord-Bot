from dotenv import load_dotenv
import discord
import os
from discord.ext import commands
# from discord_slash import SlashCommand
# from discord_buttons_plugin import ButtonsClient
from discord_components import DiscordComponents
import datetime
import json
import random
import re as regex
from utils.utils import (
    convert_stream_dict_to_json_dict,
    convert_json_dict_to_stream_dict,
    convert_user_id,
    get_time_duration,
    has_se_pakka,
    has_word,
    has_cat,
    is_probable,
    is_a_gif,
)

# bot activity
activity = discord.Streaming(
    name="Watching Cute Kitten Videos",
    url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
)

# sets up client
client = commands.Bot(
    command_prefix=commands.when_mentioned_or("."),
    Intents=discord.Intents.all(),
    case_insensitive=True,
    activity=activity,
    status=discord.Status.dnd,
)

# buttons and slash commands
# buttons = ButtonsClient(client)
# slash = SlashCommand(client, sync_commands=True)

# loads data from a file
data = {}
with open("data.json") as f:
    data = json.load(f)

# data
OWNERID = int(data["owner_id"])
target = regex.compile(data["P-mc"])
fu_emoji = data["fu_emoji"]
my_man_emoji = data["my_man_emoji"]
varied_reactions = [fu_emoji, my_man_emoji]

load_dotenv()
client.vc_joining_time = {}
vc_leaving_time = {}
client.server_wise_vc_time_spent = {}
client.streaming_start_time = {}
client.streaming_duration = {}


# Bot events
@client.event
async def on_ready():
    # when bot starts
    await client.change_presence(
        activity=discord.Streaming(
            name="Watching Cute Kitten Video",
            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        )
    )
    client.load_extension("dch")
    DiscordComponents(client)

    # loads the required files
    with open("vctime.json") as f:
        temp_dict = json.load(f)
        convert_user_id(temp_dict, client.server_wise_vc_time_spent)

    with open("streamtime.json") as f:
        temp_stream_dict = json.load(f)
        convert_json_dict_to_stream_dict(temp_stream_dict, client.streaming_duration)

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[:-3]}")
            print(f"loaded {filename[:-3]}")
    print("We have successfully logged in as {0.user}".format(client))
    print(f"I'm in {str(len(client.guilds))} servers.")


@client.event
async def on_command_error(ctx, error):
    # on error
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please send all required arguments.")

    elif isinstance(error, commands.NSFWChannelRequired):
        embed = discord.Embed(
            title="Not an NSFW Channel",
            description="Pls use this command in an NSFW channel",
        )
        embed.set_image(
            url="https://media.tenor.com/images/427826c9f65604e63f7b13cdf155ec4c/tenor.gif"
        )

        embed.set_author(name=f"{ctx.author}")
        await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "You do not have the following permissions: ", error.missing_perms
        )

    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send(
            "Bot does not have the following permissions: ", error.missing_perms
        )

    elif isinstance(error, commands.CommandError):
        return

    else:
        raise error


@client.event
async def on_voice_state_update(member, before, after):
    # on changing user's voice state
    # i.e on joining or leaving voice channel

    if member.bot:
        return
    guild = member.guild
    server_id = str(guild.id)

    # initialising data
    if server_id not in client.vc_joining_time:
        client.vc_joining_time[server_id] = {}
    if server_id not in vc_leaving_time:
        vc_leaving_time[server_id] = {}
    if server_id not in client.server_wise_vc_time_spent:
        client.server_wise_vc_time_spent[server_id] = {}
    if server_id not in client.streaming_start_time:
        client.streaming_start_time[server_id] = {}
    if server_id not in client.streaming_duration:
        client.streaming_duration[server_id] = {}

    # adds roll to a user, when the user is connected to a voice channel
    rolename = "In a Voice Channel."
    found_roles = [role for role in guild.roles if role.name == rolename]
    if len(found_roles) == 0:
        found_roles.append(await guild.create_role(name=rolename))

    # user joined voice channel
    if before.channel is None and after.channel is not None:
        joining_time = datetime.datetime.now()
        client.vc_joining_time[server_id][member.id] = joining_time
        await member.add_roles(found_roles[0])

    # user left voice channel
    elif before.channel is not None and after.channel is None:
        leaving_time = datetime.datetime.now()
        vc_leaving_time[server_id][member.id] = leaving_time
        await member.remove_roles(found_roles[0])

    if (
        member.id in client.vc_joining_time[server_id].keys()
        and member.id in vc_leaving_time[server_id].keys()
    ):
        # when a user leaves the voice channel

        if (
            vc_leaving_time[server_id][member.id]
            < client.vc_joining_time[server_id][member.id]
        ):
            # if bot restarted, when user was in a voice connection
            vc_leaving_time[server_id].pop(member.id)
            return

        # gets the time duration of the user in the voice channel
        time_duration = get_time_duration(
            client.vc_joining_time[server_id][member.id],
            vc_leaving_time[server_id][member.id],
        )

        # updates the user's voice connection time
        if member.id in client.server_wise_vc_time_spent[server_id]:
            client.server_wise_vc_time_spent[server_id][member.id] += time_duration

        else:
            client.server_wise_vc_time_spent[server_id][member.id] = time_duration

        # writes the time in a file
        with open("vctime.json", "w") as f:
            json.dump(client.server_wise_vc_time_spent, f)

        # removes the member from joining and leaving dict
        client.vc_joining_time[server_id].pop(member.id)
        vc_leaving_time[server_id].pop(member.id)

    # user started streaming
    if before.self_stream is False and after.self_stream is True:
        starting_time = datetime.datetime.now()
        client.streaming_start_time[server_id][member.id] = starting_time

    # user ended streaming
    elif before.self_stream is True and (
        after.self_stream is False or after.channel is None
    ):
        if member.id not in client.streaming_start_time[server_id]:
            # bot restarted during stream
            return
        if member.id not in client.streaming_duration[server_id]:
            client.streaming_duration[server_id][member.id] = datetime.timedelta(
                days=0, seconds=0
            )

        # updates the user's stream time
        client.streaming_duration[server_id][member.id] += (
            datetime.datetime.now() - client.streaming_start_time[server_id][member.id]
        )

        # writes the stream time on a file
        with open("streamtime.json", "w") as f:
            json.dump(convert_stream_dict_to_json_dict(client.streaming_duration), f)

        client.streaming_start_time[server_id].pop(member.id)


@client.command()
async def load(ctx, extension):
    # command to load a particular cog
    # to be used only by the owner

    if ctx.author.id == OWNERID:
        if extension == "botmanage":
            await ctx.send("Base cog of the Bot is always loaded")
        else:
            client.load_extension(f"cogs.{extension}")
            await ctx.send(f"Successfully loaded {extension} cog!")

    else:
        await ctx.send("Command can only be used by Kitten Lord!")


@client.command()
async def unload(ctx, extension):
    # command to unload a particular cog
    # to be used only by the owner

    if ctx.author.id == OWNERID:
        if extension == "botmanage":
            await ctx.send("Base cog of the Bot cannot be unloaded")
        else:
            client.unload_extension(f"cogs.{extension}")
            await ctx.send(f"Successfully unloaded {extension} cog!")

    else:
        await ctx.send("Command can only be used by Kitten Lord!")


@client.command()
async def reload(ctx, extension):
    # command to reload a particular cog
    # to be used only by the owner

    if ctx.author.id == OWNERID:
        if extension == "botmanage":
            await ctx.send("Base cog of the Bot cannot be reloaded")
        else:
            client.unload_extension(f"cogs.{extension}")

        client.load_extension(f"cogs.{extension}")
        await ctx.send(f"Successfully reloaded {extension} cog!")

    else:
        await ctx.send("Command can only be used by Kitten Lord!")


@client.command()
async def cogs(ctx):
    # command to list all cogs
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            coglist = []
            coglist.append(filename)
            for cognames in coglist:
                cognamesfinal = cognames[:-3]
                x = []
                x.append(cognamesfinal)
                await ctx.send(f"Cog-{x}")


@client.command()
async def ping(ctx):
    # ping command
    await ctx.send(f"**Pong!** Latency : {round(client.latency * 1000)}ms")


@client.event
async def on_message(message):
    # bot event, triggers when someone writes a message

    # if message is by a bot, we ignore it
    if message.author == client.user or message.author.bot:
        return

    await client.process_commands(message)

    # react to message by a particular user
    if (
        message.author.id == int(data["sheshit"])
        and message.content.lower() == "no"
        and is_probable()
    ):
        no_u_reactions = ["🇳", "🇴", "🇺"]
        for emoji in no_u_reactions:
            await message.add_reaction(emoji)

    if (
        message.author.id == int(data["Tushar"])
        and has_word(message.content.lower(), target)
        and is_probable()
    ):
        await message.add_reaction("🤣")

    # react to message if it has some content
    if has_se_pakka(message.content) and is_probable():
        noc_rections = ["🇳", "🇴", "🇨"]
        for emoji in noc_rections:
            await message.add_reaction(emoji)

    # reacts to message sent by other bots
    if message.author.bot and message.author.id != data["bots"][0] and is_probable():
        r = random.choice(varied_reactions)
        await message.add_reaction(r)

    # reacts to messages which has a Cat GIF
    if has_cat(str(is_a_gif(message.content))) and is_probable():
        meow_reactions = ["🇲", "🇪", "🇴", "🇼"]
        for reaction in meow_reactions:
            await message.add_reaction(reaction)

    if message.guild is None:
        # DM messages to bot
        msg = message.content
        l = msg.split(";")

        # if user is not authorized, then they can't send notices
        if message.author.id not in data["authorized_users"] and l:
            await message.channel.send("Fancy seeing you here!")
            return

        # sends notice to server, sent to bot via DM
        if len(l) != 3:
            await message.channel.send(
                "Try sending message in this format `sender_name;destination;content`"
            )
        else:
            heading = f"{l[0]} just posted something on {l[1]}"
            msg_content = l[2]
            destination_channel = int(data["notice-channel"])

            embed = discord.Embed(
                title=heading, description=msg_content, color=discord.Color.random()
            )
            if message.attachments:
                embed.set_image(url=message.attachments[0].url)
            await client.get_channel(destination_channel).send(
                content="@everyone Can I have your attention please?", embed=embed
            )


client.run(os.environ["DISCORD_TOKEN"])
