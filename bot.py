from multiprocessing import freeze_support

import nonebot

from nonebot.adapters.onebot.v11 import Adapter



if __name__ == '__main__':
    #初始化
    nonebot.init()
    #app = nonebot.get_asgi()
    driver = nonebot.get_driver()
    driver.register_adapter(Adapter)

    #加载导入的包插件
    #nonebot.load_plugin('nonebot_plugin_chatgpt')
    nonebot.load_plugin('nonebot_plugin_addFriend')

    #加载本地插件
    nonebot.load_plugins("src/plugins")

    #run
    nonebot.run()
    freeze_support()
