import openai
openai.api_key ="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"
model_engine = "text-davinci-003"
prompt = "如何评价哈尔滨工业大学威海校区"
try:
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=4000
    )
except:
    text="出错了，再出错超市你"
else:
    text=response.choices[0].text

# 输出响应文本
print(response.choices[0].text)