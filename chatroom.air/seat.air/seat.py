# -*- encoding=utf8 -*-
__author__ = "DingShuang"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# 验证上麦
touch(Template(r"tpl1681116125318.png", record_pos=(-0.349, -0.12), resolution=(1080, 2400)))

wait(Template(r"tpl1681116663505.png", record_pos=(-0.001, 0.914), resolution=(1080, 2400)))
touch(Template(r"tpl1681116671175.png", record_pos=(-0.007, 0.912), resolution=(1080, 2400)))
# 获上麦成公屏消息
name_text = poco("com.starmakerinteractive.starmaker:id/root_view")[3].get_text
name_long = len(name_text)
# 获取上麦用户昵称
name = name_text[:name_long-5]

touch(Template(r"tpl1681116932631.png", record_pos=(-0.375, -0.474), resolution=(1080, 2400)))
wait(Template(r"tpl1681116960287.png", record_pos=(0.0, 0.714), resolution=(1080, 2400)))
touch(Template(r"tpl1681116971734.png", record_pos=(-0.391, 0.516), resolution=(1080, 2400)))
if exists(Template(r"tpl1681117297337.png", record_pos=(-0.014, -0.352), resolution=(1080, 2400))):
    log('上麦成功')
    
    
# 验证下麦
touch(Template(r"tpl1681118337738.png", record_pos=(-0.367, -0.471), resolution=(1080, 2400)))
sleep(1)

touch(Template(r"tpl1681118403180.png", record_pos=(-0.408, 0.637), resolution=(1080, 2400)))
sleep(1)


# text = poco(text="ds7777777778   离开了1号麦")
# 获取下麦成功公屏消息
text = poco("com.starmakerinteractive.starmaker:id/tv_name").get_text
text2 = "离开了1号麦"
# 拼接下麦成功公屏文案
expect_name = name+text2
# 断言下麦成功公屏消息是否与期望值一致
assert_equal(text, expect_name, "下麦")



# 验证打开申请上麦权限
touch(Template(r"tpl1681122497126.png", record_pos=(0.098, 0.923), resolution=(1080, 2400)))

sleep(1)
touch(Template(r"tpl1681122525073.png", record_pos=(0.436, -0.156), resolution=(1080, 2400)))
sleep(1.0)
touch(Template(r"tpl1681122555593.png", record_pos=(-0.274, 0.756), resolution=(1080, 2400)))
# 断言举手上麦设置成功
if exists(Template(r"tpl1681122576634.png", record_pos=(-0.343, -0.135), resolution=(1080, 2400))):
    log("已更改上麦方式为同意后上麦")
touch(Template(r"tpl1681122737251.png", record_pos=(-0.012, -0.691), resolution=(1080, 2400)))


# 验证设置等级权限上麦



def take_seat():
    touch(Template(r"tpl1681122962268.png", record_pos=(-0.251, -0.971), resolution=(1080, 2400)))
    sleep(1.0)
    touch(Template(r"tpl1681122989938.png", record_pos=(-0.026, 0.905), resolution=(1080, 2400)))
    sleep(1.0)
    touch(Template(r"tpl1681123010398.png", record_pos=(-0.33, 0.816), resolution=(1080, 2400)))
    sleep(1.0)
    touch(Template(r"tpl1681123059043.png", record_pos=(-0.367, 0.4), resolution=(1080, 2400)))
    sleep(1.0)
    # 断言5级以上用户上麦设置成功
    if exists(Template(r"tpl1681123081877.png", record_pos=(0.0, 0.813), resolution=(1080, 2400))):
        log("5级以上用户可上麦")

    touch(Template(r"tpl1681123166158.png", record_pos=(-0.355, 0.815), resolution=(1080, 2400)))
    sleep(1.0)
    touch(Template(r"tpl1681123179038.png", record_pos=(-0.355, 0.766), resolution=(1080, 2400)))
    sleep(1.0)
    # 断言30级以上用户上麦设置成功
    if exists(Template(r"tpl1681123191782.png", record_pos=(0.008, 0.81), resolution=(1080, 2400))):
        log("30级以上用户可上麦")

    touch(Template(r"tpl1681123237320.png", record_pos=(-0.347, 0.815), resolution=(1080, 2400)))
    sleep(1.0)
    touch(Template(r"tpl1681123251020.png", record_pos=(-0.357, 0.274), resolution=(1080, 2400)))
    sleep(1.0)
    # 断言仅家族成员可上麦设置成功
    if exists(Template(r"tpl1681123263606.png", record_pos=(-0.006, 0.819), resolution=(1080, 2400))):
        log("仅家族成员可上麦")

    touch(Template(r"tpl1681123343700.png", record_pos=(-0.353, 0.821), resolution=(1080, 2400)))
    sleep(1.0)
    touch(Template(r"tpl1681123355609.png", record_pos=(-0.365, 0.16), resolution=(1080, 2400)))
    sleep(1.0)
    # 断言任意用户可上麦设置成功
    if exists(Template(r"tpl1681123376250.png", record_pos=(-0.001, 0.818), resolution=(1080, 2400))):
        log("任意用户可上麦")

        
#如果当前房类型是多麦房，验证上麦权限设置


if exists(Template(r"tpl1681125608044.png", record_pos=(0.026, -0.968), resolution=(1080, 2400))):
    touch(566,157)
    sleep(1.0)
    touch(Template(r"tpl1681125084999.png", record_pos=(-0.323, -0.113), resolution=(1080, 2400)))
    sleep(1)
    take_seat()

    
else: 
    take_seat()


    











