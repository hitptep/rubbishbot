# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/10 19:46
# Description:

from nonebot import on_request, on_notice, on_command
from nonebot.adapters.onebot.v11 import Event, FriendRequestEvent, GroupRequestEvent
from nonebot.log import logger
from nonebot.plugin.on import on_message
from nonebot.typing import T_State
from nonebot.adapters import Bot
from nonebot.rule import to_me


__usage__ = '''这不是你该看的功能'''

__help_version__ = '' 

__help_plugin_name__ = "自动功能2" 


friend_req = on_request()

ai = on_message(rule=to_me(), priority=99, block=False)

@friend_req.handle()
async def friend_req(bot: Bot, event: FriendRequestEvent, state: T_State):
    logger.debug('friend req called')
    logger.debug(event.json())
    await bot.call_api('set_friend_add_request', flag=event.flag, approve=True)
    message = "你好！我是垃圾bot！\n我的家：https://github.com/hitptep/rubbishbot\n我的教程：http://zzy.js.cool/posts/2022/09/26/Python%E6%90%AD%E5%BB%BAQQbot.html"
    await ai.finish(message=message)
    # await bot.set_friend_add_request()


group_req = on_request()


@group_req.handle()
async def group_req(bot: Bot, event: GroupRequestEvent, state: T_State):
    logger.debug('group req called')
    logger.debug(event.json())
    logger.debug(event.flag)
    await bot.call_api('set_group_add_request', flag=event.flag, approve=True)
    message = "你好！我是垃圾bot！\n我的家：https://github.com/hitptep/rubbishbot\n我的教程：http://zzy.js.cool/posts/2022/09/26/Python%E6%90%AD%E5%BB%BAQQbot.html"
    await ai.finish(message=message)
    # await bot.set_group_add_request(approve=True)