import time
import schedule
#import healthreport
from jinchengxianshi import xianshi
from xiaoxi import sendGL
import caozuojson
import caozuo
from huoquip import get_host_ip
ipname='192.168.0.1'
def jianceip():
    global ipname
    newip=get_host_ip()
    if newip!=ipname:
        ipname=newip
        sendGL(newip,2084222530)
        print(newip)
def daka():
    name,password=caozuojson.readjson('liukang')
    caozuo.caozuo(name,password)
cishu=0
def xianshi2():
    global cishu
    xianshi(cishu)
    cishu+=1
    cishu=cishu%11
if __name__ == "__main__":
    #healthreport.daka()
    #信息填写区
    print('start')
    sendGL('start',2084222530)
    schedule.every().second.do(xianshi2)
    #schedule.every().minute.do(jianceip)
    schedule.every().day.at('09:00').do(daka)
    while(1):
        schedule.run_pending()
        time.sleep(1)