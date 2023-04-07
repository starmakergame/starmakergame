# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)
#至此都为创建脚本自动写入
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
#引用安卓poco插件，无实际意义，此脚本内使用了获取安卓java控件内的text值，并对这个值进行了一些操作
#这里应该判断是否有创建，没有创建继续走，已创建的话抛出异常
#这里其实最好配合登录时，登录一个没有房间的号使用
#点击创建房间
touch(Template(r"tpl1680853983913.png", record_pos=(-0.354, -0.123), resolution=(1080, 2400)))
#等待房间房间列表弹出
wait(Template(r"tpl1680854142741.png", record_pos=(0.001, -0.632), resolution=(1080, 2400)))
#收缩输入法
touch(Template(r"tpl1680854031583.png", record_pos=(-0.285, 1.03), resolution=(1080, 2400)))
#等待输入法收起
wait(Template(r"tpl1680854377270.png", record_pos=(-0.001, -0.004), resolution=(1080, 2400)))
#点击随机一个房名
#这里默认点击了一起唱歌，我这里先以一起唱歌作为示范，就不点击别的了
touch(Template(r"tpl1680854384410.png", record_pos=(0.368, 0.044), resolution=(1080, 2400)))
#这里逻辑就比较复杂了，先判断点击的是一起唱歌类型
if exists(Template(r"tpl1680854526458.png", record_pos=(-0.327, -0.829), resolution=(1080, 2400))):
    #定义一个text获取房名输入框中的text
    text=poco("com.starmakerinteractive.starmaker:id/edt_room_name").get_text()
    #log(text)
    #定义一个aaa，并把text获取的文本前四位赋值给aaa，因为随机房名，是以房间类型作为前几位，后几位随机字符串的，所以我们对于一起唱歌，只需要判断前4位一致就行了
    aaa = text[:4]
    #log(aaa)
    #这里做一个断言，断言我们选择类型的前4位和获取的前四位是否一致，如果一致则输出到报告里
    assert_equal("一起唱歌", aaa, "点击一起唱歌类型的随机房名，产生对应名字")
#名字验证无问题之后，点击创建房间    
touch(Template(r"tpl1680856159078.png", rgb=True, record_pos=(-0.004, 0.115), resolution=(1080, 2400)))
#检测图片符合度，确认是否创建成功并输出
if exists(Template(r"tpl1680856221851.png", record_pos=(0.001, -0.47), resolution=(1080, 2400)))
    log("创建房间成功")
    
#创建房间之后，应该要把当前登录账号的房间删掉，以后省的切换账号，暂时未完成    