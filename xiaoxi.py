#import _thread
import time
#from flask import Flask,request
from json import loads
import requests
import os
import websocket
import schedule
#from websocket import create_connection
import json
# 为线程定义一个函数

def send(content,qunqq):
    api_url = 'http://127.0.0.1:5700/send_msg'#酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    data = {'msg_type': 'group','group_id':qunqq,'message':content}
    requests.post(api_url,data=data)
    print('成功给群发送消息')

def sendGL(content,GLQQ):
    data = {'user_id':GLQQ,'message':content,'auto_escape':False}
    api_url = 'http://127.0.0.1:5700/send_private_msg'
    requests.post(api_url,data=data)
    print('成功给管理员发消息')
#sendGL('123',2084222530)