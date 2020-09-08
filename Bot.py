import discord
from discord import utils
from discord.ext import commands
import random
import asyncio
import time
import nekos
import json
import datetime
import os

Bot = commands.Bot(command_prefix='!') Arguments = ['feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo', 'solog', 'feetg', 'cum', 'erokemo', 'les', 'wallpaper', 'lewdk', 'ngif', 'tickle', 'lewd', 'feed', 'gecg', 'eroyuri', 'eron', 'cum_jpg', 'bj', 'nsfw_neko_gif', 'solo', 'kemonomimi', 'nsfw_avatar', 'gasm', 'poke', 'anal', 'slap', 'hentai', 'avatar', 'erofeet', 'holo', 'keta', 'blowjob', 'pussy', 'tits', 'holoero', 'lizard', 'pussy_jpg', 'pwankg', 'classic', 'kuni', 'waifu', 'pat', '8ball', 'kiss', 'femdom', 'neko', 'spank', 'cuddle', 'erok', 'fox_girl', 'boobs', 'random_hentai_gif', 'smallboobs', 'hug', 'ero', 'smug', 'goose', 'baka', 'woof']
def is_nsfw():
    async def predicate(ctx):
        return ctx.channel.is_nsfw()
    return commands.check(predicate)

queue = []

from discord import Activity, ActivityType

@Bot.event
async def on_ready():
    print("Бот запустился")
    await Bot.change_presence(status=discord.Status.idle,activity=Activity(name="Наблюдает за коронавирусом",type=ActivityType.watching))


@Bot.command(aliases=['roll'])
async def _roll(ctx, number:int):
	num = random.randint(0,random.randint(0, number))
	await ctx.send(f'Вам выпало число: {num}')


@Bot.command()
async def mute(ctx,member:discord.Member,time:int,reason):
    role = discord.utils.get(ctx.guild.roles,id=742127675237335060)
    channel = Bot.get_channel(738748365118111744)
    await member.add_roles(role)
    emb = discord.Embed(title="Мут",color=0x2f3136)
    emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Нарушитель',value=member.mention,inline=False)
    emb.add_field(name='Причина',value=reason,inline=False)
    emb.add_field(name="Время",value=time,inline=False)
    await channel.send(embed = emb)
    await asyncio.sleep(time*60 )
    emb = discord.Embed(title="Анмут",color=0x2f3136)
    emb.add_field(name='Модератор',value='<@709725675711496233>',inline=False)
    emb.add_field(name='Нарушитель',value=member.mention,inline=False)
    emb.add_field(name='Причина',value="Время мута вышло",inline=False)
    await channel.send(embed=emb)
    await member.remove_roles(role)


@Bot.command()
async def unmute(ctx,member:discord.Member):
    channel = Bot.get_channel(738748365118111744)
    muterole = discord.utils.get(ctx.guild.roles,id=742127675237335060)
    emb = discord.Embed(title="Анмут",color=0xff0000)
    emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Нарушитель',value=member.mention,inline=False)
    await channel.send(embed = emb)
    await member.remove_roles(muterole)


@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def kick(ctx,member:discord.Member,reason):
    channel = Bot.get_channel(738748365118111744)
    emb = discord.Embed(title="Кик",color=0xff0000)
    emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Нарушитель',value=member.mention,inline=False)
    emb.add_field(name='Причина',value=reason,inline=False)
    await member.kick()
    await channel.send(embed = emb)


@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def ban(ctx,member:discord.Member,reason):
    channel = Bot.get_channel(738748365118111744)
    emb = discord.Embed(title="Кик",color=0xff0000)
    emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Нарушитель',value=member.mention,inline=False)
    emb.add_field(name='Причина',value=reason,inline=False)
    await member.ban()
    await channel.send(embed = emb)
 
 
@Bot.command()
async def clear(ctx,amount=10):
    await ctx.message.channel.purge(limit=amount + 1)


@Bot.command()
async def info(ctx,member:discord.Member):
    emb = discord.Embed(title='Информация о пользователе',color=0xff0000)
    emb.add_field(name="Когда присоединился:",value=member.joined_at,inline=False)
    emb.add_field(name='Имя:',value=member.display_name,inline=False)
    emb.add_field(name='Айди:',value=member.id,inline=False)
    emb.add_field(name="Аккаунт был создан:",value=member.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"),inline=False)
    emb.set_thumbnail(url=member.avatar_url)
    emb.set_footer(text=f"Вызвано:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
    emb.set_author(name=ctx.message.author,icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed = emb)



@Bot.command()
async def timely(ctx):
    with open('economy.json','r') as f:
        money = json.load(f)
    if not str(ctx.author.id) in money:
        money[str(ctx.author.id)] = {}
        money[str(ctx.author.id)]['Money'] = 0

    if not str(ctx.author.id) in queue:
        emb = discord.Embed(description=f'**{ctx.author}** Вы получили свои 1250 монет')
        await ctx.send(embed= emb)
        money[str(ctx.author.id)]['Money'] += 1250
        queue.append(str(ctx.author.id))
        with open('economy.json','w') as f:
            json.dump(money,f)
        await asyncio.sleep(12*60)
        queue.remove(str(ctx.author.id))
    if str(ctx.author.id) in queue:
        emb = discord.Embed(description=f'**{ctx.author}** Вы уже получили свою награду')
        await ctx.send(embed= emb)

@Bot.command(aliases=['bal'])
async def balance(ctx,member:discord.Member = None):
    if member == ctx.author or member == None:
        with open('economy.json','r') as f:
            money = json.load(f)
        emb = discord.Embed(description=f'У **{ctx.author}** {money[str(ctx.author.id)]["Money"]} монет')
        await ctx.send(embed= emb)
    else:
        with open('economy.json','r') as f:
            money = json.load(f)
        emb = discord.Embed(description=f'У **{member}** {money[str(member.id)]["Money"]} монет')
        await ctx.send(embed= emb)

@Bot.command()
async def give(ctx,member:discord.Member,arg:int):
    with open('economy.json','r') as f:
        money = json.load(f)
    if money[str(ctx.author.id)]['Money'] >= arg:
        emb = discord.Embed(description=f'**{ctx.author}** подарил **{member}** **{arg}** монет')
        money[str(ctx.author.id)]['Money'] -= arg
        money[str(member.id)]['Money'] += arg
        await ctx.send(embed = emb)
    else:
        await ctx.send('У вас недостаточно денег')
    with open('economy.json','w') as f:
        json.dump(money,f)


@Bot.command()
@is_nsfw()
async def cum(ctx):
    emb = discord.Embed(color=0xebebeb)
    emb.set_image(url=nekos.img('cum'))
    await ctx.send(embed=emb)


token = os.environ.get('token')
