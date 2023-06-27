# -*- encoding=utf8 -*-
__author__ = "cuimeina"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

#启动APP
# start_app("com.starmakerinteractive.starmaker")
# sleep(10)


#私信歌房，合唱，发送表情，信息通用
def message_sing():
    
    #点击输入框
    poco("com.starmakerinteractive.starmaker:id/message_edit").click()
    #输入内容
    text("1123344")
    #点击发送按钮
    poco("com.starmakerinteractive.starmaker:id/send_button").click()
    #点击表情图标
    poco("com.starmakerinteractive.starmaker:id/btn_chat_bottom_emoji").click()
    #选择一个表情
    #poco("com.starmakerinteractive.starmaker:id/tv_emoji_item").click()
    touch([99, 1505])
    #点击发送按钮
    poco("com.starmakerinteractive.starmaker:id/send_button").click()
                        
    #点击➕号
    poco("com.starmakerinteractive.starmaker:id/btn_chat_bottom_more").click()
    #点击歌房
    poco("com.starmakerinteractive.starmaker:id/iv_icon")[0].click()
    #点击历史记录tab列表的第一个
    poco("com.starmakerinteractive.starmaker:id/txt_title")[0].click()
    #点击是
    poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_positive").click()
    
    #点击＋，收起歌房
    poco("com.starmakerinteractive.starmaker:id/btn_chat_bottom_more").click()
    #点击分享
    poco("com.starmakerinteractive.starmaker:id/iv_icon")[1].click()
    
    #等待加载
    sleep(1)
    #发送第一个动态
    poco("com.starmakerinteractive.starmaker:id/btn_send").click()
    #点击＋，收起分享
    poco("com.starmakerinteractive.starmaker:id/btn_chat_bottom_more").click()
    #点击合唱按钮
    poco("com.starmakerinteractive.starmaker:id/btn_chat_bottom_chorus").click()
            
    
    #直接发起新合唱
    poco("com.starmakerinteractive.starmaker:id/iv_add").click()
    #如果第一次发起，出现体验时，直接点击立即体验
    if exists(Template(r"tpl1684999653263.png", record_pos=(-0.006, -0.013), resolution=(1080, 2400))):
        poco("com.starmakerinteractive.starmaker:id/btn_positive").click()
    #等待歌曲页面加载
    sleep(5)
    #点击为你推荐中第一首歌曲
    poco("com.starmakerinteractive.starmaker:id/tv_add").click()
    #点击授权弹窗
    if exists(Template(r"tpl1685349136605.png", record_pos=(-0.001, -0.019), resolution=(1080, 2400))):
        poco("com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
         
    #点击推荐使用耳机的我知道了按钮
    poco("com.starmakerinteractive.starmaker:id/recording_headset_dialog_i_know_btn").click()
    #等待歌曲加载完成
    sleep(10)
    #如果是合唱新页面
    if exists(Template(r"tpl1687159724376.png", record_pos=(-0.003, -0.684), resolution=(1080, 2400))):
        #点击顶部的发起合唱
        poco("com.starmakerinteractive.starmaker:id/duet_create").click()
        #点击开始按钮
        poco("com.starmakerinteractive.starmaker:id/rbtn_record_recorder_song_fragment_song_record").click()
    else:
        #直接点击开始按钮
        touch([532, 1995])
    
    #如果存在跳过前奏按钮的话，则直接点击
    if exists(Template(r"tpl1685346211514.png", target_pos=3, record_pos=(0.001, 0.628), resolution=(1080, 2400))):
        touch(Template(r"tpl1685346211514.png", target_pos=3, record_pos=(0.001, 0.628), resolution=(1080, 2400)))
    #快速滑动录制页面
    swipe([118, 1719],[91, 742])
    swipe([118, 1719],[91, 742])
    swipe([118, 1719],[91, 742])
    swipe([118, 1719],[91, 742])
    #等待出现跳过结尾按钮
    sleep(15)
    #如果出现跳过结尾按钮，则点击
    if exists(Template(r"tpl1685346256716.png", record_pos=(-0.005, 0.628), resolution=(1080, 2400))):
        touch(Template(r"tpl1685346266743.png", record_pos=(-0.001, 0.626), resolution=(1080, 2400)))
    else:
        swipe([118, 1719],[91, 742])
        swipe([118, 1719],[91, 742])
        sleep(8)
        if exists(Template(r"tpl1685346256716.png", record_pos=(-0.005, 0.628), resolution=(1080, 2400))):
            touch(Template(r"tpl1685346266743.png", record_pos=(-0.001, 0.626), resolution=(1080, 2400)))
        else:
            sleep(10)
    #等待评级评分页面出现
    sleep(8)
    #在发布预览页，点击发布按钮进行发布
    poco("com.starmakerinteractive.starmaker:id/tv_next_baserecord_fragment_edit_btn").click()
    #等待页面加载中
    sleep(2)
    #点击页面右上角完成按钮
    poco("com.starmakerinteractive.starmaker:id/tv_done").click()


#发送私聊
#点击聊天底tab
poco("com.starmakerinteractive.starmaker:id/tab_animation_view")[2].click()
#点击顶部聊天tab
poco("com.starmakerinteractive.starmaker:id/tv_tab_title")[1].click()
#点击聊天列表中第一个用户进入
#如果没有已聊天的好友，则进到个人中心找好友 
if exists(Template(r"tpl1686899545422.png", record_pos=(-0.013, -0.406), resolution=(1080, 2400))):
    #进到个人中心  
    poco("com.starmakerinteractive.starmaker:id/tab_animation_view")[3].click()   
    #点击已关注，进入关注列表
    poco("com.starmakerinteractive.starmaker:id/item_title")[1].click()
    #找到列表里的第一个人
    touch([769, 291])
    #进到私信聊天界面
    poco("com.starmakerinteractive.starmaker:id/tv_top_fan").click()

    #发送聊天内容
    message_sing()
else:
    #点击最顶部的好友进行聊天
    poco("com.starmakerinteractive.starmaker:id/conversation_End_top").click()
    #调用通用发送信息
    message_sing()
      

        
#点击创建群聊
sleep(5)
#点击聊天底tab
poco("com.starmakerinteractive.starmaker:id/tab_animation_view")[2].click()
#点击右上角的➕
poco("com.starmakerinteractive.starmaker:id/iv_create_conversation").click()
#点击创建群聊
touch([903, 785])
#选择前三个好友进行创建
poco("com.starmakerinteractive.starmaker:id/tv_name")[0].click()
poco("com.starmakerinteractive.starmaker:id/tv_name")[1].click()
poco("com.starmakerinteractive.starmaker:id/tv_name")[2].click()
#点击右上角创建按钮
poco("com.starmakerinteractive.starmaker:id/btn_create").click()
#进行统一的发送内容
message_sing()
sleep(3)

#进行下一场景
sleep(2)
#广场say hi
#点击动态tab
poco("com.starmakerinteractive.starmaker:id/tab_animation_view")[1].click()
#如果出现授权联系人弹窗
if exists(Template(r"tpl1686899666016.png", record_pos=(0.001, -0.011), resolution=(1080, 2400))):
    #点击不用了，谢谢将弹窗关闭
    poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_negative").click()
#进入已关注 列表
poco("com.starmakerinteractive.starmaker:id/tv_tab_title").click()
#找到say hi 按钮即可
if exists(Template(r"tpl1684130958207.png", record_pos=(-0.056, 0.028), resolution=(1080, 2400))):
    #点击say hi 按钮，调起半屏聊天框
    poco("com.starmakerinteractive.starmaker:id/btn_say").click()
else:
    #向下滑动页面，找到say hi 按钮进行点击
    swipe([271, 1983],[344, 880])
    swipe([271, 1983],[344, 880])
    #点击say hi 按钮，调起半屏聊天框
    poco("com.starmakerinteractive.starmaker:id/btn_say").click()
#点击发送按钮
poco("com.starmakerinteractive.starmaker:id/send_button").click()
#关闭半屏聊天框
keyevent("BACK")
keyevent("BACK")

#进到个人中心进行家族对话
#点击我的，进到个人中心
poco("com.starmakerinteractive.starmaker:id/tab_animation_view")[3].click()
#点击家族，进入家族主页
poco("com.starmakerinteractive.starmaker:id/tv_has_family_arrow").click()
#如果有欢迎做任务卡片，则点击卡片将其关闭
if exists(Template(r"tpl1685348880993.png", record_pos=(0.006, 0.347), resolution=(1080, 2400))):
    #点击关闭按钮
    poco("com.starmakerinteractive.starmaker:id/iv_button").click()

#poco("com.starmakerinteractive.starmaker:id/family_img_ghost").click()
#点击聊天按钮，进到加入聊天页面
poco("com.starmakerinteractive.starmaker:id/iv_button")[2].click()
#点击表情图标
poco("com.starmakerinteractive.starmaker:id/btn_chat_bottom_emoji").click()
#选择一个表情
touch([99, 1505])
#点击发送按钮
poco("com.starmakerinteractive.starmaker:id/send_button").click()
keyevent("BACK")
keyevent("BACK")
keyevent("BACK")



 
         




    
    

