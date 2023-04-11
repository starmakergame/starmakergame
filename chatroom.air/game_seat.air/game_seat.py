# -*- encoding=utf8 -*-
__author__ = "DingShuang"

from airtest.core.api import *

auto_setup(__file__)

# 进入房间
touch(Template(r"tpl1681200454996.png", record_pos=(-0.356, -0.109), resolution=(1080, 2400)))
sleep(1.0)
touch(Template(r"tpl1681200468168.png", record_pos=(-0.017, 0.913), resolution=(1080, 2400)))
sleep(1.0)
touch(579,165)
sleep(1.0)
touch(Template(r"tpl1681200536294.png", record_pos=(-0.322, -0.5), resolution=(1080, 2400)))
sleep(2.0)

# 验证上麦
touch(62,328)
sleep(1.0)
touch(Template(r"tpl1681200628767.png", record_pos=(-0.406, 0.519), resolution=(1080, 2400)))
touch(Template(r"tpl1681202639157.png", record_pos=(-0.004, 0.37), resolution=(1080, 2400)))
if exists(Template(r"tpl1681202656156.png", record_pos=(-0.424, -0.81), resolution=(1080, 2400))):
    log('游戏及房间上麦成功')

