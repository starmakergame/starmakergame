poco('com.starmakerinteractive.starmaker:id/switcher').click()#进入搜索
poco('com.starmakerinteractive.starmaker:id/searchView').click()#点击搜索
text("一路向北",search=True)#输入搜索
poco('com.starmakerinteractive.starmaker:id/rings_tv_rings_name')[3].click()#播放音乐
sleep(5)
poco('com.starmakerinteractive.starmaker:id/btn_add')[3].click() #铃声设置
while poco('com.starmakerinteractive.starmaker:id/lrc_view').exists() is False:
    time.sleep(0.5)                
if poco(text='支持设置来电铃声啦').exists():#判断首次弹窗是否存在
    poco(text='我知道了').click()
    log(aaa)
    
swipe()
touch(duration=0.3,)
sleep(6)#声音剪辑页播放6秒