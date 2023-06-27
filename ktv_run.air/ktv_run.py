# -*- encoding=utf8 -*-
__author__ = "DingShuang"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# screen_size = poco.get_screen_size()
# # print(screen_size)  # 列表[1080, 2400]
# wid = screen_size[0]
# leng = screen_size[1]
        
using("ktv.air")
from ktv import *

# grant_permission('com.starmakerinteractive.starmaker')

sing_now()
fast_game()
live_tab()
feed_tab()
more_tab()
join_ktv()
announcement_ktv()
share_ktv()
sing_ktv()
take_seat()

# invite_seat()
left_seat()
open_relation()
seat_setting_anyone()
seat_ktv()
join_ktv_setting()
game_take_seat()
close_seat()
exp()
setting_tag()
programme()