# -*- encoding=utf8 -*-
__author__ = "YSH"

from airtest.core.api import *

auto_setup(__file__)



from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

using("function.air")
from function import *

##########初始化###########
# start_app("com.starmakerinteractive.starmaker")#启动APP
waitting(resource_id="com.starmakerinteractive.starmaker:id/tv_tab_title",time=20)
##########判断是否存在活动弹窗###########
if poco("com.starmakerinteractive.starmaker:id/open_promotion_iv_image").exists():
    poco("com.starmakerinteractive.starmaker:id/open_promotion_iv_close").click()
##########判断是否存在ktv邀请弹窗###########
if poco("com.starmakerinteractive.starmaker:id/ktv_guide_tip").exists():
        poco("com.starmakerinteractive.starmaker:id/close").click()   
##########判断是否存在家族邀请弹窗###########
if poco("com.starmakerinteractive.starmaker:id/recommend_reason").exists():
        poco("com.starmakerinteractive.starmaker:id/close").click()     
##########判断是否存在升级弹窗###########
if poco("com.starmakerinteractive.starmaker:id/tv_level_up_tips").exists():
        poco("com.starmakerinteractive.starmaker:id/iv_close").click()  
##########跳转至sing页面###########
shell("am start sm://vocal_enter")
##########等待页面歌曲封面元素出现，执行下一步###########
waitting(resource_id="com.starmakerinteractive.starmaker:id/img_cover",time=60)



sing_search()###搜索框模块功能验证
sing_dailyreward()###每日福利页面跳转功能验证
sing_mysongs()###已点tab功能验证
sing_duet()###合唱tab功能验证
sing_artist()###歌手tab功能验证
sing_selection()###专题tab功能验证
sing_list()###排行榜tab功能验证
sing_party()###歌房tab功能验证
sing_live()###直播tab功能验证
sing_freestyle()###清唱tab功能验证
sing_family()###家族tab功能验证
sing_foryou()###foryou tab功能验证
#sing_Celebrity()###明星Gtab功能验证   Android839版本sing页面去掉明星tab

##########跳转至me页面###########
shell("am start sm://discovery")

