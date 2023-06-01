TOKENHERE = str(input("Enter your token key: "))
APPID = int(input("Enter your appid: "))
imagekey2 = str(input("Enter your large image key: "))
imagetext2 = str(input("Enter your large image name: "))
imagekey0 = str(input("Enter your small image key: "))
imagetext0 = str(input("Enter your small image name: "))


# do not modify / edit the rest of this if you have little to no python / discord.py knowledge

import os 
import time
import sys
os.system("clear")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(f"{bcolors.WARNING}DISCORD RPC{bcolors.ENDC}")
print(f"{bcolors.WARNING}Version 1.5{bcolors.ENDC} - Discord_RPC")
time.sleep(1.5)
print(f"{bcolors.UNDERLINE}                           {bcolors.ENDC}")
print("")
print(f"{bcolors.OKBLUE}Importing required modules{bcolors.ENDC}")
print(f"{bcolors.UNDERLINE}                           {bcolors.ENDC}")
print("")
time.sleep(2.0)
print ("\033[A                             \033[A")
print ("\033[A                             \033[A")
print ("\033[A                             \033[A")
print ("\033[A                             \033[A")
print(f"{bcolors.OKBLUE}Import Complete{bcolors.ENDC}")
print("")

# importing required packages
import datetime
import discord
import asyncio
from discord.ext import commands
import threading
from threading import Thread
# Customize Here

imagekey1 = imagekey2 + "?size=480#"
imagekey3 = imagekey0 + "?size=480#"
presentDate = datetime.datetime.now() 
unix_timestamp = datetime.datetime.timestamp(presentDate)*1000

entercmd = 'na'
prefix = '!!'
client = discord.Client()
name1 = input("Enter the app name: ")
print("")
detail1 = input("App Details: ")
print("")
print("State:")
state1 = input("[type n to turn off]: ")
print("")
print("Elapsed Time")
elapsed1 = input("[type n to turn off]: ")
print("")
print(f"{bcolors.WARNING}[BETA]{bcolors.ENDC} Status Type")
print("W for Watching")
print("S for Streaming")
print("L for Listening")
print(f"{bcolors.BOLD}NOTE:{bcolors.ENDC} Playing type is the most stable, other options will probably not support Image")
type1 = input("[skip for Playing Type]: ")

if type1.lower() == "w":
    type1 = discord.ActivityType.watching
elif type1.lower() == "s":
    type1 = discord.ActivityType.streaming
elif type1.lower() == "l":
    type1 = discord.ActivityType.listening
else :
    type1 = discord.ActivityType.playing
    
#Preparing prefix

bot = commands.Bot(command_prefix=prefix, self_bot=True)
yeselapsed = bot.change_presence(activity=discord.Activity(application_id=APPID, name=name1, type=type1, state=state1, details=detail1, assets={'large_image' : imagekey1, 'large_text' : imagetext2, 'small_image' : imagekey3, 'small_text' : imagetext0}, timestamps={'start' : unix_timestamp}))
noelapsed = bot.change_presence(activity=discord.Activity(application_id=APPID, name=name1, type=type1, state=state1, details=detail1, assets={'large_image' : imagekey1, 'large_text' : 'The Roooook', 'small_image' : imagekey3, 'small_text' : imagetext0}))
noelapsednostate = bot.change_presence(activity=discord.Activity(application_id=APPID, name=name1, type=type1, details=detail1, assets={'large_image' : imagekey1, 'large_text' : imagetext2, 'small_image' : imagekey3, 'small_text' : imagetext0}))
yeselapsednostate = bot.change_presence(activity=discord.Activity(application_id=APPID, name=name1, type=type1, details=detail1, assets={'large_image' : imagekey1, 'large_text' : imagetext2, 'small_image' : imagekey3, 'small_text' : imagetext0}, timestamps={'start' : unix_timestamp}))

user_input = "not available"

#This is still ongoing, just cant find the way how to do it im noob
class Script2:
    def awesome():
        user_input = input("Discord CMD-")
        if user_input.lower() == "end":
            exit()
            os.system("clear")
            print("script will end")
        elif user_input.lower() == "reset":
            os.execv(sys.executable, ['python'] + sys.argv)
        elif user_input.lower() == "help":
            print("Type End to end the script")
            print("Type Reset to restart the script")
            print("More commands in the future")
            sc1.awesome()
        else :
            print("Unknown Command. Please type Help for more info.")
            sc1.awesome()
#sc1 = Script2()



@bot.event 
async def on_ready():
    print(f"{bcolors.UNDERLINE}                           {bcolors.ENDC}")
    print("")
    print(f"Logged in as {bcolors.OKGREEN}{bot.user.name}! {bcolors.ENDC}")
    print(f"{bcolors.FAIL}Do not share your token")
    print(f"with anyone else!{bcolors.ENDC}")
    time.sleep(1.5)
    print("")
    if elapsed1 == "n" :
        if state1 == "n" :
            await noelapsednostate
        else :
            await noelapsed
    else :
        if state1 == "n" :
            await yeselapsednostate
        else:
            await yeselapsed
    print(f"{bcolors.OKBLUE}Custom Status applied{bcolors.ENDC}")
    print(f"{bcolors.UNDERLINE}                           {bcolors.ENDC}")
    print("")
    print("Press CTRL + C to end the custom status")
    
bot.run(TOKENHERE, bot = False)
