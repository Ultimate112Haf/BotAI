import discord
from discord.ext import commands
import os, random
from get_model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            nama_file = file.filename
            url_file = file.url
            await file.save(f'./{nama_file}')
            await ctx.send(f'file telah disimpan {nama_file}')

            nama, skor = get_class(image=nama_file, model='keras_model.h5', label="labels.txt")
            #Baju Musim Dingin
            if nama == 'Beku\n' and skor >= 0.65:
                await ctx.send("itu adalah baju tebal")
                await ctx.send("Baju itu berwarna gelap dan cocok untuk suhu dingin")
                await ctx.send("Kalau keluar menggenakan itu, seharusnya kamu bisa")
                await ctx.send("Aman dari suhu dingin.")
            #Baju Musim Panas
            elif nama == 'sum\n' and skor >= 0.4:
                await ctx.send("baju itu tipis")
                await ctx.send("cocok untuk musim panas")
                await ctx.send("Tapi kalau diluar dingin, tolong pakai lapisan tambahan")
                await ctx.send("agar aman dari suhu dingin")
            else:
                await ctx.send("kurang jelas")    

                # memang agak random nama class nya, semoga ga masalah

    
    else:
        await ctx.send("tidak ada file terkirim")

bot.run("tokenGoesHere")

