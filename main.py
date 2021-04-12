import discord,random,os,time,json
import jishaku as jsk
from discord.ext import commands

#move later
div=lambda:print("-"*os.get_terminal_size().columns)
fp=lambda *x:os.path.join(".",*x)
j=lambda *x:os.path.join(".")

async def say(ctx,s):
	res=await ctx.send(s)
	return res

#CONFIG FILE FP
conf_fp=fp("conf.json")

f=open(conf_fp,"r+")
conf=json.load(f)
f.close()
del f

t=conf["token"]
description=conf["description"]
pfx=conf["prefix"]
color=discord.Color(int(conf["color"].replace("#","").lower(),16))
game=conf["game"]


bot=commands.Bot(command_prefix=pfx,case_insensitive=True,description=description,intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=game),status=discord.Status.dnd)
    div()
    print("Logged in as:")
    print(f"@{bot.user.name}#{bot.user.discriminator}")
    print(f"<@!{bot.user.id}>")
    div()

@bot.group()
async def hsk(ctx):
    if ctx.invoked_subcommand is None:
    	await say(ctx,":x: __***F U C K Y O U***__ :x:")

@hsk.command(name="do")
async def _do(ctx):
	msg=await say(ctx,"```\nDoing...\n```")
	time.sleep(5)
	await msg.edit(content="```\nDone!!!\n```")

@hsk.command(name="kys")
async def _kys(ctx):
	e=discord.Embed(title="I cant take it anymore...",color=color)
	await ctx.send(embed=e)
	await bot.close()

@bot.command(name="add")
async def _add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command(name="roll")
async def _roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(name="choose",description='For when you wanna settle the score some other way')
async def _choose(ctx, *choices: str):
	await ctx.send(random.choice(choices))

@bot.command(name="repeat")
async def _repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)
        
@bot.command(name="rep")
async def _rep(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

@bot.command(name="joined")
async def _joined(ctx, member: discord.Member):
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.group()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@cool.command(name='bot')
async def _bot(ctx):
    await ctx.send('Yes, the bot is cool.')

bot.load_extension("jishaku")
bot.run(t)