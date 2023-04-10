# -*- encoding=utf8 -*-
__author__ = "DingShuang"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1681116125318.png", record_pos=(-0.349, -0.12), resolution=(1080, 2400)))

wait(Template(r"tpl1681116663505.png", record_pos=(-0.001, 0.914), resolution=(1080, 2400)))
touch(Template(r"tpl1681116671175.png", record_pos=(-0.007, 0.912), resolution=(1080, 2400)))
touch(Template(r"tpl1681116932631.png", record_pos=(-0.375, -0.474), resolution=(1080, 2400)))
wait(Template(r"tpl1681116960287.png", record_pos=(0.0, 0.714), resolution=(1080, 2400)))
touch(Template(r"tpl1681116971734.png", record_pos=(-0.391, 0.516), resolution=(1080, 2400)))
if exists(Template(r"tpl1681117297337.png", record_pos=(-0.014, -0.352), resolution=(1080, 2400))):
    log('上麦成功')








