
import os

# 事件响应器函数
from nonebot import on_message, logger
# bot使用的对象和字典
from nonebot.adapters import Bot, Event
# massage是使用cq码的必要函数
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.rule import startswith



rubbishhelp = on_message(rule=startswith("help"), priority=1, block=True)


@rubbishhelp.handle()
async def handle_first_receive(bot: Bot, event: Event):
    await rubbishhelp.send(MessageSegment.text("我是啵啵bot，目前有以下功能：\n①ChatGPT聊天：艾特机器人并搭配文字即可聊天\n②自动加群/好友:机器人会自动同意好友和群请求\n③随机发送一张顶针图:发以丁真为开头的话，即可收到一张一眼丁真的祝福"))