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
import sys
import random
import requests
import json
import time
import pyowm
import datetime
import config
import psutil
import aiohttp
from concurrent.futures._base import CancelledError
import glob

client = Bot(description='covid grapher', command_prefix='#')
filename_state = "/home/pi/not/alcebot/states.csv"
filename_county = "/home/pi/not/alcebot/counties.csv"
county_graph = '/home/pi/not/alcebot/plot-county.png'
state_graph = '/home/pi/not/alcebot/plot-state.png'

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
async def covid(ctx, type, *, state):
    
    if(type == "state"):

        if (not os.path.exists(filename_state) or file_age_in_seconds(filename_state) > 3600):
            urllib.request.urlretrieve("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv", filename_state)

        df = pd.read_csv(filename_state)
        df_state = df[ df['state'] == state ]
        df_state.plot(x='date', y=['cases', 'deaths'], label=['Cases', 'Deaths'], linestyle='-', linewidth=4)
        plt.savefig(state_graph)
        await ctx.send(file=discord.File(state_graph))


    if(type == "county"):

        if (not os.path.exists(filename_county) or file_age_in_seconds(filename_county) > 3600):
            urllib.request.urlretrieve("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv", filename_county)
        df = pd.read_csv(filename_county)
        df_county = df[ df['county'] == state ]
        df_county.plot(x='date', y=['cases', 'deaths'], label=['Cases', 'Deaths'], linestyle='-', linewidth=4)
        plt.savefig(county_graph)
        await ctx.send(file=discord.File(county_graph))


client.run('token')
