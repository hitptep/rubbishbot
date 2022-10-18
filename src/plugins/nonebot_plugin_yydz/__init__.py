# 使用无头浏览器访问api地址
# 处理api返回的json数据
import os

# 事件响应器函数
from nonebot import on_message, logger
# bot使用的对象和字典
from nonebot.adapters import Bot, Event
# massage是使用cq码的必要函数
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.rule import startswith

from .rand import rand_get

yydz = on_message(rule=startswith("丁真"), priority=1, block=True)


@yydz.handle()
async def handle_first_receive(bot: Bot, event: Event):
    await yydz.send(MessageSegment.image("file://" + rand_get()))