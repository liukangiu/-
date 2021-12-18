#coding=utf-8
import json
def readjson(xingming):
    message=open('loginmessage.json','r',encoding='utf-8')
    messagejson = json.load(message)
    message.close()
    return(messagejson[xingming]['name'],messagejson[xingming]['password'])
    
def writejson(xingming,name,password):
    message=open('loginmessage.json','r',encoding='utf-8')
    messagejson = json.load(message)
    message.close()
    messagejson[xingming]={}
    messagejson[xingming]['name']=name
    messagejson[xingming]['password']=password
    message1 = json.dumps(messagejson,ensure_ascii=False)
    message=open('loginmessage.json','w',encoding='utf-8')
    message.write(message1)
    message.close()
