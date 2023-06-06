# -*- encoding=utf8 -*-
__author__ = "DingShuang"

from airtest.core.api import *

auto_setup(__file__)
#def inti_poco():
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

    #global poco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# 验证卡拉ok房间跳转成功
def sing_now():
    # 点击立即演唱按钮
    poco("com.starmakerinteractive.starmaker:id/tv_button_name").click()
    sleep(1.0)
    assert_exists(Template(r"tpl1684314223140.png", record_pos=(-0.281, -0.98), resolution=(1080, 2400)), "成功进入卡拉ok房间")
    # 退出房间
    poco("com.starmakerinteractive.starmaker:id/img_close_room").click()
    sleep(1.0)

# 验证快速游戏半屏
def fast_game():
    # 点击快速游戏按钮
    poco("android.view.ViewGroup")[2].click()
    sleep(1.0)
    assert_exists(Template(r"tpl1684314740480.png", record_pos=(-0.001, 0.636), resolution=(1080, 2400)), "成功打开快速游戏半屏页面")
    # 点击其他位置关闭半屏
    keyevent("BACK")
# 验证跳转直播页面
def live_tab():
    poco("android.view.ViewGroup")[0].click()
    sleep(1.0)
    if exists(Template(r"tpl1684315196822.png", record_pos=(-0.006, -0.021), resolution=(1080, 2400))):
        poco("com.starmakerinteractive.starmaker:id/tv_check").click()
        sleep(1.0)
        poco("com.starmakerinteractive.starmaker:id/tv_confirm").click()
        sleep(1.0)
    # 点击直播按钮
    poco("com.starmakerinteractive.starmaker:id/ic_live_start_live").click()
    sleep(1.0)
    if exists(Template(r"tpl1684315392841.png", record_pos=(-0.015, -0.206), resolution=(1080, 2400))):
        poco("com.starmakerinteractive.starmaker:id/permissionOkTv").click()
        sleep(1.0)
        # 授权允许视频拍摄
        touch(Template(r"tpl1684315491894.png", record_pos=(0.008, 0.087), resolution=(1080, 2400)))
        sleep(1.0)
        touch(Template(r"tpl1684315491894.png", record_pos=(0.008, 0.087), resolution=(1080, 2400)))
        sleep(1.0)
    # 取消通知粉丝
    if exists(Template(r"tpl1684315681544.png", rgb=True, record_pos=(-0.132, -0.431), resolution=(1080, 2400))):

        poco("com.starmakerinteractive.starmaker:id/img_push").click()
    # 设置没验开启直播
    # 磨皮开到最大
    poco("com.starmakerinteractive.starmaker:id/live_create_beautify").click()
    sleep(1.0)
    swipe(Template(r"tpl1684316128538.png", record_pos=(-0.166, 0.355), resolution=(1080, 2400)), Template(r"tpl1684316149350.png", record_pos=(0.399, 0.35), resolution=(1080, 2400)),vector=[0.2504, 0.0092],duration=0.05)
    sleep(1.0)

    # 瘦脸开到最大
    poco("com.starmakerinteractive.starmaker:id/iv_image_live_view_filter_item")[1].click()
    sleep(1.0)
    swipe(Template(r"tpl1684316424785.png", record_pos=(-0.285, 0.354), resolution=(1080, 2400)),Template(r"tpl1684316436016.png", record_pos=(0.398, 0.349), resolution=(1080, 2400)) ,vector=[0.7083, 0.0151],duration=0.05)
    sleep(1.0)
    # 点击滤镜
    poco(text="滤镜").click()
    sleep(1.0)
    #使用第一个滤镜
    poco("com.starmakerinteractive.starmaker:id/iv_image_live_view_filter_item")[1].click()
    sleep(2.0)
    keyevent("BACK")
    # 点击开始直播
    poco("com.starmakerinteractive.starmaker:id/txv_start_live_content").click()
    sleep(4.0)
    assert_exists(Template(r"tpl1684316760912.png", record_pos=(0.006, 0.92), resolution=(1080, 2400)), "成功开启直播")
    
    # 关闭直播返回主页面
    poco("com.starmakerinteractive.starmaker:id/iv_room_quit").click()
    sleep(1.0)
    poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_positive").click()
    sleep(1.0)
    keyevent("BACK")
    keyevent("BACK")
        
# 验证feedtab
def feed_tab():
#     # 点击推荐tab按钮
#     poco(text="推荐").click()
#     assert_exists(Template(r"tpl1684310850401.png", record_pos=(-0.362, 0.216), resolution=(1080, 2400)), "推荐tab下有聊天房")
#     assert_exists(Template(r"tpl1684310895507.png", record_pos=(0.136, 0.219), resolution=(1080, 2400)), "推荐tab下有音乐房")
    

    # 点击音乐tab
    poco(text="音乐").click()
    assert_exists(Template(r"tpl1684313808219.png", record_pos=(-0.034, -0.129), resolution=(1080, 2400)), "成功跳转音乐tab")
    
    # 点击游戏tab
    poco(text="游戏").click()
    assert_exists(Template(r"tpl1684313870939.png", record_pos=(-0.008, -0.133), resolution=(1080, 2400)), "成功跳转游戏tab")
# 验证更多页面    
def more_tab():
    # 点击更多按钮
    poco("com.starmakerinteractive.starmaker:id/tv_room_desc").click()
    sleep(1.0)
    assert_exists(Template(r"tpl1684314028256.png", record_pos=(-0.262, -0.98), resolution=(1080, 2400)), "更多页面跳转成功")
    # 返回主页面
    keyevent("BACK")

# 进入房间
def join_ktv():
    # 点击房间icon
    poco("com.starmakerinteractive.starmaker:id/iv_room_avatar").click()
    sleep(1.0)
    # 点击进入房间
    poco("com.starmakerinteractive.starmaker:id/tv_edit_room").click()
    sleep(1)
    
# 进入编辑房间页面
def edit_ktv():
    poco("com.starmakerinteractive.starmaker:id/room_name").click()
    sleep(1.0)
    poco("com.starmakerinteractive.starmaker:id/tv_edit_room").click()
    sleep(1.0)

    
# 验证公告编辑及设置
def announcement_ktv():
    # 点击公告按钮
    poco("com.starmakerinteractive.starmaker:id/room_announcement").click()
    sleep(1.0)
    if exists(Template(r"tpl1684320499972.png", record_pos=(-0.087, 0.03), resolution=(1080, 2400))):

        # 设置主动弹出
        poco("com.starmakerinteractive.starmaker:id/cb_switch").click()
        assert_exists(Template(r"tpl1684305387665.png", record_pos=(-0.09, 0.031), resolution=(1080, 2400)), "成功设置主动弹出")
    else:
        poco("com.starmakerinteractive.starmaker:id/cb_switch").click()
        assert_exists(Template(r"tpl1684320572058.png", record_pos=(-0.096, 0.033), resolution=(1080, 2400)), "取消公告主动弹出")
    # 编辑公告
    poco("com.starmakerinteractive.starmaker:id/tv_edit").click()
    sleep(1.0)
    for i in range(500):
        text=poco("com.starmakerinteractive.starmaker:id/edt_text").get_text()
#         log(text)
        if text != '房间里没有公告。':
            keyevent("KEYCODE_DEL")
        else:
            break     
    # 输入编辑内容        
    poco("com.starmakerinteractive.starmaker:id/edt_text").set_text("edit announcement_ktv")
    sleep(1.0)
    # 点击完成按钮
    poco("com.starmakerinteractive.starmaker:id/right_tv").click()
    sleep(1.0)
    keyevent("BACK")
    sleep(1.0)
    # 点击公告按钮
    poco("com.starmakerinteractive.starmaker:id/room_announcement").click()
    sleep(1.0)
    ann_text = poco("com.starmakerinteractive.starmaker:id/tv_content").get_text()
    #log(ann_text)
    # 断言房间公告编辑成功
    assert_equal(ann_text, "edit announcement_ktv", "成功更改房间公告")
    # 关闭公告弹窗
    poco("com.starmakerinteractive.starmaker:id/iv_close").click()
# announcement_ktv()

# from airtest.core.api import *

# auto_setup(__file__)
# from poco.drivers.android.uiautomation import AndroidUiautomationPoco

# global poco
# poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 验证分享功能
def share_ktv():
    # 点击分享按钮
    poco("com.starmakerinteractive.starmaker:id/share_room").click()
    sleep(1.0)
    # 点击第二位好友
    poco("com.starmakerinteractive.starmaker:id/item_rl")[0].click()
    sleep(1.0)
    # 点击分享按钮
    poco("com.starmakerinteractive.starmaker:id/tv_share").click()
#     sleep(1.0)
    if exists(Template(r"tpl1684304371540.png", record_pos=(-0.007, 0.774), resolution=(1080, 2400))):
        log("好友分享成功")
    sleep(1.0)
    # 点击我的好友，跳转好友列表页
    # 点击分享按钮
    poco("com.starmakerinteractive.starmaker:id/share_room").click()
    sleep(1.0)
    #点击我的好友
    poco(text="我的好友").click()
    wait(Template(r"tpl1684304708097.png", record_pos=(-0.222, -0.91), resolution=(1080, 2400)))
    # 选中第一个好友，点击分享
    poco("com.starmakerinteractive.starmaker:id/cb_choose")[0].click()
    poco("com.starmakerinteractive.starmaker:id/btn_share").click()
    assert_exists(Template(r"tpl1684304371540.png", record_pos=(-0.007, 0.774), resolution=(1080, 2400)), "跳转好友页分享成功")
    
    # 点击复制
    # 点击分享按钮
    poco("com.starmakerinteractive.starmaker:id/share_room").click()
    sleep(1.0)
    #点击复制
    poco(text="复制链接").click()
    assert_exists(Template(r"tpl1684304972312.png", record_pos=(-0.019, 0.795), resolution=(1080, 2400)), "成功复制链接")

# share_ktv()
# from airtest.core.api import *

# auto_setup(__file__)
# from poco.drivers.android.uiautomation import AndroidUiautomationPoco

# global poco
# poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

#验证音乐房
def sing_ktv():
    if exists(Template(r"tpl1684294975414.png", record_pos=(0.026, -0.947), resolution=(1080, 2400))):
        
        # 点击演唱按钮
        poco("com.starmakerinteractive.starmaker:id/tv_singing").click()
        sleep(1.0)
        # 点歌页面点击第一首歌曲点歌按钮
        poco("com.starmakerinteractive.starmaker:id/btn_sing")[0].click()
        sleep(1.0)
        # 点击独唱
        poco(text="独唱").click()
        wait(Template(r"tpl1684295403105.png", record_pos=(-0.002, -0.008), resolution=(1080, 2400)))

        # 点击弹窗开始唱按钮
        poco("com.starmakerinteractive.starmaker:id/sing_start").click()
        sleep(1.0)
        assert_exists(Template(r"tpl1684295459543.png", record_pos=(-0.078, -0.966), resolution=(1080, 2400)), "开始独唱成功")
        #停止演唱
        #点击完成按钮
        poco("com.starmakerinteractive.starmaker:id/sing_finish").click()
        wait(Template(r"tpl1684295642267.png", record_pos=(0.001, -0.019), resolution=(1080, 2400)))
        poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_positive").click()
        sleep(1.0)
        assert_exists(Template(r"tpl1684295753041.png", record_pos=(0.317, 0.02), resolution=(1080, 2400)), "成功停止演唱")


        #发起合唱
        # 点击演唱按钮
        poco("com.starmakerinteractive.starmaker:id/tv_singing").click()
        sleep(1.0)
        # 点歌页面点击第一首歌曲点歌按钮
        poco("com.starmakerinteractive.starmaker:id/btn_sing")[0].click()
        sleep(1.0)
        # 点击发起合唱
        poco(text="发起合唱").click()
        sleep(1.0)
        # 唱粉色部分
        poco("com.starmakerinteractive.starmaker:id/pink_part_tv").click()
        wait(Template(r"tpl1684303602833.png", record_pos=(-0.126, -0.85), resolution=(1080, 2400)))
        assert_exists(Template(r"tpl1684303617775.png", record_pos=(-0.002, 0.01), resolution=(1080, 2400)), "成功发起合唱")
    else:
        # 切换至音乐房
        poco("com.starmakerinteractive.starmaker:id/switch_mode_icon").click()
        sleep(1.0)
        poco("com.starmakerinteractive.starmaker:id/iv_bg")[2].click()
        sleep(1.0)
         # 点击演唱按钮
        poco("com.starmakerinteractive.starmaker:id/tv_singing").click()
        sleep(1.0)
        # 点歌页面点击第一首歌曲点歌按钮
        poco("com.starmakerinteractive.starmaker:id/btn_sing")[0].click()
        sleep(1.0)
        # 点击独唱
        poco(text="独唱").click()
        wait(Template(r"tpl1684295403105.png", record_pos=(-0.002, -0.008), resolution=(1080, 2400)))

        # 点击弹窗开始唱按钮
        poco("com.starmakerinteractive.starmaker:id/sing_start").click()
        sleep(1.0)
        assert_exists(Template(r"tpl1684295459543.png", record_pos=(-0.078, -0.966), resolution=(1080, 2400)), "开始独唱成功")
        #停止演唱
        #点击完成按钮
        poco("com.starmakerinteractive.starmaker:id/sing_finish").click()
        wait(Template(r"tpl1684295642267.png", record_pos=(0.001, -0.019), resolution=(1080, 2400)))
        poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_positive").click()
        sleep(1.0)
        assert_exists(Template(r"tpl1684295753041.png", record_pos=(0.317, 0.02), resolution=(1080, 2400)), "成功停止演唱")


        #发起合唱
        # 点击演唱按钮
        poco("com.starmakerinteractive.starmaker:id/tv_singing").click()
        sleep(1.0)
        # 点歌页面点击第一首歌曲点歌按钮
        poco("com.starmakerinteractive.starmaker:id/btn_sing")[0].click()
        sleep(1.0)
        # 点击发起合唱
        poco(text="发起合唱").click()
        sleep(1.0)
        # 唱粉色部分
        poco("com.starmakerinteractive.starmaker:id/pink_part_tv").click()
        wait(Template(r"tpl1684303602833.png", record_pos=(-0.126, -0.85), resolution=(1080, 2400)))
        assert_exists(Template(r"tpl1684303617775.png", record_pos=(-0.002, 0.01), resolution=(1080, 2400)), "成功发起合唱")
    # 取消发起合唱
    poco("com.starmakerinteractive.starmaker:id/txt_cancel").click()
    poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_positive").click()
    poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_positive").click()
# sing_ktv()

    
# 上麦
def take_seat():
    if not exists(Template(r"tpl1684322032720.png", record_pos=(0.016, -0.956), resolution=(1080, 2400))):
        # 切换至聊天房
        poco("com.starmakerinteractive.starmaker:id/switch_mode_icon").click()
        sleep(1.0)
        poco(text="聊天").click()
        sleep(1.0)
        poco("com.starmakerinteractive.starmaker:id/v_seat_bg")[1].click()
        sleep(1.0)
        poco(text="入座").click()
#         # 获上麦成公屏消息
#         name_take = poco("com.starmakerinteractive.starmaker:id/tv_name").get_text()
#         log(name_take)
#         name_text = poco("com.starmakerinteractive.starmaker:id/root_view")[3].get_text
      
#         name_long = len(name_text)
#         # 获取上麦用户昵称
#         name = name_text[:name_long-5]
        if exists(Template(r"tpl1684390219599.png", record_pos=(-0.167, 0.613), resolution=(1080, 2400))):
            log('上麦成功')
        
#验多麦房打开亲密麦位
def open_relation():
    # 判断是否是聊天房
    if exists(Template(r"tpl1684293906477.png", record_pos=(0.015, -0.955), resolution=(1080, 2400))):

        # 点击玩法入口
        poco("com.starmakerinteractive.starmaker:id/v_menu_play_center").click()
        sleep(1.0)
        # 点击关系模式按钮
        touch(Template(r"tpl1684391176361.png", record_pos=(0.01, 0.851), resolution=(1080, 2400)))

        sleep(1.0)
    else:
        # 切换至聊天房
        poco("com.starmakerinteractive.starmaker:id/switch_mode_icon").click()
        sleep(1.0)
        poco("com.starmakerinteractive.starmaker:id/iv_bg")[10].click()
        sleep(1.0)
        # 点击玩法入口
        poco("com.starmakerinteractive.starmaker:id/v_menu_play_center").click()
        sleep(1.0)
        # 点击关系模式按钮
        poco(text="关系模式").click()
        sleep(1.0)

    # 断言亲密麦位开启成功
    assert_exists(Template(r"tpl1684291436332.png", record_pos=(0.012, -0.358), resolution=(1080, 2400)), "亲密麦位开启成功")

        
        
# from airtest.core.api import *

# auto_setup(__file__)
# from poco.drivers.android.uiautomation import AndroidUiautomationPoco

# global poco
# poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 验证邀请上麦
def invite_seat():
    # 操作序列号为R58N53KLRKY的设备
    set_current("R58N53KLRKY")
    # 进入线上环境820968房间
    # 点击搜索输入框
    poco("com.starmakerinteractive.starmaker:id/tv_search_content").click()
    sleep(1)
    # 在搜索输入框输入房间id820968
    poco("com.starmakerinteractive.starmaker:id/searchView").set_text("820968")
    # 点击键盘搜索按钮
    touch(Template(r"tpl1684232257585.png", record_pos=(0.41, 0.903), resolution=(720, 1600)))
    sleep(1.0)
    # 点击搜索结果第一个房间,进房
    poco("com.starmakerinteractive.starmaker:id/img_cover").click()
    sleep(5.0)
    # 操作另一台设备10.100.7.202:5555
    set_current("10.100.7.202:5555")
    sleep(5.0)

    # 进入我自己的房间
    poco("com.starmakerinteractive.starmaker:id/iv_room_avatar").click()
    sleep(1.0)

    poco("com.starmakerinteractive.starmaker:id/tv_edit_room").click()
    sleep(1.0)

    # 打开在线用户列表
    poco("com.starmakerinteractive.starmaker:id/online_user_num_text").click()
    sleep(1.0)

    # 点击第二位用户头像
    poco("com.starmakerinteractive.starmaker:id/civ_head_view").click()
    sleep(1.0)
    # 点击用户卡片上麦按钮
    poco("com.starmakerinteractive.starmaker:id/btn_operation_request_mic").click()
    sleep(1.0)
    # 选择2号麦位
    poco(text="2号麦").click()
    sleep(5.0)

    # 操作对方设备
    set_current("R58N53KLRKY")
    sleep(5.0)

    # 点击弹窗确认按钮
    poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_positive").click
    assert_exists(Template(r"tpl1684234667012.png", record_pos=(-0.222, -0.487), resolution=(720, 1600)), "2号上麦成功")
    # 下麦
    poco("com.starmakerinteractive.starmaker:id/civ_head_view").click()
    sleep(1.0)
    poco(text="离开").click()
    sleep(1.0)
    
# invite_seat()    
  
# 验证下麦
def left_seat():
    touch(Template(r"tpl1684390406582.png", record_pos=(-0.369, -0.482), resolution=(1080, 2400)))
    sleep(1)

    touch(Template(r"tpl1681118403180.png", record_pos=(-0.408, 0.637), resolution=(1080, 2400)))
    sleep(1)
    assert_exists(Template(r"tpl1684323048980.png", record_pos=(-0.004, -0.366), resolution=(1080, 2400)), "下麦成功")



#     # text = poco(text="ds7777777778   离开了1号麦")
#     # 获取下麦成功公屏消息
#     text = poco("com.starmakerinteractive.starmaker:id/tv_name").get_text
#     text2 = "离开了1号麦"
#     # 拼接下麦成功公屏文案
#     expect_name = name+text2
#     # 断言下麦成功公屏消息是否与期望值一致
#     assert_equal(text, expect_name, "下麦")



# 验证打开申请上麦权限
def seat_setting_anyone():
    
    touch(Template(r"tpl1681122497126.png", record_pos=(0.098, 0.923), resolution=(1080, 2400)))

    sleep(1)
    touch(Template(r"tpl1681122525073.png", record_pos=(0.436, -0.156), resolution=(1080, 2400)))
    sleep(1.0)
    touch(Template(r"tpl1681122555593.png", record_pos=(-0.274, 0.756), resolution=(1080, 2400)))
    # 断言举手上麦设置成功
    if exists(Template(r"tpl1681122576634.png", record_pos=(-0.343, -0.135), resolution=(1080, 2400))):
        log("已更改上麦方式为同意后上麦")
    keyevent("BACK")


# 验证多麦房设置等级权限上麦
def who_seat_setting():
    touch(Template(r"tpl1681123010398.png", record_pos=(-0.33, 0.816), resolution=(1080, 2400)))
    sleep(1.0)
    touch(Template(r"tpl1681123059043.png", record_pos=(-0.367, 0.4), resolution=(1080, 2400)))
    sleep(1.0)
    # 断言5级以上用户上麦设置成功
    if exists(Template(r"tpl1681123081877.png", record_pos=(0.0, 0.813), resolution=(1080, 2400))):
        log("5级以上用户可上麦")

    touch(Template(r"tpl1681123166158.png", record_pos=(-0.355, 0.815), resolution=(1080, 2400)))
    sleep(1.0)
    
    if exists(Template(r"tpl1681194725731.png", record_pos=(-0.331, 0.764), resolution=(1080, 2400))):

        touch(Template(r"tpl1681123179038.png", record_pos=(-0.355, 0.766), resolution=(1080, 2400)))
    else:
        touch(Template(r"tpl1681194789870.png", record_pos=(-0.361, 0.641), resolution=(1080, 2400)))

    sleep(1.0)
    # 断言30级以上用户上麦设置成功
    if exists(Template(r"tpl1681123191782.png", record_pos=(0.008, 0.81), resolution=(1080, 2400)))or(Template(r"tpl1681194828055.png", record_pos=(-0.007, 0.812), resolution=(1080, 2400))):
        log("30/20级以上用户可上麦")

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
    keyevent("BACK")
    keyevent("BACK")



        
#如果当前房类型是多麦房，验证上麦权限设置
def seat_ktv():
    if exists(Template(r"tpl1681125608044.png", record_pos=(0.026, -0.968), resolution=(1080, 2400))):
        touch(566,157)
        sleep(1.0)
        touch(Template(r"tpl1681125084999.png", record_pos=(-0.323, -0.113), resolution=(1080, 2400)))
        sleep(1)
        who_seat_setting()
    else:
        who_seat_setting()
        
#  验证设置进房权限        
def join_ktv_setting():
    touch(Template(r"tpl1681198452505.png", record_pos=(-0.344, 0.695), resolution=(1080, 2400)))
    sleep(1)
    touch(Template(r"tpl1681198467177.png", record_pos=(-0.338, 0.765), resolution=(1080, 2400)))
    sleep(1.0)
    if exists(Template(r"tpl1681198483739.png", record_pos=(-0.009, 0.684), resolution=(1080, 2400))):
        log('仅本地区用户进房设置成功')

    # 验证设置家族权限
    touch(Template(r"tpl1681198494734.png", record_pos=(-0.365, 0.696), resolution=(1080, 2400)))
    sleep(1.0)
    touch(Template(r"tpl1681198567596.png", record_pos=(-0.358, 0.639), resolution=(1080, 2400)))
    sleep(1.0)
    if exists(Template(r"tpl1681198582933.png", record_pos=(-0.006, 0.698), resolution=(1080, 2400))):
        log('仅家族成员用户进房设置成功')
    # 验证设置任意用户可进房
    touch(Template(r"tpl1681198613053.png", record_pos=(-0.361, 0.69), resolution=(1080, 2400)))
    sleep(1.0)
    poco(text="任意用户").click()
    if exists(Template(r"tpl1681198644289.png", record_pos=(-0.001, 0.688), resolution=(1080, 2400))):
        log('任意用户可进房设置成功')
    sleep(1.0)
    # 验证设置房主关注的人可进房
    touch(Template(r"tpl1681198731240.png", record_pos=(-0.355, 0.693), resolution=(1080, 2400)))
    sleep(1.0)
    poco(text="房主关注的人").click()
    sleep(1.0)
    if exists(Template(r"tpl1681198760439.png", record_pos=(-0.01, 0.698), resolution=(1080, 2400))):
        log('房主关注的人可进房设置成功')
    # 返回主页面
    keyevent("BACK")
    keyevent("BACK")

    

def game_take_seat():
    if not exists(Template(r"tpl1684376831453.png", record_pos=(0.022, -0.955), resolution=(1080, 2400)) or Template(r"tpl1684376853504.png", record_pos=(0.018, -0.958), resolution=(1080, 2400)) or Template(r"tpl1684376867598.png", record_pos=(0.022, -0.952), resolution=(1080, 2400)) or Template(r"tpl1684376882821.png", record_pos=(0.021, -0.952), resolution=(1080, 2400))):
        poco("com.starmakerinteractive.starmaker:id/switch_mode_icon").click()
        sleep(1.0)
        poco(text="LUDO").click()
        sleep(1.0)

    # 验证上麦
    touch([73, 348])
    sleep(1.0)
    touch(Template(r"tpl1681200628767.png", record_pos=(-0.406, 0.519), resolution=(1080, 2400)))
    touch(Template(r"tpl1681202639157.png", record_pos=(-0.004, 0.37), resolution=(1080, 2400)))
    if exists(Template(r"tpl1684377147089.png", record_pos=(-0.276, 0.823), resolution=(1080, 2400))):
        log('游戏及房间上麦成功')

# 验证关闭麦位
def close_seat():
    # 点击房间模式icon
    butoon = poco("com.starmakerinteractive.starmaker:id/switch_mode_icon")
    butoon.click()
    sleep(1.0)
    # 点击合唱房位置
    touch([503, 408])    
    sleep(2.0)
    # 点击第一个麦位位置
    poco("com.starmakerinteractive.starmaker:id/v_seat_bg")[0].click()
    sleep(1.0)
    touch(Template(r"tpl1681203279140.png", record_pos=(-0.339, 0.641), resolution=(1080, 2400)))
    sleep(1.0)
    # 断言合唱房关闭麦位成功
    assert_exists(Template(r"tpl1681203397957.png", record_pos=(-0.009, -0.058), resolution=(1080, 2400)), "合唱房第一个麦位被锁")
    

# 验证送礼经验值增加
def exp():
    # 获取exp文本
    exp_text = poco("com.starmakerinteractive.starmaker:id/head_bar_tv_exp_fraction").get_text()
#     log(type(exp_text))
    # 获取当前房间经验值
    exp_before = exp_text[:-5]
    # 转换为整型
    exp_bef = int(exp_before)
    log(exp_before)
    log(type(exp_bef))
    # 点击礼物面板
    poco("com.starmakerinteractive.starmaker:id/v_menu_send_gift").click()
    sleep(1)
    if exists(Template(r"tpl1684377345295.png", record_pos=(0.298, 0.246), resolution=(1080, 2400))):
        poco("android.widget.ImageView").click()
        sleep(1.0)
    # 默认赠送1个第一个礼物
    poco("com.starmakerinteractive.starmaker:id/btn_send_gift").click()
    sleep(2.0)
    if exists(Template(r"tpl1684378534970.png", record_pos=(-0.11, 0.16), resolution=(1080, 2400))):

        # 点击其他位置关闭礼物面板
        poco("com.starmakerinteractive.starmaker:id/gift_click_outside").click()
        sleep(1.0)

    # 再次获取exp文本
    exp_text_after = poco("com.starmakerinteractive.starmaker:id/head_bar_tv_exp_fraction").get_text()
    log(exp_text)
    # 获取当前房间经验值
    exp_gift_after = int(exp_text_after[:-5])
#     log(type(exp_gift_after))
    log(exp_gift_after)
    # 断言赠送礼物后经验值增加
    if exp_bef < exp_gift_after:
        assert_not_equal(exp_bef, exp_gift_after, "请填写测试点.")
    else:
        log('赠送礼物经验证未增加')
    
#设置房间标签

def setting_tag():
    # 点击选择房间标签按钮
    poco("com.starmakerinteractive.starmaker:id/tv_tag").click()
    sleep(1.0)

#     # 获取当前标签数
#     label_str = poco("com.starmakerinteractive.starmaker:id/tv_selected_label").get_text()[4]
#     label = int(label_str)
#     log(label)
#     log(type(label))
    if exists(Template(r"tpl1684379814067.png", record_pos=(-0.378, -0.415), resolution=(1080, 2400))):
        # 点击交朋友
        poco(text="交朋友").click()
        # 点击保存按钮
        poco("com.starmakerinteractive.starmaker:id/tv_save").click()
        sleep(1)
        # 断言交朋友标签设置成功
        text_friend = poco("com.starmakerinteractive.starmaker:id/tv_tag").get_text()
        log(text_friend)
#         assert_exists(text_friend, "标签设置成功")
        assert_equal(text_friend, "交朋友", "标签设置成功.")

    else:
        # 删除标签
#         poco("com.starmakerinteractive.starmaker:id/tv_tag").click()
#         sleep(1.0)
        # 点击编辑按钮
        poco("com.starmakerinteractive.starmaker:id/tv_edit").click()
        sleep(1.0)
        for i in range(3):
            # 点击第一个标签删除按钮
            poco("com.starmakerinteractive.starmaker:id/tag_icon").click()
            sleep(1)
            # 获取当前标签数
            label_str = poco("com.starmakerinteractive.starmaker:id/tv_selected_label").get_text()[4]
            label = int(label_str)
            log(label)
            log(type(label))
            if label == 0:
                break
        # 点击保存按钮
        poco("com.starmakerinteractive.starmaker:id/tv_save").click()
        sleep(1.0)
        # 断言标签删除成功
        del_label = poco("com.starmakerinteractive.starmaker:id/tv_tag").get_text()

        assert_equal(del_label, "请选择房间标签", "房间标签删除成功.")



# 验证节目单跳转
def programme():
    # 点击节目单标签箭头
    poco("com.starmakerinteractive.starmaker:id/room_programme_entrance_view").click()
        # 定义节目单控件存在
    a_bool = poco("com.starmakerinteractive.starmaker:id/cl_bg").exists
    for i in range(10):
        if a_bool:
#             log('a_bool')
            # 点击节目单控件
            poco("com.starmakerinteractive.starmaker:id/cl_bg").click()
            break
        else:
            poco("com.starmakerinteractive.starmaker:id/cl_bg").refresh()
        sleep(1.0)

    # 断言节目单跳转成功
    assert_exists(Template(r"tpl1684379314947.png", record_pos=(-0.196, -0.318), resolution=(1080, 2400)), "节目单跳转成功")
    # 关闭节目单
    touch(Template(r"tpl1684380160360.png", record_pos=(-0.438, -0.355), resolution=(1080, 2400)))



# programme()





#intipoco()
sing_now()
fast_game()
live_tab()
feed_tab()
more_tab()
join_ktv()
announcement_ktv()
share_ktv()
sing_ktv()
take_seat()
left_seat()
open_relation()
# invite_seat()
seat_setting_anyone()
edit_ktv()
seat_ktv()
edit_ktv()
join_ktv_setting()
game_take_seat()
close_seat()
exp()
setting_tag()
programme()














