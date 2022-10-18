import json
import os
import time
import requests
import timeout_decorator
from src.plugins.nonebot_plugin_aipaint import abspath

folder_path = abspath.load_file()

@timeout_decorator.timeout(20)
def get(prompt, style='32'):
    s = requests.session()
    login_url = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key' \
                '=AIzaSyDCvp5MTJLUdtBYEKYWXJrlLzu1zuKM6Xw '
    url = 'https://paint.api.wombo.ai/api/tasks/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    payload = {
        "returnSecureToken": True,
        "email": "zzy@zzy.com",
        "password": "8*cRrmR^6WTn3@ii"
    }
    payload = json.dumps(payload)
    login_respone = s.request('POST', url=login_url, headers=headers, data=payload)
    idtoken = login_respone.json()['idToken']
    headers['authorization'] = 'bearer ' + idtoken
    respone = s.request('POST', url=url, headers=headers)
    new_headers = respone.json()
    print(new_headers)
    new_id = new_headers['id']
    param = {
        'input_spec': {
            "style": str(style),
            "prompt": prompt,
            "display_freq": '10'
        }
    }
    param = json.dumps(param)
    respone2 = s.put(url=url + new_id, headers=headers, data=param)
    result = respone2.json()
    while True:
        time.sleep(4)
        respone2 = s.request('GET', url=url + new_id, headers=headers, data=new_headers)
        result = respone2.json()
        print(result)
        if result['result'] is not None:
            break
    pic_url = result['result']['final']
    pic = s.request('GET', url=pic_url, headers=headers).content
    pic_name = 0
    img_path = folder_path + str(pic_name) + ".jpg"
    while os.path.exists(img_path):
        pic_name = pic_name + 1
        img_path = folder_path + str(pic_name) + ".jpg"
    with open(img_path, 'wb') as f:
        f.write(pic)
    print(f'下载完毕,路径：{img_path}')
    return img_path

def get_pic (prompt, style='32'):
    try:
        return get(prompt,style='32')
    except Exception as e:
        print("超时！！")
        return "timeout"