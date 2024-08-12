# @client.command()
# async def load(ctx, extension):
#     client.load_extension(f'cogs.{extension}')


# @client.command()
# async def unload(ctx, extension):
#     client.unload_extension(f'cogs.{extension}')

# for filename in os.listdir('./cogs'):
#     if filename.endswith('.py'):
#         client.load_extension(f'cogs.{filename[:-3]}')


# @client.slash_command()
# async def hi(ctx):
#     await ctx.respond("waow slesh cmd")

# @client.command()
# async def form(ctx):
#     await ctx.send(
#         "Join The Kitten Ketvolution",
#         components=[
#             Button(label="This is a Button", custom_id="button2")
#         ]
#     )
#     interaction = await client.wait_for("button_click", check=lambda i: i.custom_id == "button2")

#     await interaction.send(content=f"https://www.theraleighregister.com/join-the-kitten-amry.html")


# @client.command()
# async def button(ctx):
#     await ctx.send("Button Test",
#                    components=[
#                        Button(label="Click", custom_id="button1")
#                    ]
#                    )

#     interaction = await client.wait_for("button_click", check=lambda i: i.custom_id == "button1")

#     await interaction.send(content="https://c.tenor.com/uhnVFBgGehUAAAAC/rick-astley-dancing.gif")

# @client.command(pass_context=True)
# async def pause(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     if voice.is_playing():
#         voice.pause()
#     else:
#         await ctx.send("Bc kuch play hi ni karra kya pause karu.")


# @client.command(pass_context=True)
# async def resume(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     if voice.is_paused():
#         voice.pause()
#     else:
#         await ctx.send("Resume karne ke liye song pause hona chaiye. nub")


# @client.command(pass_context=True)
# async def stop(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     voice.stop()

# @client.command(pass_context=True)
# async def queue(ctx, arg):
#     voice = ctx.guild.voice_client
#     source = FFmpegPCMAudio(arg)

#     guild_id = ctx.message.guild.id

#     if guild_id in queues:
#         queues[guild_id].append(source)

#     else:
#         queues[guild_id] = source

#     await ctx.send("Added to queue")

# @commands.command(pass_context=True)
# async def play(ctx, url):
#     server = ctx.message.server
#     voice_client = client.voice_client_in(server)
#     player = await voice_client.create_ytdl_player(url)
#     players[server.id] = player
#     player.start()
#     # async def play(ctx, arg):
#     #     voice = ctx.guild.voice_client
#     #     source = FFmpegPCMAudio(arg)
#     #     player = voice.play(source)


# import random
# def r(): return random.randint(0, 255)


# print('#%02X%02X%02X' % (r(), r(), r()))

# from googletrans import Translator

# translator = Translator()

# n = input('Enter text: ')

# translated = translator.translate(n)

# res = translated.text

# print(res)


# https://discord.com/api/oauth2/authorize?client_id=880434967547633734&permissions=8&scope=bot%20applications.commands

# from datetime import date

# today = date.today()

# print(today)


# from datetime import date, datetime, timedelta
# from collections import namedtuple

# Entry = namedtuple('Entry', 'name birthdate')
# bday_list: list[Entry] = [
#     Entry("Kataria", date(2002, 8, 23)),
#     Entry("Varun", date(2001, 3, 22)),
#     Entry("Shashwat", date(2001, 12, 27)),
#     Entry("Rushikesh", date(2002, 5, 28)),
#     Entry("Sarvesh", date(2002, 6, 1)),
#     Entry("Shreyas", date(2002, 5, 10)),
#     Entry("Tushar", date(2002, 7, 19)),
#     Entry("Shrikant", date(2002, 10, 14)),
#     Entry("Tanay", date(2002, 11, 8)),
#     Entry("Ishpreet", date(2000, 5, 15)),
#     Entry("Rohit", date(2004, 1, 10)),
#     Entry("Jayant", date(2001, 8, 5)),
#     Entry("Mannan", date(2001, 8, 11)),
# ]

# today = datetime.today().date()

# for entry in bday_list:
#     if entry.birthdate.month == today.month and entry.birthdate.day == today.day:
#         print(f'Happy birthday {entry.name}')


# def comparator(entry: Entry):
#     birthday = entry.birthdate
#     today = datetime.today().date()

#     this_year = date(today.year, birthday.month, birthday.day)
#     if this_year - today >= timedelta(seconds=0):
#         return this_year - today
#     else:
#         return date(today.year+1, birthday.month, birthday.day) - today


# bday_list.sort(key=comparator)
# print(bday_list)


# import re
# from datetime import date
# bday_list = [("Kataria", date(2002, 8, 23)),
#              ("Varun", date(2001, 3, 22)),
#              ("Shashwat", date(2001, 12, 27)),
#              ("Rushikesh", date(2002, 5, 28)),
#              ("Sarvesh", date(2002, 6, 11)),
#              ("Shreyas", date(2002, 5, 10)),
#              ("Tushar", date(2002, 7, 19)),
#              ("Shrikant", date(2002, 10, 14)),
#              ("Tanay", date(2002, 11, 8)),
#              ("Ishpreet", date(2000, 5, 15)),
#              ("Rohit", date(2004, 1, 10)),
#              ("Jayant", date(2001, 8, 5)),
#              ("Mannan", date(2001, 8, 11))]

# today_day = date.today().day
# today_month = date.today().month
# today_year = int(date.today().year)
# for birthday in bday_list:
#     if(today_day == birthday[1].day and today_month == birthday[1].month):
#         print(
#             f"Wishing {birthday[0]} a very happy birthday!! Hope turning {today_year-birthday[1].year} isn't a big deal")

# print("Upcoming birthdays: ")
# bday_list_sorted_daywise = sorted(bday_list, key=lambda tup: tup[1].day)
# bday_list_sorted_monthwise = sorted(
#     bday_list_sorted_daywise, key=lambda tup: tup[1].month)


# def date_extractor(message):
#     a = re.search(r'(\d?\d)-(\d?\d)-(\d{4})', message)
#     bday_month = a.group(2)
#     bday_day = a.group(1)
#     bday_year = a.group(3)
#     birthday = date(int(bday_year), int(bday_month), int(bday_day))
#     return birthday


# upcoming_bdays = []
# break_point = 0
# for i in range(len(bday_list_sorted_monthwise)):
#     if((bday_list_sorted_monthwise[i][1].month > today_month) or (bday_list_sorted_monthwise[i][1].month == today_month and bday_list_sorted_monthwise[i][1].day >= today_day)):
#         break_point = i
#         break

# for j in range(break_point, len(bday_list_sorted_monthwise)):
#     upcoming_bdays.append(
#         (bday_list_sorted_monthwise[j][0], bday_list_sorted_monthwise[j][1].day, bday_list_sorted_monthwise[j][1].month, today_year))

# for j in range(break_point):
#     upcoming_bdays.append(
#         (bday_list_sorted_monthwise[j][0], bday_list_sorted_monthwise[j][1].day, bday_list_sorted_monthwise[j][1].month, today_year+1))

# for j in upcoming_bdays:
#     print(j)

# message = input("Enter command: ")
# birthday_date = date_extractor(message)
# print(f"Birthday day extracted is {birthday_date}")
# print(f'Birthday Month {birthday_date.month}')
