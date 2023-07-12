# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

#refresh_poco通用刷新poco列表

def refresh_poco(needclick_poco):
    
    a_bool=poco(needclick_poco).exists
    while a_bool:
        if a_bool:
            #如果布尔类型为True
            #log("aaa")
            poco(needclick_poco).click()
            #点击按钮
            break
            #跳出循环
        else:
            #如果布尔类型为False
            poco(needclick_poco).refresh()
        
        
        
def double_changeuse(devices,devices2):
#多台设备使用
#print(G.DEVICE_LIST)
    set_current(devices)


    set_current(devices2)

def poco_Parametric ():
    sleep(1)
    sss='com.starmakerinteractive.starmaker'#这里参数名大家按函数名的定义去走，我这里示范就随便写的
    qqq=':id/tab_animation_view'

    #name=sss+':id/tab_animation_view'使用第三个参数去拼接
    #poco(name)[2].click()
    
    #直接一半去拼接，这样的方法好在定义了包名的话，以后tvp或者sm都可以使用
    #poco(sss+':id/tab_animation_view')[2].click()
    
    #直接在poco里面去用+拼接，这样最省事
    poco(sss+qqq)[2].double_click()
    print(aaa)
    
def back_paryt():
    #使用deepling跳转到party页
    shell("am start sm://discovery")
# back_party()


def init_room(function):
    #使用房间在线人数判断是否处于房间内
    if poco("com.starmakerinteractive.starmaker:id/online_user_num_text").exists()==True:
#         执行对应代码
#        
#    在房间内
        #poco("com.starmakerinteractive.starmaker:id/online_user_num_text").click()
        function()
        #back_paryt()
        #log("aaa")
    else:
        #不在房间内
        #log("bbb")
        shell("am start sm://party_room?roomId=7885")
#init_room(back_paryt)
#使用方法