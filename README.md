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

### 二、修改src中go-cqhttps文件夹下的config.yml

```
universal: ws://127.0.0.1:这里填写.env文件中的PORT/onebot/v11/ws
```

若不是Windows 64位系统，请使用
