import os
import json
import asyncio
import random
from random import randint
#discord
import discord
from discord.ext import commands
#keep awake
from keep_awake import keep_awake

bot = commands.Bot(command_prefix='~')
bot.remove_command('help')

#update and add hearts in user_hearts.json
async def update_hearts(user_hearts, user):
  if not f'{user.id}' in user_hearts:
    user_hearts[f'{user.id}'] = {}
    user_hearts[f'{user.id}']['hearts'] = 0
async def add_hearts(user_hearts, user, hearts):
  user_hearts[f'{user.id}']['hearts'] += hearts   

#dummy thicc maths for sauce
def randomN(n):
  range_start = 10**(n-1)
  range_end = (10**n)-1
  return randint(range_start, range_end)

##Events
@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name="~help"))
  print('Ready')

##creater
@bot.command()
async def creater(ctx):
  messages = ["`Rim#0003`"]
  await ctx.reply(random.choice(messages), mention_author=False)

##Interactions
@bot.command()
async def yo(ctx):
  messages = ["Yo <:ShizueEmbarrassedTears:850973942650765332>", "Yoo <:ShizueEmbarrassedTears:850973942650765332>"]
  await ctx.reply(random.choice(messages), mention_author=False)
@bot.command()
async def hi(ctx):
  messages = ["hii <:ShizueEmbarrassedTears:850973942650765332>", "hewoo <:ShizueEmbarrassedTears:850973942650765332>", "heyy <:ShizueEmbarrassedTears:850973942650765332>", "aa..aa.. shuna and shion making me wear bunny costume again.. <:ShizueEmbarrassedTears:850973942650765332>"]
  await ctx.reply(random.choice(messages), mention_author=False)
@bot.command()
async def hello(ctx):
  messages = ["hii <:ShizueEmbarrassedTears:850973942650765332>", "hewoo <:ShizueEmbarrassedTears:850973942650765332>", "heyy <:ShizueEmbarrassedTears:850973942650765332>", "aa..aa.. shuna and shion making me wear bunny costume again.. <:ShizueEmbarrassedTears:850973942650765332>"]
  await ctx.reply(random.choice(messages), mention_author=False) 
@bot.command()
async def hey(ctx):
  messages = ["hii <:ShizueEmbarrassedTears:850973942650765332>", "hewoo <:ShizueEmbarrassedTears:850973942650765332>", "heyy <:ShizueEmbarrassedTears:850973942650765332>", "aa..aa.. shuna and shion making me wear bunny costume again.. <:ShizueEmbarrassedTears:850973942650765332>"]
  await ctx.reply(random.choice(messages), mention_author=False)       
@bot.command()
async def goodnight(ctx):
  messages = ["good night <:ShizueEmbarrassedTears:850973942650765332>", "night <:ShizueEmbarrassedTears:850973942650765332>"]
  await ctx.reply(random.choice(messages), mention_author=False)
@bot.command()
async def goodmorning(ctx):
  messages = ["good morning <:ShizueEmbarrassedTears:850973942650765332>", "morning <:ShizueEmbarrassedTears:850973942650765332>"]
  await ctx.reply(random.choice(messages), mention_author=False)  
@bot.command()
async def badslime(ctx):
  messages = ["<:ShizueEmbarrassedTears:850973942650765332>", "nuu.. i am not a bad slime <:ShizueEmbarrassedTears:850973942650765332>"]
  await ctx.reply(random.choice(messages), mention_author=False)  
@bot.command()
async def goodslime(ctx):
  messages = ["<:ShizueEmbarrassedTears:850973942650765332>", "<:ShizueEmbarrassedTears:850973942650765332>"]
  await ctx.reply(random.choice(messages), mention_author=False)                      
@bot.command()
async def rimuru(ctx):
  messages = ["Yes <:ShizueEmbarrassedTears:850973942650765332>", "? <:ShizueEmbarrassedTears:850973942650765332>",]
  await ctx.reply(random.choice(messages), mention_author=False) 
@bot.command()
async def bye(ctx):
  messages = ["nuu.. dont go <:ShizueEmbarrassedTears:850973942650765332>", "ahh.. come back soon <:ShizueEmbarrassedTears:850973942650765332>", "bye bye <:ShizueEmbarrassedTears:850973942650765332>", "byee <:ShizueEmbarrassedTears:850973942650765332>"]
  await ctx.reply(random.choice(messages), mention_author=False)      

##fun
#todo
@bot.command()
async def todo(ctx):
  messages = [":umbrella: mm.. make it rain!! <:ShizueEmbarrassedTears:850973942650765332>", ":snowman2: woo.. make a snowman!! <:ShizueEmbarrassedTears:850973942650765332>", ":fork_knife_plate: get something to eat!! <:ShizueEmbarrassedTears:850973942650765332>", ":soap: cleaning? <:ShizueEmbarrassedTears:850973942650765332>", ":beach: lets go to a beach!! <:ShizueEmbarrassedTears:850973942650765332>", ":bubble_tea: get something to drink!! <:ShizueEmbarrassedTears:850973942650765332>", ":island: lets go to some island!! <:ShizueEmbarrassedTears:850973942650765332>", ":video_game: wanna play some games with me!! <:ShizueEmbarrassedTears:850973942650765332>", ":yarn: just sleep.. <:ShizueEmbarrassedTears:850973942650765332>", ":bowling: lets go bowling!! <:ShizueEmbarrassedTears:850973942650765332>", ":microphone: sing something!! <:ShizueEmbarrassedTears:850973942650765332>", ":golf: lets go golfing!! <:ShizueEmbarrassedTears:850973942650765332>", ":rainbow: woo.. make a rainbow!! <:ShizueEmbarrassedTears:850973942650765332>", ":boxing_glove: boing!! foof..ffof.. <:ShizueEmbarrassedTears:850973942650765332>"]
  await ctx.reply(random.choice(messages), mention_author=False) 

#tierlist
@bot.command()
async def tierlist(ctx):
  embed=discord.Embed(color=discord.Color.blue()) 
  embed.set_image(url="https://i.imgur.com/kHH1AKB.png")     
  await ctx.reply(embed=embed, mention_author=False) 

##profile
#simp
@bot.command()
async def simp(ctx):   
  boo = ["💙", "💜", "💚", "❤️", "🧡"]
  embed=discord.Embed(title=random.choice(boo), color=discord.Color.blue()) 
  await ctx.reply(embed=embed, mention_author=False) 
#hearts   
  with open('user_hearts.json', 'r') as f:
    user_hearts = json.load(f)
  await update_hearts(user_hearts, ctx.author)
  await add_hearts(user_hearts, ctx.author, 1)
  with open('user_hearts.json', 'w') as f:
    json.dump(user_hearts, f)      

#hearts
@bot.command()
async def hearts(ctx):   
  with open('user_hearts.json', 'r') as f:
    user_hearts = json.load(f)
    authorID = ctx.author.id     
    hearts = user_hearts[str(authorID)]['hearts']  
    embed = discord.Embed(color=discord.Color.blue())
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)  
    embed.add_field(name="hearts earned <:ShizueEmbarrassedTears:850973942650765332> :", value= hearts, inline=True) 
    await ctx.reply(embed=embed, mention_author=False) 

#avatar    
@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member=None):
  if not user:
    embed = discord.Embed(color=discord.Color.blue())
    embed.set_image(url=ctx.message.author.avatar_url) 
    await ctx.reply(embed=embed, mention_author=False)
  else:
    embed = discord.Embed(color=discord.Color.blue())
    embed.set_image(url=user.avatar_url)
    await ctx.reply(embed=embed, mention_author=False)

##roleplay
#nickname
@bot.command()
async def nickname(ctx):    
  nicknames = ["Acheron", "Adbeel", "Azazel", "Belial", "Buer", "Charon", "Dagon", "Damien", "Eligor", "Forneus", "Gresill", "Helel", "Iblis", "Lestat", "Leviatha", "Lucifer", "Malacoda", "Naberius", "Orobas", "Radna", "Samael", "Sedit", "Seth", "Ubel", "Zagan", "Achlys", "Akeldama", "Carmen", "Carmilla", "Claudia", "Enyo", "Gello", "Hel", "Lilin", "Mare", "Mircalla", "Pandora", "Puck", "Selene"]
  await ctx.author.edit(nick=(random.choice(nicknames)))
  await ctx.message.add_reaction('✅')          

#sing  
@bot.command()
async def sing(ctx):    
  vc = ctx.author.voice   
  if vc:
    await vc.channel.connect() 
    await ctx.message.add_reaction('✅')        
  if vc is None:
    await ctx.message.add_reaction('❌')  
    embed=discord.Embed(description="You have to be in a voice channel first!!", color=discord.Color.blue()) 
    await ctx.send(embed=embed, mention_author=False)                   
  guild = ctx.guild
  voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)    
  audio_source = discord.FFmpegPCMAudio('https://mp3.fastupload.co/data/1622193194/rimuru.mp3')
  if not voice_client.is_playing():
    voice_client.play(audio_source, after=None)    
  await asyncio.sleep(90)                                       
  await voice_client.disconnect()   

#shizue
@bot.command()
async def shizue(ctx): 
  messages = ["i..i.. like Rimuru-sama <:ShizueEmbarrassedTears:850973942650765332> ~aa"]
  await ctx.reply(random.choice(messages), mention_author=False)        

##actions
@bot.command(pass_context=True)
async def cuddle(ctx, otaku: discord.Member=None): 
  if not otaku:
    await ctx.message.add_reaction('❌') 
    embed = discord.Embed(description="tag @someone", color=discord.Color.blue())      
    await ctx.send(embed=embed, mention_author=False)
  else:
    gif = ["https://i.imgur.com/zEpEFdR.gif", "https://i.imgur.com/0vMxXPD.gif", "https://i.imgur.com/BBltNs5.gif", "https://i.imgur.com/AbwGSGe.gif"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_author(name="{0} cuddles {1}!! aww!!".format(ctx.message.author.name, otaku.name), icon_url=ctx.author.avatar_url)  
    embed.set_image(url=random.choice(gif))       
    await ctx.send(embed=embed, mention_author=False) 
  
@bot.command(pass_context=True)
async def hug(ctx, otaku: discord.Member=None): 
  if not otaku:
    await ctx.message.add_reaction('❌') 
    embed = discord.Embed(description="tag @someone", color=discord.Color.blue())          
    await ctx.send(embed=embed, mention_author=False)
  else:  
    gif = ["https://i.imgur.com/BLWNnFl.gif", "https://i.imgur.com/ZNexQYs.gif", "https://i.imgur.com/AmW4JXv.gif", "https://i.imgur.com/jPI7d39.gif"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_author(name="{0} huggs {1}!! aa!!".format(ctx.message.author.name, otaku.name), icon_url=ctx.author.avatar_url)      
    embed.set_image(url=random.choice(gif))       
    await ctx.send(embed=embed, mention_author=False)
@bot.command(pass_context=True)
async def pat(ctx, otaku: discord.Member=None): 
  if not otaku:
    await ctx.message.add_reaction('❌') 
    embed = discord.Embed(description="tag @someone", color=discord.Color.blue())          
    await ctx.send(embed=embed, mention_author=False)
  else:  
    gif = ["https://i.imgur.com/jalh0TO.gif", "https://i.imgur.com/jyGKbIt.gif", "https://i.imgur.com/waDgdYE.gif", "https://i.imgur.com/y8hzJj3.gif", "https://i.imgur.com/WnWbaBI.gif", "https://i.imgur.com/MzaOifc.gif", "https://i.imgur.com/twu1Elb.gif", "https://i.imgur.com/XShvBry.gif", "https://i.imgur.com/DwcgM7X.gif", "https://i.imgur.com/wXfqvwZ.gif", "https://i.imgur.com/M6whfdx.gif"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_author(name="{0} pats {1}!! pat..pat!!".format(ctx.message.author.name, otaku.name), icon_url=ctx.author.avatar_url)   
    embed.set_image(url=random.choice(gif))       
    await ctx.send(embed=embed, mention_author=False)
@bot.command(pass_context=True)
async def kiss(ctx, otaku: discord.Member=None): 
  if not otaku:
    await ctx.message.add_reaction('❌') 
    embed = discord.Embed(description="tag @someone", color=discord.Color.blue())         
    await ctx.send(embed=embed, mention_author=False)
  else:  
    gif = ["https://i.imgur.com/GDti9sg.gif", "https://i.imgur.com/pFboGNv.gif", "https://i.imgur.com/tTNi2ny.gif", "https://i.imgur.com/FQB8F7f.gif", "https://i.imgur.com/CCOE8cJ.gif"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_author(name="{0} kisses {1}!! chuu!!".format(ctx.message.author.name, otaku.name), icon_url=ctx.author.avatar_url)   
    embed.set_image(url=random.choice(gif))       
    await ctx.send(embed=embed, mention_author=False)
@bot.command(pass_context=True)
async def lick(ctx, otaku: discord.Member=None):
  if not otaku:
    await ctx.message.add_reaction('❌') 
    embed = discord.Embed(description="tag @someone", color=discord.Color.blue())         
    await ctx.send(embed=embed, mention_author=False)
  else:   
    gif = ["https://i.imgur.com/VGHwWUa.gif", "https://i.imgur.com/yi7CU5t.gif", "https://i.imgur.com/LHrs2i5.gif", "https://i.imgur.com/J3mRLc8.gif", "https://i.imgur.com/eE9BLra.gif", "https://i.imgur.com/nZYYcmr.gif", "https://i.imgur.com/MDsvf8w.gif", "https://i.imgur.com/P2zPziT.gif"]
    embed=discord.Embed(color=discord.Color.blue())
    embed.set_author(name="{0} licks {1}!! lzzz!!".format(ctx.message.author.name, otaku.name), icon_url=ctx.author.avatar_url)    
    embed.set_image(url=random.choice(gif))       
    await ctx.send(embed=embed, mention_author=False) 
@bot.command(pass_context=True)
async def bite(ctx, otaku: discord.Member=None):
  if not otaku:
    await ctx.message.add_reaction('❌') 
    embed = discord.Embed(description="tag @someone", color=discord.Color.blue())         
    await ctx.send(embed=embed, mention_author=False)
  else:   
    gif = ["https://i.imgur.com/oEBOetR.gif", "https://i.imgur.com/OgzfiuM.gif", "https://i.imgur.com/8qvlj0M.gif", "https://i.imgur.com/MUgRpL5.gif", "https://i.imgur.com/PHqBMPG.mp4"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_author(name="{0} bites {1}!! nom..nom!!".format(ctx.message.author.name, otaku.name), icon_url=ctx.author.avatar_url)   
    embed.set_image(url=random.choice(gif))       
    await ctx.send(embed=embed, mention_author=False)
@bot.command(pass_context=True)
async def poke(ctx, otaku: discord.Member=None):
  if not otaku:
    await ctx.message.add_reaction('❌') 
    embed = discord.Embed(description="tag @someone", color=discord.Color.blue())         
    await ctx.send(embed=embed, mention_author=False)
  else:  
    gif = ["https://i.imgur.com/X7pNyfw.gif", "https://i.imgur.com/KTL5UbY.gif", "https://i.imgur.com/FvBgoh6.gif", "https://i.imgur.com/BdxvlrD.gif", "https://i.imgur.com/PS31oUs.gif", "https://i.imgur.com/dmAjEZF.gif"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_author(name="{0} pokes {1}!! poke..poke!!".format(ctx.message.author.name, otaku.name), icon_url=ctx.author.avatar_url)   
    embed.set_image(url=random.choice(gif))       
    await ctx.send(embed=embed, mention_author=False)
@bot.command(pass_context=True)
async def slap(ctx, otaku: discord.Member=None): 
  if not otaku:
    await ctx.message.add_reaction('❌') 
    embed = discord.Embed(description="tag @someone", color=discord.Color.blue())        
    await ctx.send(embed=embed, mention_author=False)
  else:  
    gif = ["https://i.imgur.com/af7n02p.gif", "https://i.imgur.com/UZRKtQ0.gif", "https://i.imgur.com/CWdDw6x.gif", "https://i.imgur.com/uvIDSxi.gif", "https://i.imgur.com/vUTJUWG.gif"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_author(name="{0} slaps {1}!! whip!!".format(ctx.message.author.name, otaku.name), icon_url=ctx.author.avatar_url)   
    embed.set_image(url=random.choice(gif))       
    await ctx.send(embed=embed, mention_author=False) 
@bot.command(pass_context=True)
async def punch(ctx, otaku: discord.Member=None):
  if not otaku:
    await ctx.message.add_reaction('❌') 
    embed = discord.Embed(description="tag @someone", color=discord.Color.blue())         
    await ctx.send(embed=embed, mention_author=False)
  else:   
    gif = ["https://i.imgur.com/AVnDEnx.gif", "https://i.imgur.com/A1uSB0q.gif", "https://i.imgur.com/xcGvJfh.gif", "https://i.imgur.com/aI3vBjX.gif", "https://i.imgur.com/sV44BxK.gif", "https://i.imgur.com/valk8VY.gif", "https://i.imgur.com/ALR0hTq.gif"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_author(name="{0} punches {1}!! whoom!!".format(ctx.message.author.name, otaku.name), icon_url=ctx.author.avatar_url)   
    embed.set_image(url=random.choice(gif))       
    await ctx.send(embed=embed, mention_author=False)        
@bot.command(pass_context=True)
async def kill(ctx, otaku: discord.Member=None): 
  if not otaku:
    await ctx.message.add_reaction('❌') 
    embed = discord.Embed(description="tag @someone", color=discord.Color.blue())          
    await ctx.send(embed=embed, mention_author=False)
  else:  
    gif = ["https://i.imgur.com/JUJcXN6.gif", "https://i.imgur.com/x7CVt5X.gif", "https://i.imgur.com/nNgJdci.gif", "https://i.imgur.com/eN5Pb2x.gif", "https://i.imgur.com/BwhkFBj.gif", "https://i.imgur.com/LBfxEry.gif", "https://i.imgur.com/XJmObBf.gif", "https://i.imgur.com/VUdvFGF.gif", "https://i.imgur.com/DP7h49u.gif"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_author(name="{0} kills {1}!! wasted!!".format(ctx.message.author.name, otaku.name), icon_url=ctx.author.avatar_url)   
    embed.set_image(url=random.choice(gif))       
    await ctx.send(embed=embed, mention_author=False)    

##hard drive 
#neko
@bot.command()
async def neko(ctx): 
  neko = ["https://i.imgur.com/gYmWit8.jpg", "https://i.imgur.com/YODUPBx.png", "https://i.imgur.com/WEIzYqj.jpg", "https://i.imgur.com/muHjCd2.jpg", "https://i.imgur.com/xlLFGuw.jpg", "https://i.imgur.com/yb9dteM.png", "https://i.imgur.com/l185fRO.jpg", "https://i.imgur.com/fX6fN8m.jpg", "https://i.imgur.com/fitUjO8.jpg", "https://i.imgur.com/lwQQsHZ.jpg", "https://i.imgur.com/HGHxQU7.jpg", "https://i.imgur.com/I1Crh5n.jpg", "https://i.imgur.com/UTV94q8.jpg", "https://i.imgur.com/CcAV0Z1.jpg", "https://i.imgur.com/6duC1GW.jpg", "https://i.imgur.com/lELf8LB.jpg", "https://i.imgur.com/AO5alF0.jpg", "https://i.imgur.com/FP6GRBn.png", "https://i.imgur.com/3NdDaUp.jpg", "https://i.imgur.com/VPmTxCi.jpg", "https://i.imgur.com/2kDKsVP.jpg", "https://i.imgur.com/erF8QdO.jpg", "https://i.imgur.com/w7L5rxI.jpg", "https://i.imgur.com/KEWo1nb.png", ""]
  embed=discord.Embed(color=discord.Color.blue()) 
  embed.set_image(url=random.choice(neko)) 
  await ctx.reply(embed=embed, mention_author=False) 

#bunny
@bot.command()
async def bunny(ctx): 
  bunny = ["https://i.imgur.com/3Xx1NfG.jpg", "https://i.imgur.com/2A8svw1.jpg", "https://i.imgur.com/LRIyDDa.jpg", "https://i.imgur.com/pryD7oj.jpg", "https://i.imgur.com/eqeXcFa.jpg", "https://i.imgur.com/UckaWyt.jpg", "https://i.imgur.com/mb21UaR.jpg", "https://i.imgur.com/MPNzrXn.jpg", "https://i.imgur.com/bbsbu5V.jpg", "https://i.imgur.com/ApDP1KE.png", "https://i.imgur.com/Si1mJcb.png", "https://i.imgur.com/afG01qp.jpg", "https://i.imgur.com/ZUrdICw.jpg", "https://i.imgur.com/g7SxAzR.jpg", "https://i.imgur.com/uqVOeJk.jpg", "https://i.imgur.com/hcxhZtL.jpg", "https://i.imgur.com/vygVrUt.jpg"]
  embed=discord.Embed(color=discord.Color.blue()) 
  embed.set_image(url=random.choice(bunny))  
  await ctx.reply(embed=embed, mention_author=False) 

#sauce
@bot.command()
async def sauce(ctx):
  number = randomN(6)
  embed=discord.Embed(description=number, color=discord.Color.blue()) 
  em= await ctx.reply(embed=embed, mention_author=False)
  await asyncio.sleep(4) 
  await em.delete()
  await ctx.reply("<:AquaThumbsup:855300510345330719>", mention_author=False)
  
##restaurant
@bot.command()
async def pizza(ctx):
  gif= ["https://i.imgur.com/JTbKdiS.gif", "https://i.imgur.com/GSZtfEq.gif", "https://i.imgur.com/u9YJuZn.gif", "https://i.imgur.com/o6ePExQ.gif"]
  embed=discord.Embed(color=discord.Color.blue()) 
  embed.set_author(name="{0} noms pizza!! 🍕".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)     
  embed.set_image(url=random.choice(gif))  
  await ctx.reply(embed=embed, mention_author=False) 
@bot.command()
async def taco(ctx):
  gif= ["https://i.imgur.com/dzICh3g.gif"]
  embed=discord.Embed(color=discord.Color.blue()) 
  embed.set_author(name="{0} noms taco!! 🌮".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)       
  embed.set_image(url=random.choice(gif))  
  await ctx.reply(embed=embed, mention_author=False)           
@bot.command()
async def hotdog(ctx):
  gif= ["https://i.imgur.com/DziE0MZ.png", "https://i.imgur.com/paAhqyy.png", "https://i.imgur.com/TUbQQDh.jpg"]
  embed=discord.Embed(color=discord.Color.blue()) 
  embed.set_author(name="{0} noms hotdog!! 🌭".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)       
  embed.set_image(url=random.choice(gif))  
  await ctx.reply(embed=embed, mention_author=False)    
@bot.command()
async def hamburger(ctx):
  gif= ["https://i.imgur.com/VbwcLZ4.gif", "https://i.imgur.com/pPJu9Ct.gif", "https://i.imgur.com/t9J3BWH.gif", "https://i.imgur.com/xRaOHH0.gif", "https://i.imgur.com/4v0VRRp.gif", "https://i.imgur.com/CMtIZs9.gif"]
  embed=discord.Embed(color=discord.Color.blue()) 
  embed.set_author(name="{0} noms hamburger!! 🍔".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)     
  embed.set_image(url=random.choice(gif))  
  await ctx.reply(embed=embed, mention_author=False)  
@bot.command()
async def sandwitch(ctx):
  gif= ["https://i.imgur.com/GLWvMQ7.gif", "https://i.imgur.com/htjnT7s.gif", "https://i.imgur.com/Wi52BOb.mp4", "https://i.imgur.com/Tq4egqt.gif"]
  embed=discord.Embed(color=discord.Color.blue()) 
  embed.set_author(name="{0} noms sandwich!! 🥪".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)     
  embed.set_image(url=random.choice(gif))  
  await ctx.reply(embed=embed, mention_author=False)  
@bot.command()
async def fries(ctx):
  gif= ["https://i.imgur.com/43Oz4bP.gif", "https://i.imgur.com/Hy24Mbw.gif", "https://i.imgur.com/KeHVDH1.gif"]
  embed=discord.Embed(color=discord.Color.blue()) 
  embed.set_author(name="{0} noms fries!! 🍟".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)     
  embed.set_image(url=random.choice(gif))  
  await ctx.reply(embed=embed, mention_author=False)  
@bot.command()
async def popcorn(ctx):
  gif= ["https://i.imgur.com/6A0VZHq.gif", "https://i.imgur.com/lBBcid6.gif", "https://i.imgur.com/8myIZ9N.gif"]
  embed=discord.Embed(color=discord.Color.blue())
  embed.set_author(name="{0} noms popcorn!! 🍿".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)      
  embed.set_image(url=random.choice(gif))  
  await ctx.reply(embed=embed, mention_author=False)     
@bot.command()
async def doughnut(ctx):
  gif= ["https://i.imgur.com/QaModRS.gif", "https://i.imgur.com/MUPZjhO.gif", "https://i.imgur.com/cvcPfo4.gif", "https://i.imgur.com/JUh24u4.gif", "https://i.imgur.com/S82madx.gif"]
  embed=discord.Embed(color=discord.Color.blue()) 
  embed.set_author(name="{0} noms doughnut!! 🍩".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)     
  embed.set_image(url=random.choice(gif))  
  await ctx.reply(embed=embed, mention_author=False)   
@bot.command()
async def cupcake(ctx):
  gif= ["https://i.imgur.com/PmAOEYK.gif", "https://i.imgur.com/3ewilnf.gif", "https://i.imgur.com/e4BRkXO.gif"]
  embed=discord.Embed(color=discord.Color.blue()) 
  embed.set_author(name="{0} noms a cupcake!! 🧁".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)     
  embed.set_image(url=random.choice(gif))  
  await ctx.reply(embed=embed, mention_author=False)   
@bot.command()
async def cake(ctx):
  gif= ["https://i.imgur.com/H26HjFP.gif", "https://i.imgur.com/SQ5Vu2b.gif", "https://i.imgur.com/fxXRZV9.gif", "https://i.imgur.com/1LjyV1C.gif"]
  embed=discord.Embed(color=discord.Color.blue()) 
  embed.set_author(name="{0} noms a cake!! 🍰".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)     
  embed.set_image(url=random.choice(gif))  
  await ctx.reply(embed=embed, mention_author=False)          

##bar
@bot.command()
async def beer(ctx):
  gif= ["https://i.imgur.com/2te1Zys.gif"]
  embed=discord.Embed(color=discord.Color.blue()) 
  embed.set_author(name="{0} sips beer!! 🍺".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)     
  embed.set_image(url=random.choice(gif))  
  await ctx.reply(embed=embed, mention_author=False)                          
@bot.command()
async def wine(ctx):
  gif= ["https://i.imgur.com/BiaVOM6.gif", "https://i.imgur.com/ufls5Qk.gif"]
  embed=discord.Embed(color=discord.Color.blue()) 
  embed.set_author(name="{0} sips wine!! 🍷".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)     
  embed.set_image(url=random.choice(gif))  
  await ctx.reply(embed=embed, mention_author=False)  
@bot.command()
async def juice(ctx):
  gif= ["https://i.imgur.com/DudlCsV.gif"]
  embed=discord.Embed(color=discord.Color.blue()) 
  embed.set_author(name="{0} sips juice!! 🧃".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)     
  embed.set_image(url=random.choice(gif))  
  await ctx.reply(embed=embed, mention_author=False)  
@bot.command()
async def coffee(ctx):
  gif= ["https://i.imgur.com/YpVz8CH.gif", "https://i.imgur.com/bfitiyN.gif", "https://i.imgur.com/b7E5RZw.gif"]
  embed=discord.Embed(color=discord.Color.blue()) 
  embed.set_author(name="{0} sips coffee!! ☕".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)     
  embed.set_image(url=random.choice(gif))  
  await ctx.reply(embed=embed, mention_author=False)      
@bot.command()
async def milk(ctx):
  gif= ["https://i.imgur.com/9rPwykB.gif"]
  embed=discord.Embed(color=discord.Color.blue()) 
  embed.set_author(name="{0} sips milk!! 🥛".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)     
  embed.set_image(url=random.choice(gif))  
  await ctx.reply(embed=embed, mention_author=False)  
@bot.command()
async def water(ctx):
  gif= ["https://i.imgur.com/K5wRRkx.gif"]
  embed=discord.Embed(color=discord.Color.blue()) 
  embed.set_author(name="{0} sips water!! 🥤".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)     
  embed.set_image(url=random.choice(gif))  
  await ctx.reply(embed=embed, mention_author=False)  

##festival games    
#fortune
@bot.command()
async def fortune(ctx):
  messages = [":tanabata_tree: great blessing (大吉, dai-kichi)", ":tanabata_tree: middle blessing (中吉, chū-kichi)", ":tanabata_tree: small blessing (小吉, shō-kichi)", ":tanabata_tree: blessing (吉, kichi)", ":tanabata_tree: half-blessing (半吉, han-kichi)", ":tanabata_tree: future blessing (末吉, sue-kichi)", ":tanabata_tree: future small blessing (末小吉, sue-shō-kichi)", ":ghost: curse (凶, kyō)", ":ghost: small curse (小凶, shō-kyō)", ":ghost: half-curse (半凶, han-kyō)", ":ghost: future curse (末凶, sue-kyō)", ":ghost: great curse (大凶, dai-kyō)"] 
  await ctx.reply(random.choice(messages), mention_author=False)   
       
#slots
@bot.command()
async def slots(ctx):
  msg = [" :tangerine: " , " :apple: ", " :watermelon: ", " <:ShizueEmbarrassedTears:850973942650765332> "]
  embed=discord.Embed(description=" <:ShizueEmbarrassedTears:850973942650765332> <:ShizueEmbarrassedTears:850973942650765332> <:ShizueEmbarrassedTears:850973942650765332> <:ShizueEmbarrassedTears:850973942650765332> <:ShizueEmbarrassedTears:850973942650765332> <:ShizueEmbarrassedTears:850973942650765332> ", color=discord.Color.blue())
  embed.set_author(name="Roll 6 Shizue!!", icon_url="https://i.imgur.com/IehVlWn.png") 
  embedd=discord.Embed(description=random.choice(msg) + random.choice(msg) + random.choice(msg) + random.choice(msg) + random.choice(msg) + random.choice(msg), color=discord.Color.blue()) 
  embedd.set_author(name="Roll 6 Shizue!!", icon_url="https://i.imgur.com/IehVlWn.png")  
  embed0=discord.Embed(description=random.choice(msg) + random.choice(msg) + random.choice(msg) + random.choice(msg) + random.choice(msg) + random.choice(msg), color=discord.Color.blue()) 
  embed0.set_author(name="Roll 6 Shizue!!", icon_url="https://i.imgur.com/IehVlWn.png")  
  embed1=discord.Embed(description=random.choice(msg) + random.choice(msg) + random.choice(msg) + random.choice(msg) + random.choice(msg) + random.choice(msg), color=discord.Color.blue())
  embed1.set_author(name="Roll 6 Shizue!!", icon_url="https://i.imgur.com/IehVlWn.png") 
  embed1.set_footer(text="aww~ better luck next time!!")      
  embed2=discord.Embed(description=" <:ShizueEmbarrassedTears:850973942650765332> <:ShizueEmbarrassedTears:850973942650765332> <:ShizueEmbarrassedTears:850973942650765332> <:ShizueEmbarrassedTears:850973942650765332> <:ShizueEmbarrassedTears:850973942650765332> <:ShizueEmbarrassedTears:850973942650765332> ", color=discord.Color.blue())
  embed2.set_author(name="Roll 6 Shizue!!", icon_url="https://i.imgur.com/IehVlWn.png") 
  embed2.set_footer(text="YaY~ You won!!") 
  ems =  [embed1, embed1, embed2, embed1, embed1]                      
  em = await ctx.reply(embed=embed, mention_author=False)
  await em.add_reaction('🎰') 
  def check(reaction, user):
    return user == ctx.author and str(reaction.emoji) == '🎰'
  await bot.wait_for('reaction_add', timeout=60.0, check=check)  
  await em.edit(embed=embed0, mention_author=False)         
  await asyncio.sleep(0.5)  
  await em.edit(embed=embedd, mention_author=False)  
  await asyncio.sleep(0.5)
  await em.edit(embed=embed0, mention_author=False)         
  await asyncio.sleep(0.5)   
  await em.edit(embed=(random.choice(ems)), mention_author=False)                  

#throwball
@bot.command()
async def throwball(ctx):
  embed=discord.Embed(color=discord.Color.blue())
  embed.set_author(name="hit Gobuta!!", icon_url="https://i.imgur.com/KBMesb1.png")    
  embed.add_field(name="<:GobutaGlassesCool:851641124686528524>", value="\u200b", inline=True)
  embed.add_field(name="\u200b", value="\u200b", inline=False) 
  embed.add_field(name="\u200b", value="\u200b", inline=False) 
  embed.set_footer(text="React below to hit!!") 
  embed1=discord.Embed(color=discord.Color.blue())
  embed1.set_author(name="hit Gobuta!", icon_url="https://i.imgur.com/KBMesb1.png")      
  embed1.add_field(name="<:GobutaGlassesCool:851641124686528524>", value="\u200b", inline=True)
  embed1.add_field(name="\u200b", value="\u200b", inline=False)  
  embed1.add_field(name="\u200b", value=":soccer:", inline=False) 
  embed1.set_footer(text="hm~ You suck!!")  
  embed2=discord.Embed(color=discord.Color.blue())
  embed2.set_author(name="hit Gobuta!", icon_url="https://i.imgur.com/KBMesb1.png")     
  embed2.add_field(name="<:GobutaGlassesCool:851641124686528524>", value="\u200b", inline=True)
  embed2.add_field(name="\u200b", value="\u200b", inline=False)
  embed2.add_field(name=":soccer:", value=":soccer:", inline=False) 
  embed2.set_footer(text="waa~ not even close!!")  
  embed3=discord.Embed(color=discord.Color.blue())
  embed3.set_author(name="hit Gobuta!", icon_url="https://i.imgur.com/KBMesb1.png")     
  embed3.add_field(name="<:GobutaGlassesCool:851641124686528524>", value="\u200b", inline=True) 
  embed3.add_field(name="\u200b", value=":soccer:", inline=False) 
  embed3.add_field(name=":soccer:", value=":soccer:", inline=False)
  embed3.set_footer(text="aa~ You missed!!")  
  embed4=discord.Embed(color=discord.Color.blue())
  embed4.set_author(name="hit Gobuta!", icon_url="https://i.imgur.com/KBMesb1.png")  
  embed4.add_field(name="<:GobutaGlassesCool:851641124686528524>", value="\u200b", inline=True)
  embed4.add_field(name=":soccer:", value=":soccer:", inline=False)
  embed4.add_field(name=":soccer:", value=":soccer:", inline=False) 
  embed4.set_footer(text="eh~ just a little more!!")   
  embed5=discord.Embed(color=discord.Color.blue())
  embed5.set_author(name="hit Gobuta!", icon_url="https://i.imgur.com/KBMesb1.png")   
  embed5.add_field(name=":wind_blowing_face:", value=":soccer:", inline=True)
  embed5.add_field(name=":soccer:", value=":soccer:", inline=False)
  embed5.add_field(name=":soccer:", value=":soccer:", inline=False) 
  embed5.set_footer(text="wowo~ a clear hit!!")   
  ems = [embed1, embed2, embed3, embed4, embed5]                                     
  em = await ctx.reply(embed=embed, mention_author=False) 
  await em.add_reaction('⚽') 
  def check(reaction, user):
    return user == ctx.author and str(reaction.emoji) == '⚽'
  await bot.wait_for('reaction_add', timeout=60.0, check=check)  
  await em.edit(embed=(random.choice(ems)), mention_author=False)  

##help
@bot.command()
async def help(ctx): 
  embed = discord.Embed(title=":t_rex:  Rimuru", url="https://top.gg/bot/841573836445188136/vote", color=discord.Color.blue())  
  embed.set_thumbnail(url="https://i.imgur.com/j5EyoN2.jpg")   
  embed.add_field(name=":calling:  Interactions", value="`rimuru`  `yo`  `hi`  `hello`  `hey`  `goodmorning`  `goodnight`  `badslime`  `goodslime`  `bye`", inline=False)
  embed.add_field(name=":jigsaw:  Fun", value="`todo`  `tierlist`", inline=False)       
  embed.add_field(name=":earth_americas:  Profile", value="`simp`  `hearts`  `avatar`", inline=False) 
  embed.add_field(name=":performing_arts:  Roleplay", value="`nickname`  `sing`  `shizue`", inline=False) 
  embed.add_field(name=":adhesive_bandage:  Hard Drive", value="`neko`  `bunny`  `sauce`", inline=False)     
  embed.add_field(name=":jack_o_lantern:  Actions", value="`cuddle`  `hug`  `pat`  `kiss`  `lick`  `bite`  `poke`  `slap`  `punch`  `kill`", inline=False)   
  embed.add_field(name=":fork_and_knife:  Restaurant", value="`pizza`  `taco`  `hotdog`  `hamburger`  `sandwich`  `fries`  `popcorn`  `doughnut`  `cupcake`  `cake`", inline=False)    
  embed.add_field(name=":beers:  Bar", value="`water`  `milk`  `coffee`  `juice`  `wine`  `beer`", inline=False)
  embed.add_field(name=":crystal_ball:  Festival Games", value="`fortune`  `slots`  `throwball`", inline=False) 
  embed.add_field(name=":construction:  Diablo", value="`~`", inline=False)                          
  await ctx.reply(embed=embed, mention_author=False) 

##run
keep_awake()
bot.run(os.getenv('TOKEN'))        
