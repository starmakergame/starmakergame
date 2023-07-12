# -*- encoding=utf8 -*-
__author__ = "han'yuan'lin"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
#全局等待，每执行完一行代码等待
ST.OPDELAY=1

def recommend_topic():
    #点击动态tab
    poco('com.starmakerinteractive.starmaker:id/tab_name' ,text="动态" ).click()
    #判断是否有回礼弹窗
    if poco('com.starmakerinteractive.starmaker:id/list'  ).exists():
        poco('com.starmakerinteractive.starmaker:id/close' ).click()
    #点击关注tab
    poco('com.starmakerinteractive.starmaker:id/tv_tab_title').click()
    #判断是否有联系人权限申请弹窗
    if poco('com.starmakerinteractive.starmaker:id/tv_tip').exists():
        poco('com.starmakerinteractive.starmaker:id/common_dialog_btn_negative').click()
    #判断是否有去发布话题tab，有话题tab点击发布
    if poco('com.starmakerinteractive.starmaker:id/tv_topic_name' ).exists():
        poco('com.starmakerinteractive.starmaker:id/btn_action' ).click()   
        if poco('com.starmakerinteractive.starmaker:id/btn_positive').exists():
            poco('com.starmakerinteractive.starmaker:id/btn_positive').click()
        #满足上方条件返回广场tab
        keyevent("keycode_back")
    #点击话题标签
    if poco('com.starmakerinteractive.starmaker:id/item_topic_name').exists():
        poco('com.starmakerinteractive.starmaker:id/item_topic_name')[0].click()
        sleep(2.0)
        #点击话题圈页面分享按钮
        poco('com.starmakerinteractive.starmaker:id/iv_share').click()
    #分享页面点击搜索
        w='fdxqwertyuiop'
        for i in w:
            poco('com.starmakerinteractive.starmaker:id/et_search').click()
            text(i, search=True)
            if poco(resourceId='com.starmakerinteractive.starmaker:id/iv_star').exists() == True:
                poco("com.starmakerinteractive.starmaker:id/et_search").click(),keyevent("DEL")
            else:
                break
        #选择关注人        
        poco('com.starmakerinteractive.starmaker:id/cb_choose').click()
        #点击分享按钮
        poco('com.starmakerinteractive.starmaker:id/btn_share').click()   
        snapshot(msg="分享成功")
        #判断是否有在线成员，有的话点击用户头像进入个人页
        if poco('com.starmakerinteractive.starmaker:id/tv_online_num').exists():
            poco('com.starmakerinteractive.starmaker:id/tv_online_num').click()   
        if poco('com.starmakerinteractive.starmaker:id/tv_tab_title').exists():
            poco('com.starmakerinteractive.starmaker:id/imb_backward').click()       
        sleep(2.0)
        if poco('com.starmakerinteractive.starmaker:id/tv_recording_use_num').exists():
            poco('com.starmakerinteractive.starmaker:id/tv_recording_use_num').click()
        #点击圈友列表关注按钮后点击消息按钮进入聊天页
        for i in poco("com.starmakerinteractive.starmaker:id/btn_action"):
            if i.attr("text")=="关注":
                poco("com.starmakerinteractive.starmaker:id/btn_action",text="关注").click()
                if poco("com.starmakerinteractive.starmaker:id/btn_action",text="消息").exists():
                    break
        poco("com.starmakerinteractive.starmaker:id/btn_action",text="消息").click()            
        if poco('com.starmakerinteractive.starmaker:id/btn_login' ).exists():
            poco('com.starmakerinteractive.starmaker:id/btn_login' ).click()
        if poco('com.starmakerinteractive.starmaker:id/card_stage_name').exists():
            keyevent("keycode_back")
        #返回话题圈一级tab
        keyevent("keycode_back")
        #点击参与讨论进入发布页
        poco('com.starmakerinteractive.starmaker:id/fab' ).click()
        if poco('com.starmakerinteractive.starmaker:id/tv_tab_title').exists():
            poco('com.starmakerinteractive.starmaker:id/imb_close').click()
        if poco('com.starmakerinteractive.starmaker:id/fab').exists():
            poco('com.starmakerinteractive.starmaker:id/imb_backward').click()
def recommend_following():        
    #向上滑动关注tab
    poco.swipe([0.487, 0.782],[0.51, 0.243])
    #点击say hi按钮
    poco('com.starmakerinteractive.starmaker:id/btn_say').click()
    #判断是否有其他设备登录账号
    if poco('com.starmakerinteractive.starmaker:id/btn_relogin').exists():
        poco('com.starmakerinteractive.starmaker:id/btn_relogin').click()
    #点击发送私信按钮    
    poco('com.starmakerinteractive.starmaker:id/send_button' ).click()
    #点击消息输入框
    poco('com.starmakerinteractive.starmaker:id/message_edit' ).click()
    text("这是一个断言",enter = False)
    poco('com.starmakerinteractive.starmaker:id/send_button' ).click()
    assert_exists(Template(r"tpl1684380929990.png", record_pos=(0.238, -0.224), resolution=(1080, 2400)), "success")
    #展开私信半屏
    poco('com.starmakerinteractive.starmaker:id/iv_half_page_full_screen').click()
    sleep(2.0)
    #返回广场推荐tab
    poco.click([0.068, 0.069])


#发布器部分
def  recommend_publish():
    #广场推荐tab点击
    poco('com.starmakerinteractive.starmaker:id/tab_name',text="动态" ).click()
    #点击广场右上角发布器icon
    poco('com.starmakerinteractive.starmaker:id/publish_icon').click()
    #点击录制按钮   
    poco('com.starmakerinteractive.starmaker:id/tv_add' ).click()
    #
    resouceList = ["com.starmakerinteractive.starmaker:id/permissionOkTv","com.android.permissioncontroller:id/permission_allow_foreground_only_button","com.android.permissioncontroller:id/permission_allow_button"]
    for resource in resouceList:
        if poco(resource).exists():
            poco(resource).click()  
    #未插入耳机弹窗按钮点击
    poco('com.starmakerinteractive.starmaker:id/recording_headset_dialog_i_know_btn' ).click()
    sleep(5.0)
    #开始录制按钮点击
    poco('com.starmakerinteractive.starmaker:id/rbtn_record_recorder_song_fragment_song_record' ).click()
    sleep(2.0)
    #向上滑动歌词
    poco.swipe([0.51, 0.68],[0.494, 0.129])
    sleep(5.0)
    #录制完成按钮点击
    poco('com.starmakerinteractive.starmaker:id/iv_done_recorder_song_fragment_song_record').click()
    if poco('com.starmakerinteractive.starmaker:id/common_dialog_content' ).exists():
        poco('com.starmakerinteractive.starmaker:id/common_dialog_btn_positive').click()
    sleep(10.0)
    #点击作品tab
    poco.click([0.567, 0.551])
    sleep(3.0)
    #向上滑动作品tab
    poco.swipe([0.497, 0.743],[0.467, 0.206])
    #描述框点击
    poco('com.starmakerinteractive.starmaker:id/ret_input_baserecord_fragment_editor').click()
    text("love")
    #点击空白处保存输入的文字
    poco('com.starmakerinteractive.starmaker:id/v_place').click()
    #是否允许加入合唱入口点击
    poco('com.starmakerinteractive.starmaker:id/ll_duet_baserecord_fragment_edit' ).click()
    #点击不允许加入
    poco('com.starmakerinteractive.starmaker:id/choice_no_allow_duet_check').click()
    poco('com.starmakerinteractive.starmaker:id/choice_ok' ).click()
    #发布作品
    poco('com.starmakerinteractive.starmaker:id/tv_next_baserecord_fragment_edit_btn').click()
    #点击关闭进度页，进入广场tab
    poco('com.starmakerinteractive.starmaker:id/iv_close'  ).click()
    #广场推荐tab点击
    poco('com.starmakerinteractive.starmaker:id/tab_name',text="动态" ).click()
    #点击广场右上角发布器icon
    poco('com.starmakerinteractive.starmaker:id/publish_icon').click()
    #点击伴奏搜索栏调起搜索面板
    poco('com.starmakerinteractive.starmaker:id/txt_search').click()
    #点击半屏搜索栏，输入文字
    poco('com.starmakerinteractive.starmaker:id/searchView').click()
    text("love", search=True)
    #点击录制按钮
    poco('com.starmakerinteractive.starmaker:id/lyt_sing' ).click()
    #录制权限是否打开
    resouceList = ["com.starmakerinteractive.starmaker:id/permissionOkTv","com.android.permissioncontroller:id/permission_allow_foreground_only_button","com.android.permissioncontroller:id/permission_allow_button"]
    for resource in resouceList:
        if poco(resource).exists():
            poco(resource).click() 
    #未插入耳机弹窗按钮点击    
    poco('com.starmakerinteractive.starmaker:id/recording_headset_dialog_i_know_btn' ).click()
    sleep(5.0)
    #开始录制按钮点击
    poco('com.starmakerinteractive.starmaker:id/rbtn_record_recorder_song_fragment_song_record' ).click()
    sleep(3.0)
    #向上滑动歌词
    poco.swipe([0.51, 0.68],[0.494, 0.129])
    sleep(5.0)
    #录制完成按钮点击
    poco('com.starmakerinteractive.starmaker:id/iv_done_recorder_song_fragment_song_record').click()
    if poco('com.starmakerinteractive.starmaker:id/common_dialog_content' ).exists():
        poco('com.starmakerinteractive.starmaker:id/common_dialog_btn_positive').click()
    sleep(10.0)
    #点击作品tab
    poco.click([0.567, 0.551])
    sleep(3.0)
    #向上滑动作品tab
    poco.swipe([0.497, 0.743],[0.467, 0.206])
    #描述框点击
    poco('com.starmakerinteractive.starmaker:id/ret_input_baserecord_fragment_editor').click()
    text("love")
    #点击空白处保存输入的文字
    poco('com.starmakerinteractive.starmaker:id/v_place' ).click()
    #是否允许加入合唱入口点击
    poco('com.starmakerinteractive.starmaker:id/ll_duet_baserecord_fragment_edit' ).click()
    #点击不允许加入
    poco('com.starmakerinteractive.starmaker:id/choice_no_allow_duet_check').click()
    poco('com.starmakerinteractive.starmaker:id/choice_ok' ).click()
    #发布作品
    poco('com.starmakerinteractive.starmaker:id/tv_next_baserecord_fragment_edit_btn').click()
    #点击关闭进度页，进入广场tab
    poco('com.starmakerinteractive.starmaker:id/iv_close'  ).click()
    #广场推荐tab点击
    poco('com.starmakerinteractive.starmaker:id/tab_name',text="动态" ).click()
    #点击广场右上角发布器icon
    poco('com.starmakerinteractive.starmaker:id/publish_icon').click()
    sleep(2.0)
    #点击图文发布tab
    poco.click([0.206, 0.918])
    #录制权限是否打开
    resouceList = ["com.starmakerinteractive.starmaker:id/permissionOkTv","com.android.permissioncontroller:id/permission_allow_foreground_only_button","com.android.permissioncontroller:id/permission_allow_button"]
    for resource in resouceList:
        if poco(resource).exists():
            poco(resource).click()  
    sleep(2.0) 
    #选择两张图片
    poco.click([0.278, 0.162])
    poco.click([0.613, 0.162])
    #选择话题
    poco('com.starmakerinteractive.starmaker:id/tv_topic' ).click()
    #点击下一步按钮
    poco('com.starmakerinteractive.starmaker:id/btn_next').click()
    sleep(2.0)
    #点击描述框输入描述
    poco('com.starmakerinteractive.starmaker:id/ret_post_desc' ).click()
    text("love")
    #点击完成按钮完成输入
    poco('com.starmakerinteractive.starmaker:id/tv_done').click()
    sleep(2.0)
    #发布作品
    poco('com.starmakerinteractive.starmaker:id/tv_post').click()
    #广场推荐tab点击
    poco('com.starmakerinteractive.starmaker:id/tab_name',text="动态" ).click()
    #点击广场右上角发布器icon
    poco('com.starmakerinteractive.starmaker:id/publish_icon').click()
    #点击故事tab
    poco.click([0.357, 0.922])
    if poco('com.starmakerinteractive.starmaker:id/permissionOkTv').exists():
        poco('com.starmakerinteractive.starmaker:id/permissionOkTv').click()
        resouceList = ["com.starmakerinteractive.starmaker:id/permissionOkTv","com.android.permissioncontroller:id/permission_allow_foreground_only_button","com.android.permissioncontroller:id/permission_allow_button"]
    for resource in resouceList:
        if poco(resource).exists():
            poco(resource).click()  
    #录制10秒
    poco('com.starmakerinteractive.starmaker:id/rbtn_record_capturelib_fragment_capture' ).long_click(duration=10)
    sleep(3.0)
    #输入描述
    poco('com.starmakerinteractive.starmaker:id/ret_post_desc' ).click()
    text("love")
    #完成输入描述
    poco('com.starmakerinteractive.starmaker:id/tv_done').click()
    sleep(2.0)
    #发布作品
    poco('com.starmakerinteractive.starmaker:id/tv_post').click()
    