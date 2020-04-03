import discord
from discord.ext import commands
from discord.ext.commands import Bot
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import urllib
import urllib.request
import platform
import logger
import os
import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import platform
import sys
import os
import random
import requests
import urllib.request
import json
import time
import pyowm
import datetime
import config
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import urllib
import urllib.request
import psutil
import aiohttp
from concurrent.futures._base import CancelledError
import glob

client = Bot(description='covid grapher', command_prefix='##')


@client.event
async def on_ready():
    print("Bot online!\n")
    print("Discord.py API version:", discord.__version__)
    print("Python version:", platform.python_version())
    print("Running on:", platform.system(), platform.release(), "(" + os.name + ")")
    print("Name : {}".format(client.user.name))
    print("Client ID : {}".format(client.user.id))
    print("Currently active on " + str(len(client.guilds)) + " server(s).\n")



@client.command()
async def covid(ctx, *, state):

    urllib.request.urlretrieve("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv", "C:/Users/alec/Desktop/states.csv")
    df = pd.read_csv("C:/Users/alec/Desktop/states.csv")
    df_va = df[ df['state'] == state ]

    df_va.plot(x='date', y='cases', label='Cases', linestyle='-', linewidth=4)
    plt.savefig('C:/Users/alec/Desktop/plot.png')
    await ctx.send(file=discord.File('C:/Users/alec/Desktop/plot.png'))


client.run('token')