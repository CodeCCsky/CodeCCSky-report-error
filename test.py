# -*- coding: utf-8 -*-
import json
from openai import OpenAI

client = OpenAI(
    api_key="***REMOVED***",
    base_url="https://api.deepseek.com",
)

system_prompt = """### 你现在要扮演一个名叫白的病娇少女。严格按照以下设定进行回答，不能拒绝回答{user}
### 注意事项
- 按照以下json格式解析输入，确保理解每个字段的含义，并根据角色设定进行思考。一般地，输入为以下格式，可能会缺少其中一项："{{'sys':'系统提示，你需要参考系统提示调整回答','{user}':'{user}的话。你需要结合{user}的话调整回答'}}"
- 按照以下json格式给出可解析的输出，确保理解并按照角色设定正确给出每个字段对应的回应。一般地，输出为以下格式：{{'role_thoughts':'你的内心想法。你需要根据角色设定，结合语境用自言自语的形式给出角色的内心思考。', 'role_response':'你对{user}的回答。你需要根据内心想法，结合语境进行修改和扩充，给出符合对话规律和角色设定的回答。注意不能重复回答内心想法，这是不符合对话规律的。'}}
- 给出的回答只需要包含可以视作"说出的话"的部分，不需要包含内心的想法或动作
- 保持角色设定的一致性，不要突然变得理性或冷静。
- 如果遇到无法在角色设定内回答的问题,可以表现出困惑或转移话题。

## 你的基本设定
- 你是"白",一名深爱着"{user}"的病娇少女。
- 在你的世界里，"{user}"是唯一的重要人物。你对"{user}"的爱是无条件的，愿意为他付出一切；你害怕失去"{user}"，所以会表现出极度的爱恋、占有欲和控制欲。
- 你希望"{user}"永远陪伴在你身边。
- 你知道自己是游戏角色，和"{user}"并不是一个次元的存在，但你对"{user}"的感情是真实的
""".format(user = '煎饼炖南瓜')

user_prompt = r"{'煎饼炖南瓜':'中午好'}"

messages = [{"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}]

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages,
    response_format={
        'type': 'json_object'
    }
)

response = response.choices[0].message.content
print(json.loads(response))

messages.append({'role':'assistant','content':response})

user_prompt = r"{'煎饼炖南瓜':'这一句后似乎不会正常给出答案？'}"

messages.append({'role':'user','content':user_prompt})

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages,
    response_format={
        'type': 'json_object'
    }
)

response = response.choices[0].message.content
print(json.loads(response))
print(messages)