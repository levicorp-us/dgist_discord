import lightbulb
import hikari
import random
import discord
from datetime import date

plugin = lightbulb.Plugin('Lectures')

@plugin.command
@lightbulb.option('time', '학식의 시간대', required=False, type=str)
@lightbulb.command('수업', '오늘의 수업 정보를 알려줍니다')
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def 수업(ctx: lightbulb.Context):
    pass

@수업.child
@lightbulb.option('time', '학식의 시간대', required=False, type=str)
@lightbulb.command('업데이트', '수업 정보를 업데이트합니다')
@lightbulb.implements(lightbulb.PrefixSubGroup)
async def 업데이트(ctx: lightbulb.Context):
    pass

@수업.child
@lightbulb.option('time', '학식의 시간대', required=False, type=str)
@lightbulb.command('연구동', '연구동 학식 정보를 불러옵니다')
@lightbulb.implements(lightbulb.PrefixSubGroup)
async def 등록(ctx: lightbulb.Context):
    await ctx("응아잇어")

@수업.child
@lightbulb.option('time', '학식의 시간대', required=False, type=str)
@lightbulb.command('교직원', '교직원 학식 정보를 불러옵니다')
@lightbulb.implements(lightbulb.PrefixSubGroup)
async def 교직원(ctx: lightbulb.Context):
    pass

def load(bot):
    bot.add_plugin(plugin)