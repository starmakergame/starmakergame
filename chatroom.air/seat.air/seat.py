# -*- encoding=utf8 -*-
__author__ = "DingShuang"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

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
    
    
touch(Template(r"tpl1681118337738.png", record_pos=(-0.367, -0.471), resolution=(1080, 2400)))
sleep(1)

touch(Template(r"tpl1681118403180.png", record_pos=(-0.408, 0.637), resolution=(1080, 2400)))
exists(Template(r"tpl1681118474315.png", record_pos=(-0.004, -0.36), resolution=(1080, 2400)))


# text = poco(text="ds7777777778   离开了1号麦")
# 获取下麦成功公屏消息
text = poco("com.starmakerinteractive.starmaker:id/tv_name").get_text
text2 = "离开了1号麦"
# 拼接下麦成功公屏文案
expect_name = name+text2
# 断言下麦成功公屏消息是否与期望值一致
assert_equal(text, expect_name, "下麦")









