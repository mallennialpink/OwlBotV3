import os
import random
import interactions
import requests

response = requests.get("https://neo-owls.net/itemdata/cherry%20blossom%20garland")

print(response.json())

print(response.status_code)

response = requests.get("https://neo-owls.net/transactions/cherry%20blossom%20garland")

print(response.json())

# from dotenv import load_dotenv
# load_dotenv('.env')

# from nc_bot_sql import *

images = [
    'https://i.imgur.com/x6nMAnJ.png']


# token = os.getenv("DISCORD_TOKEN")

bot = interactions.Client(TOKEN_HERE)

@bot.event
async def on_ready():
    print("yeehaw")

@bot.command()
async def hello(ctx):
    test = interactions.Embed(
        title = "Hello,",
        description = "world!"
    )
    await ctx.send(embeds = test)

# @bot.command(
#     name = "report",
#     description = "Submit your trades to the database."
# )


@bot.command(
    name = "help",
    description = "View command info for OwlsBot."
)

async def help(ctx):
    help = interactions.Embed (
        title = 'Help',
        description = 
        """This bot helps record and display NC trade report data submitted by the community.
        Type `/` followed by a command (or find the command in the slash commands menu) to interact with the bot.

        \n\n
        **/report**\n
        ```\n Submit a trade report. You will be prompted to input what you sent and what you received.\n\n
        You may also choose to add a note to your report as well as record the date in YYYY-MM-DD format
        (if you do not input a date, the current date will be used).\n

        ```\n**/search**\n```
        \nSearch the database. You will be prompted to input the item which you wish to view trade reports for.\n
        """,
        color = 0xE5D8D9
    )
    help.set_thumbnail(url=random.choice(images))
                    
    await ctx.send(embeds=help)



bot.start()