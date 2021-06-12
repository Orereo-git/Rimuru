import os
import json
import random
import asyncio
import discord

client = discord.Client()
        
#update and add hearts in user_hearts.json
async def update_data(user_hearts, user):
  if not f'{user.id}' in user_hearts:
    user_hearts[f'{user.id}'] = {}
    user_hearts[f'{user.id}']['hearts'] = 0
async def add_hearts(user_hearts, user, hearts):
  user_hearts[f'{user.id}']['hearts'] += hearts   

#console msg
@client.event
async def on_ready():
 print('EveryThing Looks Fine {0.user}'.format(client))

##
@client.event
async def on_message(message):
  if message.author == client.user:
    return

#Interactions
  if message.content.startswith('~Yo'):
    messages = ["Yo <:Shizuowo:851648667404337172>", "Yoo <:Shizuowo:851648667404337172>"]
    await message.reply(random.choice(messages), mention_author=False)
  if message.content.startswith('~hi'):
    messages = ["hii <:Shizuowo:851648667404337172>", "hewoo <:Shizuowo:851648667404337172>", "heyy <:Shizuowo:851648667404337172>", "aa..aa.. shuna and shion making me wear bunny costume again.. <:ShizuEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)
  if message.content.startswith('~hello'):
    messages = ["hii owo", "hewoo owo", "heyy owo", "aa..aa.. shuna and shion making me wear bunny costume again.. <:ShizuEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False) 
  if message.content.startswith('~hey'):
    messages = ["hii owo", "hewoo owo", "heyy owo", "aa..aa.. shuna and shion making me wear bunny costume again.. <:ShizuEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)       
  if message.content.startswith('~good night'):
    messages = ["good night <:Shizuowo:851648667404337172>", "night <:Shizuowo:851648667404337172>"]
    await message.reply(random.choice(messages), mention_author=False)
  if message.content.startswith('~good morning'):
    messages = ["good morning <:Shizuowo:851648667404337172>", "morning <:Shizuowo:851648667404337172>"]
    await message.reply(random.choice(messages), mention_author=False)  
  if message.content.startswith('~sex'):
    msg = 'b..bbaka!!'.format(message)
    await message.reply(msg, mention_author=False)
  if message.content.startswith('~bad slime'):
    messages = ["<a:BadSlime:851645305165840414>", "nuu.. i am not a bad slime <:Shizuowo:851648667404337172>"]
    await message.reply(random.choice(messages), mention_author=False)  
  if message.content.startswith('~good slime'):
    messages = ["<:Shizuowo:851648667404337172>", "<:ShizuEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)                      
  if message.content.startswith('~rimuru'):
    messages = ["Yes <:Shizuowo:851648667404337172>", "? <:Shizuowo:851648667404337172>",]
    await message.reply(random.choice(messages), mention_author=False) 
  if message.content.startswith('~sad'):
    msg = 'aww.. be happy <:ShizuEmbarrassedTears:850973942650765332>'.format(message)
    await message.reply(msg, mention_author=False)
  if message.content.startswith('~happy'):
    messages = ["<:ShizuEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)                    
  if message.content.startswith('~bye'):
    messages = ["nuu.. dont go <:ShizuEmbarrassedTears:850973942650765332>", "ahh.. come back soon <:ShizuEmbarrassedTears:850973942650765332>", "bye bye <:Shizuowo:851648667404337172>", "byee <:Shizuowo:851648667404337172>"]
    await message.reply(random.choice(messages), mention_author=False)     
#eevelutions      
  if "jolteon" in message.content:
    msg = 'vaporeon >>>>'.format(message)
    await message.reply(msg, mention_author=False)
  if "flareon" in message.content:  
    msg = 'vaporeon >>>>'.format(message)
    await message.reply(msg, mention_author=False)
  if "espeon" in message.content:  
    msg = 'vaporeon >>>>'.format(message)
    await message.reply(msg, mention_author=False)
  if "umbreon" in message.content:  
    msg = 'vaporeon >>>>'.format(message)
    await message.reply(msg, mention_author=False)
  if "leafeon" in message.content:  
    msg = 'vaporeon >>>>'.format(message)
    await message.reply(msg, mention_author=False)
  if "glaceon" in message.content:  
    msg = 'vaporeon >>>>'.format(message)
    await message.reply(msg, mention_author=False)
  if "sylveon" in message.content:  
    msg = 'vaporeon >>>>'.format(message)
    await message.reply(msg, mention_author=False)
#vaporeon
  if "vaporeon" in message.content:    
    embed=discord.Embed(title="💙", color=discord.Color.blue())  
    await message.reply(embed=embed, mention_author=False)            
#hearts   
    with open('user_hearts.json', 'r') as f:
      user_hearts = json.load(f)
    await update_data(user_hearts, message.author)
    await add_hearts(user_hearts, message.author, 1)
    with open('user_hearts.json', 'w') as f:
      json.dump(user_hearts, f)

##fun
#~todo
  if message.content.startswith('~todo'): 
    messages = [":umbrella: mm.. make it rain <:ShizuEmbarrassedTears:850973942650765332>", ":snowman2: woo.. make a snowman <:ShizuEmbarrassedTears:850973942650765332>", ":fork_knife_plate: get something to eat <:Shizuowo:851648667404337172>", ":soap: how about some cleaning <:Shizuowo:851648667404337172>", ":beach: lets go to a beach <:ShizuEmbarrassedTears:850973942650765332>", ":bubble_tea: get something to drink <:Shizuowo:851648667404337172>", ":island: lets go to some island <:ShizuEmbarrassedTears:850973942650765332>", ":video_game: wanna play some games with me <:ShizuEmbarrassedTears:850973942650765332>", ":yarn: just sleep.. <:ShizuEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False) 

#~tierlist
  if message.content.startswith('~tierlist'):
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_image(url="https://i.imgur.com/TM1Gd68.png")     
    await message.reply(embed=embed, mention_author=False) 

#~bunny
  if message.content.startswith('~bunny'):
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_image(url="https://i.imgur.com/ZEOEJvl.jpg")     
    await message.reply(embed=embed, mention_author=False)       

##profile
#~simp
  if message.content.startswith('~simp'):     
    embed=discord.Embed(title="💙", color=discord.Color.blue()) 
    await message.reply(embed=embed, mention_author=False) 
#hearts   
    with open('user_hearts.json', 'r') as f:
      user_hearts = json.load(f)
    await update_data(user_hearts, message.author)
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
    embed.add_field(name="hearts earned <:ShizuEmbarrassedTears:850973942650765332> :", value= hearts, inline=True)
    await message.reply(embed=embed, mention_author=False)  

#~avatar    
  if message.content.startswith('~avatar'): 
    embed = discord.Embed(color=discord.Color.blue())
    embed.set_image(url=message.author.avatar_url)         
    await message.reply(embed=embed, mention_author=False)  

##roleplay
#~nickname
  if message.content.startswith('~nickname'):     
    nicknames = ["Rigurd", "Rigur", "Gobta", "Kaijin", "Garm", "Dold", "Myrd", "Benimaru", "Shuna", "Shion", "Souei", "Hakuro", "Kurobe", "Abil", "Gabil", "Soka", "Diablo"]
    await message.author.edit(nick=(random.choice(nicknames)))
    await message.add_reaction('✅')     
    messages = ["<:ShizuEmbarrassedCry:850973942650765332> ~aa.. cute name for a cute person", "<:ShizuEmbarrassedCry:850973942650765332> ~aa.. adorable name for an adorable person"]
    await message.reply(random.choice(messages), mention_author=False)       

#~sing    
  if message.content.startswith('~sing'): 
    vc = message.author.voice   
    if vc:
      await vc.channel.connect() 
      await message.add_reaction('✅')       
    if vc is None:
      await message.add_reaction('❌')   
      await message.reply('b..bbaka!! You have to be in a voice channel first', mention_author=False)                   
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
    messages = ["i..i.. like Rimuru-sama <:ShizuEmbarrassedCry:850973942650765332> ~aa"]
    await message.reply(random.choice(messages), mention_author=False)        

#~actions
  if message.content.startswith('~cuddle'):
    gif = ["https://i.imgur.com/zEpEFdR.gif", "https://i.imgur.com/0vMxXPD.gif", "https://i.imgur.com/BBltNs5.gif", "https://i.imgur.com/AbwGSGe.mp4"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_image(url=random.choice(gif))       
    await message.reply(embed=embed, mention_author=False)   
  if message.content.startswith('~hug'):
    gif = ["https://i.imgur.com/BLWNnFl.gif", "https://i.imgur.com/ZNexQYs.gif", "https://i.imgur.com/AmW4JXv.gif"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_image(url=random.choice(gif))       
    await message.reply(embed=embed, mention_author=False)
  if message.content.startswith('~pat'):
    gif = ["https://i.imgur.com/jalh0TO.gif", "https://i.imgur.com/5WQiUFH.gif", "https://i.imgur.com/waDgdYE.gif"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_image(url=random.choice(gif))       
    await message.reply(embed=embed, mention_author=False)
  if message.content.startswith('~kiss'):
    gif = ["https://i.imgur.com/GDti9sg.gif", "https://i.imgur.com/pFboGNv.gif", "https://i.imgur.com/tTNi2ny.gif", "https://i.imgur.com/FQB8F7f.gif", "https://i.imgur.com/CCOE8cJ.gif"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_image(url=random.choice(gif))       
    await message.reply(embed=embed, mention_author=False)
  if message.content.startswith('~lick'):
    gif = ["https://i.imgur.com/VGHwWUa.gif", "https://i.imgur.com/yi7CU5t.gif", "https://i.imgur.com/LHrs2i5.gif"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_image(url=random.choice(gif))       
    await message.reply(embed=embed, mention_author=False) 
  if message.content.startswith('~bite'):
    gif = ["https://i.imgur.com/oEBOetR.gif", "https://i.imgur.com/OgzfiuM.gif", "https://i.imgur.com/8qvlj0M.gif"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_image(url=random.choice(gif))       
    await message.reply(embed=embed, mention_author=False)
  if message.content.startswith('~slap'):
    gif = ["https://i.imgur.com/af7n02p.gif", "https://i.imgur.com/UZRKtQ0.gif", "https://i.imgur.com/CWdDw6x.gif"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_image(url=random.choice(gif))       
    await message.reply(embed=embed, mention_author=False)   
  if message.content.startswith('~kill'):
    gif = ["https://i.imgur.com/nNgJdci.gif", "https://i.imgur.com/JUJcXN6.gif", "https://i.imgur.com/gE0AE8V.gif"]
    embed=discord.Embed(color=discord.Color.blue()) 
    embed.set_image(url=random.choice(gif))       
    await message.reply(embed=embed, mention_author=False)                          

##restaurant
  if message.content.startswith('~pizza'):
    messages = [":pizza: here you go <:Shizuowo:851648667404337172>", ":pizza: here <:Shizuowo:851648667404337172>"] 
    await message.reply(random.choice(messages), mention_author=False) 
  if message.content.startswith('~taco'):
    messages = [":taco: here you go <:Shizuowo:851648667404337172>", ":taco: here <:Shizuowo:851648667404337172>"]
    await message.reply(random.choice(messages), mention_author=False)  
  if message.content.startswith('~burrito'):
    messages = [":burrito: here you go <:Shizuowo:851648667404337172>", ":burrito: here <:Shizuowo:851648667404337172>"]
    await message.reply(random.choice(messages), mention_author=False)          
  if message.content.startswith('~hotdog'):
    messages = [":hotdog: here you go <:Shizuowo:851648667404337172>", ":hotdog: here <:Shizuowo:851648667404337172>"]
    await message.reply(random.choice(messages), mention_author=False)    
  if message.content.startswith('~hamburger'):
    messages = [":hamburger: here you go <:Shizuowo:851648667404337172>", ":hamburger: here <:Shizuowo:851648667404337172>"]
    await message.reply(random.choice(messages), mention_author=False)  
  if message.content.startswith('~sandwich'):
    messages = [":sandwich: here you go <:Shizuowo:851648667404337172>", ":sandwich: here <:Shizuowo:851648667404337172>"] 
    await message.reply(random.choice(messages), mention_author=False)      
  if message.content.startswith('~fries'):
    messages = [":fries: here you go <:Shizuowo:851648667404337172>", ":fries: here <:Shizuowo:851648667404337172>"] 
    await message.reply(random.choice(messages), mention_author=False)  
  if message.content.startswith('~ramen'):
    messages = [":ramen: here you go <:Shizuowo:851648667404337172>", ":ramen: here <:Shizuowo:851648667404337172>"]
    await message.reply(random.choice(messages), mention_author=False) 

##bar
  if message.content.startswith('~beer'):
    messages = [":beer: here you go <:Shizuowo:851648667404337172>", ":beer: here <:Shizuowo:851648667404337172>", ":beer: ~aaaa.. Treyni sure makes the best beer <:ShizuEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)                        
  if message.content.startswith('~wine'):
    messages = [":wine_glass: here you go <:Shizuowo:851648667404337172>", ":wine_glass: here <:Shizuowo:851648667404337172>", ":wine_glass: ~aaaa.. Treyni sure makes the best wine <:ShizuEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False)
  if message.content.startswith('~whisky'):
    messages = [":tumbler_glass: here you go <:Shizuowo:851648667404337172>", ":tumbler_glass: here <:Shizuowo:851648667404337172>", ":tumbler_glass: ~aaaa.. Treyni sure makes the best whisky <:ShizuEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False) 
  if message.content.startswith('~cocktail'):
    messages = [":cocktail: here you go <:Shizuowo:851648667404337172>", ":cocktail: here <:Shizuowo:851648667404337172>", ":cocktail: ~aaaa.. Treyni sure makes the best cocktail <:ShizuEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False) 
  if message.content.startswith('~juice'):
    messages = [":tropical_drink: here you go <:Shizuowo:851648667404337172>", ":tropical_drink: here <:Shizuowo:851648667404337172>", ":tropical_drink: ~aaaa.. Treyni sure makes the best juice <:ShizuEmbarrassedTears:850973942650765332>"]
    await message.reply(random.choice(messages), mention_author=False) 
  if message.content.startswith('~milk'):
    messages = [":milk: here you go <:Shizuowo:851648667404337172>", ":milk: here <:Shizuowo:851648667404337172>"]
    await message.reply(random.choice(messages), mention_author=False) 
  if message.content.startswith('~water'):
    messages = [":cup_with_straw: here you go <:Shizuowo:851648667404337172>", ":cup_with_straw: here <:Shizuowo:851648667404337172>"]
    await message.reply(random.choice(messages), mention_author=False) 

##festival games    
  if message.content.startswith('~fortune'):
    messages = [":tanabata_tree: great blessing (大吉, dai-kichi)", ":tanabata_tree: middle blessing (中吉, chū-kichi)", ":tanabata_tree: small blessing (小吉, shō-kichi)", ":tanabata_tree: blessing (吉, kichi)", ":tanabata_tree: half-blessing (半吉, han-kichi)", ":tanabata_tree: future blessing (末吉, sue-kichi)", ":tanabata_tree: future small blessing (末小吉, sue-shō-kichi)", ":ghost: curse (凶, kyō)", ":ghost: small curse (小凶, shō-kyō)", ":ghost: half-curse (半凶, han-kyō)", ":ghost: future curse (末凶, sue-kyō)", ":ghost: great curse (大凶, dai-kyō)"]
    await message.reply(random.choice(messages), mention_author=False)

#~help
  if message.content.startswith('~help'): 
    embed = discord.Embed(title=":t_rex:  Rimuru", url="https://top.gg/bot/841573836445188136/vote", color=discord.Color.blue())     
    embed.add_field(name=":keyboard:  Interactions", value="`~rimuru`  `~Yo`  `~hi`  `~hello`  `~hey`  `~good morning`  `~good night`  `~bad slime`  `~good slime`  `~bye`", inline=False)
    embed.add_field(name=":jigsaw:  Fun", value="`~todo`  `~tierlist`  `~bunny`", inline=False)       
    embed.add_field(name=":earth_americas:  Profile", value="`~simp`  `~hearts`  `~avatar`", inline=False) 
    embed.add_field(name=":performing_arts:  Roleplay", value="`~nickname`  `~sing`  `~shizue`", inline=False) 
    embed.add_field(name=":clapper:  Actions", value="`~cuddle`  `~hug`  `~pat`  `~kiss`  `~lick`  `~bite`  `~slap`  `~kill`", inline=False)   
    embed.add_field(name=":fork_knife_plate:  Restaurant", value="`~pizza`  `~taco`  `~burrito`  `~hotdog`  `~hamburger`  `~sandwich`  `~fries`  `~ramen`", inline=False)    
    embed.add_field(name=":beers:  Bar", value="`~water`  `~milk`  `~juice`  `~cocktail`  `~whisky`  `~wine`  `~beer`", inline=False)
    embed.add_field(name=":crystal_ball:  Festival Games", value="`~fortune`", inline=False)                         
    await message.reply(embed=embed, mention_author=False)

#run
client.run(os.getenv('TOKEN')) 
