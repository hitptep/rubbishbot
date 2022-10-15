from nonebot.rule import startswith

from .picget import get_pic
# 事件响应器函数
from nonebot import on_command, on_message, logger
# bot使用的对象和字典
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
# massage是使用cq码的必要函数
from nonebot.adapters.onebot.v11 import MessageSegment
# 使用无头浏览器访问api地址
import urllib3
# 处理api返回的json数据
import os

paint = on_message(rule=startswith("piant"), priority=1, block=True)


@paint.handle()
async def handle_first_receive(bot: Bot, event: Event):
    msg = str(event.get_message())
    msg = msg.lstrip("piant")
    logger.info("发送图片:" + msg)
    img_path=get_pic(msg)
    await paint.send(MessageSegment.image("file://"+img_path))
    os.remove(img_path)
