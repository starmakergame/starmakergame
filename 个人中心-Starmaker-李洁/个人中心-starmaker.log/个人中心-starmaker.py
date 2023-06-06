# -*- encoding=utf8 -*-
__author__ = "24351"

from airtest.core.api import *
from airtest.core.android.adb import *
from airtest.core.android.android import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)



#参数化
PACKAGE = "com.starmakerinteractive.starmaker"
START_ACTIVITY = "org.cocos2dx.PlayGameActivity"
path = "D:\com.xiangshang.xiangshang_5.0.2_105.apk"
username="zizhao.wang@ushow.media"
password="a1111111"
Comment = "hello"



#获取屏幕大小的方法
print("获取屏幕大小：",poco.get_screen_size())

#返回我的页面check
def me():
    wait(Template(r"tpl1681291900690.png", record_pos=(-0.341, -0.02), resolution=(1080, 2460)),timeout =7,interval=0.5,intervalfunc=None)
    
#物理返回键
def back(a):
    for i in range(0, int(a)):
        keyevent("KEYCODE_BACK")


#上滑动
def up(b):
    for i in range(0,int(b)):
        xy = poco.get_screen_size()
        x = xy[0]
        y = xy[1]
        swipe([x * 0.5, y * 0.8], [x * 0.5, y * 0.2])

#下滑动
def down(c):
    for i in range(0,int(c)):
        xy = poco.get_screen_size()
        x = xy[0]
        y = xy[1]
        swipe([x * 0.5, y * 0.5], [x * 0.5, y * 0.8])

#左滑动
def left(d):
    for i in range(0,int(d)):
        xy = poco.get_screen_size()
        x = xy[0]
        y = xy[1]
        swipe([x * 0.8, y * 0.7], [x * 0.1, y * 0.7])

#右滑动
def right(e):
    for i in range(0,int(e)):
        xy = poco.get_screen_size()
        x = xy[0]
        y = xy[1]
        swipe([x * 0.1, y * 0.5], [x * 0.8, y * 0.5])
    

stop_app(PACKAGE)

start_app(PACKAGE,activity=None)



try:
    
    wait(Template(r"tpl1681271303883.png", record_pos=(0.407, 0.838), resolution=(900, 1600)),timeout =7,interval=0.5,intervalfunc=None)

    
    assert_exists(Template(r"tpl1681291830938.png", record_pos=(0.006, 0.936), resolution=(1080, 2460)), "判断是否有进入主页")
    
    
except Exception as e:
    print(e.args)
    
    
poco(text="我的").click()
    
# #----------进入个人中心页面    
wait(Template(r"tpl1681291900690.png", record_pos=(-0.341, -0.02), resolution=(1080, 2460)),timeout =7,interval=0.5,intervalfunc=None)

    
me()



# #-----【顶部信息】进入虚拟形象页

poco(name="com.starmakerinteractive.starmaker:id/btn_virtual_charaters").click()

assert_exists(Template(r"tpl1684984628233.png", record_pos=(0.413, -0.76), resolution=(1080, 2340)), "判断是否进入虚拟形象页面")


back(1)

me()

# #-----【顶部信息】进入查找好友页面

poco(name="com.starmakerinteractive.starmaker:id/imb_friends").click()


assert_exists(Template(r"tpl1681294554013.png", record_pos=(0.006, -0.034), resolution=(1080, 2460)), "判断是否进入查找好友")

poco(name="com.starmakerinteractive.starmaker:id/btw_dialog_close").click()

back(1)

me()

# #-----【顶部信息】进入绑定社交账号页面

poco(name="com.starmakerinteractive.starmaker:id/btn_link_me").click()


assert_exists(Template(r"tpl1681294863011.png", record_pos=(-0.003, -0.024), resolution=(1080, 2460)), "判断是否弹出社交账号弹框")

back(1)

me()

#-----【顶部信息】进入分享页面

poco(name="com.starmakerinteractive.starmaker:id/btn_share").click()

assert_exists(Template(r"tpl1681295531799.png", record_pos=(0.003, -1.019), resolution=(1080, 2460)), "判断是否弹出社交账号弹框")

back(1)

me()


#-----【顶部信息】进入设置页面

poco(name="com.starmakerinteractive.starmaker:id/imb_settings").click()

assert_exists(Template(r"tpl1681297096968.png", record_pos=(-0.284, -0.978), resolution=(1080, 2460)), "判断是否进入设置页面")

assert_equal(poco('com.starmakerinteractive.starmaker:id/title_tv').get_text(), "设置", "判断是否进入设置页面.")

poco(text='编辑主页').click()

assert_exists(Template(r"tpl1681367493935.png", record_pos=(-0.232, -1.007), resolution=(1080, 2460)), "判断是否进入编辑主页页面")

back(1)

poco(text='账号安全').click()

assert_exists(Template(r"tpl1681367992887.png", record_pos=(-0.246, -1.007), resolution=(1080, 2460)), "判断是否进入账号安全页面")

back(1)


poco(text='帐户隐私').click()

assert_exists(Template(r"tpl1681368054740.png", record_pos=(-0.235, -1.005), resolution=(1080, 2460)), "判断是否进入账号安全页面")

back(1)



poco(text='黑名单').click()

assert_exists(Template(r"tpl1681368201030.png", record_pos=(-0.226, -1.0), resolution=(1080, 2460)), "判断是否进入账号安全页面")

back(1)


poco(text='陌生人消息').click()

assert_exists(Template(r"tpl1681369532412.png", record_pos=(-0.193, -1.005), resolution=(1080, 2460)), "判断是否进入陌生人消息页面")

back(1)


poco(text='主播召唤消息').click()

assert_exists(Template(r"tpl1681369577495.png", record_pos=(-0.176, -1.003), resolution=(1080, 2460)), "判断是否进入主播召唤消息页面")

back(1)



poco(text='VIP').click()

assert_exists(Template(r"tpl1681369700088.png", record_pos=(-0.303, -1.006), resolution=(1080, 2460)), "判断是否进入VIP页面")

back(1)



poco(text='收入').click()

assert_exists(Template(r"tpl1681369860041.png", record_pos=(-0.178, -0.975), resolution=(1080, 2460)), "判断是否进入分成页面")

back(1)

poco(text='充值').click()

assert_exists(Template(r"tpl1681369934171.png", record_pos=(-0.326, -0.916), resolution=(1080, 2460)), "判断是否充值页面")

back(1)


poco(text='通知').click()

assert_exists(Template(r"tpl1681370171516.png", record_pos=(-0.287, -1.003), resolution=(1080, 2460)), "判断是否通知页面")

up(1)

back(2)

#-----【个人页】底部页签操作

poco(text='首页').click()

up(1)

poco(text='个人信息').click()

assert_exists(Template(r"tpl1681367493935.png", record_pos=(-0.232, -1.007), resolution=(1080, 2460)), "判断是否进入编辑主页页面")

up(1)

poco(text='添加').click()
assert_exists(Template(r"tpl1681886143451.png", record_pos=(-0.264, -0.963), resolution=(1080, 2340)), "判断是否进入编辑主页页面")

back(2)
sleep(1)
up(1)

poco(text='相册').click()

assert_exists(Template(r"tpl1681886275287.png", record_pos=(-0.314, -0.967), resolution=(1080, 2340)), "判断是否进入MV相册页面")

back(1)

poco(name='com.starmakerinteractive.starmaker:id/iv_my_party_main_photo').click()

assert_exists(Template(r"tpl1684991801626.png", record_pos=(-0.001, 0.089), resolution=(1080, 2340)), "判断是否进入KTV房间内")
#---原本检查房间底部编辑栏 assert_equal(poco('com.starmakerinteractive.starmaker:id/v_menu_msg_input').get_text(), "一起聊聊", "判断是否进入KTV房间页面.")
back(1)

poco(name='com.starmakerinteractive.starmaker:id/close').click()

touch(Template(r"tpl1681889910901.png", record_pos=(0.258, -0.821), resolution=(1080, 2340)))

poco(name='com.starmakerinteractive.starmaker:id/cl_song').click()

assert_exists(Template(r"tpl1681894749426.png", record_pos=(-0.206, 0.956), resolution=(1080, 2340)), "判断是否进入播放详情页面")

poco(name='com.starmakerinteractive.starmaker:id/imb_back').click()

assert_exists(Template(r"tpl1681892657167.png", record_pos=(-0.285, -0.008), resolution=(1080, 2340)), "判断是否显示了悬浮播放球")

up(3)
    
poco(text='动态').click()

poco(text='评论...').click()

assert_exists(Template(r"tpl1681894749426.png", record_pos=(-0.206, 0.956), resolution=(1080, 2340)), "判断是否进入播放详情页面")

poco(name='com.starmakerinteractive.starmaker:id/imb_back').click()

poco(text='歌单').click()

poco(text='我的作品').click()

poco(text='播放全部').click()

assert_exists(Template(r"tpl1681892657167.png", record_pos=(-0.285, -0.008), resolution=(1080, 2340)), "判断是否显示了悬浮播放球")

poco(name='com.starmakerinteractive.starmaker:id/iv_back_activity_sing_song_detail_new').click()

poco(text='合唱').click()

assert_equal(poco('com.starmakerinteractive.starmaker:id/btn_action').get_text(), "邀请", "判断是否进入合唱列表.")

poco(text='邀请').click()

assert_exists(Template(r"tpl1681895520209.png", record_pos=(-0.314, -0.961), resolution=(1080, 2340)), "判断是否进入分享页面")

poco(name='com.starmakerinteractive.starmaker:id/cb_choose').click()

poco(name='com.starmakerinteractive.starmaker:id/btn_share').click()

poco(text='短视频').click()

poco(name='com.starmakerinteractive.starmaker:id/img_recording_cover').click()

assert_exists(Template(r"tpl1681895876334.png", record_pos=(-0.374, 0.761), resolution=(1080, 2340)), "判断是否进入播放详情页面")

poco(name='com.starmakerinteractive.starmaker:id/imb_back').click()

assert_exists(Template(r"tpl1681896043758.png", record_pos=(0.381, 0.815), resolution=(1080, 2340)), "判断是否返回个人页面")

poco(name='com.starmakerinteractive.starmaker:id/fab_expand_menu_button').click()

poco(name='com.starmakerinteractive.starmaker:id/float_bt2').click()

assert_exists(Template(r"tpl1681896232061.png", record_pos=(-0.002, -0.767), resolution=(1080, 2340)), "判断是否进入授权页面")

poco(name='com.starmakerinteractive.starmaker:id/permissionOkTv').click()

assert_exists(Template(r"tpl1681896360334.png", record_pos=(-0.135, 0.654), resolution=(1080, 2340)), "判断是否弹出授权面板")

poco(name='com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()

poco(name='com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()

poco(name='com.android.permissioncontroller:id/permission_allow_button').click()

assert_equal(poco('com.starmakerinteractive.starmaker:id/tv_reord_tip_capturelib_fragment_capture').get_text(), "轻触拍摄，长按摄像", "判断是否进入小视频拍摄页.")

touch(Template(r"tpl1681896993382.png", record_pos=(0.005, 0.744), resolution=(1080, 2340)),duration=5,times=1)

sleep(3)

assert_equal(poco('com.starmakerinteractive.starmaker:id/ret_post_desc').get_text(), "说点什么吧...", "判断是否进入编辑发布页.")

poco(name='com.starmakerinteractive.starmaker:id/ret_post_desc').click()

text("good job")

poco(name='com.starmakerinteractive.starmaker:id/tv_done').click()

poco(name='com.starmakerinteractive.starmaker:id/tv_post').click()

sleep(5)

assert_exists(Template(r"tpl1681898270922.png", record_pos=(-0.2, 0.987), resolution=(1080, 2340)), "判断是否有进入主页")

poco(text='我的').click()

down(3)

wait(Template(r"tpl1681291900690.png", record_pos=(-0.341, -0.02), resolution=(1080, 2460)),timeout =7,interval=0.5,intervalfunc=None)

poco(text='亲密关系').click()

assert_exists(Template(r"tpl1681899388182.png", record_pos=(-0.26, -0.963), resolution=(1080, 2340)), "判断是否进入亲密关系页面")

back(1)

wait(Template(r"tpl1681291900690.png", record_pos=(-0.341, -0.02), resolution=(1080, 2460)),timeout =7,interval=0.5,intervalfunc=None)

poco(name='com.starmakerinteractive.starmaker:id/family_image').click()

assert_exists(Template(r"tpl1681899530005.png", record_pos=(-0.167, -0.519), resolution=(1080, 2340)), "判断是否进入亲密关系页面")

up(2)

poco(name='com.starmakerinteractive.starmaker:id/imb_sala').click()

up(2)

back(2)

wait(Template(r"tpl1681291900690.png", record_pos=(-0.341, -0.02), resolution=(1080, 2460)),timeout =7,interval=0.5,intervalfunc=None)

poco(text='已点').click()

up(2)

assert_exists(Template(r"tpl1681899845774.png", record_pos=(-0.261, -0.963), resolution=(1080, 2340)), "判断是否进入已点歌曲页面")

left(1)
back(1)

wait(Template(r"tpl1681291900690.png", record_pos=(-0.341, -0.02), resolution=(1080, 2460)),timeout =7,interval=0.5,intervalfunc=None)

poco(text='已关注').click()

right(1)
back(1)

wait(Template(r"tpl1681291900690.png", record_pos=(-0.341, -0.02), resolution=(1080, 2460)),timeout =7,interval=0.5,intervalfunc=None)





