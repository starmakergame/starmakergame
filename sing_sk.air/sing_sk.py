# -*- encoding=utf8 -*-
__author__ = "beiying"
from airtest.core.api import *
auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
ST.OPDELAY = 0.7#全局等待
#前置条件：线上IN印度大区；正式环境；未设置系统权限，vivo手机v2061A；没有首页弹窗；没有弹窗da'rao

#sing_首页播放验证                 
poco('com.starmakerinteractive.starmaker:id/tab_animation_view')[4].click()#首页sing页面元素
poco('com.starmakerinteractive.starmaker:id/tv_tab_title',text='手机铃声').click()#sing页面手机铃声（当前页面未找到）
poco(resourceId='com.starmakerinteractive.starmaker:id/tv_tab_title',text='发现').click()#铃声tab下发现页
poco('com.starmakerinteractive.starmaker:id/rings_tv_rings_name')[3].click()#列表歌曲-播放
sleep(6)#等待6秒播放
poco('com.starmakerinteractive.starmaker:id/rings_tv_rings_name')[3].click()#列表歌曲-暂停
poco('com.starmakerinteractive.starmaker:id/btn_add')[3].click()#歌曲设置铃声按钮


#sing_储存权限判断
if poco(resourceId='com.android.permissioncontroller:id/permission_message',text='“StarMaker”请求存储权限，是否允许？').exists():#判断是否有通知权限
    poco('com.android.permissioncontroller:id/permission_allow_button',text='允许').click()#设置储存权限
while poco(resourceId='com.starmakerinteractive.starmaker:id/tv_title_dialog_download_share_file',text='资源准备中...').exists():
    sleep(3)    
if poco('com.starmakerinteractive.starmaker:id/img_guide').exists:#判断是否到达3头盔权限页
    poco('com.starmakerinteractive.starmaker:id/img_guide').click()
if poco(resourceId='com.starmakerinteractive.starmaker:id/btn_grants',text='设置').exists():#判断是否有通知权限
    if poco('vivo:id/main').exists():
        poco('com.starmakerinteractive.starmaker:id/btn_grants')[0].click()#设置通知权限
        poco('android:id/checkbox').click()#打开通知权限
        keyevent("back")#返回页面

        
if poco(resourceId='com.starmakerinteractive.starmaker:id/txt_primary',text='勿扰模式').exists():#判断是否有勿扰权限
    poco('com.starmakerinteractive.starmaker:id/btn_grants').click()#设置勿扰权限
    while poco(resourceId='android:id/title',text='StarMaker').exists() == False:#寻找APP
        swipe([493, 1929],[356, 575])#上下滑动
    poco(resourceId='android:id/title',text='StarMaker').click()#进入勿扰权限页
    poco(resourceId='android:id/title',text='允许勿扰模式').click()#权限开关打开
    poco(resourceId='android:id/button2',text='拒绝').click()#允许权限
    poco(resourceId='android:id/title',text='允许勿扰模式').click()#权限开关再次打开
    poco(resourceId='android:id/button1',text='允许').click()#允许权限
    keyevent("back")#返回
    keyevent("back")
    poco(resourceId='com.starmakerinteractive.starmaker:id/common_dialog_btn_negative',text='已开启').click()#已开启全部权限
sleep(1)


#sing_每日任务+权限判断
poco(resourceId='com.starmakerinteractive.starmaker:id/btn_action',text='领取奖励').click()#领取奖励
if poco(resourceId='com.starmakerinteractive.starmaker:id/tv_title',text='签到').exists():#判断首次弹出页面
    poco(resourceId='com.starmakerinteractive.starmaker:id/iv_close').click()#关闭签到弹窗
if poco(resourceId='com.starmakerinteractive.starmaker:id/common_dialog_btn_positive',text='知道了').exists():#判断首次弹出页面
    poco(resourceId='com.starmakerinteractive.starmaker:id/common_dialog_btn_positive',text='知道了').click()
for i in range(4):
        swipe([493, 1929],[356, 575])#每日福利页滑动
keyevent('back')
keyevent('back')
for i in range(4):#循环
        swipe([493, 1929],[356, 575])#发现页滑动

        
#sing_我的铃声页验证                 
poco(resourceId='com.starmakerinteractive.starmaker:id/tv_tab_title',text='我的铃声').click()#进入我的铃声tab
if poco(resourceId='com.starmakerinteractive.starmaker:id/rings_list_title',text='当前铃声').exists():#判断是否存在
    poco(resourceId='com.starmakerinteractive.starmaker:id/ll_close').click()#点击更多
    poco(text='取消').click()
    poco(resourceId='com.starmakerinteractive.starmaker:id/ll_close').click()#点击更多
    poco(text='恢复系统铃声').click()
    poco(resourceId='com.starmakerinteractive.starmaker:id/common_dialog_btn_negative',text='取消').click()
    poco(resourceId='com.starmakerinteractive.starmaker:id/ll_close').click()#点击更多
    poco(text='恢复系统铃声').click()
    poco(resourceId='com.starmakerinteractive.starmaker:id/common_dialog_btn_positive',text='确认').click()
    
    
#sing_我的作品页验证
poco(resourceId='com.starmakerinteractive.starmaker:id/tv_tab_title',text='我的作品').click()#铃声tab我的作品
if poco(resourceId='com.starmakerinteractive.starmaker:id/iv_play_state').exists():#判断作品是否为空                 
    poco('com.starmakerinteractive.starmaker:id/iv_play_state').click()#播放音乐
sleep(5)    
poco('com.starmakerinteractive.starmaker:id/btn_add').click() #铃声设置
while poco(resourceId='com.starmakerinteractive.starmaker:id/hsl_wave_capturelib_view_trimmer_audio').exists() is False:
     sleep(1)#判断是否进入声音剪辑页
sleep(3)


#铃声验证
if poco(text='支持设置来电铃声啦').exists():#判断首次弹窗是否存在
    poco(text='我知道了').click()
if poco(text='无歌词原声').exists()==False:#判断是否存在歌词
    for i in range(4):
        swipe([82, 575],[62, 1502])
swipe([282, 1939],[732, 1946])
sleep(6)#声音剪辑页播放6秒
if poco(resourceId='com.starmakerinteractive.starmaker:id/tv_auto_select',text='智能截取').exists():#判断是否存在
    poco(resourceId='com.starmakerinteractive.starmaker:id/tv_auto_select',text='智能截取').click() 
poco(resourceId='com.starmakerinteractive.starmaker:id/iv_play').click()#暂停歌曲
poco(text='设为铃声').click()
keyevent('back')#返回我的作品tab



#sing_铃声广场验证
poco(resourceId='com.starmakerinteractive.starmaker:id/tv_tab_title',text='我的作品').click()#铃声tab我的作品入口
poco('com.starmakerinteractive.starmaker:id/btn_add').click()#设置铃声

sleep(6)
poco(text='更多精彩铃声 >').click()#进入铃声广场
poco('com.starmakerinteractive.starmaker:id/iv_play_state').click()#播放音乐
sleep(5)


poco(resourceId='com.starmakerinteractive.starmaker:id/tv_tab_title',text='我的铃声').click()#进入我的铃声tab
if poco(resourceId='com.starmakerinteractive.starmaker:id/rings_list_title',text='当前铃声').exists():#判断是否存在
    poco(resourceId='com.starmakerinteractive.starmaker:id/ll_close').click()#点击更多
    poco(text='取消').click()
    poco(resourceId='com.starmakerinteractive.starmaker:id/ll_close').click()#点击更多
    poco(text='恢复系统铃声').click()
    poco(resourceId='com.starmakerinteractive.starmaker:id/common_dialog_btn_negative',text='取消').click()
    poco(resourceId='com.starmakerinteractive.starmaker:id/ll_close').click()#点击更多
    poco(text='恢复系统铃声').click()
    poco(resourceId='com.starmakerinteractive.starmaker:id/common_dialog_btn_positive',text='确认').click()
poco(resourceId='com.starmakerinteractive.starmaker:id/rings_iv_more').click()#点击更多
poco('com.starmakerinteractive.starmaker:id/text',text='常见问题').click()#更多常见问题
sleep(5)#等待跳转完成
keyevent('back') 


poco(resourceId='com.starmakerinteractive.starmaker:id/tv_tab_title',text='我的作品').click()#铃声tab我的作品
if poco(resourceId='com.starmakerinteractive.starmaker:id/iv_play_state').exists():#判断作品是否为空                 
    poco('com.starmakerinteractive.starmaker:id/iv_play_state').click()#播放音乐
    sleep(5)
poco('com.starmakerinteractive.starmaker:id/btn_add')[0].click()#设置铃声
while poco(resourceId='com.starmakerinteractive.starmaker:id/hsl_wave_capturelib_view_trimmer_audio').exists() is False:
     sleep(1)#判断是否进入声音剪辑页
if poco(resourceId='com.starmakerinteractive.starmaker:id/hsl_wave_capturelib_view_trimmer_audio').exists():#判断是否进入页
    sleep(2)
    keyevent('back') 
    poco('com.starmakerinteractive.starmaker:id/common_dialog_btn_negative',text='退出').click()   
sleep(2)
poco('com.starmakerinteractive.starmaker:id/rings_iv_search').click()#进入搜索
sleep(1)
poco('com.starmakerinteractive.starmaker:id/searchView').click()#点击搜索
sleep(1)
text("一路向北",search=True)#输入搜索
sleep(1)
poco('com.starmakerinteractive.starmaker:id/rings_tv_rings_name')[3].click()#播放音乐
sleep(1)
poco('com.starmakerinteractive.starmaker:id/btn_add')[3].click()#歌曲设置铃声按钮
while poco(resourceId='com.starmakerinteractive.starmaker:id/tv_title_dialog_download_share_file',text='资源准备中...').exists():
    sleep(3)
if poco(resourceId='com.starmakerinteractive.starmaker:id/hsl_wave_capturelib_view_trimmer_audio').exists():
    keyevent('back')
    poco('com.starmakerinteractive.starmaker:id/common_dialog_btn_negative',text='退出').click()
    sleep(1)
    keyevent('back')#从铃声广场退出
    sleep(1)
    keyevent('back')#回到sing手机铃声
keyevent('back')
sleep(1)
keyevent('back')
assert_exists(Template(r"tpl1684492176718.png", record_pos=(0.003, -0.006), resolution=(1080, 2408)), "手机铃声tab测试完成")


