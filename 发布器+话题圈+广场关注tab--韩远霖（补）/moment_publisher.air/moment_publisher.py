# -*- encoding=utf8 -*-
__author__ = "han'yuan'lin"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
#点击动态tab
poco('com.starmakerinteractive.starmaker:id/tab_name',text="动态" ).click()
sleep(1.0)
#判断是否有回礼弹窗
if exists(Template(r"tpl1684376458096.png", record_pos=(-0.003, -0.016), resolution=(1080, 2400))):
    touch([918, 565])
#点击关注tab
poco('com.starmakerinteractive.starmaker:id/tv_tab_title').click()
sleep(1.0)
#判断是否有联系人权限申请弹窗
if exists(Template(r"tpl1684295707075.png", record_pos=(0.003, -0.014), resolution=(1080, 2400))):
    touch(Template(r"tpl1684295733951.png", record_pos=(-0.188, 0.247), resolution=(1080, 2400)))
#判断是否有去发布话题tab
if exists(Template(r"tpl1684808755818.png", record_pos=(0.005, -0.83), resolution=(1080, 2400))):
    touch(Template(r"tpl1684808761541.png", record_pos=(0.33, -0.827), resolution=(1080, 2400)))
sleep(1.0)    
#判断发布器页面首次进入提示弹窗
if exists(Template(r"tpl1684206111024.png", record_pos=(0.003, -0.022), resolution=(1080, 2400))):
    touch(Template(r"tpl1684206214681.png", record_pos=(-0.004, 0.239), resolution=(1080, 2400)))
assert_exists(Template(r"tpl1684304978835.png", record_pos=(-0.108, -0.736), resolution=(1080, 2400)), "success")
#满足上方条件返回广场tab
keyevent("keycode_back")
sleep(2.0)
#点击话题标签
touch([88, 444])
sleep(3.0)
#点击话题圈页面分享按钮
poco('com.starmakerinteractive.starmaker:id/iv_share').click()
sleep(0.5)
#分享页面点击搜索
poco('com.starmakerinteractive.starmaker:id/et_search').click()
#分享搜索栏输入
text("1", search=True)
sleep(2.0)
#判断是否搜索到了用户
if exists(Template(r"tpl1684314260590.png", record_pos=(0.027, 0.149), resolution=(1080, 2400))):
    keyevent("KEYCODE_DEL"),text("a", search=True)
sleep(1.5)
#搜索到用户点击选中
if not exists(Template(r"tpl1684377739439.png", record_pos=(0.027, 0.127), resolution=(1080, 2400))):
    touch([1004, 474])
sleep(1.0)
#点击分享按钮
poco('com.starmakerinteractive.starmaker:id/btn_share').click()
assert_exists(Template(r"tpl1684377290997.png", record_pos=(-0.019, 0.783), resolution=(1080, 2400)), "success")
sleep(1.5)
#判断是否有在线成员，有的话点击用户头像进入个人页
if exists(Template(r"tpl1684382637991.png", record_pos=(0.005, -0.487), resolution=(1080, 2400))):
    touch([129, 805])
sleep(1.0)    
if exists(Template(r"tpl1684381839505.png", record_pos=(-0.094, 0.815), resolution=(1080, 2400))):
    keyevent("keycode_back")
sleep(2.0)
touch(Template(r"tpl1684382715505.png", record_pos=(-0.056, -0.594), resolution=(1080, 2400)))
sleep(1.5)
#点击圈友列表关注按钮
poco('com.starmakerinteractive.starmaker:id/btn_action')[1].click()
if exists(Template(r"tpl1684317097375.png", record_pos=(-0.013, -0.399), resolution=(1080, 2400))):
    touch(Template(r"tpl1684317107220.png", record_pos=(-0.009, -0.137), resolution=(1080, 2400)))
if not exists(Template(r"tpl1684309929820.png", record_pos=(0.018, 0.846), resolution=(1080, 2400))):
    touch(Template(r"tpl1684317076779.png", record_pos=(0.38, -0.678), resolution=(1080, 2400)))
if exists(Template(r"tpl1684317097375.png", record_pos=(-0.013, -0.399), resolution=(1080, 2400))):
    touch(Template(r"tpl1684317107220.png", record_pos=(-0.009, -0.137), resolution=(1080, 2400)))
if exists(Template(r"tpl1684376847417.png", record_pos=(0.011, 0.918), resolution=(1080, 2400))):
    keyevent("keycode_back")
sleep(1.5)
#返回话题圈一级tab
touch([71, 132])
assert_exists(Template(r"tpl1684381542210.png", record_pos=(-0.004, 0.896), resolution=(1080, 2400)), "success")
#点击参与讨论进入发布页
poco('com.starmakerinteractive.starmaker:id/fab' ).click()
sleep(1.0)
if exists(Template(r"tpl1684379961855.png", record_pos=(-0.164, 0.925), resolution=(1080, 2400))):
    keyevent("keycode_back")
assert_exists(Template(r"tpl1684380018921.png", record_pos=(-0.001, 0.901), resolution=(1080, 2400)), "success")
sleep(1.0)
keyevent("keycode_back")
#向上滑动关注tab
swipe([537, 1969],[551, 449])
#点击say hi按钮
poco('com.starmakerinteractive.starmaker:id/btn_say').click()
#判断是否有其他设备登录账号
if exists(Template(r"tpl1684380227279.png", record_pos=(0.009, 0.146), resolution=(1080, 2400))):
    touch([532, 1476])
#点击发送私信按钮    
poco('com.starmakerinteractive.starmaker:id/send_button' ).click()
sleep(1.0)
#点击消息输入框
poco('com.starmakerinteractive.starmaker:id/message_edit' ).click()
text("这是一个断言",enter = False)
poco('com.starmakerinteractive.starmaker:id/send_button' ).click()
assert_exists(Template(r"tpl1684380929990.png", record_pos=(0.238, -0.224), resolution=(1080, 2400)), "success")
sleep(1.0)
#展开私信半屏
touch(Template(r"tpl1684392098446.png", record_pos=(0.425, -0.559), resolution=(1080, 2400)))
sleep(2.0)
#返回广场推荐tab
touch([68, 148])
assert_exists(Template(r"tpl1684381129364.png", record_pos=(-0.181, -0.978), resolution=(1080, 2400)), "success")
#发布器部分
#广场推荐tab点击
poco('com.starmakerinteractive.starmaker:id/tab_name',text="动态" ).click()
sleep(1.0)
#点击广场右上角发布器icon
poco('com.starmakerinteractive.starmaker:id/publish_icon').click()
sleep(1.0)
if exists(Template(r"tpl1684206111024.png", record_pos=(0.003, -0.022), resolution=(1080, 2400))):
    touch(Template(r"tpl1684206214681.png", record_pos=(-0.004, 0.239), resolution=(1080, 2400)))
#点击录制按钮   
poco('com.starmakerinteractive.starmaker:id/tv_add' ).click()
if exists(Template(r"tpl1684206880847.png", record_pos=(-0.035, 0.621), resolution=(1080, 2400))):
    touch(Template(r"tpl1684206889636.png", record_pos=(0.006, 0.6), resolution=(1080, 2400)))
#未插入耳机弹窗按钮点击
poco('com.starmakerinteractive.starmaker:id/recording_headset_dialog_i_know_btn' ).click()
sleep(5.0)
#开始录制按钮点击
poco('com.starmakerinteractive.starmaker:id/rbtn_record_recorder_song_fragment_song_record' ).click()
sleep(2.0)
#向上滑动歌词
swipe([518, 1658],[532, 747])
sleep(10.0)
#录制完成按钮点击
poco('com.starmakerinteractive.starmaker:id/iv_done_recorder_song_fragment_song_record').click()
if exists(Template(r"tpl1684224574053.png", record_pos=(-0.001, -0.019), resolution=(1080, 2400))):
    touch(Template(r"tpl1684224590847.png", record_pos=(0.202, 0.113), resolution=(1080, 2400)))
sleep(10.0)
#点击作品tab
touch([612, 1313])
sleep(3.0)
#向上滑动作品tab
swipe([510, 1867],[543, 720])
#描述框点击
poco('com.starmakerinteractive.starmaker:id/ret_input_baserecord_fragment_editor').click()
text("love")
#点击空白处保存输入的文字
poco('com.starmakerinteractive.starmaker:id/v_place').click()
#是否允许加入合唱入口点击
poco('com.starmakerinteractive.starmaker:id/ll_duet_baserecord_fragment_edit' ).click()
sleep(0.5)
#点击不允许加入
poco('com.starmakerinteractive.starmaker:id/choice_no_allow_duet_check').click()
sleep(0.5)
poco('com.starmakerinteractive.starmaker:id/choice_ok' ).click()
sleep(0.5)
#发布作品
poco('com.starmakerinteractive.starmaker:id/tv_next_baserecord_fragment_edit_btn').click()
#点击关闭进度页，进入广场tab
poco('com.starmakerinteractive.starmaker:id/iv_close'  ).click()
assert_exists(Template(r"tpl1684227286327.png", record_pos=(-0.24, -0.373), resolution=(1080, 2400)), "success")
#广场推荐tab点击
poco('com.starmakerinteractive.starmaker:id/tab_name',text="动态" ).click()
sleep(1.0)
#点击广场右上角发布器icon
poco('com.starmakerinteractive.starmaker:id/publish_icon').click()
sleep(1.0)
if exists(Template(r"tpl1681956281440.png", record_pos=(0.003, -0.015), resolution=(720, 1600))):
    touch(Template(r"tpl1681956343304.png", record_pos=(-0.017, 0.253), resolution=(720, 1600)))
#点击伴奏搜索栏调起搜索面板
poco('com.starmakerinteractive.starmaker:id/txt_search').click()
sleep(1)
#点击半屏搜索栏，输入文字
poco('com.starmakerinteractive.starmaker:id/searchView').click()
text("love", search=True)
sleep(1)
#点击录制按钮
poco('com.starmakerinteractive.starmaker:id/lyt_sing' ).click()
if exists(Template(r"tpl1684206880847.png", record_pos=(-0.035, 0.621), resolution=(1080, 2400))):
    touch(Template(r"tpl1684206889636.png", record_pos=(0.006, 0.6), resolution=(1080, 2400)))
#未插入耳机弹窗按钮点击    
poco('com.starmakerinteractive.starmaker:id/recording_headset_dialog_i_know_btn' ).click()
sleep(5.0)
#开始录制按钮点击
poco('com.starmakerinteractive.starmaker:id/rbtn_record_recorder_song_fragment_song_record' ).click()
sleep(3.0)
#向上滑动歌词
swipe([518, 1658],[532, 747])
sleep(10.0)
#录制完成按钮点击
poco('com.starmakerinteractive.starmaker:id/iv_done_recorder_song_fragment_song_record').click()
if exists(Template(r"tpl1684224574053.png", record_pos=(-0.001, -0.019), resolution=(1080, 2400))):
    touch(Template(r"tpl1684224590847.png", record_pos=(0.202, 0.113), resolution=(1080, 2400)))
sleep(10.0)
#点击作品tab
touch([612, 1313])
sleep(3.0)
#向上滑动作品tab
swipe([510, 1867],[543, 720])
#描述框点击
poco('com.starmakerinteractive.starmaker:id/ret_input_baserecord_fragment_editor').click()
text("love")
#点击空白处保存输入的文字
poco('com.starmakerinteractive.starmaker:id/v_place' ).click()
#是否允许加入合唱入口点击
poco('com.starmakerinteractive.starmaker:id/ll_duet_baserecord_fragment_edit' ).click()
sleep(0.5)
#点击不允许加入
poco('com.starmakerinteractive.starmaker:id/choice_no_allow_duet_check').click()
sleep(0.5)
poco('com.starmakerinteractive.starmaker:id/choice_ok' ).click()
sleep(0.5)
#发布作品
poco('com.starmakerinteractive.starmaker:id/tv_next_baserecord_fragment_edit_btn').click()
#点击关闭进度页，进入广场tab
poco('com.starmakerinteractive.starmaker:id/iv_close'  ).click()
assert_exists(Template(r"tpl1684227286327.png", record_pos=(-0.24, -0.373), resolution=(1080, 2400)), "success")
#广场推荐tab点击
poco('com.starmakerinteractive.starmaker:id/tab_name',text="动态" ).click()
sleep(1.0)
#点击广场右上角发布器icon
poco('com.starmakerinteractive.starmaker:id/publish_icon').click()
sleep(1.0)
if exists(Template(r"tpl1681956281440.png", record_pos=(0.003, -0.015), resolution=(720, 1600))):
    touch(Template(r"tpl1681956343304.png", record_pos=(-0.017, 0.253), resolution=(720, 1600)))
sleep(2.0)
#点击图文发布tab
touch([217, 2204])
sleep(1.0)
if exists(Template(r"tpl1684227563818.png", record_pos=(0.003, 0.641), resolution=(1080, 2400))):
    touch(Template(r"tpl1684227573141.png", record_pos=(-0.016, 0.716), resolution=(1080, 2400)))
sleep(2.0) 
#选择两张图片
touch([300, 375]),touch([659, 377])
sleep(1.0)
#选择话题
poco('com.starmakerinteractive.starmaker:id/tv_topic' ).click()
sleep(1.0)
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
assert_exists(Template(r"tpl1684227286327.png", record_pos=(-0.24, -0.373), resolution=(1080, 2400)), "success")
#广场推荐tab点击
poco('com.starmakerinteractive.starmaker:id/tab_name',text="动态" ).click()
sleep(1.0)
#点击广场右上角发布器icon
poco('com.starmakerinteractive.starmaker:id/publish_icon').click()
if exists(Template(r"tpl1681956281440.png", record_pos=(0.003, -0.015), resolution=(720, 1600))):
    touch(Template(r"tpl1681956343304.png", record_pos=(-0.017, 0.253), resolution=(720, 1600)))
sleep(1.0)
#点击故事tab
touch([251, 1476])
if exists(Template(r"tpl1684231637398.png", record_pos=(-0.001, -0.244), resolution=(1080, 2400))):
    touch(Template(r"tpl1684231651478.png", record_pos=(0.001, 0.232), resolution=(1080, 2400)))
#录制10秒
touch([551, 1939],duration=10)
sleep(3.0)
#输入描述
poco('com.starmakerinteractive.starmaker:id/ret_post_desc' ).click()
text("love")
#完成输入描述
poco('com.starmakerinteractive.starmaker:id/tv_done').click()
sleep(2.0)
#
touch([560, 2179])
assert_exists(Template(r"tpl1684227286327.png", record_pos=(-0.24, -0.373), resolution=(1080, 2400)), "success")