# coding = utf-8
import os
# ---------------------------------基础类型设置-------------------------------------------
deviceType = "app"                                                             # 设备类别：app、win和web
devices = ['R58N51LLHSV']                            		# 设备信息，只有当deviceType为app是有效，decices 在Airtest运行过程中可以在控制台看到
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))         # 工程根目录
air_path = os.path.join(root_path, 'air')                                        # 脚本目录（由根目录和air拼接：root/air）
log_path = os.path.join(root_path, 'log')                                         # 日志目录
data_path = os.path.join(root_path, 'data')                                     # 测试数据目录
#需要用户名，密码
username= "youxi1@126.com"
password="521xiaoyuH"
#需要平台和包名
system="Android","iOS"
#需要语言和大区
Language="chinses"
area="india"
#需要屏幕尺寸
#size=""
#deeplink表