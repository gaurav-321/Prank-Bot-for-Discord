import os
import random
import time
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='/')
abuse_list = []
abuse_chan = 1043168791187689473
started = False


async def abuse_func():
    global started
    a_channel = bot.get_channel(abuse_chan)
    while started:
        for ban_m in abuse_list:
            try:
                await ban_m.move_to(a_channel)
            except Exception as e:
                print(e)
                pass
        time.sleep(10)


@bot.command(name='abuse', help='Abuse user')
async def nine_nine(ctx, ban_m: discord.Member):
    global started
    abuse_list.append(ban_m) if ban_m not in abuse_list else None
    a_channel = bot.get_channel(abuse_chan)
    vc = await a_channel.connect()
    vc.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\ffmpeg.exe", source='abuse_2.mp3'))
    if not started:
        started = True
        asyncio.ensure_future(abuse_func())
    await ctx.send(f"He is getting abused")


@bot.command(name='stopabuse', help='stop Abuse user')
async def nine_nine(ctx, ban_m: discord.Member):
    abuse_list.remove(ban_m) if ban_m in abuse_list else None
    await ctx.send(f"Abuse Has Been Stopped")


bot.run(TOKEN)
