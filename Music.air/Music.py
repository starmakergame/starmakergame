# -*- encoding=utf8 -*-
__author__ = "jiuzhang"

from airtest.core.api import *

auto_setup(__file__)



from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
touch([532, 2316])#首页点击唱歌sing
touch(Template(r"tpl1684320111480.png", record_pos=(-0.022, -0.862), resolution=(1080, 2408)))
sleep(1)
touch(Template(r"tpl1684320137216.png", record_pos=(-0.427, -0.731), resolution=(1080, 2408)))
touch([442, 598])#点击第一行歌曲播放
sleep(6)#等待唱歌6秒
wait(Template(r"tpl1684406710612.png", threshold=0.4, record_pos=(-0.321, 0.406), resolution=(1080, 2408)),timeout=5)#等待播放完成
touch([442, 598])#点击第一行歌曲暂停
poco('com.starmakerinteractive.starmaker:id/btn_add')[0].click()#点击元素第一个铃声按钮
sleep(2)
wait(Template(r"tpl1684395454259.png", record_pos=(0.005, -0.57), resolution=(1080, 2408)),timeout=10)#等待加载完成
touch([477, 2253])#领取奖励
for i in range(4):#滑动循环4次
    swipe([493, 1929],[356, 575])#上下滑
touch([74, 152])#返回
wait(Template(r"tpl1684395454259.png", record_pos=(0.005, -0.57), resolution=(1080, 2408)),timeout=10)#等待加载完成
touch([74, 152])#返回
for i in range(10):#默认在最上面向下滑动10次
    swipe([493, 1929],[356, 575])#上下滑
touch(Template(r"tpl1684397771417.png", record_pos=(-0.234, -0.728), resolution=(1080, 2408)))
touch([442, 598])#点击第一行歌曲播放
sleep(6)#等待播放6秒
wait(Template(r"tpl1684406710612.png", threshold=0.4, record_pos=(-0.321, 0.406), resolution=(1080, 2408)),timeout=5)#等待这个状态
touch([442, 598])#点击第一行歌曲暂停
poco('com.starmakerinteractive.starmaker:id/btn_add')[0].click()#点击元素第一个铃声按钮
while poco('com.starmakerinteractive.starmaker:id/lrc_view').exists()  is False:
    time.sleep(0.5)
sleep(6)#声音剪辑页播放6秒
wait(Template(r"tpl1684402015176.png", record_pos=(-0.305, 0.905), resolution=(1080, 2408)),timeout=5)
touch(Template(r"tpl1684402118421.png", record_pos=(-0.312, 0.897), resolution=(1080, 2408)))#播放暂停
for i in range(2):#循环2次滑动
    swipe([82, 575],[62, 1502])#上下滑
sleep(5)#等待播放5秒
if exists(Template(r"tpl1684404082885.png", record_pos=(0.353, 0.517), resolution=(1080, 2408))):#如果出现这个
    touch(Template(r"tpl1684404082885.png", record_pos=(0.353, 0.517), resolution=(1080, 2408)))#进行点击
for i in range(1):#循环1次
    swipe([774, 1917],[305, 1948])#时长左右滑动
sleep(5)#等待播放5秒
touch(Template(r"tpl1684406445518.png", record_pos=(0.173, 0.895), resolution=(1080, 2408)))#声音剪辑设置铃声
wait(Template(r"tpl1684395454259.png", record_pos=(0.005, -0.57), resolution=(1080, 2408)),timeout=10)#等待加载完成
touch(Template(r"tpl1684392961398.png", record_pos=(0.006, 0.96), resolution=(1080, 2408)))
for i in range(4):#滑动循环4次
    swipe([493, 1929],[356, 575])#上下滑
touch([82, 156])#返回
sleep(3)
wait(Template(r"tpl1684395454259.png", record_pos=(0.005, -0.57), resolution=(1080, 2408)),timeout=8)#等待加载完成
touch([82, 156])#回到手机铃声，我的作品页
poco('com.starmakerinteractive.starmaker:id/btn_add')[0].click()#点击元素第一个铃声按钮
while poco('com.starmakerinteractive.starmaker:id/lrc_view').exists()  is False:
    time.sleep(0.5)
sleep(5)#等待
touch([583, 2336])#进入铃声广场，更多精彩铃声
sleep(3)
touch([86, 551])#发现页
touch([410, 978])#点击第二行歌曲播放
sleep(6)#等待
wait(Template(r"tpl1684406710612.png", threshold=0.4, record_pos=(-0.321, 0.406), resolution=(1080, 2408)),timeout=5)#等待播放完成
touch([410, 978])#点击第一行歌曲暂停
for i in range(10):#滑动循环10次
    swipe([493, 1929],[356, 575])#上下滑
sleep(3)
touch(Template(r"tpl1684489241002.png", record_pos=(-0.238, -0.858), resolution=(1080, 2408)))
touch([438, 1197])#点击第三行歌曲播放
sleep(5)
touch(Template(r"tpl1684489219310.png", record_pos=(-0.015, -0.858), resolution=(1080, 2408)))
sleep(2)
touch([450, 583])#有当前铃声时点击
sleep(6)#等待播放6秒
wait(Template(r"tpl1684406710612.png", threshold=0.4, record_pos=(-0.321, 0.406), resolution=(1080, 2408)),timeout=5)#等待这个状态
touch([450, 583])#点击第一行歌曲播放
sleep(2)
touch([1009, 586])#点击更多
sleep(2)
touch([187, 2144])#点击更多恢复系统铃声
sleep(2)
touch([297, 1357])#弹窗取消重置铃声
sleep(1)
touch([1009, 586])#点击更多
sleep(2)
touch([187, 2144])#点击更多恢复系统铃声
sleep(2)
touch([536, 2308])#点击取消
sleep(2)
touch([1009, 586])#点击更多
sleep(2)
touch([211, 2144])#点击更多恢复系统铃声
sleep(2)
touch([731, 1377])#点击确定重置手机铃声
sleep(2)
touch(Template(r"tpl1684489219310.png", record_pos=(-0.015, -0.858), resolution=(1080, 2408)))
poco('com.starmakerinteractive.starmaker:id/btn_add')[2].click()#点击元素第3个铃声按钮
sleep(5)
wait(Template(r"tpl1684395454259.png", record_pos=(0.005, -0.57), resolution=(1080, 2408)),timeout=10)#等待加载完成
touch(Template(r"tpl1684392961398.png", record_pos=(0.006, 0.96), resolution=(1080, 2408)))
for i in range(4):#滑动循环4次
    swipe([493, 1929],[356, 575])#上下滑
sleep(2)
touch([78, 144])#返回
sleep(2)
wait(Template(r"tpl1684395454259.png", record_pos=(0.005, -0.57), resolution=(1080, 2408)),timeout=8)#等待加载完成
touch([78, 144])#回到广场，我的作品页
sleep(2)
touch([876, 140])#搜索点击
sleep(2)
touch(Template(r"tpl1684467867630.png", record_pos=(-0.001, -0.983), resolution=(1080, 2408)))
text("一路向北",search=True)
touch([375, 273])
sleep(10)
touch([375, 273])
touch([896, 148])#删除之前搜索文字
text("珊瑚海",search=True)
poco('com.starmakerinteractive.starmaker:id/btn_add')[2].click()#点击元素
while poco('com.starmakerinteractive.starmaker:id/lrc_view').exists()  is False:
    time.sleep(0.5)
sleep(3)
touch([62, 156])#点击左上角退出
sleep(2)
touch([356, 1381])#弹窗确认退出
sleep(2)
touch([78, 136])#再次退出
sleep(2)
touch([1017, 148])#铃声广场更多按钮
sleep(2)
touch([148, 2144])#更多常见问题
sleep(5)#等待
touch([86, 160])
sleep(3)
touch([86, 160])#连续退出2次
assert_exists(Template(r"tpl1684492176718.png", record_pos=(0.003, -0.006), resolution=(1080, 2408)), "手机铃声tab测试完成")
touch(Template(r"tpl1684835839157.png", record_pos=(-0.236, -0.864), resolution=(1080, 2408)))
sleep(3)
touch([230, 410])#点击地区
sleep(2)
touch([207, 301])#选择地区
sleep(2)
touch([450, 829])#进入NO.1作品
sleep(5)
for i in range(5):#滑动循环
    swipe([493, 1929],[356, 575])#上下滑
touch([109, 2312])#点击关注
sleep(5)
touch([109, 2312])#取消关注
sleep(3)
touch(Template(r"tpl1684836535303.png", record_pos=(-0.207, 1.007), resolution=(1080, 2408)))
sleep(2)
touch([207, 2296])#点击评论框
text("一路向北")
sleep(1)
touch([986, 2281])#单独点击发送评论
sleep(1)
touch(Template(r"tpl1684837153619.png", record_pos=(-0.011, 1.009), resolution=(1080, 2408)))
sleep(2)
touch([911, 802])#取消礼物面板
touch([727, 2308])#点击分享面板
sleep(2)
touch([911, 802])#取消分享面板
sleep(2)
touch([986, 156])#右上角更多
sleep(2)
touch(Template(r"tpl1684912184416.png", record_pos=(-0.117, 0.763), resolution=(1080, 2408)))
sleep(1)
touch(Template(r"tpl1684837592051.png", record_pos=(0.105, 0.234), resolution=(1080, 2408)))
touch(Template(r"tpl1684912184416.png", record_pos=(-0.117, 0.763), resolution=(1080, 2408)))
touch(Template(r"tpl1684837627394.png", record_pos=(0.271, 0.234), resolution=(1080, 2408)))
touch(Template(r"tpl1684912210801.png", record_pos=(0.11, 0.769), resolution=(1080, 2408)))

sleep(2)
touch([70, 133])#举报页返回
sleep(2)
touch([986, 156])#右上角更多
if exists(Template(r"tpl1684912257341.png", record_pos=(-0.343, 0.763), resolution=(1080, 2408))):
    touch(Template(r"tpl1684912257341.png", record_pos=(-0.343, 0.763), resolution=(1080, 2408)))
if exists(Template(r"tpl1684838712592.png", record_pos=(0.012, 0.63), resolution=(1080, 2408))):
    touch(Template(r"tpl1684837856573.png", record_pos=(0.005, 1.02), resolution=(1080, 2408)))
sleep(1)
touch([986, 156])#右上角更多
sleep(3)
touch([986, 156])#右上角更多
sleep(2)
poco('com.starmakerinteractive.starmaker:id/item_icon').click()#拉黑点击ID
sleep(2)
touch([1009, 524])
touch(Template(r"tpl1684912430927.png", record_pos=(0.01, 0.187), resolution=(1080, 2408)))
sleep(2)
touch(Template(r"tpl1684912466021.png", record_pos=(-0.008, -0.733), resolution=(1080, 2408)))
for i in range(5):#滑动循环
    swipe([493, 1929],[356, 575])#上下滑
sleep(2)
touch([230, 1502])#随机进入NO作品
sleep(2)
for i in range(5):#滑动循环
    swipe([493, 1929],[356, 575])#上下滑
sleep(1)    
touch([50, 148])#退出作品NO1
sleep(1)  
touch(Template(r"tpl1684912700267.png", record_pos=(0.126, -0.735), resolution=(1080, 2408)))
sleep(2)
for i in range(5):#滑动循环
    swipe([493, 1929],[356, 575])#上下滑
touch([504, 1396])
sleep(2)
touch([50, 148])#退出作品NO1
sleep(2)
poco('com.starmakerinteractive.starmaker:id/tv_tab_title')[7].click()#财富榜
sleep(2)
for i in range(5):#滑动循环
    swipe([493, 1929],[356, 575])#上下滑
touch([504, 1396])
sleep(2)
touch([50, 148])#退出作品NO1



