# -*- encoding=utf8 -*-
__author__ = "han'yuan'lin"

from airtest.core.api import *

auto_setup(__file__)


using("moment_publisher.air")
from moment_publisher import *

recommend_topic()
recommend_following()
recommend_publish()