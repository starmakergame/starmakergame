# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)
#至此都为创建脚本自动写入
#定义name和password用于登录
name='youxi1@126.com'
password='521xiaoyuH'                                                       
#引用安卓poco插件，无实际意义，这个脚本内也无用
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
#启动app，这里我用的是starmaker
start_app("com.starmakerinteractive.starmaker")

#,activity="com.ushowmedia.starmaker.splash.SplashActivity")这里想直接调用登录界面，但是需要传参数，等我再研究下
#等待5s，防止启动时间过长
sleep(5.0)

#以下的所有if语句都未做异常判断，以后再加
#通过是否有登录按钮，判断是否是已经登录状态
if exists(Template(r"tpl1680254729323.png", record_pos=(-0.005, 0.799), resolution=(1080, 2400))):
    #如果存在登录按钮，则点击登录
   touch(Template(r"tpl1680254802786.png", record_pos=(0.0, 0.796), resolution=(1080, 2400)))

#等待登录方式弹窗弹出，这里不等待有可能会造成异常
#wait就是等待某个界面出现，sleep就是纯等待时间
wait(Template(r"tpl1680254880607.png", record_pos=(-0.002, 0.443), resolution=(1080, 2400)))
#出现后点击更多，暂时只用邮箱登录
touch(Template(r"tpl1680254888450.png", record_pos=(0.004, 0.807), resolution=(1080, 2400)))
wait(Template(r"tpl1680254897283.png", record_pos=(0.004, 0.805), resolution=(1080, 2400)))
touch(Template(r"tpl1680254902644.png", record_pos=(-0.002, 0.795), resolution=(1080, 2400)))
#定位输入框，方便输入账号密码
touch(Template(r"tpl1680600902106.png", record_pos=(-0.305, -0.513), resolution=(1080, 2400)))

sleep(1.0)
#把之前定义的name值输入
text(name)
sleep(1.0)
#如果下一步变红，则可以点击，这里判断增加了颜色值的判断，可以双击图片查看rgb选项勾选
if exists(Template(r"tpl1680578500677.png", rgb=True, record_pos=(-0.001, -0.299), resolution=(1080, 2400))):
 
    touch(Template(r"tpl1680578517406.png", rgb=True, record_pos=(-0.003, -0.296), resolution=(1080, 2400)))
    sleep(2.0)
#输入密码
touch(Template(r"tpl1680600684069.png", record_pos=(-0.306, -0.586), resolution=(1080, 2400)))
text(password)
#同样的登录判断
if exists(Template(r"tpl1680600742233.png", record_pos=(-0.002, -0.431), resolution=(1080, 2400))):
    touch(Template(r"tpl1680600768888.png", record_pos=(-0.002, -0.43), resolution=(1080, 2400)))
#if条件成功后，在报告中输出log22222，左上角运行，打开报告目录就可以查看网页版报告
    log(22222)

