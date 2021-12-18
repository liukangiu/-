import time
import schedule
#import healthreport
from jinchengxianshi import xianshi
from xiaoxi import sendGL
import caozuojson
import caozuo
from huoquip import get_host_ip
name,password=caozuojson.readjson('liukang')
caozuo.caozuo(name,password)