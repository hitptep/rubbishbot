import re

import openai
from nonebot.plugin.on import on_message, on_notice, on_command
from nonebot.rule import to_me
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import (
    GroupMessageEvent,
    Message,
    MessageEvent,
    PokeNotifyEvent,
    MessageSegment
)


# 优先级99, 条件: 艾特bot就触发
zzychatgpt = on_message(rule=to_me(), priority=99, block=False)
# 优先级1, 不会向下阻断, 条件: 戳一戳bot触发
#poke_ = on_notice(rule=to_me(), block=False)


@zzychatgpt.handle()
async def _(event: MessageEvent):
    # 获取消息文本
    msg = str(event.get_message())
    # 去掉带中括号的内容(去除cq码)
    msg = re.sub(r"\[.*?\]", "", msg)
    # 如果是光艾特bot(没消息返回),就回复以下内容
    if msg.isspace():
        print("有人艾特我")
        text="你好呀"
    else:
        print("用户输入了:"+msg)

    # 设置API密钥和模型ID
    openai.api_key = "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"
    model_id = "text-davinci-003"

    # 设置请求参数
    prompt = msg
    temperature = 0.5
    max_tokens = 300
    stop = None
    try:
        # 发送API请求
        response = openai.Completion.create(
            model=model_id,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            stop=stop
        )

        # 检查响应状态码
        print(response)
        output_text = response["choices"][0]["text"]
    except openai.error.RateLimitError as limit:
        print("出错了",limit)
        output_text="憋叭叭了，ChatGPT都崩了，等会吧"

    await zzychatgpt.send(MessageSegment.text(output_text))




