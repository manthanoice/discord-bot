#importing necessary libraries
from fileinput import filename
import discord
import random
from hawww import *
from discord.ext import commands
from discord import FFmpegPCMAudio
import requests
import json
from googleapiclient.discovery import build
from colors import *
import os

#api key
api_key = os.environ.get('API_KEY')

#token of bot
TOKEN = os.environ.get('TOKEN')

#creating the bot object
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents = intents)

#making queues directory
queues = {}

#checking if the song is already in the queue :)
def check_queue(ctx, id):
    if queues[id]!=[]:
        voice = ctx.guild.voice_client
        source = queues[id].pop(0)
        player = voice.play(source)

#bot event to make sure the bot is working proeprly
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

#first hello command :O🐝
@bot.command()
async def hello(ctx):
    x = random.randint(0, len(hehe)-1)
    y = random.randint(0, len(cutie)-1)
    some_color = random.randint(0, len(color)-1)
    embedVar = discord.Embed(title=f'You are my {cutie[y]}! :)', color=color[some_color])
    embedVar.add_field(name=f'Hello {hehe[x]}', value="Do a backflip!")
    await ctx.send(embed=embedVar)

#the command which will show pictures of cute doggos
@bot.command()
async def beautiful(ctx):
    num = random.randint(0, 196)
    num2 = random.randint(0, len(sheisbest)-1)
    file = discord.File(f"The doggos\{num}.jpg", filename=f"{num}.jpg")
    some_color = random.randint(0, len(color)-1)
    embed = discord.Embed(title=f"Look at this {sheisbest[num2]} doggo!", color=color[some_color])
    embed.set_image(url=f"attachment://{num}.jpg")
    embed.add_field(name=f"She is my doggo", value="I love theo!")
    await ctx.send(file=file, embed=embed)

#the command which will show pictures of a ___
@bot.command()
async def badhuman(ctx):
    badnum = random.randint(0, 191)
    file = discord.File(f"badhuman\{badnum}.jpg", filename=f"{badnum}.jpg")
    some_color = random.randint(0, len(color)-1)
    embed = discord.Embed(title=f"Henlo", color=color[some_color])
    embed.set_image(url=f"attachment://{badnum}.jpg")
    embed.add_field(name=f'Hehe', value="Not Hehe")
    await ctx.send(file=file, embed=embed)

#the command which will make our bot join voice channel
@bot.command(pass_context = True)
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        await ctx.send("NAMSUM joined the voice channel, NAMSUM is so happy, Thank you Human :)")
    else:
        await ctx.send("You are not even in voice channel human!")

#the command which will make our bot leave voice channel
@bot.command(pass_context = True)
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Hawww Humnan? You really made me leave the voice channel, NAMSUM is sed :(")
    else:
        await ctx.send("I am not even in voice channel Human!")

#the command which will play some random beatles songs :)
@bot.command(pass_context = True)
async def playbeatles(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        bnum = random.randint(1, 4)
        voice = await channel.connect()
        source = FFmpegPCMAudio(f"xhe beatles\{bnum}.mp3")
        player = voice.play(source)
    else:
        await ctx.send("I am not even in voice channel Human!")

#the command we will use to pause a perticular song that's playing right now
@bot.command(pass_context = True)
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild = ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Human there's nothing playing what you tryna pause")

#the command to resume the song we just paused ::
@bot.command(pass_context = True)
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild = ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Human the song is alreay playing, what you tryna resume?")

#the command to stop the song from playing
@bot.command(pass_context = True)
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild = ctx.guild)
    voice.stop()

#the command to play any song we want :)
@bot.command(pass_context = True)
async def play(ctx, arg):
    if(ctx.author.voice):
        voice = ctx.guild.voice_client
        source = FFmpegPCMAudio(f'hehe\{arg}'+'.mp3')
        player = voice.play(source, after = lambda x=None: check_queue(ctx, ctx.message.guild.id))
    else:
        await ctx.send("Human, use !join command first to let this cute NAMSUM in :(")

#let's add songs to queue hehe ;)
@bot.command(pass_context = True)
async def queue(ctx, arg):
    voice = ctx.guild.voice_client
    song = f'hehe\{arg}'+'.mp3'
    source = FFmpegPCMAudio(song)
    
    guild_id = ctx.message.guild.id
    if guild_id in queues:
        queues[guild_id].append(source)
    else:
        queues[guild_id] = [source]
    
    await ctx.send("Added to queue")

#some memes?
@bot.command(pass_context = True)
async def meme(ctx):
    #for memes
    response = requests.get(url="https://meme-api.herokuapp.com/gimme").text
    json_response = json.loads(response)
    meme_url = json_response["url"]
    meme_title = json_response["title"]
    some_color = random.randint(0, len(color)-1)
    embed1 = discord.Embed(title=f"{meme_title}", color=color[some_color])
    embed1.set_image(url=meme_url)
    await ctx.send(embed=embed1)

#some wholesome memes
@bot.command(pass_context = True)
async def search(ctx, search):
    ran = random.randint(0,9)
    resource = build("customsearch","v1",developerKey=api_key).cse()
    result = resource.list(q=f"{search}", cx="e37162fb62031607e", searchType="image").execute()
    url = result["items"][ran]["link"]
    embed1 = discord.Embed(title=f"Oh Human so you searched for {search} hehe :)")
    embed1.set_image(url=url)
    await ctx.send(embed=embed1)

#some random jokes
@bot.command(pass_context = True)
async def joke(ctx):
    url = "https://dad-jokes.p.rapidapi.com/random/joke"

    headers = {
        "X-RapidAPI-Key": os.environ.get('RAPID_API_KEY'),
        "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers).text

    final_text = json.loads(response)

    first_line = final_text["body"]

    hehe = first_line[0]["setup"]
    lmao = first_line[0]["punchline"]

    some_color = random.randint(0, len(color)-1)
    embedVar = discord.Embed(title=f'Something to make the human laugh :)', color=color[some_color])
    embedVar.add_field(name=f'{hehe}', value=f"{lmao}")
    await ctx.send(embed=embedVar)

#cute cats hehe 
@bot.command(pass_context = True)
async def cat(ctx):
    response = requests.get("https://api.thecatapi.com/v1/images/search").text
    final_text = json.loads(response)
    img = final_text[0]["url"]

    some_color = random.randint(0, len(color)-1)
    embed1 = discord.Embed(title=f"OMG Human look at this cute cat! NAMSUM will be happy if you're happy :)", color=color[some_color])

    embed1.set_image(url=img)
    embed1.add_field(name=f'You and cat both cute hehe', value="I appriciate you!")
    await ctx.send(embed=embed1)

#cute doggos hehe
@bot.command(pass_context = True)
async def dog(ctx):
    response = requests.get("https://dog.ceo/api/breeds/image/random").text
    final_text = json.loads(response)
    img = final_text["message"]
    some_color = random.randint(0, len(color)-1)
    embed1 = discord.Embed(title=f"OMG Human look at this cut doggo", color=color[some_color])
    embed1.set_image(url=img)
    embed1.add_field(name=f'One street dog we gonna adopt', value="doggos >>>>>")
    await ctx.send(embed=embed1)

#make the human simle
@bot.command(pass_context = True)
async def smile(ctx):
    the_num = random.randint(0, 119)
    file = discord.File(f"wholesome\{the_num}.jpg", filename=f"{the_num}.jpg")
    some_color = random.randint(0, len(color)-1)
    embed = discord.Embed(title=f"Hey human smile :D", color=color[some_color])
    embed.set_image(url=f"attachment://{the_num}.jpg")
    embed.add_field(name=f'I appriciate you', value="You're amazing :)")
    await ctx.send(file=file, embed=embed)

#owls 🦉
@bot.command(pass_context = True)
async def owl(ctx):
    owlnum = random.randint(0, 19)
    file = discord.File(f"owl\{owlnum}.jpg", filename=f"{owl}.jpg")
    some_color = random.randint(0, len(color)-1)
    embed = discord.Embed(title=f"Human can't wait to adopt an owl 🦉", color=color[some_color])
    embed.set_image(url=f"attachment://{owl}.jpg")
    embed.add_field(name=f'Owl are cuties', value="🦉🦉🦉🦉")
    await ctx.send(file=file, embed=embed)

#guess the number 🔢
@bot.command(pass_context = True)
async def guess(ctx):
    num = random.randint(1, 100)
    for i in range(0, 5):
        response = await bot.wait_for('message')
        guess = int(response.content)
        if guess > num:
            await ctx.send('bigger')
        elif guess < num:
            await ctx.send('smaller')
        elif guess == num:
            await ctx.send('true')

@bot.command()
async def guessnice(ctx):
    correct_number = random.randint(60, 70)
    numbers = await bot.wait_for('message')
    number = int(numbers.content)
    if correct_number == number == 69:
        embedVar = discord.Embed(title=f'Your Number Is {number}', color=0xFF0000)
        embedVar.add_field(name='You Picked The NICE Number! You Won', value="Hehe")
        await ctx.send(embed=embedVar)
    if number == correct_number and number != 69:
        embedVar = discord.Embed(title=f'Your Number Is {number}', color=0xFF0000)
        embedVar.add_field(name='You Picked The Correct Number!', value="Hehe")
        await ctx.send(embed=embedVar)
    else:
        embedVar = discord.Embed(title=f'Your Number Is {number}', color=0xFF0000)
        embedVar.add_field(name=f"Oopsie Human, You Picked The Wrong Number :( correct number was {correct_number}", value="Not hehe")
        await ctx.send(embed=embedVar)

#jUsT dOeS tHiS
@bot.command()
async def mock(ctx, *, msg):
    ans = ""
    for i in range(len(msg)):
        if i%2==0 and msg[i]!=" ":
            ans+=msg[i].lower()
        elif i%2!=0 and msg[i]!= " ":
            ans+=msg[i].upper()
        elif msg[i]==" ":
            ans+=" "
    await ctx.send(ans)

@bot.command()
async def hamster(ctx):
    num = random.randint(0, 51)
    file = discord.File(f"hamster\{num}.jpg", filename=f"{num}.jpg")
    some_color = random.randint(0, len(color)-1)
    embed = discord.Embed(title=f"Look at this cute little hamster!!", color=color[some_color])
    embed.set_image(url=f"attachment://{num}.jpg")
    embed.add_field(name=f"She/he's so cute", value="Cutereee")
    await ctx.send(file=file, embed=embed)

#to run our bot
bot.run(TOKEN)