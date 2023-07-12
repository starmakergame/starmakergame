# -*- encoding=utf8 -*-
__author__ = "李洁"

from airtest.core.api import *

auto_setup(__file__)

using("profile_lijie.air")
from profile_lijie import * 

# PACKAGE = "com.starmakerinteractive.starmaker"
# stop_app(PACKAGE)
# start_app(PACKAGE,activity=None)

#登录APP
loginapp()
#家族卡片
profile_family()
# #个人页【首页】tab
profile_homepage_info()
profile_homepage_album()
profile_homepage_ktv()
profile_homepage_cover()
profile_homepage_playlist()
# #个人页动态tab
profile_moment()
# #个人页歌单tab
profile_playlist()
# #个人页作品tab
profile_cover()
# #个人页合唱tab
profile_duet()  
# #个人页小视频tab
profile_shortvideo()
#个人页发布器按钮
profile_productbtn()
