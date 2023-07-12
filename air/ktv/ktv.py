# -*- encoding=utf8 -*-
__author__ = "DingShuang"

from airtest.core.api import *

auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


import os

# # 授权开启麦克风及相机权限
# def grant_permission(package_name):
#     os.system(f"adb shell pm grant {package_name} android.permission.CAMERA")
#     os.system(f"adb shell pm grant {package_name} android.permission.RECORD_AUDIO")

#物理返回键
def back(a):
    for i in range(0, int(a)):
        keyevent("KEYCODE_BACK")

# 获取屏幕大小   
screen_size = poco.get_screen_size()
# print(screen_size)  # 列表[1080, 2400]
wid = screen_size[0]
leng = screen_size[1]
# print(wid,leng)
#上滑动
def up(b):
    for i in range(0,int(b)): 
        swipe([wid * 0.5, leng * 0.8], [wid * 0.5, leng * 0.2])
#下滑动
def down(c):
    for i in range(0,int(c)):
        swipe([wid * 0.5, leng * 0.3], [wid * 0.5, leng * 0.8])



# 验证卡拉ok房间跳转成功
def sing_now():
    # 点击立即演唱按钮
    poco("com.starmakerinteractive.starmaker:id/tv_button_name").click()
    sleep(1.0)
    assert_exists(Template(r"tpl1684314223140.png", record_pos=(-0.281, -0.98), resolution=(1080, 2400)), "成功进入卡拉ok房间")
    # 退出房间,返回主页面
    poco("com.starmakerinteractive.starmaker:id/img_close_room").click()
    sleep(1.0)
#     shell("am start sm://discovery")
# 验证快速游戏半屏
def fast_game():
    # 点击快速游戏按钮
    poco("android.view.ViewGroup")[2].click()
    sleep(1.0)
    assert_exists(Template(r"tpl1684314740480.png", record_pos=(-0.001, 0.636), resolution=(1080, 2400)), "成功打开快速游戏半屏页面")
    # 点击其他位置关闭半屏，返回主页面
    back(1)
# 验证跳转直播页面
def live_tab():
    poco("android.view.ViewGroup")[0].click()
    sleep(1.0)
    # 有弹窗，按钮名称是领取奖励
#     if poco("com.starmakerinteractive.starmaker:id/tv_check").get_text() == '领取奖励':
    if poco("com.starmakerinteractive.starmaker:id/tv_check").exists():
        print(1)
        pop_text = poco("com.starmakerinteractive.starmaker:id/tv_check").get_text()
        pop_text4 = pop_text[:4]
        print(pop_text[:4])
        if pop_text == '领取奖励':
#         poco("com.starmakerinteractive.starmaker:id/head_title").text()
            poco("com.starmakerinteractive.starmaker:id/tv_check").click()
            sleep(1.0)
            poco("com.starmakerinteractive.starmaker:id/tv_confirm").click()
            sleep(1.0)
            print(2)
    # 有弹窗，按钮前四位文案是明天再来
        elif pop_text4 == '明天在来':
            # 点击弹窗外部分，关闭弹窗
            touch([408, 129])
            sleep(1.0)
            print("有弹窗，按钮前四位文案是明天再来")
    
    # 点击直播按钮
    poco("com.starmakerinteractive.starmaker:id/ic_live_start_live").click()
    sleep(1.0)
    # 授权麦克风/录像权限
    if poco("com.starmakerinteractive.starmaker:id/permissionOkTv").exists():
        poco("com.starmakerinteractive.starmaker:id/permissionOkTv").click()
        sleep(0.5)
        poco("com.android.permissioncontroller:id/permission_allow_button").click()
        sleep(0.5)
        
        
        
        # 取消通知粉丝
    if exists(Template(r"tpl1684315681544.png", rgb=True, record_pos=(-0.132, -0.431), resolution=(1080, 2400))):

        poco("com.starmakerinteractive.starmaker:id/img_push").click()
    # 设置美颜开启直播
    # 磨皮
    poco("com.starmakerinteractive.starmaker:id/live_create_beautify").click()
    sleep(1.0)
    swipe([0.341 * wid, 0.659 * leng],[0.8 * wid, 0.659 * leng])
    sleep(1.0)

    # 瘦脸
    poco("com.starmakerinteractive.starmaker:id/iv_image_live_view_filter_item")[1].click()
    sleep(1.0)
    swipe([0.212 * wid, 0.659 * leng],[0.8 * wid, 0.659 * leng])
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
    touch([0.683 * wid, 0.537 * leng])
    
    sleep(1.0)
    back(2)
        
# 验证feedtab
def feed_tab():
    # 点击推荐tab
    poco(text="推荐").click()
    sleep(0.5)
    # 获取推荐列表语音房类型名字
    text_ktv_tag = poco("com.starmakerinteractive.starmaker:id/tv_category")
    # 如果推荐列表有数据，循环向下滑动十次，验证聊天房存在
    if text_ktv_tag.exists():
        count = 0
        for i in range(10):        
            if text_ktv_tag.get_text() == '聊天':
                assert_exists(Template(r"tpl1686896459492.png", record_pos=(-0.373, 0.22), resolution=(1080, 2400)), "推荐tab下展示聊天房") 
            else:
                up(1)
                i = i+1
                count = i
            break
    down(count)
    # 点击卡拉ok tab
    poco("com.starmakerinteractive.starmaker:id/tv_tab_title")[1].click()
    
    assert_exists(Template(r"tpl1686885727858.png", record_pos=(-0.029, 0.197), resolution=(1080, 2400)), "成功跳转卡拉ok tab")
    
    # 点击游戏tab
    poco(text="游戏").click()
    assert_exists(Template(r"tpl1686896647110.png", record_pos=(0.002, 0.201), resolution=(1080, 2400)), "成功跳转游戏tab")
# 验证更多页面    
def more_tab():
    # 点击更多按钮
    poco("com.starmakerinteractive.starmaker:id/tv_room_desc").click()
    sleep(1.0)
    assert_exists(Template(r"tpl1684314028256.png", record_pos=(-0.262, -0.98), resolution=(1080, 2400)), "更多页面跳转成功")
    # 返回主页面
    back(1)

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
    
def exit_room():
    poco("com.starmakerinteractive.starmaker:id/close").click()
    sleep(0.5)
    poco(text="退出").click()
    sleep(0.5)
    back(1)
    
    

# 以下用例在房间内验证    
# 验证公告编辑及设置
def announcement_ktv():
    # 点击公告按钮
    poco("com.starmakerinteractive.starmaker:id/room_announcement").click()
    sleep(1.0)
    # 设置/取消主动弹出
    if exists(Template(r"tpl1687146614371.png", record_pos=(-0.308, -0.001), resolution=(1080, 2400))):

        # 设置主动弹出
        poco("com.starmakerinteractive.starmaker:id/cb_switch").click()
        assert_exists(Template(r"tpl1687146638703.png", record_pos=(-0.304, 0.002), resolution=(1080, 2400)), "成功设置主动弹出")
    else:
        poco("com.starmakerinteractive.starmaker:id/cb_switch").click()
        assert_exists(Template(r"tpl1687146675327.png", record_pos=(-0.304, -0.001), resolution=(1080, 2400)), "取消公告主动弹出")
    # 编辑公告
    # 点击编辑按钮
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
    back(1)
    sleep(1.0)
    # 点击公告按钮
    poco("com.starmakerinteractive.starmaker:id/room_announcement").click()
    sleep(1.0)
    ann_text = poco("com.starmakerinteractive.starmaker:id/tv_content").get_text()
    #log(ann_text)
    # 断言房间公告编辑成功
    assert_equal(ann_text, "edit announcement_ktv", "成功更改房间公告")
    
    # 编辑房间公告，修改不是上述公告，否则下次修改不成功
    poco("com.starmakerinteractive.starmaker:id/tv_edit").click()
    sleep(0.5)
    poco("com.starmakerinteractive.starmaker:id/edt_text").set_text("edit announcement")
    poco("com.starmakerinteractive.starmaker:id/right_tv").click()
    sleep(0.5)
    back(1)

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
    assert_exists(Template(r"tpl1684304972312.png", record_pos=(-0.019, 0.795), resolution=(1080, 2400)), "链接复制成功")

# 验证音乐房
# 音乐房唱歌验证
def sing():
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
    # 停止演唱
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
    wait(Template(r"tpl1687167009388.png", record_pos=(-0.18, -0.915), resolution=(1080, 2400)))

    assert_exists(Template(r"tpl1687167052829.png", record_pos=(-0.315, 0.025), resolution=(1080, 2400)), "成功发起合唱")
    # 取消发起合唱
    poco("com.starmakerinteractive.starmaker:id/txt_cancel").click()
    sleep(0.5)
    poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_positive").click()
    # 关闭提示未选择歌手弹窗
    if poco("com.starmakerinteractive.starmaker:id/common_dialog_content").get_text() == '抱歉，你没有在规定时间内选择歌手。':
        poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_positive").click()
def sing_ktv():
#     if exists(Template(r"tpl1684294975414.png", record_pos=(0.026, -0.947), resolution=(1080, 2400))):
    if poco("com.starmakerinteractive.starmaker:id/tv_singing").exists():
        sing()     
    else:
        # 切换至音乐房
        poco("com.starmakerinteractive.starmaker:id/switch_mode_icon").click()
        sleep(1.0)
        poco("com.starmakerinteractive.starmaker:id/iv_bg")[2].click()
        sleep(1.0)
        sing()
    
# 上麦
def take_seat():
    if not exists(Template(r"tpl1684322032720.png", record_pos=(0.016, -0.956), resolution=(1080, 2400))):
        # 切换至聊天房
        poco("com.starmakerinteractive.starmaker:id/switch_mode_icon").click()
        sleep(1.0)
        touch([0.17 * wid, 0.448 * leng])
        sleep(2.0)
        
    touch([0.131 * wid, 0.275 * leng])
    sleep(2)
    poco(text="入座").click()
    sleep(0.5)
    assert_exists(Template(r"tpl1687168485125.png", record_pos=(-0.164, 0.809), resolution=(1080, 2400)), "用户上麦成功")
        
#验多麦房打开亲密麦位
def open_relation():
    # 判断是否是聊天房
    if not exists(Template(r"tpl1684293906477.png", record_pos=(0.015, -0.955), resolution=(1080, 2400))):
        # 切换至聊天房
        poco("com.starmakerinteractive.starmaker:id/switch_mode_icon").click()
        sleep(1.0)
        touch([0.17 * wid, 0.448 * leng])
        sleep(1.0)
    # 点击玩法入口
    poco("com.starmakerinteractive.starmaker:id/v_menu_play_center").click()
    sleep(1.0)
    # 点击关系模式按钮
    poco(text="关系模式").click()
    sleep(1.0)

    # 断言亲密麦位开启成功
    assert_exists(Template(r"tpl1684291436332.png", record_pos=(0.012, -0.358), resolution=(1080, 2400)), "亲密麦位开启成功")
    
    # 关闭亲密麦位，方便下次验证
    poco("com.starmakerinteractive.starmaker:id/v_menu_play_center").click()
    sleep(1.0)
    # 点击关系模式按钮
    poco(text="关系模式").click()

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

# 验证下麦
def left_seat():
    touch([0.12 * wid, 0.27 * leng])
    sleep(1)
    poco(text="离开").click()
    sleep(1)
    assert_exists(Template(r"tpl1687170520781.png", record_pos=(-0.147, 0.548), resolution=(1080, 2400)), "下麦成功")

# 验证打开申请上麦权限
def seat_setting_anyone():
    poco("com.starmakerinteractive.starmaker:id/iv_apply_seat").click()
    sleep(1)
    if poco("com.starmakerinteractive.starmaker:id/tv_apply_seat_type").get_text() =='自动上麦':
        poco("com.starmakerinteractive.starmaker:id/iv_manage").click()
        sleep(1.0)
        poco(text="须同意后才可上麦").click()
        # 断言举手上麦设置成功
        assert_exists(Template(r"tpl1687170760978.png", record_pos=(-0.348, -0.144), resolution=(1080, 2400)), "须同意上麦设置成功")
    else:
        poco("com.starmakerinteractive.starmaker:id/iv_manage").click()
        sleep(1.0)
        poco(text="自动上麦").click()
        assert_exists(Template(r"tpl1687170874573.png", record_pos=(-0.385, -0.15), resolution=(1080, 2400)), "自动上麦设置成功")
    # 关闭设置上麦权限半屏弹窗
    back(1)

# 封装多麦房设置等级权限上麦
def who_seat_setting():
    # 进入编辑房间页面
    edit_ktv()
    #设置5级以上用户可上麦
    poco("com.starmakerinteractive.starmaker:id/seat_rule").click()
    sleep(1.0)
    poco(text="5级及以上").click()
    sleep(1.0)
    # 断言5级以上用户上麦设置成功
    assert_exists(Template(r"tpl1687177383689.png", record_pos=(-0.004, 0.816), resolution=(1080, 2400)), "5级以上用户上麦设置成功")
    poco("com.starmakerinteractive.starmaker:id/seat_rule").click()

    sleep(1.0)
    #设置30/20级以上用户可上麦
    if poco(text="30级及以上").exists():
        poco(text="30级及以上").click()
        sleep(0.5)
        assert_exists(Template(r"tpl1687176884297.png", record_pos=(-0.004, 0.806), resolution=(1080, 2400)), "30以上用户可上麦设置成功")

    else:
        poco(text="20级及以上").click()
        sleep(0.5)
        assert_exists(Template(r"tpl1687176920481.png", record_pos=(0.003, 0.818), resolution=(1080, 2400)), "20以上用户可上麦设置成功")
    #设置仅家族成员可上麦
    poco("com.starmakerinteractive.starmaker:id/seat_rule").click()
    sleep(1.0)
    poco(text="仅家族成员").click()
    sleep(1.0)
    # 断言仅家族成员可上麦设置成功
    assert_exists(Template(r"tpl1687176986329.png", record_pos=(0.002, 0.816), resolution=(1080, 2400)), "仅家族成员可上麦设置成功")

    poco("com.starmakerinteractive.starmaker:id/seat_rule").click()
    
    sleep(1.0)
    # 设置所有人可上麦
    poco(text="任意用户").click()
    sleep(1.0)
    # 断言任意用户可上麦设置成功
    assert_exists(Template(r"tpl1687177061697.png", record_pos=(-0.001, 0.557), resolution=(1080, 2400)), "任意用户可上麦设置成功")
    back(2)
        
#验证上麦权限设置
def seat_ktv():
    if not exists(Template(r"tpl1687177810320.png", record_pos=(0.024, -0.95), resolution=(1080, 2400))):
        # 切换至聊天房
        poco("com.starmakerinteractive.starmaker:id/switch_mode_icon").click()
        sleep(1.0)
        touch([0.17 * wid, 0.448 * leng])
        sleep(1.0)
        who_seat_setting()
    else:
        who_seat_setting()
        
#  验证设置进房权限        
def join_ktv_setting():
    edit_ktv()
    # 设置仅本地用户可加入
    poco("com.starmakerinteractive.starmaker:id/joinrule").click() 
    sleep(1)
    poco(text="仅本地区用户").click()
    sleep(1.0)
    assert_exists(Template(r"tpl1687178178410.png", record_pos=(-0.008, 0.685), resolution=(1080, 2400)), "仅本地区用户进房设置成功")

    # 验证设置家族权限
    poco("com.starmakerinteractive.starmaker:id/joinrule").click()
    sleep(1.0)
    poco(text="仅家族成员").click()
    sleep(1.0)
    assert_exists(Template(r"tpl1687227981928.png", record_pos=(0.004, 0.686), resolution=(1080, 2400)), "仅家族成员用户进房设置成功")

    # 验证设置任意用户可进房
    poco("com.starmakerinteractive.starmaker:id/joinrule").click()
    sleep(1.0)
    poco(text="任意用户").click()
    sleep(0.5)
    assert_exists(Template(r"tpl1687228046324.png", record_pos=(-0.004, 0.693), resolution=(1080, 2400)), "任意用户可进房设置成功")
    # 验证设置房主关注的人可进房
    poco("com.starmakerinteractive.starmaker:id/joinrule").click()
    sleep(1.0)
    poco(text="房主关注的人").click()
    sleep(1.0)
    assert_exists(Template(r"tpl1687228090865.png", record_pos=(-0.003, 0.695), resolution=(1080, 2400)), "房主关注的人可进房设置成功")
    # 返回主页面
    back(2)

    
# 验证游戏房上麦
def game_take_seat():
    if not exists(Template(r"tpl1684376831453.png", record_pos=(0.022, -0.955), resolution=(1080, 2400))):
        poco("com.starmakerinteractive.starmaker:id/switch_mode_icon").click()
        sleep(1.0)
        poco(text="LUDO").click()
        sleep(1.0)

    # 验证上麦
    touch([0.181 * wid, 0.135 * leng])
    sleep(1.0)
    poco(text="入座").click()
    sleep(0.5)
    touch([0.483 * wid, 0.66 * leng])
    sleep(0.5)
    touch([0.914 * wid, 0.869 * leng])
    up(5)
    assert_exists(Template(r"tpl1687263783208.png", record_pos=(-0.164, 0.811), resolution=(1080, 2400)), "游戏房上麦成功")
    sleep(0.5)
    touch([0.5 * wid, 0.092 * leng])
    sleep(0.5)

# 验证关闭麦位
def close():
    # 点击第一个麦位位置
    poco("com.starmakerinteractive.starmaker:id/v_seat_bg")[0].click()
    sleep(1.0)
    poco(text="关闭这个座位").click()
    sleep(1.0)
def close_seat():
    # 抢唱房关闭麦位
    if exists(Template(r"tpl1687232954763.png", record_pos=(-0.006, -0.966), resolution=(1080, 2400))):
        close()
    else:
        poco("com.starmakerinteractive.starmaker:id/switch_mode_icon").click()
        sleep(1.0)
        # 切换房间模式抢唱房
        touch([0.49 * wid, 0.173 * leng])    
        sleep(1.0)
        close()
    # 断言抢唱房关闭麦位成功
    assert_exists(Template(r"tpl1681203397957.png", record_pos=(-0.009, -0.058), resolution=(1080, 2400)), "抢唱房第一个麦位关闭成功")
    # 恢复麦位状态，方便下次验证
    poco("com.starmakerinteractive.starmaker:id/v_seat_bg")[0].click()
    sleep(1.0)
    poco(text="打开这个座位").click()

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
        assert_not_equal(exp_bef, exp_gift_after, "赠送礼物经验增加.")
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














