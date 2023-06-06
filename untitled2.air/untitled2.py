# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
[0.182, 0.131]

auto_setup(__file__)

# using("login.air")
# import login.air
using("untitled3.air")#引用untitled3.air这个项目，这里我把2个项目放在一个根目录下，可以直接引用，如果不是在同一个根目录下，则需要去使用路径引用
from untitled3 import *#这里使用*时因为，我调用了untitled3中的全部函数，所以使用了*，如果只调用quick_game（），那么这里只需要写quick_game就可以了
quick_game()#这里就是调用函数，值得说一句的就是，函数调用在这里，那么在untitled2中，不需要调用函数，否则，这里你看到的效果就是执行了2遍quick_game
aaa()