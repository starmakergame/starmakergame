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
touch(Template(r"tpl1681202995628.png", record_pos=(-0.013, -0.725), resolution=(1080, 2400)))
sleep(2.0)
touch(97,1130)
sleep(1.0)
touch(Template(r"tpl1681203279140.png", record_pos=(-0.339, 0.641), resolution=(1080, 2400)))
sleep(1.0)
# 断言合唱房关闭麦位成功
assert_exists(Template(r"tpl1681203397957.png", record_pos=(-0.009, -0.058), resolution=(1080, 2400)), "合唱房第一个麦位被锁")

