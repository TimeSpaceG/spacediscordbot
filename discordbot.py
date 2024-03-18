import discord
from discord.ext import commands

# 봇 설정
TOKEN = 'QAIUu22utYQZv82IEGId7QWtoBUEiou3'
bot = commands.Bot(command_prefix='!')

# 봇이 준비되었을 때 실행할 코드
@bot.event
async def on_ready():
    print(f'{bot.user}이(가) 성공적으로 로그인했습니다.')

# 메시지 처리: "안녕" 명령어에 대한 응답
@bot.command(name='정애니맨')
async def say_hello(ctx):
    await ctx.send('네 안녕하세요 정애니맨 봇입니다.')

# 음성 채널 지원: 음성 채널 입장
@bot.command(name='들어와')
async def join_voice(ctx):
    channel = ctx.author.voice.channel
    if channel:
        await channel.connect()
    else:
        await ctx.send("음성 채널에 먼저 들어가주세요.")

# 이벤트 처리: 사용자 조인 시 환영 메시지 전송
@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel:
        await channel.send(f'{member.mention}님, 환영합니다!')

# 멀티 서버 지원: 현재 서버 목록 출력
@bot.command(name='서버목록')
async def list_servers(ctx):
    servers = list(bot.guilds)
    server_list = "\n".join([f"{server.name} (ID: {server.id})" for server in servers])
    await ctx.send(f"현재 봇이 참여한 서버 목록:\n{server_list}")

# 봇 실행
bot.run(TOKEN)
