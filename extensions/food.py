import lightbulb
import sys
import json
import random
import datetime

td = datetime.timedelta(hours=9)
tz = datetime.timezone(td)

sys.path.append('/home/dgist/discord/dgist_discord/background')

plugin = lightbulb.Plugin('학식')

in_update = False

def get_food_info(p=None, t=None):
    with open('food.json', 'r') as f:
        data = json.load(f)
    food_court_list = ['연구동 점심', '연구동 저녁', '학생식당 점심 일반식', '학생식당 점심 특식', '학생식당 저녁', '교직원 점심']
    food_data = ['**' + place + '**:\n```' + time + '```' for place, time in zip(food_court_list, data.values())]
    if p==None and t==None:
        return ''.join(food_data)
    if p==None and t != None:
        if t == '점심': return''.join([food_data[0], food_data[2],food_data[3],food_data[5]])
        elif t == '저녁': return''.join([food_data[1], food_data[4]])
        else: return '\'점심\' 혹은 \'저녁\'을 입력하여 주세요'
    elif p == '연구동':
        if t == None: return ''.join(food_data[0:2])
        if t == '점심': return food_data[0]
        elif t == '저녁': return food_data[1]
        else: return '\'점심\' 혹은 \'저녁\'을 입력하여 주세요'
    if p == '학생식당':
        if t == None: return ''.join(food_data[2:5])
        if t == '점심': return ''.join(food_data[2:4])
        elif t == '저녁': return food_data[4]
        else: return '\'점심 일반식\' 혹은 \'점심 특식\' 혹은 \'저녁\'을 입력하여 주세요'
    if p == '교직원':
        if t == None or t == '점심': return food_data[5]
        else: return '교직원 식당은 점심만 운영합니다\n' + food_data[5]

def roll_dice(probability:float)->bool:
    num = random.randint(0,100)
    if num <= probability:
        return True
    return False

@plugin.command
@lightbulb.option('time', '학식의 시간대', required=False, type=str)
@lightbulb.command('학식', '학식 정보를 알려줍니다')
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def 학식(ctx: lightbulb.Context):
    if roll_dice(3):
        await ctx.respond("먹지마")
    elif ctx.options.time:
        await ctx.respond(get_food_info(None, ctx.options.time))
    elif datetime.datetime.now(tz=tz).strftime('%H') >= "13":
        await ctx.respond(get_food_info(None, '저녁'))
    else:
        await ctx.respond(get_food_info(None, '점심'))

@학식.child
@lightbulb.option('time', '학식의 시간대', required=False, type=str)
@lightbulb.command('학생식당', '학생식당 학식 정보를 불러옵니다')
@lightbulb.implements(lightbulb.PrefixSubGroup)
async def 학생식당(ctx: lightbulb.Context):
    print(ctx.options.time)
    if roll_dice(3):
        await ctx.respond("먹지마")
    else:
        await ctx.respond(get_food_info('학생식당', ctx.options.time))

@학식.child
@lightbulb.option('time', '학식의 시간대', required=False, type=str)
@lightbulb.command('연구동', '연구동 학식 정보를 불러옵니다')
@lightbulb.implements(lightbulb.PrefixSubGroup)
async def 연구동(ctx: lightbulb.Context):
    print(ctx.options.time)
    if roll_dice(3):
        await ctx.respond("먹지마")
    else:
        await ctx.respond(get_food_info('연구동', ctx.options.time))

@학식.child
@lightbulb.option('time', '학식의 시간대', required=False, type=str)
@lightbulb.command('교직원', '교직원 학식 정보를 불러옵니다')
@lightbulb.implements(lightbulb.PrefixSubGroup)
async def 교직원(ctx: lightbulb.Context):
    print(ctx.options.time)
    if roll_dice(3):
        await ctx.respond("먹지마")
    else:
        await ctx.respond(get_food_info('교직원', ctx.options.time))

def load(bot):
    bot.add_plugin(plugin)