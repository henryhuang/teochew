from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# rom django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teochew.views.home', name='home'),
    # url(r'^teochew/', include('teochew.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    
)

urlpatterns += patterns((''),
    (r'^weixin/', include('weixin.urls')),
)
