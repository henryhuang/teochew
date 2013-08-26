# -*- coding: utf-8 -*-
import os
import sys
import urllib2
import json

from xml.dom.minidom import Document

apiKey = '8GdDUCk2oasGUNBdzjKzoBGA'

def getBaiduTranslate(content):
        
    url = 'http://openapi.baidu.com/public/2.0/bmt/translate?client_id=' + apiKey + '&q=' + content + '&from=auto&to=auto'
    tranResult = urllib2.urlopen(url).read()

    str = jsonStr['trans_result'][0]['dst']
    return str

'''
if len(sys.argv) != 2:
    print '输入长度错误，翻译第一个参数'

content = sys.argv[1]
transResult = getBaiduTranslate(content)

print transResult

jsonStr = json.loads(transResult)

print 'source:' + jsonStr['from']
print 'target:' + jsonStr['to']

print 'src:' + jsonStr['trans_result'][0]['src']
print 'dst:' + jsonStr['trans_result'][0]['dst']

# 构造xml，这里直接使用构造字符串，不使用Document

xmlStr = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[%s]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"

print xmlStr % ('Henry', 'HuangYijie', '2013-08-25', 'text', '这是内容')
'''




