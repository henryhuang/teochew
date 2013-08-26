from django.conf.urls.defaults import *

urlpatterns = patterns(('weixin.views'),
    url(r'^api', 'weixin_api', name = 'weixin_api'),
)