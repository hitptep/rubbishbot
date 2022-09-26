import nonebot

from nonebot.adapters.onebot.v11 import Adapter


#初始化
nonebot.init()
#app = nonebot.get_asgi()
driver = nonebot.get_driver()
driver.register_adapter(Adapter)

#加载导入的包插件
#nonebot.load_plugin("path.to.your.plugin")

#加载本地插件
nonebot.load_plugins("src/plugins")

#run
nonebot.run()

