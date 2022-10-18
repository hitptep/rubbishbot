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

from .picget import get_pic

yydz = on_message(rule=startswith("paint"), priority=1, block=True)


@yydz.handle()
async def handle_first_receive(bot: Bot, event: Event):
    msg = str(event.get_message())
    msg = msg.lstrip("paint")
    logger.info("发送图片:" + msg)
    img_path=get_pic(msg)
    if img_path == "timeout":
        await yydz.send(MessageSegment.text("超时了！再超时就超市里～"))
    else:
        await yydz.send(MessageSegment.image("file://"+img_path))
    os.remove(img_path)
