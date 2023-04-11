# -*- encoding=utf8 -*-
__author__ = "DingShuang"

from airtest.core.api import *

auto_setup(__file__)

# 进入房间编辑页面

touch(Template(r"tpl1681197752403.png", record_pos=(-0.344, -0.114), resolution=(1080, 2400)))
sleep(1.0)
touch(Template(r"tpl1681198258381.png", record_pos=(-0.032, 0.911), resolution=(1080, 2400)))
sleep(1.0)
touch(Template(r"tpl1681198382735.png", record_pos=(-0.435, -0.965), resolution=(1080, 2400)))
sleep(1.0)
touch(Template(r"tpl1681198404975.png", record_pos=(0.001, 0.908), resolution=(1080, 2400)))
sleep(1.0)




#  验证设置地区权限
touch(Template(r"tpl1681198452505.png", record_pos=(-0.344, 0.695), resolution=(1080, 2400)))
sleep(1)
touch(Template(r"tpl1681198467177.png", record_pos=(-0.338, 0.765), resolution=(1080, 2400)))
sleep(1.0)
if exists(Template(r"tpl1681198483739.png", record_pos=(-0.009, 0.684), resolution=(1080, 2400))):
    log('仅本地区用户进房设置成功')
    
# 验证设置家族权限
touch(Template(r"tpl1681198494734.png", record_pos=(-0.365, 0.696), resolution=(1080, 2400)))
sleep(1.0)
touch(Template(r"tpl1681198567596.png", record_pos=(-0.358, 0.639), resolution=(1080, 2400)))
sleep(1.0)
if exists(touch(Template(r"tpl1681198582933.png", record_pos=(-0.006, 0.698), resolution=(1080, 2400)))
):
    log('仅家族成员用户进房设置成功')
    
# 验证设置任意用户可进房
touch(Template(r"tpl1681198613053.png", record_pos=(-0.361, 0.69), resolution=(1080, 2400)))
sleep(1.0)
touch(Template(r"tpl1681198626084.png", record_pos=(-0.376, 0.385), resolution=(1080, 2400)))
sleep(1.0)
if exists(Template(r"tpl1681198644289.png", record_pos=(-0.001, 0.688), resolution=(1080, 2400))):
    log('任意用户可进房设置成功')
    
# 验证设置房主关注的人可进房
touch(Template(r"tpl1681198731240.png", record_pos=(-0.355, 0.693), resolution=(1080, 2400)))
sleep(1.0)
touch(Template(r"tpl1681198745700.png", record_pos=(-0.335, 0.516), resolution=(1080, 2400)))
sleep(1.0)
if exists(Template(r"tpl1681198760439.png", record_pos=(-0.01, 0.698), resolution=(1080, 2400))):
    log('房主关注的人可进房设置成功')



