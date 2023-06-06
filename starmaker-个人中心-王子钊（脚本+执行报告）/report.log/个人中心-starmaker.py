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
def back():
    keyevent("KEYCODE_BACK")

#上滑动
def up():
    xy = poco.get_screen_size()
    x = xy[0]
    y = xy[1]
    swipe([x * 0.5, y * 0.8], [x * 0.5, y * 0.2])

#下滑动
def down():
    xy = poco.get_screen_size()
    x = xy[0]
    y = xy[1]
    swipe([x * 0.5, y * 0.5], [x * 0.5, y * 0.8])

#左滑动
def left():
    xy = poco.get_screen_size()
    x = xy[0]
    y = xy[1]
    swipe([x * 0.8, y * 0.7], [x * 0.1, y * 0.7])

#右滑动
def right():
    xy = poco.get_screen_size()
    x = xy[0]
    y = xy[1]
    swipe([x * 0.2, y * 0.5], [x * 0.8, y * 0.5])



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

assert_exists(Template(r"tpl1681293266162.png", record_pos=(0.384, -0.558), resolution=(1080, 2460)), "判断是否进入虚拟形象页面")


keyevent("KEYCODE_BACK")

me()

# #-----【顶部信息】进入查找好友页面

poco(name="com.starmakerinteractive.starmaker:id/imb_friends").click()


assert_exists(Template(r"tpl1681294554013.png", record_pos=(0.006, -0.034), resolution=(1080, 2460)), "判断是否进入查找好友")

poco(name="com.starmakerinteractive.starmaker:id/btw_dialog_close").click()

back()

me()

# #-----【顶部信息】进入绑定社交账号页面

poco(name="com.starmakerinteractive.starmaker:id/btn_link_me").click()


assert_exists(Template(r"tpl1681294863011.png", record_pos=(-0.003, -0.024), resolution=(1080, 2460)), "判断是否弹出社交账号弹框")

back()

me()

#-----【顶部信息】进入分享页面

poco(name="com.starmakerinteractive.starmaker:id/btn_share").click()

assert_exists(Template(r"tpl1681295531799.png", record_pos=(0.003, -1.019), resolution=(1080, 2460)), "判断是否弹出社交账号弹框")

back()

me()


#-----【顶部信息】进入设置页面

poco(name="com.starmakerinteractive.starmaker:id/imb_settings").click()

assert_exists(Template(r"tpl1681297096968.png", record_pos=(-0.284, -0.978), resolution=(1080, 2460)), "判断是否进入设置页面")

assert_equal(poco('com.starmakerinteractive.starmaker:id/title_tv').get_text(), "设置", "判断是否进入设置页面.")

poco(text='编辑主页').click()

assert_exists(Template(r"tpl1681367493935.png", record_pos=(-0.232, -1.007), resolution=(1080, 2460)), "判断是否进入编辑主页页面")

back()

poco(text='账号安全').click()

assert_exists(Template(r"tpl1681367992887.png", record_pos=(-0.246, -1.007), resolution=(1080, 2460)), "判断是否进入账号安全页面")

back()


poco(text='帐户隐私').click()

assert_exists(Template(r"tpl1681368054740.png", record_pos=(-0.235, -1.005), resolution=(1080, 2460)), "判断是否进入账号安全页面")

back()



poco(text='黑名单').click()

assert_exists(Template(r"tpl1681368201030.png", record_pos=(-0.226, -1.0), resolution=(1080, 2460)), "判断是否进入账号安全页面")

back()


poco(text='陌生人消息').click()

assert_exists(Template(r"tpl1681369532412.png", record_pos=(-0.193, -1.005), resolution=(1080, 2460)), "判断是否进入陌生人消息页面")

back()


poco(text='主播召唤消息').click()

assert_exists(Template(r"tpl1681369577495.png", record_pos=(-0.176, -1.003), resolution=(1080, 2460)), "判断是否进入主播召唤消息页面")

back()



poco(text='VIP').click()

assert_exists(Template(r"tpl1681369700088.png", record_pos=(-0.303, -1.006), resolution=(1080, 2460)), "判断是否进入VIP页面")

back()



poco(text='收入').click()

assert_exists(Template(r"tpl1684144596025.png", record_pos=(-0.186, -0.986), resolution=(1080, 2460)), "判断是否进入分成页面")

back()

poco(text='充值').click()

assert_exists(Template(r"tpl1681369934171.png", record_pos=(-0.326, -0.916), resolution=(1080, 2460)), "判断是否充值页面")

back()


poco(text='通知').click()

assert_exists(Template(r"tpl1681370171516.png", record_pos=(-0.287, -1.003), resolution=(1080, 2460)), "判断是否通知页面")


back()

up()


poco(text='通用设置').click()
assert_exists(Template(r"tpl1684144803839.png", record_pos=(-0.237, -1.007), resolution=(1080, 2460)), "判断是否通用设置页面")

back()

up()

poco(text='自动播放设置').click()
assert_exists(Template(r"tpl1684144860922.png", record_pos=(-0.165, -1.007), resolution=(1080, 2460)), "判断是否自动播放设置页面")


back()



poco(text='清空缓存').click()
assert_exists(Template(r"tpl1684144887777.png", record_pos=(-0.231, -1.008), resolution=(1080, 2460)), "判断是否进入清空缓存页面")


back()

poco(text='网络诊断').click()
assert_exists(Template(r"tpl1684145558611.png", record_pos=(-0.232, -1.01), resolution=(1080, 2460)), "判断是否进入清空缓存页面")


back()


poco(text='客户服务中心').click()
assert_exists(Template(r"tpl1684145594073.png", record_pos=(-0.178, -1.005), resolution=(1080, 2460)), "判断是否进入清空缓存页面")


back()


poco(text='关于 StarMaker').click()
assert_exists(Template(r"tpl1684145658030.png", record_pos=(-0.295, -1.007), resolution=(1080, 2460)), "判断是否进入清空缓存页面")


back()
back()

me()

# 头像部分

poco(name='com.starmakerinteractive.starmaker:id/civ_head_view').click()



assert_exists(Template(r"tpl1684145953081.png", record_pos=(-0.115, 0.77), resolution=(1080, 2460)), "判断点击头像页面")


poco(text='拍摄一张图片').click()

assert_exists(Template(r"tpl1684146246196.png", record_pos=(-0.001, 0.826), resolution=(1080, 2460)), "判断进入相机页面")

poco(name='com.transsion.camera:id/shutter_button').click()


assert_exists(Template(r"tpl1684146319652.png", record_pos=(0.206, 0.816), resolution=(1080, 2460)), "判断进入相机页面")


poco(name='com.transsion.camera:id/done_button').click()


assert_exists(Template(r"tpl1684146372074.png", record_pos=(0.42, -0.964), resolution=(1080, 2460)), "判断选择图片")


poco(text='完成').click()

me()



# 编辑昵称

nick_name = "testwzz12366666666"

poco(name='com.starmakerinteractive.starmaker:id/tv_edit').click()


assert_exists(Template(r"tpl1684146730284.png", record_pos=(-0.229, -1.008), resolution=(1080, 2460)), "判断选择图片")


poco("com.starmakerinteractive.starmaker:id/et_username").set_text(nick_name)



poco(text='保存').click()




# assert_equal(poco('com.starmakerinteractive.starmaker:id/user_name_view_tv_name').get_text(), "nick_name", "判断是否修改成.")


# 添加标签

poco(name='com.starmakerinteractive.starmaker:id/iv_add_query_tags').click()

assert_exists(Template(r"tpl1684202245141.png", record_pos=(-0.266, -0.96), resolution=(1080, 2460)), "判断进入添加标签")

poco(text="80's").click()
     
poco(text='完成').click()


# 亲密关系
poco(text='亲密关系').click()

assert_exists(Template(r"tpl1684202755341.png", record_pos=(0.002, -0.989), resolution=(1080, 2460)), "判断进入亲密关系页面")

back()


# 中部4tab（粉丝，已关注，段位，礼物）

poco(text='粉丝').click()

assert_exists(Template(r"tpl1684202863490.png", record_pos=(-0.127, -0.983), resolution=(1080, 2460)), "判断进入粉丝页面")



left()
left()
right()
right()

back()


poco(text='已关注').click()

assert_exists(Template(r"tpl1684203659208.png", record_pos=(-0.103, -0.988), resolution=(1080, 2460)), "判断进入已关注页面")

back()


poco(text='段位').click()


assert_exists(Template(r"tpl1684203712213.png", record_pos=(-0.239, -1.009), resolution=(1080, 2460)), "判断进入排行纪录页面")


back()


poco(text='礼物').click()

assert_exists(Template(r"tpl1684203768281.png", record_pos=(-0.164, -0.978), resolution=(1080, 2460)), "判断进入礼物页面")


back()


# 家族页面

poco(name='com.starmakerinteractive.starmaker:id/family_image').click()


assert_exists(Template(r"tpl1684203891442.png", record_pos=(-0.171, -0.506), resolution=(1080, 2460)), "判断进入家族页面")

back()



# 中部子tab页签Template(r"tpl1684204019911.png", record_pos=(-0.008, 0.468), resolution=(1080, 2460))


poco(text='本地录音').click()


assert_exists(Template(r"tpl1684204108587.png", record_pos=(-0.258, -1.01), resolution=(1080, 2460)), "判断进入本地录音页面")

back()


poco(text='已点').click()


assert_exists(Template(r"tpl1684204491131.png", record_pos=(-0.142, -0.854), resolution=(1080, 2460)), "判断进入已点页面")

back()


poco(text='手机铃声').click()


assert_exists(Template(r"tpl1684204544435.png", record_pos=(-0.02, -0.861), resolution=(1080, 2460)), "判断进入已点页面")

back()


poco(text="我的").click()



poco(text='VIP').click()


assert_exists(Template(r"tpl1684204636319.png", record_pos=(-0.296, -1.0), resolution=(1080, 2460)), "判断进入vip页面")

back()


poco(text='每日任务').click()


assert_exists(Template(r"tpl1684204699947.png", record_pos=(-0.232, -1.014), resolution=(1080, 2460)), "判断进入每日福利页面")

back()

poco(text='游戏').click()


assert_exists(Template(r"tpl1684204742461.png", record_pos=(-0.122, -0.981), resolution=(1080, 2460)), "判断进入游戏页面")

back()



poco(text='勋章').click()

assert_exists(Template(r"tpl1684204773402.png", record_pos=(-0.295, -1.01), resolution=(1080, 2460)), "判断进入勋章页面")

back()


poco(text='充值').click()

assert_exists(Template(r"tpl1681369934171.png", record_pos=(-0.326, -0.916), resolution=(1080, 2460)), "判断是否充值页面")

back()

sleep(2)

left()

poco(text='亲密关系').click()

assert_exists(Template(r"tpl1684206540926.png", record_pos=(-0.012, -0.988), resolution=(1080, 2460)), "判断进入亲密关系页面")

back()

poco(text='认证').click()

assert_exists(Template(r"tpl1684206604933.png", record_pos=(0.006, -0.363), resolution=(1080, 2460)), "判断进入认证页面")

back()

poco(text='贵族').click()

assert_exists(Template(r"tpl1684206654430.png", record_pos=(-0.172, -0.977), resolution=(1080, 2460)), "判断进入贵族页面")

back()


poco(text='商店').click()

assert_exists(Template(r"tpl1684207697510.png", record_pos=(-0.181, -0.982), resolution=(1080, 2460)), "判断进入商店页面")

back()

poco(text='道具').click()

assert_exists(Template(r"tpl1684207135838.png", record_pos=(-0.377, -0.862), resolution=(1080, 2460)), "判断进入道具页面")

back()

poco(text='反馈').click()

assert_exists(Template(r"tpl1684207169563.png", record_pos=(-0.181, -0.978), resolution=(1080, 2460)), "判断进入反馈页面")

back()


poco(text='收入').click()

assert_exists(Template(r"tpl1684207191641.png", record_pos=(-0.181, -0.981), resolution=(1080, 2460)), "判断进入反馈页面")

back()

poco(text='魅力等级').click()

assert_exists(Template(r"tpl1684207231722.png", record_pos=(-0.066, -0.98), resolution=(1080, 2460)), "判断进入魅力等级页面")

back()

sleep(1)

left()

poco(text='名人').click()

assert_exists(Template(r"tpl1684207288355.png", record_pos=(-0.16, -0.98), resolution=(1080, 2460)), "判断进入魅力等级页面")

back()

poco(text='我的直播').click()

assert_exists(Template(r"tpl1684207315917.png", record_pos=(-0.127, -0.978), resolution=(1080, 2460)), "判断进入我的直播页面")

back()


poco(text='教程').click()

assert_exists(Template(r"tpl1684207356396.png", record_pos=(0.253, -0.651), resolution=(1080, 2460)), "判断进入教程页面")

back()




























