# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
def quick_game():#定义一个quick_game函数，方便以后调用，这里起名字我们使用某一个固定的原则，我这里是习惯使用这样的规则，中间使用下划线
    poco(text="快速加入游戏").click()#找到文本显示是快速游戏的按钮并进行点击
    #poco(text="选择游戏立刻开玩").click()
    #if poco(text="LUDO").wait_for_appearance():
    #sleep(1)
    poco(text="LUDO").click()#找到文本显示是LUDO的按钮并进行点击
    poco(text="开始匹配").click()#找到文本显示是开始匹配的按钮并进行点击
    #poco("com.starmakerinteractive.starmaker:id/tab_animation_view")[3].click()
#quick_game()    
def aaa():#这里是受进国那个框架的启发，他把每个用到的控件都进行了命名，这样子方便以后修改，但是我考虑到咱们普遍的水平，这里直接使用参数来拼接控件名，更加简单一点，也方便日后的修改
    sleep(1)
    sss='com.starmakerinteractive.starmaker'#这里参数名大家按函数名的定义去走，我这里示范就随便写的
    qqq=':id/tab_animation_view'

    #name=sss+':id/tab_animation_view'使用第三个参数去拼接
    #poco(name)[2].click()
    
    #直接一半去拼接，这样的方法好在定义了包名的话，以后tvp或者sm都可以使用
    #poco(sss+':id/tab_animation_view')[2].click()
    
    #直接在poco里面去用+拼接，这样最省事
    poco(sss+qqq)[2].click()
    print(aaa)
#aaa()    