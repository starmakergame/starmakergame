# -*- encoding=utf8 -*-
__author__ = "YSH"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)



###需将账号设置为中东大区，APP语言设置为中文

def notification_swipe():                     
    if poco("android:id/right_icon").exists():
        swipe(p1=[0.482, 0.14],p2=[0.482, 0.063])

def System_permissions():
    if poco("com.android.permissioncontroller:id/permission_message",text = "要允许StarMaker录音吗？").exists():
        poco("com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
    elif poco("com.android.permissioncontroller:id/permission_message",text = "要允许“StarMaker”拍摄照片和录制视频吗？").exists():
        poco("com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
        
def ktv_guide():
    if poco("com.starmakerinteractive.starmaker:id/ktv_guide_tip").exists():
        poco("com.starmakerinteractive.starmaker:id/close").click()

def guide():
    if poco("com.starmakerinteractive.starmaker:id/switcher").exists():
        sleep(3.0)
        
        
def solo_publish():  #歌曲录制完成，点击发布，发布成功页面
    if poco("com.starmakerinteractive.starmaker:id/recording_headset_dialog_msg_tv").exists():
        poco("com.starmakerinteractive.starmaker:id/recording_headset_dialog_i_know_btn").click()
        while not exists(Template(r"tpl1684493667928.png", record_pos=(0.001, 0.789), resolution=(1440, 3120))):
            
                         sleep(1.0)
        poco("com.starmakerinteractive.starmaker:id/rbtn_record_recorder_song_fragment_song_record").click()
        swipe([767, 2492],[735, 771])
        while not exists(Template(r"tpl1684980026069.png", threshold=0.99, rgb=True, record_pos=(0.353, 0.874), resolution=(1440, 3120))):
                         sleep(1.0)
        poco("com.starmakerinteractive.starmaker:id/iv_done_recorder_song_fragment_song_record").click()
        if poco("com.starmakerinteractive.starmaker:id/common_dialog_content",text = "录音还未完成，你确定要现在结束录音吗？"):
            poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_positive").click()
        poco("com.starmakerinteractive.starmaker:id/tv_next_baserecord_fragment_edit_btn").wait_for_appearance(timeout = 60) 
        if exists(Template(r"tpl1684920470033.png", threshold=0.99, rgb=True, record_pos=(0.287, 0.848), resolution=(1440, 3120))):
            
            poco("com.starmakerinteractive.starmaker:id/share_entrance_iv0").click()
        poco("com.starmakerinteractive.starmaker:id/tv_next_baserecord_fragment_edit_btn").click()
        poco("com.starmakerinteractive.starmaker:id/txt_upload_success_new",text = "上传成功，设置为来电铃声～").wait_for_appearance(120)
        

def iknow_start_back():   #点击我知道了，点击关闭录制页面
    if poco("com.starmakerinteractive.starmaker:id/recording_headset_dialog_msg_tv").exists():        
        poco("com.starmakerinteractive.starmaker:id/recording_headset_dialog_i_know_btn").click()
        poco("com.starmakerinteractive.starmaker:id/iv_close_recorder_song_fragment_song_record").click()

        
def reload():     #for you，热门tab重新加载
    if poco("com.starmakerinteractive.starmaker:id/iv_loading_error").exists():
        poco("com.starmakerinteractive.starmaker:id/tv_refresh").click()
        poco("com.starmakerinteractive.starmaker:id/img_cover").wait(timeout = 120)
        
        
        
start_app("com.starmakerinteractive.starmaker")
sleep(5.0)


if poco("com.starmakerinteractive.starmaker:id/open_promotion_iv_image").exists():
    poco("com.starmakerinteractive.starmaker:id/open_promotion_iv_close").click()
if poco("com.starmakerinteractive.starmaker:id/iv_img").exists():
    touch([763, 444])
    
ktv_guide()
guide()


while exists(Template(r"tpl1684980621809.png", record_pos=(-0.001, 0.958), resolution=(1440, 3120))):
    touch(Template(r"tpl1684980638023.png", record_pos=(0.0, 0.96), resolution=(1440, 3120)))
    sleep(1.0)
if poco("com.starmakerinteractive.starmaker:id/tv_feedback_click").exists():
    poco("com.starmakerinteractive.starmaker:id/tv_feedback_click").click()
while not poco("com.starmakerinteractive.starmaker:id/img_cover").exists():
    sleep(1.0)
touch(Template(r"tpl1684291073924.png", record_pos=(-0.419, -0.826), resolution=(1440, 3120)))    



    

    
    
    
notification_swipe()
ktv_guide()
guide()
poco("com.starmakerinteractive.starmaker:id/switcher").wait_for_appearance(60)
poco("com.starmakerinteractive.starmaker:id/switcher").click()
poco("com.starmakerinteractive.starmaker:id/tv_name").wait_for_appearance(60)
assert_exists(Template(r"tpl1684900113718.png", record_pos=(-0.394, -0.581), resolution=(1440, 3120)), "搜索页跳转失败")

searchkeywords1= poco("com.starmakerinteractive.starmaker:id/searchView").get_text()
print(searchkeywords1)
text(text = "",search = True)
poco("com.starmakerinteractive.starmaker:id/iv_icon").wait_for_appearance(60)
searchkeywords2= poco("com.starmakerinteractive.starmaker:id/searchView").get_text()
print(searchkeywords2)
assert_equal(searchkeywords1, searchkeywords2, "搜索失败.")
poco(name = "com.starmakerinteractive.starmaker:id/tv_tab_title",text = "动态").click()
poco("com.starmakerinteractive.starmaker:id/iv_cover").wait_for_appearance(60)
poco("com.starmakerinteractive.starmaker:id/iv_cover")[0].click()
keyevent("back")
poco("com.starmakerinteractive.starmaker:id/delete_iv").click()
text("God Is A Girl",search = True)
poco(name = "com.starmakerinteractive.starmaker:id/tv_tab_title",text = "歌曲").click()
poco("com.starmakerinteractive.starmaker:id/iv_icon").wait_for_appearance(60)
poco("com.starmakerinteractive.starmaker:id/lyt_sing")[0].click()
System_permissions()
poco("com.starmakerinteractive.starmaker:id/recording_headset_dialog_i_know_btn").click()
poco("com.starmakerinteractive.starmaker:id/iv_close_recorder_song_fragment_song_record").click()
poco("com.starmakerinteractive.starmaker:id/delete_iv").click()
poco("com.starmakerinteractive.starmaker:id/tv_name").wait_for_appearance(60)
poco("com.starmakerinteractive.starmaker:id/tv_name")[4].click()
poco("com.starmakerinteractive.starmaker:id/iv_icon").wait_for_appearance(60)
poco("com.starmakerinteractive.starmaker:id/delete_iv").click()
poco("com.starmakerinteractive.starmaker:id/tv_name").wait_for_appearance(60)
poco("com.starmakerinteractive.starmaker:id/follow_icon")[0].click()
#assert_exists(Template(r"tpl1684900581655.png", record_pos=(0.411, 0.153), resolution=(1440, 3120)), "喜欢的人关注失败")
poco("com.starmakerinteractive.starmaker:id/iv_back").click()












notification_swipe()
ktv_guide()
guide()
poco("com.starmakerinteractive.starmaker:id/iv_task").wait_for_appearance(60)
poco("com.starmakerinteractive.starmaker:id/iv_task").click()
if poco("com.starmakerinteractive.starmaker:id/iv_close").exists():
    poco("com.starmakerinteractive.starmaker:id/iv_close").click()
if poco("com.starmakerinteractive.starmaker:id/desc_list").exists():
    poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_positive").click()
assert_exists(Template(r"tpl1684914690385.png", record_pos=(0.0, 0.396), resolution=(1440, 3120)), "每日福利跳转失败")

keyevent("back")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#唱歌tab“已点”模块跳转验证
poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name").wait_for_appearance(20)
poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name")[0].click()
while not poco("com.starmakerinteractive.starmaker:id/img_cover").exists():
    sleep(1.0)
assert_exists(Template(r"tpl1684313453371.png", record_pos=(-0.001, -0.79), resolution=(1440, 3120)), "点唱页面跳转失败")
poco("com.starmakerinteractive.starmaker:id/img_cover")[5].click()  #点唱页面跳转歌曲详情页验证    
sleep(2.0)
poco("com.starmakerinteractive.starmaker:id/iv_back_activity_sing_song_detail_new").click()
clickedsongname = poco(resourceId ="com.starmakerinteractive.starmaker:id/txt_artist")[6].get_text()   #获取已点页面预下载歌手名称
print(clickedsongname)
poco(resourceId ="com.starmakerinteractive.starmaker:id/btn_sing")[6].click()   #点击进入歌曲录制页面下载歌曲
poco("com.starmakerinteractive.starmaker:id/recording_headset_dialog_i_know_btn").click()
while not exists(Template(r"tpl1684493667928.png", record_pos=(0.001, 0.789), resolution=(1440, 3120))):
    sleep(1.0)
poco("com.starmakerinteractive.starmaker:id/iv_close_recorder_song_fragment_song_record").click()
touch(Template(r"tpl1682232348938.png", record_pos=(-0.257, -0.658), resolution=(1440, 3120)))
sleep(2.0)
loadsongname = poco(resourceId ="com.starmakerinteractive.starmaker:id/txt_artist")[0].get_text()   #获取已下载页面下载歌手名称
print(loadsongname)
assert_equal(clickedsongname, loadsongname, "点唱页面歌曲下载成功加入已下载tab.")
poco(resourceId = "com.starmakerinteractive.starmaker:id/imb_backward").click()





  
    
    
    
    
 #唱歌tab“诗歌”模块跳转验证
poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name").wait_for_appearance(timeout = 20)
poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name")[1].click()
while not poco("com.starmakerinteractive.starmaker:id/img_cover").exists():
    sleep(1.0)
assert_exists(Template(r"tpl1684314551551.png", record_pos=(0.001, -0.8), resolution=(1440, 3120)), "诗歌页面跳转失败")
poemspoetryname =poco(resourceId ="com.starmakerinteractive.starmaker:id/txt_artist")[5].get_text()
poco("com.starmakerinteractive.starmaker:id/img_cover")[5].click()  #诗歌页面跳转歌曲详情页验证
print(poemspoetryname)
if poco("com.starmakerinteractive.starmaker:id/tv_singer_name_oncover_activity_sing_song_detail_new").get_text() == poemspoetryname:
    touch(Template(r"tpl1682244965765.png", record_pos=(0.326, -0.704), resolution=(1440, 3120)))
    print("跳转诗歌详情页成功")
else:
    print("跳转诗歌详情页错误")
touch(Template(r"tpl1682231913985.png", record_pos=(0.004, 0.214), resolution=(1440, 3120)))
poco("com.starmakerinteractive.starmaker:id/iv_close_recorder_song_fragment_song_record").click()
poco("com.starmakerinteractive.starmaker:id/iv_back_activity_sing_song_detail_new").click()
poco("com.starmakerinteractive.starmaker:id/tv_tab_title",text = "作品").click()
sleep(3.0)
coverspoetryname1 = poco("com.starmakerinteractive.starmaker:id/txt_song_name")[2].get_text()   #获取作品页点击作品名称
poco(resourceId ="com.starmakerinteractive.starmaker:id/txt_song_name")[2].click()
coverspoetryname2 = poco("com.starmakerinteractive.starmaker:id/tv_tweet_use_time").get_text()#获取作品页作品名称
assert_equal(coverspoetryname2, coverspoetryname1, "跳转诗歌详情页失败.")
poco(resourceId = "com.starmakerinteractive.starmaker:id/imb_back").click()
poco(resourceId = "com.starmakerinteractive.starmaker:id/imb_backward").click()











#唱歌tab“合唱”模块跳转验证
poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name").wait_for_appearance(timeout = 20)
poco(resourceId ="com.starmakerinteractive.starmaker:id/tv_sing_label_name")[2].click()
while not poco("com.starmakerinteractive.starmaker:id/img_recording_cover").exists():
    sleep(1.0)
assert_exists(Template(r"tpl1684315247774.png", record_pos=(0.003, -0.797), resolution=(1440, 3120)), "合唱页面跳转失败")
recommendduetname1 = poco("com.starmakerinteractive.starmaker:id/txt_song_name")[1].get_text()   #获取推荐页面点击合唱作品名称
poco("com.starmakerinteractive.starmaker:id/txt_song_name")[1].click()
poco("com.starmakerinteractive.starmaker:id/img_sing").wait_for_appearance(timeout = 10)
poco("com.starmakerinteractive.starmaker:id/img_sing").click()
if exists(Template(r"tpl1684323047684.png", record_pos=(-0.006, 0.483), resolution=(1440, 3120))):
    touch(Template(r"tpl1684323066873.png", record_pos=(0.017, 0.848), resolution=(1440, 3120)))
System_permissions()
solo_publish()
swipe(v1=[781, 2481],v2=[781, 537])
recommendduetname2 = poco("com.starmakerinteractive.starmaker:id/layout_party_recommend_music_name").get_text()
assert_equal(recommendduetname1, recommendduetname2, "合唱跳转失败.")
touch(Template(r"tpl1684317026102.png", record_pos=(-0.419, -0.967), resolution=(1440, 3120)))
touch(Template(r"tpl1684317566601.png", record_pos=(0.003, 0.961), resolution=(1440, 3120)))
touch(Template(r"tpl1684317587186.png", record_pos=(0.066, -0.643), resolution=(1440, 3120)))
poco(resourceId = "com.starmakerinteractive.starmaker:id/tv_tab_title")[0].click()
sleep(3.0)
poco("com.starmakerinteractive.starmaker:id/img_recording_play")[0].click()
poco("com.starmakerinteractive.starmaker:id/imb_back").click()
poco(resourceId = "com.starmakerinteractive.starmaker:id/imb_backward").click()










#唱歌tab“歌手”模块跳转验证
poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name").wait_for_appearance(timeout = 20)
poco(resourceId ="com.starmakerinteractive.starmaker:id/tv_sing_label_name")[3].click()
while not poco("com.starmakerinteractive.starmaker:id/iv_avatar").exists():
    sleep(1.0)
assert_exists(Template(r"tpl1684318177970.png", record_pos=(-0.003, -0.915), resolution=(1440, 3120)), "歌手页面跳转失败")
poco(text = "Foreign singers").click()
hotsongername1 = poco(resourceId="com.starmakerinteractive.starmaker:id/tv_name")[0].get_text()
poco(resourceId="com.starmakerinteractive.starmaker:id/iv_avatar")[0].click()
hotsongername2 = poco("com.starmakerinteractive.starmaker:id/title_tv").get_text()
assert_equal(hotsongername1, hotsongername2, "歌手详情页跳转错误.")
poco(resourceId = "com.starmakerinteractive.starmaker:id/common_song_item_tv")[3].click()
iknow_start_back()
poco("com.starmakerinteractive.starmaker:id/back_iv").click()
swipe([781, 2987],[781, 1370])
touch(Template(r"tpl1682321904370.png", target_pos=8, record_pos=(0.447, -0.488), resolution=(1440, 3120)))
poco(text = "Westlife").click()
sleep(3.0)
if exists(Template(r"tpl1682322661917.png", record_pos=(-0.275, -0.953), resolution=(1440, 3120))):
    singername = poco("com.starmakerinteractive.starmaker:id/common_song_item_author")[0].get_text()
    poco("com.starmakerinteractive.starmaker:id/common_song_item_head")[0].click()
    singername1 = poco("com.starmakerinteractive.starmaker:id/tv_singer_name_oncover_activity_sing_song_detail_new").get_text()
    print(singername1)
    if singername == singername1:
        poco("com.starmakerinteractive.starmaker:id/iv_back_activity_sing_song_detail_new").click()
    else:
        print("歌手详情页跳转失败")
        poco("com.starmakerinteractive.starmaker:id/iv_back_activity_sing_song_detail_new").click()
poco("com.starmakerinteractive.starmaker:id/back_iv").click()
poco("com.starmakerinteractive.starmaker:id/back_iv").click()
poco("com.starmakerinteractive.starmaker:id/iv_avatar").click()    
poco("com.starmakerinteractive.starmaker:id/back_iv").click()
poco("com.starmakerinteractive.starmaker:id/back_iv").click()






#专题模块跳转验证
poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name").wait_for_appearance(timeout = 20)
touch(Template(r"tpl1683166540216.png", record_pos=(0.435, -0.65), resolution=(1440, 3120)))
while not poco("com.starmakerinteractive.starmaker:id/iv_avatar").exists():
    sleep(1.0)
assert_exists(Template(r"tpl1684318484852.png", record_pos=(0.003, -0.913), resolution=(1440, 3120)), "专题页面跳转失败")
poco("com.starmakerinteractive.starmaker:id/tv_name")[2].click()
sleep(2.0)
poco("com.starmakerinteractive.starmaker:id/common_song_item_head")[1].click()
sleep(2.0)
touch(Template(r"tpl1683166816151.png", record_pos=(-0.438, -0.973), resolution=(1440, 3120)))
poco(resourceId = "com.starmakerinteractive.starmaker:id/common_song_item_tv")[0].click()
iknow_start_back()
poco("com.starmakerinteractive.starmaker:id/back_iv").click()
sleep(2.0)
swipe(v1 = [785, 2826], v2 = [767, 380])
swipe(v1 = [713, 2962], v2 = [713, 932])
swipe(v1 = [1341, 2740], v2 = [50, 2740])
poco("com.starmakerinteractive.starmaker:id/tv_name",text = "励志").click()
assert_equal(poco("com.starmakerinteractive.starmaker:id/title_tv").get_text(), "励志", "专题跳转失败.")
poco("com.starmakerinteractive.starmaker:id/back_iv").click()
poco("com.starmakerinteractive.starmaker:id/back_iv").click()







#排行榜模块跳转验证
poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name").wait_for_appearance(timeout = 20)
swipe(Template(r"tpl1683168651258.png", record_pos=(0.259, -0.609), resolution=(1440, 3120)), vector=[-0.6868, 0.0041])
sleep(2.0)
touch(Template(r"tpl1683168693504.png", record_pos=(0.05, -0.664), resolution=(1440, 3120)))
while not poco("com.starmakerinteractive.starmaker:id/img_cover").exists():
    sleep(1.0)
assert_exists(Template(r"tpl1684321440815.png", record_pos=(-0.003, -0.912), resolution=(1440, 3120)), "排行榜页面跳转失败")

poco("com.starmakerinteractive.starmaker:id/tv_tab_title",text = "趋势").click()
while not poco("com.starmakerinteractive.starmaker:id/txt_title").exists():
    sleep(1.0)
poco("com.starmakerinteractive.starmaker:id/txt_title").click()
while not poco("com.starmakerinteractive.starmaker:id/atv_title_oncover_activity_sing_song_detail_new").exists():
    sleep(1.0)
poco("com.starmakerinteractive.starmaker:id/iv_back_activity_sing_song_detail_new").click()
poco("com.starmakerinteractive.starmaker:id/tv_tab_title",text = "新").click()
sleep(3.0)
touch(Template(r"tpl1683168802333.png", record_pos=(0.391, -0.724), resolution=(1440, 3120)))
iknow_start_back()
touch(Template(r"tpl1683167048298.png", record_pos=(-0.437, -0.965), resolution=(1440, 3120)))
sleep(2.0)









#歌房模块跳转验证
poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name").wait_for_appearance(timeout = 20)
swipe(Template(r"tpl1683170283876.png", record_pos=(0.299, -0.639), resolution=(1440, 3120)), vector=[-0.7345, 0.011])
sleep(2.0)
touch(Template(r"tpl1683170309088.png", record_pos=(0.24, -0.669), resolution=(1440, 3120)))
while not poco("com.starmakerinteractive.starmaker:id/tab_layout").exists():
    sleep(1.0)
if exists(Template(r"tpl1684325370842.png", record_pos=(0.003, 0.172), resolution=(1440, 3120))):
    touch([753, 322])

assert_exists(Template(r"tpl1684318691538.png", record_pos=(-0.001, -0.932), resolution=(1440, 3120)), "歌房页面跳转失败")
touch(Template(r"tpl1683170378887.png", record_pos=(0.008, 0.96), resolution=(1440, 3120)))








#直播模块跳转验证

poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name").wait_for_appearance(timeout = 20)
touch(Template(r"tpl1683170519273.png", record_pos=(0.367, -0.672), resolution=(1440, 3120)))

assert_exists(Template(r"tpl1684318736320.png", record_pos=(0.005, -0.906), resolution=(1440, 3120)), "直播页面跳转失败")
if exists(Template(r"tpl1684292924618.png", record_pos=(-0.185, -0.45), resolution=(1440, 3120))):
    touch([570, 243])

touch(Template(r"tpl1683170573567.png", record_pos=(-0.422, -0.97), resolution=(1440, 3120)))








#清唱模块跳转验证
poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name").wait_for_appearance(timeout = 20)
touch(Template(r"tpl1683170819659.png", record_pos=(0.193, -0.682), resolution=(1440, 3120)))
while not poco("com.starmakerinteractive.starmaker:id/img_recording_cover").exists():
    sleep(1.0)
assert_exists(Template(r"tpl1684318858944.png", record_pos=(0.001, -0.817), resolution=(1440, 3120)), "清唱页面跳转失败")
poco("com.starmakerinteractive.starmaker:id/tv_tab_title",text = "总榜").click()
while not poco("com.starmakerinteractive.starmaker:id/tv_sing_start").exists():
    sleep(1.0)
poco("com.starmakerinteractive.starmaker:id/tv_sing_start").click()
poco("com.starmakerinteractive.starmaker:id/recording_headset_dialog_i_know_btn").click()
poco("com.starmakerinteractive.starmaker:id/tv_choose_music_recorder_song_fragment_song_record").get_text()
assert_equal(poco("com.starmakerinteractive.starmaker:id/tv_choose_music_recorder_song_fragment_song_record").get_text(), "Free Style! - RisingStar", "清唱录制失败.")
poco("com.starmakerinteractive.starmaker:id/iv_close_recorder_song_fragment_song_record").click()
poco("com.starmakerinteractive.starmaker:id/iv_back_activity_sing_song_detail_new").click()



    
    
    
    


    
    
#家族模块跳转验证
poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name").wait_for_appearance(timeout = 20)
touch(Template(r"tpl1683171346381.png", record_pos=(0.383, -0.678), resolution=(1440, 3120)))
assert_exists(Template(r"tpl1684318944829.png", record_pos=(0.003, -0.949), resolution=(1440, 3120)), "家族页面跳转失败")
if poco("com.starmakerinteractive.starmaker:id/rating_dialog_reason").exists():   #评价弹窗关闭
    poco("com.starmakerinteractive.starmaker:id/rating_dialog_close").click()
if exists(Template(r"tpl1683171570117.png", record_pos=(0.003, 0.015), resolution=(1440, 3120))):
    touch(Template(r"tpl1683171586791.png", record_pos=(-0.194, 0.283), resolution=(1440, 3120)))
    touch(Template(r"tpl1683171647114.png", record_pos=(0.006, 0.958), resolution=(1440, 3120)))
else: 
    touch(Template(r"tpl1683171647114.png", record_pos=(0.006, 0.958), resolution=(1440, 3120)))



    

    

    
    
    
    
#for you tab验证
reload()
if poco("com.starmakerinteractive.starmaker:id/tv_song_desc_chorus").exists():
    poco("com.starmakerinteractive.starmaker:id/tv_song_desc_chorus")[0].click()
    sleep(2.0)
    assert_exists(Template(r"tpl1684319135167.png", record_pos=(0.395, 0.261), resolution=(1440, 3120)), "合唱入口跳转失败")
    touch(Template(r"tpl1684206279505.png", record_pos=(-0.452, -0.981), resolution=(1440, 3120)))
else:
    print("for you本次无合唱入口")

poco("com.starmakerinteractive.starmaker:id/iv_play_state")[0].click()
assert_exists(Template(r"tpl1684319200355.png", record_pos=(-0.283, 0.011), resolution=(1440, 3120)), "播放按钮未调出小窗")
if poco("com.starmakerinteractive.starmaker:id/layout_banner").exists():
    poco("com.starmakerinteractive.starmaker:id/layout_banner").click()
    keyevent("back")
else:
    print("for you本次无banner入口")
touch(Template(r"tpl1684209257420.png", record_pos=(-0.231, -0.472), resolution=(1440, 3120)))
reload()
while not poco("com.starmakerinteractive.starmaker:id/img_cover").exists():
    sleep(1.0)
hotsongname1 = poco("com.starmakerinteractive.starmaker:id/txt_artist")[0].get_text()
poco("com.starmakerinteractive.starmaker:id/txt_artist")[0].click()
hotsongname2 = poco("com.starmakerinteractive.starmaker:id/tv_singer_name_oncover_activity_sing_song_detail_new").get_text()
assert_equal(hotsongname2, hotsongname1, "热门页面跳转歌曲详情页错误.")

touch(Template(r"tpl1684209385224.png", record_pos=(-0.432, -0.965), resolution=(1440, 3120)))
poco("com.starmakerinteractive.starmaker:id/btn_sing")[0].click()
poco("com.starmakerinteractive.starmaker:id/recording_headset_dialog_i_know_btn").click()
while not exists(Template(r"tpl1684493667928.png", record_pos=(0.001, 0.789), resolution=(1440, 3120))):
            
        sleep(1.0)
poco("com.starmakerinteractive.starmaker:id/rbtn_record_recorder_song_fragment_song_record").click()
swipe([767, 2492],[735, 771])
while not exists(Template(r"tpl1684493918092.png", threshold=0.99, rgb=True, record_pos=(0.353, 0.872), resolution=(1440, 3120))):
        sleep(1.0)
poco("com.starmakerinteractive.starmaker:id/iv_done_recorder_song_fragment_song_record").click()
if poco("com.starmakerinteractive.starmaker:id/common_dialog_content",text = "录音还未完成，你确定要现在结束录音吗？"):
        poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_negative").click()
poco("com.starmakerinteractive.starmaker:id/iv_done_recorder_song_fragment_song_record").click()
if poco("com.starmakerinteractive.starmaker:id/common_dialog_content",text = "录音还未完成，你确定要现在结束录音吗？"):
        poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_positive").click()
poco("com.starmakerinteractive.starmaker:id/tv_next_baserecord_fragment_edit_btn").wait_for_appearance(timeout = 60)
poco(text = "作品").click()

poco("com.starmakerinteractive.starmaker:id/iv_effect_item_effect_tray")[1].click()
if exists(Template(r"tpl1684920470033.png", threshold=0.99, rgb=True, record_pos=(0.287, 0.848), resolution=(1440, 3120))):
        poco("com.starmakerinteractive.starmaker:id/share_entrance_iv0").click()
swipe(v1 = [731, 2431],v2 = [731, 1423])
poco("com.starmakerinteractive.starmaker:id/ret_input_baserecord_fragment_editor").click()
text(poco("com.android.systemui:id/clock").get_text())
keyevent("back")
keyevent("back")
script = poco("com.android.systemui:id/clock").get_text()
touch(Template(r"tpl1684923496565.png", record_pos=(-0.169, 0.956), resolution=(1440, 3120)))
assert_exists(Template(r"tpl1684923528485.png", record_pos=(-0.001, 0.537), resolution=(1440, 3120)), "发布作品保存本地失败")
poco(text = "立即发布").click()
poco("com.starmakerinteractive.starmaker:id/txt_upload_success_new",text = "上传成功，设置为来电铃声～").wait_for_appearance(120)
swipe([710, 2976],[710, 756])
poco("com.starmakerinteractive.starmaker:id/tv_share_rank_button_new",text = "查看排名").click()
while not poco("com.starmakerinteractive.starmaker:id/img_recording_cover").exists():
    sleep(1.0)
public_songname = poco("com.starmakerinteractive.starmaker:id/atv_title_oncover_activity_sing_song_detail_new").get_text()
poco("com.starmakerinteractive.starmaker:id/iv_back_activity_sing_song_detail_new").click()
poco("com.starmakerinteractive.starmaker:id/iv_close").click()
sleep(2.0)
if poco("com.starmakerinteractive.starmaker:id/rating_dialog_reason").exists():   #评价弹窗关闭
    poco("com.starmakerinteractive.starmaker:id/rating_dialog_close").click()
if exists(Template(r"tpl1684209744530.png", record_pos=(-0.001, 0.024), resolution=(1440, 3120))):
    touch(Template(r"tpl1684209755686.png", record_pos=(-0.183, 0.294), resolution=(1440, 3120)))
while not poco("com.starmakerinteractive.starmaker:id/iv_cover").exists():
    sleep(1.0)
swipe([659, 555],[634, 889])
sleep(3.0)
poco("com.starmakerinteractive.starmaker:id/iv_cover")[0].click()
while not poco("com.starmakerinteractive.starmaker:id/tv_tweet_use_time").exists():
    sleep(1.0)
assert_equal(poco("com.starmakerinteractive.starmaker:id/tv_tweet_use_time").get_text(), public_songname, "foryou发布作品错误.")
assert_equal(poco("com.starmakerinteractive.starmaker:id/htv_desc").get_text().split('\n')[0], script, "foryou作品描述错误.")
poco("com.starmakerinteractive.starmaker:id/imb_back").click()             
#poco("com.starmakerinteractive.starmaker:id/tab_animation_view").click()
touch(Template(r"tpl1684984789816.png", record_pos=(0.0, 0.961), resolution=(1440, 3120)))
assert_exists(Template(r"tpl1684217375753.png", record_pos=(-0.306, -0.476), resolution=(1440, 3120)), "唱歌-foryou用例执行失败")












#诗歌tab跳转验证
poco("com.starmakerinteractive.starmaker:id/tv_tab_title",text="诗歌").click()
poco("com.starmakerinteractive.starmaker:id/img_cover").wait_for_appearance(60)
poco("com.starmakerinteractive.starmaker:id/img_cover")[0].click()
poco("com.starmakerinteractive.starmaker:id/iv_back_activity_sing_song_detail_new").click()
poco("com.starmakerinteractive.starmaker:id/btn_sing",text="朗诵")[0].click() 
poco("com.starmakerinteractive.starmaker:id/recording_headset_dialog_i_know_btn").click()
while not exists(Template(r"tpl1684493667928.png", record_pos=(0.001, 0.789), resolution=(1440, 3120))):
    sleep(1.0)
poco("com.starmakerinteractive.starmaker:id/rbtn_record_recorder_song_fragment_song_record").click()
poco("com.starmakerinteractive.starmaker:id/iv_close_recorder_song_fragment_song_record").click()
if poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_negative").exists():
    poco("com.starmakerinteractive.starmaker:id/text",text = "退出").click()
    if poco("com.starmakerinteractive.starmaker:id/common_dialog_title").exists():
        poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_positive").click()
while not poco("com.starmakerinteractive.starmaker:id/tv_apply").exists():
    sleep(1.0)
poco("com.starmakerinteractive.starmaker:id/imb_close").click()    
touch(Template(r"tpl1684218689163.png", record_pos=(-0.279, -0.704), resolution=(1440, 3120)))
poco("com.starmakerinteractive.starmaker:id/img_recording_cover").wait_for_appearance(60)
poco("com.starmakerinteractive.starmaker:id/img_recording_play")[0].click()
while not poco("com.starmakerinteractive.starmaker:id/item_card_avatar").exists():
    sleep(1.0)
poco("com.starmakerinteractive.starmaker:id/imb_back").click()
if exists(Template(r"tpl1684218863068.png", record_pos=(-0.273, 0.016), resolution=(1440, 3120))):
    touch(Template(r"tpl1684218880802.png", record_pos=(-0.281, 0.017), resolution=(1440, 3120)))
    touch(Template(r"tpl1684218957518.png", record_pos=(-0.036, 0.012), resolution=(1440, 3120)))
poco("com.starmakerinteractive.starmaker:id/btn_filter").click()
if poco("com.starmakerinteractive.starmaker:id/title").exists():
    poco("com.starmakerinteractive.starmaker:id/btn_solo_only").click()
    poco("com.starmakerinteractive.starmaker:id/btn_ok").click()
button_name0 = poco("com.starmakerinteractive.starmaker:id/tv_join_music")[0].get_text()
button_name1 = poco("com.starmakerinteractive.starmaker:id/tv_join_music")[1].get_text()
assert_equal(button_name0, button_name1, "作品筛选失败.")
