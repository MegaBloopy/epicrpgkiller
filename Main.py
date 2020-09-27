class SELFBOT():
    __linecount__ = 1
    __version__ = 0.1

import discord, time, colorama, random, numpy, ctypes, os, sys, subprocess, datetime, requests
import asyncio, json, smtplib

from discord.ext import commands, tasks
from itertools import cycle
from colorama import Fore
from PIL import Image

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')

loop = asyncio.get_event_loop()

def startprint():
    print(f'''{Fore.RESET}
                        _____   ______   _        ______   ____     ____    _______
                       / ____| |  ____| | |      |  ____| |  _ \   / __ \  |__   __|
                      | (___   | |__    | |      | |__    | |_) | | |  | |    | |
                       \___ \  |  __|   | |      |  __|   |  _ <  | |  | |    | |
                       ____) | | |____  | |____  | |      | |_) | | |__| |    | |
                      |_____/  |______| |______| |_|      |____/   \____/     |_|


                       {Fore.CYAN}EPIC-RPG {SELFBOT.__version__} | {Fore.GREEN}Logged in as: {Epicself.user.name}#{Epicself.user.discriminator} {Fore.CYAN}| ID: {Fore.GREEN}{Epicself.user.id}
                       {Fore.CYAN}Prefix: {Fore.GREEN}{prefix}
    '''+Fore.RESET)

def Clear():
    os.system('cls')
Clear()

def Init():
    if config.get('token') == "token-here":
        Clear()
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your token in the config.json file"+Fore.RESET)
    else:
        token = config.get('token')
        try:
            Epicself.run(token, bot=False, reconnect=True)
            os.system(f'title (EPIC-RPG Selfbot) - Version {SELFBOT.__version__}')
        except discord.errors.LoginFailure:
            print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed"+Fore.RESET)
            os.system('pause >NUL')

colorama.init()
Epicself = discord.Client()
Epicself = commands.Bot(command_prefix=prefix, self_bot=True)
Epicself.remove_command('help')

arenas, bosses, logs, fish, coins = 0, 0, 0, 0, 0
@Epicself.event
async def on_message(message):
    if message.author.id == 555955826880413696:
        global arenas, bosses, logs, fish, coins
        if len(message.embeds) != 0:
            if message.embeds[0].fields:
                if r"Get <:arenacookie:589286303087067156> arena cookies for each player you kill!\nOwners of the event will get an extra reward" in str(message.embeds[0].fields):
                    await asyncio.sleep(3.1)
                    await message.channel.send("join")
                    arenas += 1
                    sys.stdout.write(f"EVENTS: Arenas: {arenas} || Bosses: {bosses} || Logs: {logs} || Fish: {fish} || Coins: {coins}\r\r")
                elif r"**AN EPIC TREE HAS JUST GROWN <:woodenlog:555047053441630209> - HEIGHT:" in str(message.embeds[0].fields):
                    await asyncio.sleep(3.1)
                    await message.channel.send("chop")
                    logs += 1
                    sys.stdout.write(f"EVENTS: Arenas: {arenas} || Bosses: {bosses} || Logs: {logs} || Fish: {fish} || Coins: {coins}\r")
                elif r"Type **CATCH** (once) to collect" in str(message.embeds[0].fields):
                    await asyncio.sleep(3.0)
                    await message.channel.send("catch")
                    coins += 1
                    sys.stdout.write(f"EVENTS: Arenas: {arenas} || Bosses: {bosses} || Logs: {logs} || Fish: {fish} || Coins: {coins}\r")
                elif r"Type **FISH** (once) to collect" in str(message.embeds[0].fields):
                    await asyncio.sleep(2.8)
                    await message.channel.send("fish")
                    fish += 1
                    sys.stdout.write(f"EVENTS: Arenas: {arenas} || Bosses: {bosses} || Logs: {logs} || Fish: {fish} || Coins: {coins}\r")
                elif r"Type **TIME TO FIGHT** (once) to join the battle" in str(message.embeds[0].fields):
                    await asyncio.sleep(2.1)
                    await message.channel.send("Time to fight")
                    sys.stdout.write(f"\rEVENTS: Arenas: {arenas} || Bosses: {bosses} || Logs: {logs} || Fish: {fish} || Coins: {coins}\r")
    if message.author.id == 555955826880413696 and f'**{Epicself.user.name}** is training in the field' in message.content:
        numberdict = {"first" : 0, "second" : 1, "third" : 2, "fourth" : 3, "fifth" : 4, "sixth" : 5}
        numberword = message.content.split("**")[3]
        emojiword = message.content.split(":")[1]
        number = numberdict[numberword]
        await asyncio.sleep(1.2)
        await message.channel.send(str(emojiword[number]))
    if message.author.id == 555955826880413696 and f'**{Epicself.user.name}** is training in the river' in message.content:
        worddict = {"normiefish" : "1", "goldenfish" : "2", "EPICfish" : "3"}
        emojiword = message.content.split(":")[1]
        await asyncio.sleep(1.2)
        await message.channel.send(worddict[emojiword])
    if message.author.id == 555955826880413696 and f'**{Epicself.user.name}** got a' in message.content and 'lootbox' in message.content:
        await asyncio.sleep(2)
        await message.channel.send("rpg open")
    if message.author.id == 555955826880413696 and f'**{Epicself.user.name}** is training in the mine' in message.content:
        await asyncio.sleep(1.2)
        await message.channel.send("no")
    if 'you are in the jail' in message.content and Epicself.user.mention in message.mentions:
        global rpgcheck
        rpgcheck = 1
    await Epicself.process_commands(message)

@Epicself.event
async def on_connect():
    Clear()
    startprint()

checkhealvar = 25
axecheck, checkheal = 0, 0
checkadv = 0
async def rpghunt():
    global rpgcheck, checkheal, axecheck, checkadv, checkhealvar
    channel = Epicself.get_channel(756710779767488564)
    if rpgcheck == 0:
        axecheck += 1
        checkheal += 1
        checkadv += 1
        if checkadv == 61:
            await asyncio.sleep(1.2)
            await channel.send("rpg adventure")
            await asyncio.sleep(1.2)
            await channel.send("rpg heal")
            await asyncio.sleep(1.2)
        if axecheck == 5:
            await channel.send("rpg chainsaw")
            axecheck = 0
            await asyncio.sleep(1.2)
        await channel.send("rpg hunt")
        await asyncio.sleep(1.4)
        if checkheal >= checkhealvar:
            checkheal = 0
            await channel.send("rpg heal")
        await asyncio.sleep(random.randint(61, 63))
        await rpghunt()


@Epicself.command()
async def rpgstart(ctx):
    global rpgcheck
    await ctx.message.delete()
    rpgcheck = 0
    await rpghunt()

@Epicself.command()
async def rpgstop(ctx):
    global rpgcheck
    await ctx.message.delete()
    rpgcheck = 1


if __name__ == '__main__':
    Init()
