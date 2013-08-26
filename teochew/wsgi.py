# -*- coding: utf-8 -*-
import sae
import os
import sys
import urllib2
import json

apiKey = '8GdDUCk2oasGUNBdzjKzoBGA'

def getBaiduTranslate(content):
        
    url = 'http://openapi.baidu.com/public/2.0/bmt/translate?client_id=' + apiKey + '&q=' + content + '&from=auto&to=auto'
    transResult = urllib2.urlopen(url).read()
    jsonStr = json.loads(transResult)
    str = jsonStr['trans_result'][0]['dst']
    return str

'''
def app(environ, start_response):
    """也许是最简单的应用程序对象"""
    status = '200 OK'
    response_headers = [('Content-type','text/html; charset=UTF-8')]
    start_response(status, response_headers)
    
    str = getBaiduTranslate('I love Shantou')
    
    return [str.encode('utf-8')]

'''

def app(environ, start_response):
    
    request = Request(environ)
    
    

    return ['']