# -*- encoding=utf8 -*-
__author__ = "YSH"

from airtest.core.api import *

auto_setup(__file__)



from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

#通用方法--录制页面点击我知道了，等待歌曲下载完成后点击关闭录制页面
def Download_songs():
    #--等待耳机弹窗出现点击我知道了--#
    poco("com.starmakerinteractive.starmaker:id/recording_headset_dialog_msg_tv").wait_for_appearance()
    poco("com.starmakerinteractive.starmaker:id/recording_headset_dialog_i_know_btn").click()
    #--等待歌曲下载完成，点击开始按钮进行录制--#
    while not exists(Template(r"tpl1684493667928.png", record_pos=(0.001, 0.789), resolution=(1440, 3120))):
        sleep(1.0)
    #--下载完成点击关闭按钮--#
    poco("com.starmakerinteractive.starmaker:id/iv_close_recorder_song_fragment_song_record").click()

    
#通用方法--等待元素出现
def waitting(resource_id=None, text= None, time=30):
    if resource_id is not None and text is None:  
        try:
            poco(resourceId=resource_id).wait_for_appearance(timeout=time)
            #poco(text=text).wait_for_disappearance(timeout=time)
        except BaseException as e:
            snapshot(msg=f"{resource_id}元素未出现")
    elif resource_id is not None and text is not None:  
        try:
            poco(resourceId=resource_id,text=text).wait_for_appearance(timeout=time)
        except BaseException as e:
            snapshot(msg=f"{resource_id}{text}元素未出现")
    elif resource_id is None and text is not None:
        try:
            poco(text=text).wait_for_appearance(timeout=time)
        except BaseException as e:
            snapshot(msg=f"{text}元素未出现")
            
            
#通用方法--录制页获取权限弹窗            
def System_permissions():
    #判断是否存在麦克风权限弹窗
    resouceList = ["com.starmakerinteractive.starmaker:id/permissionOkTv","com.android.permissioncontroller:id/permission_allow_foreground_only_button","com.android.permissioncontroller:id/permission_allow_button"]
    for resource in resouceList:
        if poco(resource).exists():
            poco(resource).click()  

            
#通用方法--录制页面点击我知道了，立刻关闭录制页面
def iknow_start_back():
    poco("com.starmakerinteractive.starmaker:id/recording_headset_dialog_msg_tv").wait_for_appearance()
    poco("com.starmakerinteractive.starmaker:id/recording_headset_dialog_i_know_btn").click()
    poco("com.starmakerinteractive.starmaker:id/iv_close_recorder_song_fragment_song_record").click()


#通用方法--录制完成发布
def solo_publish():
    #等待耳机弹窗出现点击我知道了
    poco("com.starmakerinteractive.starmaker:id/recording_headset_dialog_msg_tv").wait_for_appearance()
    poco("com.starmakerinteractive.starmaker:id/recording_headset_dialog_i_know_btn").click()
    #等待歌曲下载完成，点击开始按钮进行录制
    while not exists(Template(r"tpl1684493667928.png", record_pos=(0.001, 0.789), resolution=(1440, 3120))):
        sleep(1.0)                
    poco("com.starmakerinteractive.starmaker:id/rbtn_record_recorder_song_fragment_song_record").click()
    #滑动歌词快进
    poco.swipe([0.503, 0.747],[0.503, 0.013],duration=1.0)
    #多次点击完成按钮判断是否可以结束录制
    poco("com.starmakerinteractive.starmaker:id/iv_done_recorder_song_fragment_song_record").click()
    while not poco("com.starmakerinteractive.starmaker:id/common_dialog_content",text = "录音还未完成，你确定要现在结束录音吗？").exists():
        poco("com.starmakerinteractive.starmaker:id/iv_done_recorder_song_fragment_song_record").click()
        sleep(2.0)
    #结束录音弹窗点击是
    poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_positive").click()
    #等待发布预览页出现
    poco("com.starmakerinteractive.starmaker:id/tv_next_baserecord_fragment_edit_btn").wait_for_appearance(60) 
    #--判断是否存在分享第三方入口，如果存在双击取消选择分享方式--#
    if poco("com.starmakerinteractive.starmaker:id/share_desc").exists():
        poco("com.starmakerinteractive.starmaker:id/share_entrance_iv2").click()
        poco("com.starmakerinteractive.starmaker:id/share_entrance_iv2").click()
    #点击发布按钮
    poco("com.starmakerinteractive.starmaker:id/tv_next_baserecord_fragment_edit_btn").click()
    poco("com.starmakerinteractive.starmaker:id/txt_upload_success_new",text = "上传成功，设置为来电铃声～").wait_for_appearance(120)   

        
##########搜索框功能验证###########    
def sing_search():
    #--等待搜索框可以点击--#
    waitting("com.starmakerinteractive.starmaker:id/switcher")
    poco("com.starmakerinteractive.starmaker:id/switcher").click()
    #--等待搜索页面加载成功--#
    waitting("com.starmakerinteractive.starmaker:id/tv_name")
    assert_equal(poco("com.starmakerinteractive.starmaker:id/tv_hot_search").exists(),True,"搜索页跳转成功")
    #--获取搜索暗词--#
    searchkeywords1= poco("com.starmakerinteractive.starmaker:id/searchView").get_text()
    print(searchkeywords1)
    #--不输入内容直接搜索暗词--#
    text(text = "",search = True)
    #--等待搜索结果页加载成功--#
    waitting("com.starmakerinteractive.starmaker:id/iv_icon")
    #--获取搜索结果页搜索框中的搜索词--#
    searchkeywords2= poco("com.starmakerinteractive.starmaker:id/searchView").get_text()
    print(searchkeywords2)
    assert_equal(searchkeywords1, searchkeywords2, "搜索暗词成功.")
    #--在搜索结果页切换至动态tab--#
    poco(name = "com.starmakerinteractive.starmaker:id/tv_tab_title",text = "动态").click()
    #--等待动态tab数据加载--#
    waitting("com.starmakerinteractive.starmaker:id/iv_cover")
    #--点击搜索结果页中的第一个作品，进入作品详情页--#
    poco("com.starmakerinteractive.starmaker:id/iv_cover")[0].click()
    keyevent("back")
    #--判断搜索框是否存在删除按钮，存在时删除搜索词后输入新的搜索词，不存在时直接输入新的搜索词--#
    if poco("com.starmakerinteractive.starmaker:id/delete_iv").exists():
        poco("com.starmakerinteractive.starmaker:id/delete_iv").click()
        text("God Is A Girl",search = True)
    else:
        text("God Is A Girl",search = True)
    #--在搜索结果页切换至歌曲tab--#
    poco(name = "com.starmakerinteractive.starmaker:id/tv_tab_title",text = "歌曲").click()
    #--等待搜索结果页加载成功--#
    waitting("com.starmakerinteractive.starmaker:id/iv_icon")
    #--点击搜索结果中第一首歌的演唱按钮--#
    poco("com.starmakerinteractive.starmaker:id/lyt_sing")[0].click()
    #--调用通用方法--录制页获取权限弹窗--#
    System_permissions()
    #--调用通用方法--录制页面点击我知道了，立刻关闭录制页面--#
    iknow_start_back()
    #--点击搜索框删除按钮返回搜索页--#
    poco("com.starmakerinteractive.starmaker:id/delete_iv").click()
    #--等待搜索结果页加载成功--#
    waitting("com.starmakerinteractive.starmaker:id/tv_name")
    #--点击搜索页删除搜索记录按钮--#
    poco("com.starmakerinteractive.starmaker:id/iv_delete").click()
    #--等待二次确认弹窗出现后点击确认--#
    waitting("com.starmakerinteractive.starmaker:id/common_dialog_content")
    poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_positive").click()
    assert_equal(poco("com.starmakerinteractive.starmaker:id/btn_remove").exists(),False,"删除搜索记录验证通过")
    #--返回至sing页面--#
    poco("com.starmakerinteractive.starmaker:id/iv_back").click()

    
##########每日福利功能验证###########    
def sing_dailyreward():
    #--等待每日福利入口可以点击--#
    waitting("com.starmakerinteractive.starmaker:id/iv_task")
    poco("com.starmakerinteractive.starmaker:id/iv_task").click()
    sleep(5.0)
#     #--判断是否存在每日签到弹窗--#
#     if poco("com.starmakerinteractive.starmaker:id/iv_close").exists():
#         poco("com.starmakerinteractive.starmaker:id/iv_close").click()
#     #--判断是否存在每日福利帮助说明弹窗--#    
#     if poco("com.starmakerinteractive.starmaker:id/desc_list").exists():
#         poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_positive").click()
    dailyrewardList = ["com.starmakerinteractive.starmaker:id/iv_close","com.starmakerinteractive.starmaker:id/common_dialog_btn_positive"]
    for dailyreward in dailyrewardList:
        if poco(dailyreward).exists():
            poco(dailyreward).click()
    assert_equal(poco(text="每日福利").exists(),True,"每日福利页面跳转成功")
    #--返回至sing页面--#    
    keyevent("back")
    
        
##########已点入口功能验证###########
def sing_mysongs():        
    #--点击“已点”入口--#
    poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name",text="已点").click()
    #--等待页面元素加载--#
    waitting(resource_id="com.starmakerinteractive.starmaker:id/img_cover")
    assert_equal(poco(text="我的点唱").exists(),True,"点唱页面跳转成功")
    #--判断当前账号是否存在已点歌曲--#
    if poco("com.starmakerinteractive.starmaker:id/icon_empty").exists():#当前账号无已点歌曲
        poco("com.starmakerinteractive.starmaker:id/imb_search").click()#点击搜索图标搜索歌曲
        waitting("com.starmakerinteractive.starmaker:id/tv_name")#等待搜索页加载完成
        poco("com.starmakerinteractive.starmaker:id/tv_name")[0].click()#点击热门搜索词进行搜索
        waitting("com.starmakerinteractive.starmaker:id/lyt_sing")#等待搜索结果页加载完成
        poco("com.starmakerinteractive.starmaker:id/tv_tab_title")[1].click()#切换至歌曲tab
        poco("com.starmakerinteractive.starmaker:id/lyt_sing")[0].click()#点击演唱按钮进入录制页面
        Download_songs()#--调用通用方法--录制页面点击我知道了，等待歌曲下载完成后点击关闭录制页面--#
        #--获取搜索结果页歌手名称--#
        clickedsongname = poco(resourceId ="com.starmakerinteractive.starmaker:id/tv_singer").get_text()
        print(clickedsongname)
        poco("com.starmakerinteractive.starmaker:id/iv_back").click()#点击关闭搜索页面
    else:
        poco("com.starmakerinteractive.starmaker:id/img_cover")[0].click()  #点击歌曲封面进入歌曲详情页
        #--等待歌曲详情页数据加载完成--#
        waitting("com.starmakerinteractive.starmaker:id/tv_uploader_activity_sing_song_detail_new")
        #--点击返回上一页--#
        poco("com.starmakerinteractive.starmaker:id/iv_back_activity_sing_song_detail_new").click()
        #--获取已点页面预下载歌手名称--#
        clickedsongname = poco(resourceId ="com.starmakerinteractive.starmaker:id/txt_artist")[0].get_text()   
        print(clickedsongname)
        poco(resourceId ="com.starmakerinteractive.starmaker:id/btn_sing")[0].click()#点击进入歌曲录制页面下载歌曲
        Download_songs()#--调用通用方法--录制页面点击我知道了，等待歌曲下载完成后点击关闭录制页面--#
    poco("com.starmakerinteractive.starmaker:id/tv_tab_title",text="已下载").click()#切换至已下载页面
    #--等待已下载页面数据加载完成--#
    waitting("com.starmakerinteractive.starmaker:id/img_cover")
    ##--获取已下载页面下载歌手名称--#
    loadsongname = poco(resourceId ="com.starmakerinteractive.starmaker:id/txt_artist").get_text()
    print(loadsongname)
    assert_equal(clickedsongname, loadsongname, "点唱页面歌曲下载成功加入已下载tab.")
    #--返回至sing页面--#
    poco(resourceId = "com.starmakerinteractive.starmaker:id/imb_backward").click()

    
##########合唱入口功能验证###########      
def sing_duet():  
    #--滑动查找“合唱”入口--#
    while poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name",text="合唱").exists() == False:
        poco.swipe([0.826, 0.217],[0.432, 0.217],duration=1.0)
    #--点击“合唱”入口--#
    poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name",text="合唱").click()
    #--等待页面元素加载--#
    waitting(resource_id="com.starmakerinteractive.starmaker:id/img_recording_cover")
    assert_equal(poco(text="合唱").exists(),True,"合唱页面跳转成功")
    #--获取推荐页面点击合唱作品名称--#
    recommendduetname1 = poco("com.starmakerinteractive.starmaker:id/txt_song_name")[1].get_text()  
    print(recommendduetname1)
    #--点击进入第一首作品详情页--#
    poco("com.starmakerinteractive.starmaker:id/txt_song_name")[1].click()
    #--等待作品详情页展示成功--#
    waitting("com.starmakerinteractive.starmaker:id/img_sing")
    #--点击底部加入合唱按钮--#
    poco("com.starmakerinteractive.starmaker:id/img_sing").click()
    #--调用通用方法--录制页获取权限弹窗--#
    System_permissions()
    #--调用通用方法--录制完成发布--#
    solo_publish()
    #--发布页面滑动查找榜单排名，防止广告位出现多滑动一次--#
    while poco("com.starmakerinteractive.starmaker:id/tv_share_rank_button_new",text = "查看排名").exists() == False:
        poco.swipe([0.47, 0.855],[0.47, 0.528],duration=1.0)
    #--获取榜单排名位置歌曲名称--#
    recommendduetname2 = poco("com.starmakerinteractive.starmaker:id/layout_party_recommend_music_name").get_text()
    print(recommendduetname2)
    assert_equal(recommendduetname1, recommendduetname2, "合唱跳转成功.")
    #--点击关闭发布页面--#
    poco("com.starmakerinteractive.starmaker:id/iv_close").click()
#     #--判断是否存在授权联系人弹窗--#
#     if poco("com.starmakerinteractive.starmaker:id/tv_tip").exists():
#         poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_negative").click()
#     else:
#         pass
    #--跳转至sing页面--#
    shell("am start sm://vocal_enter")
    #--点击“合唱”入口--#
    poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name")[3].click()
    #--点击切换至热门tab--#
    poco("com.starmakerinteractive.starmaker:id/tv_tab_title")[2].click()
    #--等待热门页面数据加载完成--#
    waitting("com.starmakerinteractive.starmaker:id/img_recording_cover")
    #--返回至sing页面--#
    poco("com.starmakerinteractive.starmaker:id/imb_backward").click()

       
##########歌手入口功能验证###########    
def sing_artist():
    #--滑动查找“歌手”入口--#
    while poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name",text="歌手").exists() == False:
        poco.swipe([0.826, 0.217],[0.432, 0.217],duration=1.0)
    #--点击“歌手”入口--#
    poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name",text="歌手").click()
    #--等待页面元素加载--#
    waitting(resource_id="com.starmakerinteractive.starmaker:id/iv_avatar")
    assert_equal(poco(text="歌手").exists(),True,"歌手页面跳转成功")
    #--点击Foreign singers进入Foreign singers页面--#
    poco(text = "Foreign singers").click()
    #--获取第一个歌手的歌手名称--#
    hotsongername1 = poco(resourceId="com.starmakerinteractive.starmaker:id/tv_name")[0].get_text()
    print(hotsongername1)
    #--点击第一个歌手头像进入歌手详情页--#
    poco(resourceId="com.starmakerinteractive.starmaker:id/iv_avatar")[0].click()
    #--等待歌手详情页数据加载完成-#
    waitting("com.starmakerinteractive.starmaker:id/common_song_item_head")
    #--获取歌手详情页歌手名称--#
    hotsongername2 = poco("com.starmakerinteractive.starmaker:id/title_tv").get_text()
    print(hotsongername2)
    assert_equal(hotsongername1, hotsongername2, "歌手详情页跳转成功.")
    #--点击第四首歌曲的演唱按钮--#
    poco(resourceId = "com.starmakerinteractive.starmaker:id/common_song_item_tv")[3].click()
    #--调用通用方法--录制页面点击我知道了，立刻关闭录制页面--#
    iknow_start_back()
    #--点击返回至歌手页面--#
    poco("com.starmakerinteractive.starmaker:id/back_iv").click()
    #--点击返回至sing页面--#
    poco("com.starmakerinteractive.starmaker:id/back_iv").click()
    poco("com.starmakerinteractive.starmaker:id/back_iv").click()
    
    
##########歌手入口功能验证###########      
def sing_selection():
    #--滑动查找“专题”入口--#
    while poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name",text="专题").exists() == False:
        poco.swipe([0.826, 0.217],[0.432, 0.217],duration=1.0)
    #--点击“专题”入口--#
    poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name",text="专题").click()
    #--等待页面元素加载--#
    waitting(resource_id="com.starmakerinteractive.starmaker:id/iv_avatar")
    assert_equal(poco(text="专题").exists(),True,"专题页面跳转成功")
    #--点击第一个专题入口进入第一个专题页面--#
    poco("com.starmakerinteractive.starmaker:id/tv_name")[0].click()
    #--等待页面元素加载完成--#
    waitting("com.starmakerinteractive.starmaker:id/common_song_item_head")
    #--点击第一首作品进入作品详情页--#
    poco("com.starmakerinteractive.starmaker:id/common_song_item_head")[0].click()
    #--等待页面元素加载完成--#
    waitting("com.starmakerinteractive.starmaker:id/atv_title_oncover_activity_sing_song_detail_new")
    #--点击返回专题详情页--#
    poco("com.starmakerinteractive.starmaker:id/iv_back_activity_sing_song_detail_new").click()
    #--点击第一首作品的演唱按钮进入录制页面--#
    poco(resourceId = "com.starmakerinteractive.starmaker:id/common_song_item_tv")[0].click()
    #--调用通用方法--录制页面点击我知道了，立刻关闭录制页面--#
    iknow_start_back()
    #--点击返回专题主页--#
    poco("com.starmakerinteractive.starmaker:id/back_iv").click()
    #--等待页面元素加载--#
    waitting(resource_id="com.starmakerinteractive.starmaker:id/iv_avatar")
    #--滑动查找“励志”专题--#
    while poco("com.starmakerinteractive.starmaker:id/tv_name",text="高兴").exists() == False:
        poco.swipe([0.525, 0.824],[0.525, 0.196],duration=1.0)
        poco.swipe([0.886, 0.865], [0.189, 0.865],duration=1.0)
        if poco("com.starmakerinteractive.starmaker:id/tv_name",text = "励志").exists():
            break;
    #--点击进入“励志”专题页面--#
    poco("com.starmakerinteractive.starmaker:id/tv_name",text = "励志").click()
    assert_equal(poco("com.starmakerinteractive.starmaker:id/title_tv").get_text(), "励志", "专题跳转成功.")
    #--返回至sing页面--#
    poco("com.starmakerinteractive.starmaker:id/back_iv").click()
    poco("com.starmakerinteractive.starmaker:id/back_iv").click()
    
    
##########排行榜入口功能验证###########      
def sing_list():
    #--滑动查找“排行榜”入口--#
    while poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name",text="排行榜").exists() == False:
        poco.swipe([0.826, 0.217],[0.432, 0.217],duration=1.0)
    #--点击“排行榜”入口--#
    poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name",text="排行榜").click()
    #--等待页面元素加载--#
    waitting(resource_id="com.starmakerinteractive.starmaker:id/img_cover")
    assert_equal(poco(text="List").exists(),True,"排行榜页面跳转成功")
    #--点击切换至“趋势”tab下--#
    poco("com.starmakerinteractive.starmaker:id/tv_tab_title",text = "趋势").click()
    #--等待页面元素加载完成--#
    waitting(resource_id="com.starmakerinteractive.starmaker:id/txt_title")
    #--点击第一首作品进入作品详情页--#
    poco("com.starmakerinteractive.starmaker:id/txt_title")[0].click()
    #--等待页面元素加载完成--#
    waitting(resource_id="com.starmakerinteractive.starmaker:id/atv_title_oncover_activity_sing_song_detail_new")
    #--点击返回至排行榜主页--#
    poco("com.starmakerinteractive.starmaker:id/iv_back_activity_sing_song_detail_new").click()
    #--点击切换至“新”tab下--#
    poco("com.starmakerinteractive.starmaker:id/tv_tab_title",text = "新").click()
    #--等待页面元素加载完成--#
    waitting(resource_id="com.starmakerinteractive.starmaker:id/txt_title")
    #--点击第一首作品的演唱按钮进入录制页面--#
    poco("com.starmakerinteractive.starmaker:id/btn_sing")[0].click()
    #--调用通用方法--录制页面点击我知道了，立刻关闭录制页面--#
    iknow_start_back()
    #--点击返回至sing页面--#
    keyevent("back")

    
##########派对入口功能验证###########      
def sing_party():
    #--判断当前页面是否存在“派对入口”--#
    while poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name",text="直播").exists() == False:
        poco.swipe([0.826, 0.217],[0.432, 0.217],duration=1.0)
    #--点击“派对”入口--#
    poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name",text="派对").click()
    #--判断是否存在语言偏好弹窗--#
    if poco(text="选择你的偏好语言，这将帮助我们提升你的浏览体验。我们将根据它推荐适合的内容给你，并过滤掉你不喜欢的内容").exists():
        poco.click([0.49, 0.136])
    else:
        pass
    assert_equal(poco("com.starmakerinteractive.starmaker:id/room_bg").exists(),True,"歌房页面跳转成功")
    #--返回至sing页面--#
    shell("am start sm://vocal_enter")

    
##########直播入口功能验证###########     
def sing_live():
    #--判断当前页面是否存在“直播入口”--#
    while poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name",text="直播").exists() == False:
        poco.swipe([0.826, 0.217],[0.432, 0.217],duration=1.0)
    #--点击“直播”入口--#
    poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name",text="直播").click()
    #--判断是否存在签到弹窗--#
    if poco("com.starmakerinteractive.starmaker:id/tv_current_day_count_down").exists():
        poco("com.starmakerinteractive.starmaker:id/tv_check").click()
        #--判断今日是否领取奖励--#
        if poco("com.starmakerinteractive.starmaker:id/tv_header").exists():
            poco("com.starmakerinteractive.starmaker:id/iv_close").click()
        else:
            poco.click([0.482, 0.164])
    else:
        pass
    assert_equal(poco("com.starmakerinteractive.starmaker:id/ic_live_start_live").exists(),True,"直播页面跳转成功")
    #--返回至sing页面--#
    poco("com.starmakerinteractive.starmaker:id/back_iv").click()

    
##########清唱入口功能验证###########    
def sing_freestyle():  
    #--判断当前页面是否存在“清唱入口”--#
    while poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name",text="清唱").exists() == False:
        poco.swipe([0.826, 0.217],[0.432, 0.217],duration=1.0)
    #--点击“清唱”入口--#
    poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name",text="清唱").click()
    #--等待页面元素加载--#
    waitting(resource_id="com.starmakerinteractive.starmaker:id/img_recording_cover")
    assert_equal(poco(text="Free Style!").exists(),True,"清唱页面跳转成功")
    #--点击切换至短视频tab--#
    poco("com.starmakerinteractive.starmaker:id/tv_tab_title",text = "短视频").click()
    #--等待页面元素加载--#
    waitting(resource_id="com.starmakerinteractive.starmaker:id/tv_sing_start")
    #--点击底部短视频拍摄按钮--#
    poco("com.starmakerinteractive.starmaker:id/tv_sing_start").click()
    #--调用通用方法-系统权限获取--#
    System_permissions()
    #--等待选择音乐页面加载完成--#
    waitting(resource_id="com.starmakerinteractive.starmaker:id/iv_song_cover")
    #--点击第一首音乐--#
    poco("com.starmakerinteractive.starmaker:id/iv_song_cover")[0].click()
    #--等待第一首音乐下载完成出现“使用 & 拍摄”按钮--#
    waitting(resource_id="com.starmakerinteractive.starmaker:id/tv_sing")
    #--点击“使用 & 拍摄”按钮--#
    poco("com.starmakerinteractive.starmaker:id/tv_sing").click()
    #--等待进入“声音剪辑”页面--#
    waitting(resource_id="com.starmakerinteractive.starmaker:id/tv_button_next")
    #--点击下一步按钮--#
    poco("com.starmakerinteractive.starmaker:id/tv_button_next").click()
    #--等待进入小视频录制页面--#
    waitting(resource_id="com.starmakerinteractive.starmaker:id/iv_camera_switchover_capturelib_fragment_capture")
    #--点击摄像头切换按钮，切换为后置摄像头--#
    poco("com.starmakerinteractive.starmaker:id/iv_camera_switchover_capturelib_fragment_capture").click()
    assert_equal(poco("com.starmakerinteractive.starmaker:id/iv_props_capturelib_fragment_capture").exists(),True,"跳转小视频录制页面成功")
    #--点击拍摄按钮进行录制--#
    poco("com.starmakerinteractive.starmaker:id/rbtn_record_capturelib_fragment_capture").click()
    #--等待进入小视频发布页面--#
    sleep(10.0)
    #--输入作品描述--#
    poco("com.starmakerinteractive.starmaker:id/ret_post_desc").click()
    text("小视频保存本地草稿验证",enter=False)
    poco("com.starmakerinteractive.starmaker:id/tv_done").click()
    #--点击保存本地按钮--#
    poco("com.starmakerinteractive.starmaker:id/img_post_tools_save").click()
    #--切换至个人主页--#
    shell("am start sm://me")
    #--进入“本地录音”查看小视频是否保存--#
    waitting(text="本地录音")
    poco(text="本地录音").click()
    assert_equal(poco(text="小视频保存本地草稿验证").exists(),True,"小视频保存本地草稿验证成功")
    #--全选删除本地草稿--#
    poco("com.starmakerinteractive.starmaker:id/iv_edit").click()
    poco("com.starmakerinteractive.starmaker:id/tv_select_all").click()
    poco("com.starmakerinteractive.starmaker:id/tv_delete").click()
    poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_positive").click()
    #--切换至sing页面--#
    shell("am start sm://vocal_enter")

    
##########家族入口功能验证###########      
def sing_family(): 
    #--判断当前页面是否存在“家族入口”--#
    while poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name",text="家族").exists() == False:
        poco.swipe([0.826, 0.217],[0.432, 0.217],duration=1.0)
    #--点击“家族”入口--#
    poco("com.starmakerinteractive.starmaker:id/tv_sing_label_name",text="家族").click()
    assert_equal(poco("com.starmakerinteractive.starmaker:id/publish_icon").exists(),True,"家族页面跳转成功")
    #--判断是否存在评价弹窗--#
    if poco("com.starmakerinteractive.starmaker:id/rating_dialog_reason").exists():
        poco("com.starmakerinteractive.starmaker:id/rating_dialog_close").click()
    else:
        pass
    #--判断是否存在授权联系人弹窗--#
    if poco("com.starmakerinteractive.starmaker:id/tv_tip").exists():
        poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_negative").click()
    else:
        pass
    #--切换至sing页面--#
    shell("am start sm://vocal_enter")


##########foryou tab 功能验证###########    
def sing_foryou():   
    #--判断当前页面是否存在合唱入口--#
    if poco("com.starmakerinteractive.starmaker:id/tv_song_desc_chorus").exists():
        poco("com.starmakerinteractive.starmaker:id/tv_song_desc_chorus")[0].click()
        waitting(resource_id="com.starmakerinteractive.starmaker:id/img_recording_cover")
        assert_equal(poco("com.starmakerinteractive.starmaker:id/text_join").exists(),True,"合唱入口跳转成功")
        poco("com.starmakerinteractive.starmaker:id/navigation_btn").click()
    else:
        print("for you本次无合唱入口")
    #--点击歌曲封面的播放按钮，查看是否能够调出播放小窗--#    
    poco("com.starmakerinteractive.starmaker:id/iv_play_state")[0].click()
    assert_equal(poco("com.starmakerinteractive.starmaker:id/float_more").exists(),True,"播放按钮调出小窗成功")
    #--判断当前页面banner入口是否可以点击跳转--#
    if poco("com.starmakerinteractive.starmaker:id/layout_banner").exists():
        poco("com.starmakerinteractive.starmaker:id/layout_banner").click()
        keyevent("back")
    else:
        print("for you本次无banner入口")
    #--点击切换至热门tab--#
    poco("com.starmakerinteractive.starmaker:id/tv_tab_title",text="热门").click()   
    #--等待热门页面数据加载完成--#
    waitting(resource_id="com.starmakerinteractive.starmaker:id/img_cover")
    #--获取第一首作品的歌手名称--#   
    hotsongname1 = poco("com.starmakerinteractive.starmaker:id/txt_artist")[0].get_text()
    print(hotsongname1)
    #--点击第一首作品进入作品详情页--#
    poco("com.starmakerinteractive.starmaker:id/txt_artist")[0].click()
    #--获取第一首作品的歌手名称--# 
    hotsongname2 = poco("com.starmakerinteractive.starmaker:id/tv_singer_name_oncover_activity_sing_song_detail_new").get_text()
    print(hotsongname2)
    assert_equal(hotsongname2, hotsongname1, "热门页面跳转歌曲详情页成功.")
    #--点击返回至热门页面--# 
    poco("com.starmakerinteractive.starmaker:id/iv_back_activity_sing_song_detail_new").click()
    #--点击第一首作品的演唱按钮进入录制页面--# 
    poco("com.starmakerinteractive.starmaker:id/btn_sing")[0].click()
    #--点击我知道了关闭耳机提醒弹窗--# 
    poco("com.starmakerinteractive.starmaker:id/recording_headset_dialog_i_know_btn").click()
    while not exists(Template(r"tpl1684493667928.png", record_pos=(0.001, 0.789), resolution=(1440, 3120))): #等待歌曲下载完成           
            sleep(1.0)
    #--点击开始录制,滑动快进歌词--#         
    poco("com.starmakerinteractive.starmaker:id/rbtn_record_recorder_song_fragment_song_record").click()
    poco.swipe([0.503, 0.727],[0.503, 0.013],duration=1.0)
    #############判断完成按钮是否可以点击############### 
    #--点击完成按钮--# 
    poco("com.starmakerinteractive.starmaker:id/iv_done_recorder_song_fragment_song_record").click()   
    #--判断当前是否出现结束录制的二次确认弹窗，没有出现则等待两秒后继续点击--# 
    while not poco("com.starmakerinteractive.starmaker:id/common_dialog_content",text = "录音还未完成，你确定要现在结束录音吗？").exists():
        poco("com.starmakerinteractive.starmaker:id/iv_done_recorder_song_fragment_song_record").click()
        sleep(2.0)
    #--出现二次确认弹窗后点击取消，继续录制--#     
    poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_negative").click()        
    #--点击完成按钮--# 
    poco("com.starmakerinteractive.starmaker:id/iv_done_recorder_song_fragment_song_record").click()
    #--等待二次确认弹窗出现--# 
    waitting(resource_id="com.starmakerinteractive.starmaker:id/common_dialog_content",text = "录音还未完成，你确定要现在结束录音吗？")
    #--出现二次确认弹窗后点击确认，完成录制--#   
    poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_positive").click()
    #--等待发布预览页加载完成--#  
    poco("com.starmakerinteractive.starmaker:id/tv_next_baserecord_fragment_edit_btn").wait_for_appearance(120)
    #--点击切换至“作品”tab--#  
    poco(text = "作品").click()
    #--点击使用第一个模板--#
    poco("com.starmakerinteractive.starmaker:id/iv_effect_item_effect_tray")[1].click()
    #--滑动查找输入框--#
    poco.swipe([0.52, 0.845],[0.52, 0.548],duration=1.0)
    #--点击输入框后输入当前时间，关闭输入框--#
    poco("com.starmakerinteractive.starmaker:id/ret_input_baserecord_fragment_editor").click()
    text(poco("com.android.systemui:id/clock").get_text())
    keyevent("back")
    keyevent("back")
    #--获取输入框中的输入内容--#
    script = poco("com.android.systemui:id/clock").get_text()
    print(script)
    #--判断是否存在分享第三方入口，如果存在双击取消选择分享方式--#
    if poco("com.starmakerinteractive.starmaker:id/share_desc").exists():
        poco("com.starmakerinteractive.starmaker:id/share_entrance_iv2").click()
        poco("com.starmakerinteractive.starmaker:id/share_entrance_iv2").click()
    #关闭合唱入口
    poco('com.starmakerinteractive.starmaker:id/ll_duet_baserecord_fragment_edit').click()
    #点击不允许加入
    poco('com.starmakerinteractive.starmaker:id/choice_no_allow_duet_check').click()
    poco('com.starmakerinteractive.starmaker:id/choice_ok').click()
    #--点击保存本地按钮--#
    touch(Template(r"tpl1684923496565.png", record_pos=(-0.169, 0.956), resolution=(1440, 3120)))
    #--断言是否保存本地成功--#
    assert_equal(poco("com.starmakerinteractive.starmaker:id/tv_save_tip").exists(),True,"发布作品保存本地成功")
    #--点击立即发布--#
    poco(text = "立即发布").click()
    #--等待作品发布成功--#
    waitting(resource_id="com.starmakerinteractive.starmaker:id/txt_upload_success_new",text = "上传成功，设置为来电铃声～",time=240)
    #--滑动查找作品榜单--#
    while poco("com.starmakerinteractive.starmaker:id/tv_share_rank_button_new",text = "查看排名").exists() == False:
        poco.swipe([0.47, 0.855],[0.47, 0.528],duration=1.0)
    #--在榜单中获取发布作品的歌手名称--#
    poco("com.starmakerinteractive.starmaker:id/tv_share_rank_button_new",text = "查看排名").click()
    waitting(resource_id="com.starmakerinteractive.starmaker:id/img_recording_cover")
    public_songname = poco("com.starmakerinteractive.starmaker:id/atv_title_oncover_activity_sing_song_detail_new").get_text()
    print(public_songname)
    #--点击关闭当前页面--#
    poco("com.starmakerinteractive.starmaker:id/iv_back_activity_sing_song_detail_new").click()
    #--点击关闭发布页面，进入动态--已关注页面--#
    poco("com.starmakerinteractive.starmaker:id/iv_close").click()
    sleep(2.0)
    #--判断当前页面是否存在评价弹窗--#
    if poco("com.starmakerinteractive.starmaker:id/rating_dialog_reason").exists():   #评价弹窗关闭
        poco("com.starmakerinteractive.starmaker:id/rating_dialog_close").click()
    else:
        pass
    #--判断是否存在授权联系人弹窗--#
    if poco("com.starmakerinteractive.starmaker:id/tv_tip").exists():
        poco("com.starmakerinteractive.starmaker:id/common_dialog_btn_negative").click()
    else:
        pass
    #--等待页面数据加载完成--#
    waitting(resource_id="com.starmakerinteractive.starmaker:id/iv_cover")
    #--下拉刷新--#
    poco.swipe([0.473, 0.193],[0.47, 0.377],duration=1.0)
    sleep(3.0)
    #--点击第一首作品查看是否是刚刚发布的作品--#
    poco("com.starmakerinteractive.starmaker:id/iv_cover")[0].click()
    #--等待作品详情页数据加载完成--#
    waitting(resource_id="com.starmakerinteractive.starmaker:id/tv_tweet_use_time")
    assert_equal(poco("com.starmakerinteractive.starmaker:id/tv_tweet_use_time").get_text(), public_songname, "foryou发布作品成功.")
    assert_equal(poco("com.starmakerinteractive.starmaker:id/htv_desc").get_text().split('\n')[0], script, "foryou作品描述正确.")
    #--切换至sing页面--#
    shell("am start sm://vocal_enter")
    assert_equal(poco("com.starmakerinteractive.starmaker:id/tv_tab_title").exists(),True,"唱歌-foryou用例执行成功")

    
##########明星入口功能验证###########
def sing_Celebrity():
    #--滑动查找“明星”入口--#
#     while poco("com.starmakerinteractive.starmaker:id/tv_tab_title",text="明星").exists() == False:
#         poco.swipe([0.642, 0.128],[0.271, 0.125],duration=1.0)
    poco.swipe([0.642, 0.128],[0.271, 0.125],duration=1.0)
    #--点击“明星”入口--#
    poco("com.starmakerinteractive.starmaker:id/tv_tab_title",text="明星").click()
    #--获取banner中的歌曲名称--#
    Celebritysongname1=poco("com.starmakerinteractive.starmaker:id/tv_top").get_text()
    print(Celebritysongname1)
    #--点击banner进入作品详情页--#
    poco("com.starmakerinteractive.starmaker:id/iv_background").click()
    waitting(resource_id="com.starmakerinteractive.starmaker:id/tv_music_collab_num")
    #--获取详情页中的歌曲名称--#
    Celebritysongname2=poco("com.starmakerinteractive.starmaker:id/tv_music_collab_num").get_text()
    print(Celebritysongname2)
    assert_equal(Celebritysongname1, Celebritysongname2, "banner入口跳转成功.")
    #--返回至明星页面--#
    poco("com.starmakerinteractive.starmaker:id/imb_back").click()
    #--点击录制按钮进入录制页面--#
    poco("com.starmakerinteractive.starmaker:id/btn_sing").click()
    #--调用通用方法--录制页面点击我知道了，立刻关闭录制页面--#
    iknow_start_back()
    #--滑动查找“明星合唱”入口--#
    while poco("com.starmakerinteractive.starmaker:id/img_recording_cover").exists() == False:
        poco.swipe([0.766, 0.377],[0.137, 0.377],duration=1.0)
    assert_equal(poco(text="明星合唱").exists(), True, "明星合唱页面跳转成功.")
    #--返回至明星页面--#
    poco("com.starmakerinteractive.starmaker:id/back_iv").click()
    #--点击Starmaker达人入口--#
    poco("com.starmakerinteractive.starmaker:id/tv_label_talents").click()
    assert_equal(poco(text="StarMaker达人").exists(), True, "达人页面跳转成功.")
    #--返回至明星页面--#
    keyevent("back")
    #--滑动查找“新歌日历”模块--#
    while poco("com.starmakerinteractive.starmaker:id/rl_background").exists() == False:
        poco.swipe([0.48, 0.804],[0.48, 0.35],duration=1.0)
    #--获取第一首新歌的歌曲名称--#    
    Celebritysongname1=poco("com.starmakerinteractive.starmaker:id/tv_song_name")[0].get_text()
    print(Celebritysongname1)
    #--点击进入歌曲详情页--#
    poco("com.starmakerinteractive.starmaker:id/tv_song_name")[0].click()
    waitting(resource_id="com.starmakerinteractive.starmaker:id/atv_title_oncover_activity_sing_song_detail_new")
    #--获取歌曲详情页的歌曲名称--#
    Celebritysongname2=poco("com.starmakerinteractive.starmaker:id/atv_title_oncover_activity_sing_song_detail_new")[0].get_text()
    print(Celebritysongname2)
    assert_equal(Celebritysongname1, Celebritysongname2, "新歌页面跳转成功.")
    #--点击返回明星页面--#
    poco("com.starmakerinteractive.starmaker:id/iv_back_activity_sing_song_detail_new").click()