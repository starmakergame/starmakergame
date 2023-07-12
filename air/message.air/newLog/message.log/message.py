# -*- encoding=utf8 -*-
__author__ = "cuimeina"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

#启动APP
# start_app("com.starmakerinteractive.starmaker")
# sleep(10)
#发送一条私信
def message_text(msg):
    liaotian1 = exists(Template(r"tpl1681900686360.png", rgb=True, record_pos=(0.196, 0.913), resolution=(1080, 2400)))

    if liaotian1:
        touch(Template(r"tpl1681900783791.png", record_pos=(0.199, 0.92), resolution=(1080, 2400)))

        touch(Template(r"tpl1680773957101.png", record_pos=(-0.183, -0.834), resolution=(1080, 2400)))
        

        if exists(Template(r"tpl1684999744815.png", record_pos=(-0.109, -0.722), resolution=(1080, 2400))):

            touch(Template(r"tpl1684999754743.png", record_pos=(-0.117, -0.724), resolution=(1080, 2400)))

            touch(Template(r"tpl1680601729014.png", record_pos=(-0.086, 0.775), resolution=(1080, 2400)))
            text(msg)

            touch(Template(r"tpl1680602061683.png", record_pos=(0.41, 0.004), resolution=(1080, 2400)))
            keyevent("BACK")
            

            touch(Template(r"tpl1684131883609.png", record_pos=(-0.398, 0.905), resolution=(1080, 2400)))
            touch(Template(r"tpl1684141228797.png", record_pos=(-0.407, 0.924), resolution=(1080, 2400)))
            touch(Template(r"tpl1685001765828.png", record_pos=(0.0, 0.317), resolution=(1080, 2400)))
            touch(Template(r"tpl1684140845166.png", record_pos=(0.4, 0.002), resolution=(1080, 2400)))
            
            

            touch(Template(r"tpl1684136761522.png", record_pos=(0.406, 0.13), resolution=(1080, 2400)))
            touch(Template(r"tpl1684136763836.png", record_pos=(-0.366, 0.3), resolution=(1080, 2400)))
            touch(Template(r"tpl1684136766138.png", record_pos=(-0.177, 0.224), resolution=(1080, 2400)))
            touch(Template(r"tpl1684136768269.png", record_pos=(-0.373, 0.392), resolution=(1080, 2400)))
            touch(Template(r"tpl1684136770676.png", record_pos=(0.191, 0.311), resolution=(1080, 2400)))
            touch(Template(r"tpl1684136774228.png", record_pos=(0.409, 0.133), resolution=(1080, 2400)))
            touch(Template(r"tpl1684136777657.png", record_pos=(-0.119, 0.406), resolution=(1080, 2400)))
            sleep(3)
            touch(Template(r"tpl1684136780143.png", record_pos=(0.406, 0.369), resolution=(1080, 2400)))
            
            
            touch(Template(r"tpl1684139938542.png", record_pos=(0.211, 0.136), resolution=(1080, 2400)))
            touch(Template(r"tpl1684139918937.png", record_pos=(0.381, 0.366), resolution=(1080, 2400)))
            touch(Template(r"tpl1684139967766.png", record_pos=(0.038, 0.912), resolution=(1080, 2400)))
            if exists(Template(r"tpl1684999653263.png", record_pos=(-0.006, -0.013), resolution=(1080, 2400))):
                touch(Template(r"tpl1684999667605.png", record_pos=(0.004, 0.275), resolution=(1080, 2400)))
            sleep(5)
            touch(Template(r"tpl1684139976763.png", record_pos=(0.228, -0.686), resolution=(1080, 2400)))
            sleep(3)
            if exists(Template(r"tpl1684999034798.png", record_pos=(0.0, -0.015), resolution=(1080, 2400))):
                touch(Template(r"tpl1684999049729.png", record_pos=(-0.004, -0.047), resolution=(1080, 2400)))
            
            touch(Template(r"tpl1684139991868.png", record_pos=(0.384, -0.547), resolution=(1080, 2400)))
            touch(Template(r"tpl1684140000771.png", record_pos=(0.002, 0.209), resolution=(1080, 2400)))
            sleep(5)
            touch(Template(r"tpl1684140003979.png", record_pos=(-0.009, 0.737), resolution=(1080, 2400)))
            if exists(Template(r"tpl1684141355872.png", record_pos=(-0.009, 0.626), resolution=(1080, 2400))):
                touch(Template(r"tpl1684141364532.png", record_pos=(0.002, 0.626), resolution=(1080, 2400)))


            swipe(Template(r"tpl1684145907744.png", record_pos=(-0.405, 0.527), resolution=(1080, 2400)), vector=[-0.0328, -0.5306])
            sleep(1)
            swipe(Template(r"tpl1684145907744.png", record_pos=(-0.405, 0.527), resolution=(1080, 2400)), vector=[-0.0328, -0.5306])
            sleep(1)
            swipe(Template(r"tpl1684145907744.png", record_pos=(-0.405, 0.527), resolution=(1080, 2400)), vector=[-0.0328, -0.5306])
            sleep(1)
            swipe(Template(r"tpl1684145907744.png", record_pos=(-0.405, 0.527), resolution=(1080, 2400)), vector=[-0.0328, -0.5306])
            sleep(1)
            swipe(Template(r"tpl1684145907744.png", record_pos=(-0.405, 0.527), resolution=(1080, 2400)), vector=[-0.0328, -0.5306])
            sleep(1)
            swipe(Template(r"tpl1684145907744.png", record_pos=(-0.405, 0.527), resolution=(1080, 2400)), vector=[-0.0328, -0.5306])

            sleep(30)
            touch(Template(r"tpl1684140148840.png", record_pos=(0.002, 0.916), resolution=(1080, 2400)))
            sleep(3)
            touch(Template(r"tpl1684140155390.png", record_pos=(0.42, -0.955), resolution=(1080, 2400)))




            keyevent("BACK")

            
    else:
        
        
        
        touch(Template(r"tpl1681198429272.png", record_pos=(0.41, 0.906), resolution=(1080, 2400)))
        touch(Template(r"tpl1684137849951.png", record_pos=(-0.117, 0.009), resolution=(1080, 2400)))
        touch(Template(r"tpl1685004648248.png", record_pos=(-0.106, -0.848), resolution=(1080, 2400)))

        touch(Template(r"tpl1681198450231.png", record_pos=(0.291, 0.919), resolution=(1080, 2400)))
        touch(Template(r"tpl1680601729014.png", record_pos=(-0.086, 0.775), resolution=(1080, 2400)))
        text(msg)

        touch(Template(r"tpl1680602061683.png", record_pos=(0.41, 0.004), resolution=(1080, 2400)))
        keyevent("BACK")
        keyevent("BACK")
        keyevent("BACK")
        


message_text('abcdefg')
sleep(5)

#发起私聊
touch(Template(r"tpl1684146075559.png", record_pos=(0.213, 0.908), resolution=(1080, 2400)))
sleep(3)

touch(Template(r"tpl1684122465241.png", record_pos=(0.431, -0.952), resolution=(1080, 2400)))
touch(Template(r"tpl1684122470748.png", record_pos=(0.22, -0.664), resolution=(1080, 2400)))
touch(Template(r"tpl1684146667965.png", record_pos=(-0.195, -0.711), resolution=(1080, 2400)))
touch(Template(r"tpl1684148305069.png", record_pos=(0.255, 0.916), resolution=(1080, 2400)))
touch(Template(r"tpl1680601729014.png", record_pos=(-0.086, 0.775), resolution=(1080, 2400)))
text("第一次聊")
touch(Template(r"tpl1680602061683.png", record_pos=(0.41, 0.004), resolution=(1080, 2400)))

keyevent("BACK")
keyevent("BACK")
keyevent("BACK")
keyevent("BACK")
sleep(3)
#创建群聊
touch(Template(r"tpl1684122871854.png", record_pos=(0.428, -0.952), resolution=(1080, 2400)))
touch(Template(r"tpl1684122875010.png", record_pos=(0.228, -0.391), resolution=(1080, 2400)))
touch(Template(r"tpl1685007227625.png", record_pos=(-0.189, 0.546), resolution=(1080, 2400)))
touch(Template(r"tpl1684137487297.png", record_pos=(-0.139, -0.528), resolution=(1080, 2400)))
touch(Template(r"tpl1684122894071.png", record_pos=(0.431, -0.988), resolution=(1080, 2400)))
touch(Template(r"tpl1680601729014.png", record_pos=(-0.086, 0.775), resolution=(1080, 2400)))
text("第一次创建群聊")
touch(Template(r"tpl1680602061683.png", record_pos=(0.41, 0.004), resolution=(1080, 2400)))
keyevent("BACK")
keyevent("BACK")

sleep(3)


#广场say hi
touch(Template(r"tpl1684130946070.png", record_pos=(-0.395, 0.901), resolution=(1080, 2400)))
touch(Template(r"tpl1684130949518.png", record_pos=(-0.395, -0.973), resolution=(1080, 2400)))
touch(Template(r"tpl1684130958207.png", record_pos=(-0.056, 0.028), resolution=(1080, 2400)))
touch(Template(r"tpl1684130963319.png", record_pos=(0.409, 0.777), resolution=(1080, 2400)))
keyevent("BACK")
keyevent("BACK")

#家族对话
touch(Template(r"tpl1684138068963.png", record_pos=(0.409, 0.908), resolution=(1080, 2400)))
touch(Template(r"tpl1684138133062.png", record_pos=(-0.222, 0.125), resolution=(1080, 2400)))
sleep(1)
touch(Template(r"tpl1684138117462.png", record_pos=(0.055, -0.399), resolution=(1080, 2400)))
touch(Template(r"tpl1684138102758.png", record_pos=(-0.15, -0.863), resolution=(1080, 2400)))
touch(Template(r"tpl1680601729014.png", record_pos=(-0.086, 0.775), resolution=(1080, 2400)))
text("家族聊天了哈哈")
touch(Template(r"tpl1680602061683.png", record_pos=(0.41, 0.004), resolution=(1080, 2400)))
keyevent("BACK")
keyevent("BACK")
keyevent("BACK")
keyevent("BACK")




         




    
    

