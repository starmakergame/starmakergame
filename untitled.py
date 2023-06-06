# -*- encoding=utf8 -*-
__author__ = "李洁"

from airtest.core.api import *
from airtest.core.android.adb import *
from airtest.core.android.android import *
from airtest.cli.parser import cli_setup
from airtest.cli.runner import AirtestCase, run_script

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

#参数化
PACKAGE = "com.starmakerinteractive.starmaker"
START_ACTIVITY = "org.cocos2dx.PlayGameActivity"
path ="D:\\下载\\QQ浏览器下载\\starmaker-debug-minApi21-universal-85837501-2023-06-05-14-57.apk"

#检测app是否安装
def existsapp(PACKAGE):
    dev = device()
    try:
        if dev.check_app(PACKAGE):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        print('检测异常安装')
        return False

#安装pak包
def installpak(path):
    try:
        if existsapp(PACKAGE) == True:
            print(existsapp(PACKAGE),'APP存在，卸载安装')
            uninstall(PACKAGE)
            install(path)
        else:
            print ('APP不存在，安装pak')
            install(path)
    except Exception as e:
        print(e)
        print('检测异常安装')
        install(path)
    if existsapp(PACKAGE) == True:
        print('安装成功')
    else:
        print('安装失败')
existsapp(PACKAGE)      
installpak(path)