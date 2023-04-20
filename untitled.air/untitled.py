# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

print(G.DEVICE_LIST)
set_current("R58N51LLHSV")
sleep(10.0)

touch(Template(r"tpl1681959240472.png", record_pos=(-0.356, -0.122), resolution=(1080, 2400)))
sleep(5.0)
touch(Template(r"tpl1681959256236.png", record_pos=(0.003, 0.914), resolution=(1080, 2400)))


sleep(5.0)

set_current("ad3b6d97")
sleep(10.0)
touch(Template(r"tpl1681959385678.png", record_pos=(-0.069, -0.058), resolution=(720, 1600)))
