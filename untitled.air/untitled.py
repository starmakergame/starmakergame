# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# print(G.DEVICE_LIST)

# set_current("R58N51LLHSV")
# sleep(10.0)

# touch(Template(r"tpl1681959240472.png", record_pos=(-0.356, -0.122), resolution=(1080, 2400)))
# sleep(5.0)
# touch(Template(r"tpl1681959256236.png", record_pos=(0.003, 0.914), resolution=(1080, 2400)))


# sleep(5.0)

# set_current("ad3b6d97")
# sleep(10.0)
# touch(Template(r"tpl1681959385678.png", record_pos=(-0.069, -0.058), resolution=(720, 1600)))



poco("com.starmakerinteractive.thevoice:id/room_programme_entrance_view").click()
#点击小箭头，弹出节目单
a_bool=poco("com.starmakerinteractive.thevoice:id/tv_des").exists
#初始化一个布尔类型，存储最开始为找不到控件的False
for i in range(10):
    #简单写个10次for循环，或者循环到找到控件为True
    if a_bool:
        #如果布尔类型为True
        #log("aaa")
        poco("com.starmakerinteractive.thevoice:id/tv_des").click()
        #点击按钮
        break
        #跳出循环
    else:
        #如果布尔类型为False
        poco("com.starmakerinteractive.thevoice:id/tv_des").refresh()
        #刷新poco整体状态   
#在控制刷新率提高的情况下，下一行代码可以直接完成点击
#poco("com.starmakerinteractive.thevoice:id/tv_des").click()





# bbb=poco("com.starmakerinteractive.thevoice:id/tv_des").get_text

# log(bbb)