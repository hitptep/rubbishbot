# 垃圾bot：基于Nonebot2和go-cqhttps的第五人格聊天群QQbot

**<u>声明：本项目仅供学习使用，禁止用作商业用途，使用时请遵循GPL许可证</u>**

**目前已实现的功能：**

*#自动回复*

*#自动添加好友/群*

### 使用方法：

### 一、在项目根目录下创建文件.env,文件内容为:

```
HOST=127.0.0.1  # 配置 NoneBot2 监听的 IP/主机名
PORT=  # 配置 NoneBot2 监听的端口,请注意与go-cqhttps中的监听端口一致
SUPERUSERS=["QQ号", "密码"]  # 配置 NoneBot 超级用户
NICKNAME=["垃圾bot"]  # 配置机器人的昵称
COMMAND_START=["#", ""]  # 配置命令起始字符
COMMAND_SEP=["."]  # 配置命令分割字符
```

### 二、下载go-cqhttps

请在[go-cqhttps Release](https://github.com/Mrs4s/go-cqhttp/releases/tag/v1.0.0-rc3)页面上下载系统对应的安装程序，按照安装程序运行（选择反向Websocket)后自行修改config.yml。
```
universal: ws://127.0.0.1:这里填写.env文件中的PORT/onebot/v11/ws
```

也可以修改config.yml中的QQ号和密码，不修改就使用二维码登录。

PS:go-cqhttp开发者的服务器好像被墙了，记得科学上网QAQ



### 三、开启go-cqhttps，运行bot.py

### *<u>**详细教程：[点我](http://zzy.js.cool/posts/2022/09/26/Python%E6%90%AD%E5%BB%BAQQbot.html)**</u>*
