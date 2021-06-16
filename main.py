import os
import json
import random
import asyncio
import discord
#sauce
from sauce import neko
from sauce import bunny
#to keep Rimuru awake
from keep_awake import keep_awake

client = discord.Client() 

#update and add hearts in user_hearts.json
async def update_hearts(user_hearts, user):
  if not f'{user.id}' in user_hearts:
    user_hearts[f'{user.id}'] = {}
    user_hearts[f'{user.id}']['hearts'] = 0
async def add_hearts(user_hearts, user, hearts):
  user_hearts[f'{user.id}']['hearts'] += hearts   

#update and add curses in user_curses.json
async def update_curses(user_curses, user):
  if not f'{user.id}' in user_curses:
    user_curses[f'{user.id}'] = {}
    user_curses[f'{user.id}']['curses'] = 0
async def add_curses(user_curses, user, curses):
  user_curses[f'{user.id}']['curses'] += curses   

#console msg
@client.event
async def on_ready():
 print('EveryThing Looks Fine {0.user}'.format(client))

##
@client.event
async def on_message(message):
  if message.author == client.user:
    return 

##Interactions
  if message.content.startswith('~yo'):
    messages = ["Yo <:ShizueEmbarrassedTears:850973942650765332>", "Yoo <:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)
  if message.content.startswith('~hi'):
    messages = ["hii <:ShizueEmbarrassedTears:850973942650765332>", "hewoo <:ShizueEmbarrassedTears:850973942650765332>", "heyy <:ShizueEmbarrassedTears:850973942650765332>", "aa..aa.. shuna and shion making me wear bunny costume again.. <:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)
  if message.content.startswith('~hello'):
    messages = ["hii <:ShizueEmbarrassedTears:850973942650765332>", "hewoo <:ShizueEmbarrassedTears:850973942650765332>", "heyy <:ShizueEmbarrassedTears:850973942650765332>", "aa..aa.. shuna and shion making me wear bunny costume again.. <:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False) 
  if message.content.startswith('~hey'):
    messages = ["hii <:ShizueEmbarrassedTears:850973942650765332>", "hewoo <:ShizueEmbarrassedTears:850973942650765332>", "heyy <:ShizueEmbarrassedTears:850973942650765332>", "aa..aa.. shuna and shion making me wear bunny costume again.. <:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)       
  if message.content.startswith('~good night'):
    messages = ["good night <:ShizueEmbarrassedTears:850973942650765332>", "night <:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)
  if message.content.startswith('~good morning'):
    messages = ["good morning <:ShizueEmbarrassedTears:850973942650765332>", "morning <:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)  
  if message.content.startswith('~sex'):
    msg = 'b..bbaka!!'.format(message)
    await message.reply(msg, mention_author=False)
  if message.content.startswith('~bad slime'):
    messages = ["<:ShizueEmbarrassedTears:850973942650765332>", "nuu.. i am not a bad slime <:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)  
  if message.content.startswith('~good slime'):
    messages = ["<:ShizueEmbarrassedTears:850973942650765332>", "<:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)                      
  if message.content.startswith('~rimuru'):
    messages = ["Yes <:ShizueEmbarrassedTears:850973942650765332>", "? <:ShizueEmbarrassedTears:850973942650765332>",]
    await message.reply(random.choice(messages), mention_author=False) 
  if message.content.startswith('~sad'):
    msg = 'aww.. be happy <:ShizueEmbarrassedTears:850973942650765332>'.format(message)
    await message.reply(msg, mention_author=False)
  if message.content.startswith('~happy'):
    messages = ["<:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)                    
  if message.content.startswith('~bye'):
    messages = ["nuu.. dont go <:ShizueEmbarrassedTears:850973942650765332>", "ahh.. come back soon <:ShizueEmbarrassedTears:850973942650765332>", "bye bye <:ShizueEmbarrassedTears:850973942650765332>", "byee <:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)     

##fun
#~todo
  if message.content.startswith('~todo'): 
    messages = [":umbrella: mm.. make it rain!! <:ShizueEmbarrassedTears:850973942650765332>", ":snowman2: woo.. make a snowman!! <:ShizueEmbarrassedTears:850973942650765332>", ":fork_knife_plate: get something to eat!! <:ShizueEmbarrassedTears:850973942650765332>", ":soap: cleaning? <:ShizueEmbarrassedTears:850973942650765332>", ":beach: lets go to a beach!! <:ShizueEmbarrassedTears:850973942650765332>", ":bubble_tea: get something to drink!! <:ShizueEmbarrassedTears:850973942650765332>", ":island: lets go to some island!! <:ShizueEmbarrassedTears:850973942650765332>", ":video_game: wanna play some games with me!! <:ShizueEmbarrassedTears:850973942650765332>", ":yarn: just sleep.. <:ShizueEmbarrassedTears:850973942650765332>", ":bowling: lets go bowling!! <:ShizueEmbarrassedTears:850973942650765332>", ":microphone: sing something!! <:ShizueEmbarrassedTears:850973942650765332>", ":golf: lets go golfing!! <:ShizueEmbarrassedTears:850973942650765332>", ":rainbow: woo.. make a rainbow!! <:ShizueEmbarrassedTears:850973942650765332>", ":boxing_glove: boing!! foof..ffof.. <:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False) 

#~tierlist
  if message.content.startswith('~tierlist'):
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_image(url="https://i.imgur.com/kHH1AKB.png")     
    await message.reply(embed=embed, mention_author=False) 

##profile
#~simp
  if message.content.startswith('~simp'):     
    embed=discord.Embed(title="💙", color=discord.Color.blue()) 
    await message.reply(embed=embed, mention_author=False) 
#hearts   
    with open('user_hearts.json', 'r') as f:
      user_hearts = json.load(f)
    await update_hearts(user_hearts, message.author)
    await add_hearts(user_hearts, message.author, 1)
    with open('user_hearts.json', 'w') as f:
      json.dump(user_hearts, f)      

#~hearts
  if message.content.startswith('~hearts'): 
   with open('user_hearts.json', 'r') as f:
    user_hearts = json.load(f)
    authorID = message.author.id     
    hearts = user_hearts[str(authorID)]['hearts']  
    embed = discord.Embed(color=discord.Color.blue())
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)  
    embed.add_field(name="hearts earned <:ShizueEmbarrassedTears:850973942650765332> :", value= hearts, inline=True) 
    await message.reply(embed=embed, mention_author=False) 

#~profile
  if message.content.startswith('~profile'): 
   with open('user_hearts.json', 'r') as f:
    user_hearts = json.load(f)
    authorID = message.author.id     
    hearts = user_hearts[str(authorID)]['hearts']
   with open('user_curses.json', 'r') as f:
    user_curses = json.load(f)
    authorID = message.author.id     
    curses = user_curses[str(authorID)]['curses']    
    embed = discord.Embed(color=discord.Color.blue())
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)  
    embed.add_field(name="hearts earned <:ShizueEmbarrassedTears:850973942650765332> :", value= hearts, inline=True)
    embed.add_field(name=":ghost: :", value=curses, inline=False)    
    await message.reply(embed=embed, mention_author=False)       

#~avatar    
  if message.content.startswith('~avatar'): 
    embed = discord.Embed(color=discord.Color.blue())
    embed.set_image(url=message.author.avatar_url)         
    await message.reply(embed=embed, mention_author=False)  

##roleplay
#~nickname
  if message.content.startswith('~nickname'):     
    nicknames = ["Acheron", "Adbeel", "Azazel", "Belial", "Buer", "Charon", "Dagon", "Damien", "Eligor", "Forneus", "Gresill", "Helel", "Iblis", "Lestat", "Leviatha", "Lucifer", "Malacoda", "Naberius", "Orobas", "Radna", "Samael", "Sedit", "Seth", "Ubel", "Zagan", "Achlys", "Akeldama", "Carmen", "Carmilla", "Claudia", "Enyo", "Gello", "Hel", "Lilin", "Mare", "Mircalla", "Pandora", "Puck", "Selene"]
    await message.author.edit(nick=(random.choice(nicknames)))
    await message.add_reaction('✅')     
    messages = ["<:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)       

#~sing    
  if message.content.startswith('~sing'): 
    vc = message.author.voice   
    if vc:
      await vc.channel.connect() 
      await message.add_reaction('✅')       
    if vc is None:
      await message.add_reaction('❌')   
      await message.reply('b..bbaka!! You have to be in a voice channel first!!', mention_author=False)                   
    guild = message.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)    
    audio_source = discord.FFmpegPCMAudio('https://mp3.fastupload.co/data/1622193194/rimuru.mp3')
    if not voice_client.is_playing():
      voice_client.play(audio_source, after=None)
    messages = ["woooo..", "woo.. woo..", "wowowo..", "wowo..", "wowoo..", "woowo..", "woowoo.."]
    await message.reply(random.choice(messages), mention_author=False)          
    await asyncio.sleep(90)                                       
    await voice_client.disconnect()   

#~shizue
  if message.content.startswith('~shizue'):
    messages = ["i..i.. like Rimuru-sama <:ShizueEmbarrassedTears:850973942650765332> ~aa"]
    await message.reply(random.choice(messages), mention_author=False)        

##actions
  if message.content.startswith('~cuddle'):
    gif = ["https://i.imgur.com/zEpEFdR.gif", "https://i.imgur.com/0vMxXPD.gif", "https://i.imgur.com/BBltNs5.gif", "https://i.imgur.com/AbwGSGe.mp4"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_author(name="{0}!! aww!!".format(message.author.name), icon_url=message.author.avatar_url)  
    embed.set_image(url=random.choice(gif))       
    await message.reply(embed=embed, mention_author=False)   
  if message.content.startswith('~hug'):
    gif = ["https://i.imgur.com/BLWNnFl.gif", "https://i.imgur.com/ZNexQYs.gif", "https://i.imgur.com/AmW4JXv.gif", "https://i.imgur.com/jPI7d39.gif"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_author(name="{0}!! huggy!!".format(message.author.name), icon_url=message.author.avatar_url)      
    embed.set_image(url=random.choice(gif))       
    await message.reply(embed=embed, mention_author=False)
  if message.content.startswith('~pat'):
    gif = ["https://i.imgur.com/jalh0TO.gif", "https://i.imgur.com/jyGKbIt.gif", "https://i.imgur.com/waDgdYE.gif", "https://i.imgur.com/y8hzJj3.gif", "https://i.imgur.com/WnWbaBI.gif", "https://i.imgur.com/MzaOifc.gif", "https://i.imgur.com/twu1Elb.gif", "https://i.imgur.com/XShvBry.gif", "https://i.imgur.com/DwcgM7X.gif", "https://i.imgur.com/wXfqvwZ.gif", "https://i.imgur.com/M6whfdx.gif"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_author(name="{0}!! pat..pat!!".format(message.author.name), icon_url=message.author.avatar_url)   
    embed.set_image(url=random.choice(gif))       
    await message.reply(embed=embed, mention_author=False)
  if message.content.startswith('~kiss'):
    gif = ["https://i.imgur.com/GDti9sg.gif", "https://i.imgur.com/pFboGNv.gif", "https://i.imgur.com/tTNi2ny.gif", "https://i.imgur.com/FQB8F7f.gif", "https://i.imgur.com/CCOE8cJ.gif"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_author(name="{0}!! chuu!!".format(message.author.name), icon_url=message.author.avatar_url)   
    embed.set_image(url=random.choice(gif))       
    await message.reply(embed=embed, mention_author=False)
  if message.content.startswith('~lick'):
    gif = ["https://i.imgur.com/VGHwWUa.gif", "https://i.imgur.com/yi7CU5t.gif", "https://i.imgur.com/LHrs2i5.gif", "https://i.imgur.com/J3mRLc8.gif", "https://i.imgur.com/eE9BLra.gif", "https://i.imgur.com/nZYYcmr.gif", "https://i.imgur.com/MDsvf8w.gif", "https://i.imgur.com/P2zPziT.gif"]
    embed=discord.Embed(color=discord.Color.blue())
    embed.set_author(name="{0}!! lzzzz!!".format(message.author.name), icon_url=message.author.avatar_url)    
    embed.set_image(url=random.choice(gif))       
    await message.reply(embed=embed, mention_author=False) 
  if message.content.startswith('~bite'):
    gif = ["https://i.imgur.com/oEBOetR.gif", "https://i.imgur.com/OgzfiuM.gif", "https://i.imgur.com/8qvlj0M.gif", "https://i.imgur.com/MUgRpL5.gif", "https://i.imgur.com/PHqBMPG.mp4"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_author(name="{0}!! nom!!".format(message.author.name), icon_url=message.author.avatar_url)   
    embed.set_image(url=random.choice(gif))       
    await message.reply(embed=embed, mention_author=False)
  if message.content.startswith('~poke'):
    gif = ["https://i.imgur.com/X7pNyfw.gif", "https://i.imgur.com/KTL5UbY.gif", "https://i.imgur.com/FvBgoh6.gif", "https://i.imgur.com/BdxvlrD.gif", "https://i.imgur.com/PS31oUs.gif", "https://i.imgur.com/dmAjEZF.gif"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_author(name="{0}!! poke..poke~!!".format(message.author.name), icon_url=message.author.avatar_url)   
    embed.set_image(url=random.choice(gif))       
    await message.reply(embed=embed, mention_author=False)
  if message.content.startswith('~slap'):
    gif = ["https://i.imgur.com/af7n02p.gif", "https://i.imgur.com/UZRKtQ0.gif", "https://i.imgur.com/CWdDw6x.gif", "https://i.imgur.com/uvIDSxi.gif", "https://i.imgur.com/vUTJUWG.gif"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_author(name="{0}!! whip!!".format(message.author.name), icon_url=message.author.avatar_url)   
    embed.set_image(url=random.choice(gif))       
    await message.reply(embed=embed, mention_author=False) 
  if message.content.startswith('~punch'):
    gif = ["https://i.imgur.com/AVnDEnx.gif", "https://i.imgur.com/A1uSB0q.gif", "https://i.imgur.com/xcGvJfh.gif", "https://i.imgur.com/aI3vBjX.gif", "https://i.imgur.com/sV44BxK.gif", "https://i.imgur.com/valk8VY.gif", "https://i.imgur.com/ALR0hTq.gif"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_author(name="{0}!! whoom!!".format(message.author.name), icon_url=message.author.avatar_url)   
    embed.set_image(url=random.choice(gif))       
    await message.reply(embed=embed, mention_author=False)        
  if message.content.startswith('~kill'):
    gif = ["https://i.imgur.com/JUJcXN6.gif", "https://i.imgur.com/gE0AE8V.gif", "https://i.imgur.com/nNgJdci.gif", "https://i.imgur.com/XhOC90e.gif", "https://i.imgur.com/BwhkFBj.gif", "https://i.imgur.com/LBfxEry.gif"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_author(name="{0}!! wasted!!".format(message.author.name), icon_url=message.author.avatar_url)   
    embed.set_image(url=random.choice(gif))       
    await message.reply(embed=embed, mention_author=False)                          

##hard drive 
#~hard drive?
  if message.content.startswith('~hard drive?'):
    msg = "h-how!? i thought tamura destroyed it!! <:ShizueEmbarrassedTears:850973942650765332>"
    await message.reply((msg), mention_author=False)

#~neko
  if message.content.startswith('~neko'):
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_image(url=(random.choice(neko)))     
    await message.reply(embed=embed, mention_author=False) 

#~bunny
  if message.content.startswith('~bunny'):
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_image(url=(random.choice(bunny)))     
    await message.reply(embed=embed, mention_author=False) 

##restaurant
  if message.content.startswith('~pizza'):
    messages = [":pizza: here you go!! <:ShizueEmbarrassedTears:850973942650765332>", ":pizza: here ~<:ShizueEmbarrassedTears:850973942650765332>"] 
    await message.reply(random.choice(messages), mention_author=False) 
  if message.content.startswith('~taco'):
    messages = [":taco: here you go!! <:ShizueEmbarrassedTears:850973942650765332>", ":taco: here ~<:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)  
  if message.content.startswith('~burrito'):
    messages = [":burrito: here you go!! <:ShizueEmbarrassedTears:850973942650765332>", ":burrito: here ~<:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)          
  if message.content.startswith('~hotdog'):
    messages = [":hotdog: here you go!! <:ShizueEmbarrassedTears:850973942650765332>", ":hotdog: here ~<:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)    
  if message.content.startswith('~hamburger'):
    messages = [":hamburger: here you go!! <:ShizueEmbarrassedTears:850973942650765332>", ":hamburger: here ~<:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)  
  if message.content.startswith('~sandwich'):
    messages = [":sandwich: here you go!! <:ShizueEmbarrassedTears:850973942650765332>", ":sandwich: here ~<:ShizueEmbarrassedTears:850973942650765332>"] 
    await message.reply(random.choice(messages), mention_author=False)      
  if message.content.startswith('~fries'):
    messages = [":fries: here you go!! <:ShizueEmbarrassedTears:850973942650765332>", ":fries: here ~<:ShizueEmbarrassedTears:850973942650765332>"] 
    await message.reply(random.choice(messages), mention_author=False) 
  if message.content.startswith('~popcorn'):
    messages = [":popcorn: here you go!! <:ShizueEmbarrassedTears:850973942650765332>", ":popcorn: here ~<:ShizueEmbarrassedTears:850973942650765332>"] 
    await message.reply(random.choice(messages), mention_author=False)     
  if message.content.startswith('~doughnut'):
    messages = [":doughnut: here you go!! <:ShizueEmbarrassedTears:850973942650765332>", ":doughnut: here ~<:ShizueEmbarrassedTears:850973942650765332>"] 
    await message.reply(random.choice(messages), mention_author=False)  
  if message.content.startswith('~cupcake'):
    messages = [":cupcake: here you go!! <:ShizueEmbarrassedTears:850973942650765332>", ":cupcake: here ~<:ShizueEmbarrassedTears:850973942650765332>"] 
    await message.reply(random.choice(messages), mention_author=False) 
  if message.content.startswith('~cake'):
    messages = [":cake: here you go!! <:ShizueEmbarrassedTears:850973942650765332>", ":cake: here ~<:ShizueEmbarrassedTears:850973942650765332>"] 
    await message.reply(random.choice(messages), mention_author=False)         

##bar
  if message.content.startswith('~beer'):
    messages = [":beer: here you go!! <:ShizueEmbarrassedTears:850973942650765332>", ":beer: here ~<:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)                        
  if message.content.startswith('~wine'):
    messages = [":wine_glass: here you go!! <:ShizueEmbarrassedTears:850973942650765332>", ":wine_glass: here ~<:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)
  if message.content.startswith('~whisky'):
    messages = [":tumbler_glass: here you go!! <:ShizueEmbarrassedTears:850973942650765332>", ":tumbler_glass: here ~<:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False) 
  if message.content.startswith('~cocktail'):
    messages = [":cocktail: here you go!! <:ShizueEmbarrassedTears:850973942650765332>", ":cocktail: here ~<:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False) 
  if message.content.startswith('~juice'):
    messages = [":tropical_drink: here you go!! <:ShizueEmbarrassedTears:850973942650765332>", ":tropical_drink: here ~<:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False) 
  if message.content.startswith('~coffee'):
    messages = [":coffee: here you go!! <:ShizueEmbarrassedTears:850973942650765332>", ":coffee: here ~<:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)     
  if message.content.startswith('~milk'):
    messages = [":milk: here you go!! <:ShizueEmbarrassedTears:850973942650765332>", ":milk: here ~<:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False) 
  if message.content.startswith('~water'):
    messages = [":cup_with_straw: here you go!! <:ShizueEmbarrassedTears:850973942650765332>", ":cup_with_straw: here ~<:ShizueEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False) 

##festival games    
#~fortune
  if message.content.startswith('~fortune'):
    messages = [":tanabata_tree: great blessing (大吉, dai-kichi)", ":tanabata_tree: middle blessing (中吉, chū-kichi)", ":tanabata_tree: small blessing (小吉, shō-kichi)", ":tanabata_tree: blessing (吉, kichi)", ":tanabata_tree: half-blessing (半吉, han-kichi)", ":tanabata_tree: future blessing (末吉, sue-kichi)", ":tanabata_tree: future small blessing (末小吉, sue-shō-kichi)", ":ghost: curse (凶, kyō)", ":ghost: small curse (小凶, shō-kyō)", ":ghost: half-curse (半凶, han-kyō)", ":ghost: future curse (末凶, sue-kyō)", ":ghost: great curse (大凶, dai-kyō)"]
    #curses
    with open('user_curses.json', 'r') as f:
      user_curses = json.load(f)
    await update_curses(user_curses, message.author)
    await add_curses(user_curses, message.author, 1)
    with open('user_curses.json', 'w') as f:
      json.dump(user_curses, f)
    await message.reply(random.choice(messages), mention_author=False)

#~slots
  if message.content.startswith('~slots'):
    msg = [" :tangerine: " , " :apple: ", " :watermelon: ", " <:ShizueEmbarrassedTears:850973942650765332> "]
    embed=discord.Embed(title="🎰 Slot Machine 🎰", description=" <:ShizueEmbarrassedTears:850973942650765332> <:ShizueEmbarrassedTears:850973942650765332> <:ShizueEmbarrassedTears:850973942650765332> <:ShizueEmbarrassedTears:850973942650765332> <:ShizueEmbarrassedTears:850973942650765332> <:ShizueEmbarrassedTears:850973942650765332> ", color=discord.Color.blue())
    embed0=discord.Embed(title="🎰 Slot Machine 🎰", description=random.choice(msg) + random.choice(msg) + random.choice(msg) + random.choice(msg) + random.choice(msg) + random.choice(msg), color=discord.Color.blue())
    embed1=discord.Embed(title="🎰 Slot Machine 🎰", description=random.choice(msg) + random.choice(msg) + random.choice(msg) + random.choice(msg) + random.choice(msg) + random.choice(msg), color=discord.Color.blue())
    embed1.set_footer(text="aww~ better luck next time!!")      
    embed2=discord.Embed(title="🎰 Slot Machine 🎰", description=" <:ShizueEmbarrassedTears:850973942650765332> <:ShizueEmbarrassedTears:850973942650765332> <:ShizueEmbarrassedTears:850973942650765332> <:ShizueEmbarrassedTears:850973942650765332> <:ShizueEmbarrassedTears:850973942650765332> <:ShizueEmbarrassedTears:850973942650765332> ", color=discord.Color.blue())
    embed2.set_footer(text="YaY~ You won!!") 
    ems =  [embed1, embed1, embed2, embed1, embed1]                      
    em = await message.reply(embed=embed, mention_author=False) 
    await asyncio.sleep(1) 
    await em.edit(embed=embed0, mention_author=False)          
    await em.edit(embed=(random.choice(ems)), mention_author=False)            

##~help
  if message.content.startswith('~help'): 
    embed = discord.Embed(title=":t_rex:  Rimuru", url="https://top.gg/bot/841573836445188136/vote", color=discord.Color.blue())     
    embed.add_field(name=":calling:  Interactions", value="`~rimuru`  `~yo`  `~hi`  `~hello`  `~hey`  `~good morning`  `~good night`  `~bad slime`  `~good slime`  `~bye`", inline=False)
    embed.add_field(name=":jigsaw:  Fun", value="`~todo`  `~tierlist`", inline=False)       
    embed.add_field(name=":earth_americas:  Profile", value="`~simp`  `~hearts`  `~profile`  `~avatar`", inline=False) 
    embed.add_field(name=":performing_arts:  Roleplay", value="`~nickname`  `~sing`  `~shizue`", inline=False) 
    embed.add_field(name=":adhesive_bandage:  Hard Drive", value="`~hard drive?`  `~neko`  `~bunny`", inline=False)     
    embed.add_field(name=":jack_o_lantern:  Actions", value="`~cuddle`  `~hug`  `~pat`  `~kiss`  `~lick`  `~bite`  `~poke`  `~slap`  `~punch`  `~kill`", inline=False)   
    embed.add_field(name=":fork_and_knife:  Restaurant", value="`~pizza`  `~taco`  `~burrito`  `~hotdog`  `~hamburger`  `~sandwich`  `~fries`  `~popcorn`  `~doughnut`  `~cupcake`  `~cake`", inline=False)    
    embed.add_field(name=":beers:  Bar", value="`~water`  `~milk`  `~coffee`  `~juice`  `~cocktail`  `~whisky`  `~wine`  `~beer`", inline=False)
    embed.add_field(name=":crystal_ball:  Festival Games", value="`~fortune`  `~slots`", inline=False)                         
    await message.reply(embed=embed, mention_author=False)  

#~gobuta
  if message.content.startswith('~gobuta'):
    embed=discord.Embed(color=discord.Color.blue())
    embed.set_author(name="{0}!! wants to hit gobuta!!".format(message.author.name), icon_url=message.author.avatar_url)  
    embed.add_field(name="<:GobutaGlassesCool:851641124686528524>", value="\u200b", inline=True)
    embed.add_field(name="\u200b", value="\u200b", inline=False) 
    embed.add_field(name="\u200b", value="\u200b", inline=False) 
    embed.set_footer(text="React below to hit!!") 
    embed1=discord.Embed(color=discord.Color.blue())
    embed1.set_author(name="{0}!! wants to hit gobuta!!".format(message.author.name), icon_url=message.author.avatar_url)  
    embed1.add_field(name="<:GobutaGlassesCool:851641124686528524>", value="\u200b", inline=True)
    embed1.add_field(name="\u200b", value="\u200b", inline=False)  
    embed1.add_field(name="\u200b", value=":soccer:", inline=False) 
    embed1.set_footer(text="hm~ did you even touch it!!")  
    embed2=discord.Embed(color=discord.Color.blue())
    embed2.set_author(name="{0}!! wants to hit gobuta!!".format(message.author.name), icon_url=message.author.avatar_url)  
    embed2.add_field(name="<:GobutaGlassesCool:851641124686528524>", value="\u200b", inline=True)
    embed2.add_field(name="\u200b", value="\u200b", inline=False)
    embed2.add_field(name=":soccer:", value=":soccer:", inline=False) 
    embed2.set_footer(text="waa~ You suck!!")  
    embed3=discord.Embed(color=discord.Color.blue())
    embed3.set_author(name="{0}!! wants to hit gobuta!!".format(message.author.name), icon_url=message.author.avatar_url)  
    embed3.add_field(name="<:GobutaGlassesCool:851641124686528524>", value="\u200b", inline=True) 
    embed3.add_field(name="\u200b", value=":soccer:", inline=False) 
    embed3.add_field(name=":soccer:", value=":soccer:", inline=False)
    embed3.set_footer(text="aa~ You missed!!")  
    embed4=discord.Embed(color=discord.Color.blue())
    embed4.set_author(name="{0}!! wants to hit gobuta!!".format(message.author.name), icon_url=message.author.avatar_url)  
    embed4.add_field(name="<:GobutaGlassesCool:851641124686528524>", value="\u200b", inline=True)
    embed4.add_field(name=":soccer:", value=":soccer:", inline=False)
    embed4.add_field(name=":soccer:", value=":soccer:", inline=False) 
    embed4.set_footer(text="ee~ just a little more!!")   
    embed5=discord.Embed(color=discord.Color.blue())
    embed5.set_author(name="{0}!! wants to hit gobuta!!".format(message.author.name), icon_url=message.author.avatar_url)  
    embed5.add_field(name="<:GobutaGlassesCool:851641124686528524>", value=":soccer:", inline=True)
    embed5.add_field(name=":soccer:", value=":soccer:", inline=False)
    embed5.add_field(name=":soccer:", value=":soccer:", inline=False) 
    embed5.set_footer(text="wowo~ a clear hit!!")                                          
    em = await message.reply(embed=embed, mention_author=False)
    await em.add_reaction('⚽')
    ems = [embed1, embed2, embed3, embed4, embed5] 
    await asyncio.sleep(2)   
    await em.edit(embed=(random.choice(ems)), mention_author=False)   

#run
keep_awake()
client.run(os.getenv('TOKEN')) 
