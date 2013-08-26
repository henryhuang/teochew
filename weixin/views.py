# -*- coding: utf-8 -*-

import os
import hashlib
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

token = ''

def checkSignature(request):
    
    signature = request.GET['signature']
    timestamp = request.GET['timestamp']
    nonce = request.GET['nonce']
    
    str = ''.join(sorted([signature, timestamp, nonce]))
    
    str_sha1 = hashlib.sha1(str).hexdigest()
    
    if(str_sha1 == signature):
        return True;
    else :
        return False;

def weixin_api(request):
    
    token = 'huangyijieweixinjiekou'
    
    # 标识该请求来源于微信
    if (checkSignature(request) == False):
        return render_to_response("weixin_api.html", {"requestContent": '验证失败'})
        
    '''
    因为微信api调用使用get，所以就不进行判断了
    
    微信会带4个参数：
    signature     微信加密签名
    timestamp     时间戳
    nonce         随机数
    echostr       随机字符串
    '''
    signature = request.GET['signature']
    timestamp = request.GET['timestamp']
    nonce = request.GET['nonce']
    echostr = request.GET['echostr']
    
    return render_to_response("weixin_api.html", {"requestContent": 's: %s , t: %s, n: %s, e: %s' % (signature, timestamp, nonce, echostr)})