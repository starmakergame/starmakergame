# -*- encoding=utf8 -*-
__author__ = "李洁"

from airtest.core.api import *

auto_setup(__file__)
#poco实例化
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
#获取屏幕大小的方法
print("获取屏幕大小：",poco.get_screen_size())

#判断是否在个人页
#def profile_mine():
    #判断如果没有个人页粉丝入口，就点击底部【我的】进入到个人页，但可能有个人页特效动画，所以等待5s
    #while not poco('com.starmakerinteractive.starmaker:id/item_title',text='粉丝').exists():
        #poco(text="我的").click()
        #sleep(5)

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
        
#定义登录账号参数
emailaddr='lijie5@163.com'
pwd='lijie123'
#定义登录函数
def loginapp():
    #判断是否有【登录/注册】按钮
    if exists(Template(r"tpl1686191845481.png", record_pos=(-0.018, 0.847), resolution=(1080, 2340))):
        #点击【登录/注册】按钮，唤起半屏登录弹窗
        poco("com.starmakerinteractive.starmaker:id/tv_login_guide",text = "登录/注册").click()

    #判断是否有登录半屏弹窗，如有有，则点击更多方式按钮
    if poco(name= "com.starmakerinteractive.starmaker:id/btn_more_ways",text = "更多方式").exists():
        poco("com.starmakerinteractive.starmaker:id/btn_more_ways",text = "更多方式").click()

    touch(Template(r"tpl1686191888954.png", record_pos=(-0.001, 0.853), resolution=(1080, 2340)))
    sleep(1)
    #判断是否有登录记录
    if poco("android.widget.TextView",text = "您要使用这些帐户登录吗？").exists():
        poco("com.starmakerinteractive.starmaker:id/btn_login_with_other",text = "使用另一个帐户登录").click()
        sleep(2)
        #输入邮箱地址
        poco(name='com.starmakerinteractive.starmaker:id/et_input')[0].set_text(emailaddr)
        sleep(0.5)
        poco(name='com.starmakerinteractive.starmaker:id/et_input')[1].set_text(pwd)
    elif poco(name="android.widget.TextView",text = "输入你的邮箱地址").exists():
        #输入邮箱地址
        poco(name='com.starmakerinteractive.starmaker:id/et_email').set_text(emailaddr)
        #text(name)
        sleep(0.5)
        print('输入邮箱地址')
        #点击【下一步】
        poco("com.starmakerinteractive.starmaker:id/btn_next",text = "下一步").click()
        wait(Template(r"tpl1686191921360.png", record_pos=(0.361, -0.277), resolution=(1080, 2340)),timeout =7,interval=0.5,intervalfunc=None)
        print('进入密码输入页面')
        #输入账号密码
        poco("com.starmakerinteractive.starmaker:id/et_input",text = "输入您的密码").set_text(pwd)
        sleep(0.5)
        print('输入账号密码')
        #点击【登录】按钮
    poco("com.starmakerinteractive.starmaker:id/btw_email_confirm",text = "登录").click()
    print('点击登录')
    #登录成功进入主页
    wait(Template(r"tpl1686192079896.png", record_pos=(-0.002, 0.844), resolution=(1080, 2340)),timeout =7,interval=0.5,intervalfunc=None)
    print('有弹出登录成功的toast提示')
    
#定义内容该语言选择页
def language_choose():
    #判断是否有语言选择页，如果有，则点击English选项
    if poco("com.starmakerinteractive.starmaker:id/title").exists():
        print('内容语言选择页存在')
        poco("com.starmakerinteractive.starmaker:id/txt_language",text = "English").click()
        #打印日志，语言选择完成
        print('内容语言选择完成')
    else:
        print ('内容语言选择页不存在，有问题')

#定义家族卡位
def profile_family():
    #判断是否在一级主页，否则就点返回，直到一级主页
    while not exists(Template(r"tpl1686887384597.png", record_pos=(-0.4, 0.968), resolution=(1080, 2340))):
        back(1)
        sleep(1)
    #判断是否在个人页，如果不在就点【我的】进入个人页
    if poco('com.starmakerinteractive.starmaker:id/item_title',text='粉丝').exists():
        sleep(0.5)
    else:
        poco(text="我的").click()
        sleep(5)
    if poco('com.starmakerinteractive.starmaker:id/family_image').exists():
        #点击进入家族主页，等待2s数据加载
        poco('com.starmakerinteractive.starmaker:id/family_image').click()
        sleep(1)
        #如果在家族主页顶部，就往下划两下查看
        if poco('com.starmakerinteractive.starmaker:id/family_img_ghost').exists():
            print('当前在家族主页顶部')
            assert_exists(Template(r"tpl1686898388186.png", record_pos=(0.392, -0.968), resolution=(1080, 2340)), "进入家族主页")
            up(2)
        else:
            if poco('com.starmakerinteractive.starmaker:id/tv_tab_title',text='动态').exists():
                print('进入家族主页定位在了底部动态列表')
                #下划页面知道家族主页顶部
                while not poco('com.starmakerinteractive.starmaker:id/family_img_ghost').exists():
                    down(1)
                assert_exists(Template(r"tpl1686898134993.png", record_pos=(-0.391, -0.55), resolution=(1080, 2340)), "滑动家族主页页面到顶部")
                back(2)
    else:
        print('当前用户尚未加入家族')
        #点击家族卡片进入家族广场页，等待2s数据加载
        poco('com.starmakerinteractive.starmaker:id/tv_join',text='加入').click()
        sleep(2)
        #判断一下是否有家族封面图元素，如果有说明有其他家族数据
        if poco('com.starmakerinteractive.starmaker:id/img_cover').exists():
            print('家族广场有其他家族数据')
            up(1)
            #点击一个家族item后面的【加入】按钮，发出加入家族申请，发送完之后点击返回，返回个人页
            poco('com.starmakerinteractive.starmaker:id/btn_join',text='加入').click()
            assert_exists(Template(r"tpl1686897440253.png", record_pos=(-0.001, 0.844), resolution=(1080, 2340)), "发送加入家族申请")
            #避免这里在家族广场页有其他烂七八糟的弹窗什么的，所以点击两次back
            back(2)
            #下拉刷新2次个人页，看看是否有立即通过申请的？
            down(2)
            sleep(2)
            if poco('com.starmakerinteractive.starmaker:id/family_image').exists():
                print('加入家族的申请立即被通过了，现在该用户有家族了')
            else:
                print('加入家族的申请，还没有得到批准')

#个人页homepage页签
def profile_homepage_info():
    #判断是否在一级主页，否则就点返回，直到一级主页
    while not exists(Template(r"tpl1686887384597.png", record_pos=(-0.4, 0.968), resolution=(1080, 2340))):
        back(1)
        sleep(1)
    #判断是否在个人页，如果不在就点【我的】进入个人页
    if poco('com.starmakerinteractive.starmaker:id/item_title',text='粉丝').exists():
        sleep(0.5)
    else:
        poco(text="我的").click()
        sleep(5)
    #判断首页tab，然后上划一下页面把个人信息展示区域露出来
    if poco("com.starmakerinteractive.starmaker:id/tv_tab_title",text = '首页').exists():
        poco(text='首页').click()
        up(1)
    #如果不在个人页顶部，就下拉5次，保证能在个人页头部区域，因为有可能触发下拉刷新页面，所以这里等待1s
    else:
        up(1)
        if poco("com.starmakerinteractive.starmaker:id/tv_tab_title",text = '首页').exists():
            poco(text='首页').click()
    #点击进入个人信息编辑页
    poco(text='个人信息').click()
    assert_exists(Template(r"tpl1681367493935.png", record_pos=(-0.232, -1.007), resolution=(1080, 2460)), "判断是否进入编辑主页页面")
    up(1)
    #点击教育经历选项，进入到二级编辑页
    poco(text='教育经历').click()
    assert_exists(Template(r"tpl1681886143451.png", record_pos=(-0.264, -0.963), resolution=(1080, 2340)), "判断是否进入教育经历编辑页面")
    #返回个人主页
    back(2)
    sleep(1)
    #上划一下页面，为后续操作做准备
    up(1)

#MV相册
def profile_homepage_album():
    if poco('com.starmakerinteractive.starmaker:id/tv_album_title',text='相册').exists():
        poco(text='相册').click()
        assert_exists(Template(r"tpl1686221617238.png", record_pos=(-0.314, -0.965), resolution=(1080, 2340)), "判断是否进入MV相册页面")
        print('用户有MV相册')
        back(1)
    else:
        #上划页面2次，找一下是否在下面，如果找到了，就直接点击进入mv相册页
        up(2)
        if poco('com.starmakerinteractive.starmaker:id/tv_album_title',text='相册').exists():
            poco(text='相册').click()
            assert_exists(Template(r"tpl1686221617238.png", record_pos=(-0.314, -0.965), resolution=(1080, 2340)), "判断是否进入MV相册页面")
            print('用户有MV相册')
            back(1)
        else:
            #如果上划没找到，则下划一下页面看是否在上面，如果找到了，就点击进入mv相册页
            down(1)
            if poco('com.starmakerinteractive.starmaker:id/tv_album_title',text='相册').exists():
                poco(text='相册').click()
                assert_exists(Template(r"tpl1686221617238.png", record_pos=(-0.314, -0.965), resolution=(1080, 2340)), "判断是否进入MV相册页面")
                print('用户有MV相册')
                back(1)
            else:
                #如果上下都没找到，说明用户没有mv相册
                print('用户没有mv相册')

#歌房
def profile_homepage_ktv():
    #判断是否有歌房，如果有则点击ktv房间卡片进房
    if poco('com.starmakerinteractive.starmaker:id/tv_my_party_title',text='歌房').exists():
        poco('com.starmakerinteractive.starmaker:id/iv_my_party_main_photo').click()
        wait(Template(r"tpl1686277408262.png", record_pos=(0.293, -0.962), resolution=(1080, 2340)),timeout =7,interval=0.5,intervalfunc=None)
        assert_exists(Template(r"tpl1686277408262.png", record_pos=(0.293, -0.962), resolution=(1080, 2340)), "判断是否进入KTV房间内")
        print('用户有KTV房间且已正常进房')
        #进房之后在房间内待5s，然后判断是否有弹窗，如果有邀请加入家族的弹窗，则点击一下返回键，关闭弹窗
        sleep(5)
        if poco('com.starmakerinteractive.starmaker:id/tv_title',text='邀请别人进入你的家族吧！').exists():
            back(1)
            sleep(1)
        poco(name='com.starmakerinteractive.starmaker:id/close').click()
        touch(Template(r"tpl1681889910901.png", record_pos=(0.258, -0.821), resolution=(1080, 2340)))
        print('退房返回个人页')
    else:
        #上划页面查找ktv房间卡片
        up(2)
        if poco('com.starmakerinteractive.starmaker:id/tv_my_party_title',text='歌房').exists():
            poco('com.starmakerinteractive.starmaker:id/iv_my_party_main_photo').click()
            wait(Template(r"tpl1686277408262.png", record_pos=(0.293, -0.962), resolution=(1080, 2340)),timeout =7,interval=0.5,intervalfunc=None)
            assert_exists(Template(r"tpl1686277408262.png", record_pos=(0.293, -0.962), resolution=(1080, 2340)), "判断是否进入KTV房间内")
            print('用户有KTV房间且已正常进房')
            #进房之后在房间内待5s，然后判断是否有弹窗，如果有邀请加入家族的弹窗，则点击一下返回键，关闭弹窗
            sleep(5)
            if poco('com.starmakerinteractive.starmaker:id/tv_title',text='邀请别人进入你的家族吧！').exists():
                back(1)
                sleep(1)
            poco(name='com.starmakerinteractive.starmaker:id/close').click()
            touch(Template(r"tpl1681889910901.png", record_pos=(0.258, -0.821), resolution=(1080, 2340)))
            print('退房返回个人页')
        else:
            #下划页面查找
            down(1)
            if poco('com.starmakerinteractive.starmaker:id/tv_my_party_title',text='歌房').exists():
                poco('com.starmakerinteractive.starmaker:id/iv_my_party_main_photo').click()
                wait(Template(r"tpl1686277408262.png", record_pos=(0.293, -0.962), resolution=(1080, 2340)),timeout =7,interval=0.5,intervalfunc=None)
                assert_exists(Template(r"tpl1686277408262.png", record_pos=(0.293, -0.962), resolution=(1080, 2340)), "判断是否进入KTV房间内")
                print('用户有KTV房间且已正常进房')
                #进房之后在房间内待5s，然后判断是否有弹窗，如果有邀请加入家族的弹窗，则点击一下返回键，关闭弹窗
                sleep(5)
                if poco('com.starmakerinteractive.starmaker:id/tv_title',text='邀请别人进入你的家族吧！').exists():
                    back(1)
                    sleep(1)
                poco(name='com.starmakerinteractive.starmaker:id/close').click()
                touch(Template(r"tpl1681889910901.png", record_pos=(0.258, -0.821), resolution=(1080, 2340)))
                print('退房返回个人页')
            else:
                #上下都没找到，就是没有ktv房间
                print('用户没有KTV房间')
    
#作品
def profile_homepage_cover():
    if poco('com.starmakerinteractive.starmaker:id/tv_title_name',text='作品').exists():
        poco(name='com.starmakerinteractive.starmaker:id/cl_song').click()
        assert_exists(Template(r"tpl1686298547177.png", record_pos=(-0.255, 0.047), resolution=(1080, 2340)), "判断是否进入播放详情页面")
        sleep(1)
        print('用户有作品')
        back(1)
        assert_exists(Template(r"tpl1686297040915.png", record_pos=(-0.335, 0.284), resolution=(1080, 2340)), "判断是否显示了悬浮播放球")
        print('悬浮球正在播放作品')
        #关闭播放球,有点儿问题，先屏蔽掉不关了
        #poco(name='com.starmakerinteractive.starmaker:id/img_head').click()
        #poco('com.starmakerinteractive.starmaker:id/play_close').click()
    else:
        #上划页面查找
        up(2)
        if poco('com.starmakerinteractive.starmaker:id/tv_title_name',text='作品').exists():
            poco(name='com.starmakerinteractive.starmaker:id/cl_song').click()
            assert_exists(Template(r"tpl1686298547177.png", record_pos=(-0.255, 0.047), resolution=(1080, 2340)), "判断是否进入播放详情页面")
            sleep(1)
            print('用户有作品')
            back(1)
            assert_exists(Template(r"tpl1686297040915.png", record_pos=(-0.335, 0.284), resolution=(1080, 2340)), "判断是否显示了悬浮播放球")
            print('悬浮球正在播放作品')
        else:
            #下划页面查找
            down(1)
            if poco('com.starmakerinteractive.starmaker:id/tv_title_name',text='作品').exists():
                poco(name='com.starmakerinteractive.starmaker:id/cl_song').click()
                assert_exists(Template(r"tpl1686298547177.png", record_pos=(-0.255, 0.047), resolution=(1080, 2340)), "判断是否进入播放详情页面")
                sleep(1)
                print('用户有作品')
                back(1)
                assert_exists(Template(r"tpl1686297040915.png", record_pos=(-0.335, 0.284), resolution=(1080, 2340)), "判断是否显示了悬浮播放球")
                print('悬浮球正在播放作品')
            else:
                #如果上下都没找到，说明用户没有作品
                print('用户没有作品')
    
#歌单
def profile_homepage_playlist():
    if poco('com.starmakerinteractive.starmaker:id/tv_title_name',text='歌单').exists():
        poco(name='com.starmakerinteractive.starmaker:id/iv_profile_tab_playlist').click()
        assert_exists(Template(r"tpl1686291143683.png", record_pos=(-0.36, -0.421), resolution=(1080, 2340)), "判断是否进入歌单详情页面")
        sleep(1)
        print('用户有创建的歌单，且已进入歌单详情页')
        back(1)
    else:
        #上划页面查找
        up(3)
        if poco('com.starmakerinteractive.starmaker:id/tv_title_name',text='歌单').exists():
            poco(name='com.starmakerinteractive.starmaker:id/iv_profile_tab_playlist').click()
            assert_exists(Template(r"tpl1686291143683.png", record_pos=(-0.36, -0.421), resolution=(1080, 2340)), "判断是否进入歌单详情页面")
            sleep(1)
            print('用户有创建的歌单，且已进入歌单详情页')
            back(1)
        else:
            #下划页面查找
            down(1)
            if poco('com.starmakerinteractive.starmaker:id/tv_title_name',text='歌单').exists():
                poco(name='com.starmakerinteractive.starmaker:id/iv_profile_tab_playlist').click()
                assert_exists(Template(r"tpl1686291143683.png", record_pos=(-0.36, -0.421), resolution=(1080, 2340)), "判断是否进入歌单详情页面")
                sleep(1)
                print('用户有创建的歌单，且已进入歌单详情页')
                back(1)
            else:
                #如果上下都没找到，说明用户没有歌单
                print('用户没有创建的歌单')    
    down(7)
    sleep(2)
    
#个人页moment页签
def profile_moment():
    #如果当前屏幕没有显示出来【动态】就上划一下页面，直到露出来
    while not poco(text = '动态').exists():
        up(1)
    #点击切换到【动态】页签，并上划一下页面，将下方tab页面露出来
    poco(text='动态').click()
    sleep(1)
    up(1)
    #如果露出来的tab页面上有内容搜索按钮，则寻找评论框点击进入作品播放详情页，否则输出“用户没有作品”的结论
    if poco('com.starmakerinteractive.starmaker:id/bt_search').exists():
        while not poco('com.starmakerinteractive.starmaker:id/tv_comment_hint',text='评论...').exists():
            up(1)
        poco(text='评论...').click()
        assert_exists(Template(r"tpl1686894828421.png", record_pos=(-0.428, -0.852), resolution=(1080, 2340)), "判断是否进入播放详情页")
        back(2)
    else:
        print('该用户无任何作品')
    down(3)
    sleep(2)

#个人页歌单页签
def profile_playlist():
    #如果当前屏幕没有显示出来【歌单】就上划一下页面，直到露出来
    while not poco(text = '歌单').exists():
        up(1)
    #点击切换到【动态】页签，并上划一下页面，将下方tab页面露出来
    poco(text='歌单').click()
    sleep(1)
    up(1)
    #新建一个歌单
    while not poco('com.starmakerinteractive.starmaker:id/tv_title',text = '新建').exists():
        up(1)
    poco(text='新建').click()
    sleep(1)
    text('My playlist')
    sleep(0.5)
    poco('com.starmakerinteractive.starmaker:id/common_dialog_btn_positive',text='完成').click()
    assert_exists(Template(r"tpl1686296643646.png", record_pos=(-0.006, 0.157), resolution=(1080, 2340)), "判断新建歌单成功")
    #给歌单添加歌曲并播放，返回个人页
    poco('com.starmakerinteractive.starmaker:id/tv_feedback_click',text='添加歌曲').click()
    assert_exists(Template(r"tpl1686296739874.png", record_pos=(-0.263, -0.965), resolution=(1080, 2340)), "判断进入歌曲添加页面")
    if poco('com.starmakerinteractive.starmaker:id/iv_play_list_cover').exists():
        poco('com.starmakerinteractive.starmaker:id/btn_add',text='添加').click()
        assert_exists(Template(r"tpl1686296940100.png", record_pos=(-0.002, 0.844), resolution=(1080, 2340)), "判断进入歌曲添加成功")
        back(1)
        poco('com.starmakerinteractive.starmaker:id/tv_play_btn_desc',text='播放全部').click()
        assert_exists(Template(r"tpl1686297040915.png", record_pos=(-0.335, 0.284), resolution=(1080, 2340)), "判断开始播放歌单歌曲")
        back(1)
    #否则说明无可添加歌曲，直接返回，返回到个人页
    else:
        print('暂无可添加歌曲')
        back(2)
    down(3)
    sleep(2)
    
#个人页作品页签    
def profile_cover():
    #如果当前屏幕没有显示出来【作品】就上划一下页面，直到露出来
    while not poco(text = '作品').exists():
        up(1)
    #点击切换到【作品】页签，并上划一下页面，将下方tab页面露出来
    poco(text='作品').click()
    sleep(1)
    up(1)
    #如果露出来的tab页面上有作品统计，则说明用户有作品数据；否则，输入用户没有作品的提示
    if exists(Template(r"tpl1686298129291.png", record_pos=(-0.349, -0.698), resolution=(1080, 2340))):
        poco('com.starmakerinteractive.starmaker:id/img_cover')[0].click()
        assert_exists(Template(r"tpl1686298547177.png", record_pos=(-0.255, 0.047), resolution=(1080, 2340)), "判断是否进入播放详情页")
        back(1)
    else:
        print('该用户无任何作品')
    down(3)
    sleep(2)

#定义合唱页签
def profile_duet():
    #如果当前屏幕没有显示出来【合唱】就上划一下页面，直到露出来
    while not poco(text = '合唱').exists():
        up(1)
    #点击切换到【合唱】页签，并上划一下页面，将下方tab页面露出来
    poco(text='合唱').click()
    sleep(1)
    up(1)
    #如果露出来的tab页面上有作品则邀请加入合唱；否则，输入用户没有合唱作品的提示
    if poco('com.starmakerinteractive.starmaker:id/img_cover').exists():
        poco('com.starmakerinteractive.starmaker:id/btn_action',text='邀请').click()
        assert_exists(Template(r"tpl1681895520209.png", record_pos=(-0.314, -0.961), resolution=(1080, 2340)), "判断是否进入分享页面")
        if poco('com.starmakerinteractive.starmaker:id/tv_title',text='好友').exists():
            poco(name='com.starmakerinteractive.starmaker:id/cb_choose').click()
            poco(name='com.starmakerinteractive.starmaker:id/btn_share').click()
            print('分享合唱给好友')
            assert_exists(Template(r"tpl1686540843139.png", record_pos=(-0.01, 0.844), resolution=(1080, 2340)), "成功分享给好友合唱半成品")

        else:
            print('该用户没有好友，暂不能邀请好友加入合唱')
            assert_exists(Template(r"tpl1686540749776.png", record_pos=(-0.006, 0.169), resolution=(1080, 2340)), "没有好友，无法分享合唱")

            back(1)
    else:
        print('该用户无合唱半成品')
    down(3)
    sleep(2)

#定义小视频页签
def profile_shortvideo():
    #上划一下页面，找找看短视频tab
    up(1)
    #判断一下是否有短视频tab页签，是否该地区支持短视频
    if poco('com.starmakerinteractive.starmaker:id/tv_tab_title',text='短视频').exists():
        print('该地区个人页有短视频tab')
        poco('com.starmakerinteractive.starmaker:id/tv_tab_title',text='短视频').click()
        sleep(1)
        if poco(name='com.starmakerinteractive.starmaker:id/img_recording_cover').exists():
            poco(name='com.starmakerinteractive.starmaker:id/img_recording_cover').click()
            assert_exists(Template(r"tpl1686298547177.png", record_pos=(-0.255, 0.047), resolution=(1080, 2340)), "判断是否进入播放详情页面")
            #播放详情页做个like/unlike操作
            poco('com.starmakerinteractive.starmaker:id/btn_like').click()
            back(1)
        else:
            print('用户没有小视频作品')
    else:
        print('该地区个人页有短视频tab')
    down(3)
    sleep(2)

#定义个人页发布按钮
def profile_productbtn():
    #点击发布按钮，并选择点击拍摄小视频选项
    poco(name='com.starmakerinteractive.starmaker:id/fab_expand_menu_button').click()
    poco(name='com.starmakerinteractive.starmaker:id/float_bt2').click()
    sleep(1)
    if poco('android.widget.TextView',text='图集功能上线，轻松分享生活瞬间~').exists():
        poco('com.starmakerinteractive.starmaker:id/btn_positive',text='立即体验').click()
        if poco('android.widget.TextView',text='需要开启以下权限').exists():
            poco('com.starmakerinteractive.starmaker:id/permissionOkTv',text='好，我们开始吧').click()
            while poco('com.android.permissioncontroller:id/permission_allow_foreground_only_button').exists():
                poco('com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()
            while poco('com.android.permissioncontroller:id/permission_allow_button').exists():
                poco('com.android.permissioncontroller:id/permission_allow_button').click()
        else:
            #处理完了弹窗，授权，就进入到了拍摄页了
            sleep(0.5)
    else:
        if poco('android.widget.TextView',text='需要开启以下权限').exists():
            poco('com.starmakerinteractive.starmaker:id/permissionOkTv',text='好，我们开始吧').click()
            while poco('com.android.permissioncontroller:id/permission_allow_foreground_only_button').exists():
                poco('com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()
            while poco('com.android.permissioncontroller:id/permission_allow_button').exists():
                poco('com.android.permissioncontroller:id/permission_allow_button').click()
        else:
            #处理完了弹窗，授权，就进入到了拍摄页了
            sleep(0.5)
    #判断是不是在拍摄页啊？是，长按拍摄按钮拍摄一段时长为5s的小视频
    assert_equal(poco('com.starmakerinteractive.starmaker:id/tv_reord_tip_capturelib_fragment_capture').get_text(), "轻触拍摄，长按摄像", "判断是否进入小视频拍摄页.")
    touch(Template(r"tpl1686823310056.png", record_pos=(-0.004, 0.745), resolution=(1080, 2340)),duration=5,times=1)
    sleep(3)
    #判断进入编辑发布页
    assert_equal(poco('com.starmakerinteractive.starmaker:id/ret_post_desc').get_text(), "说点什么吧...", "判断是否进入编辑发布页.")
    #点击description编辑栏，编辑 good job 的测试文案
    poco(name='com.starmakerinteractive.starmaker:id/ret_post_desc').click()
    text("good job")
    poco(name='com.starmakerinteractive.starmaker:id/tv_done').click()
    #点击发布按钮，发布小视频作品
    poco(name='com.starmakerinteractive.starmaker:id/tv_post').click()
    sleep(5)
    assert_exists(Template(r"tpl1681898270922.png", record_pos=(-0.2, 0.987), resolution=(1080, 2340)), "判断是否有进入主页")

#登录APP
#loginapp()
#判断有没有家族
#profile_family()
#个人页【首页】tab
#profile_homepage_info()
#profile_homepage_album()
#profile_homepage_ktv()
#profile_homepage_cover()
#profile_homepage_playlist()
#个人页动态tab
#profile_moment()
#个人页歌单tab
#profile_playlist()
#个人页作品tab
#profile_cover()
#个人页合唱tab
#profile_duet()  
#个人页小视频tab
#profile_shortvideo()
#个人页发布器按钮
#profile_productbtn()