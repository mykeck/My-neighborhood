from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    url(r'^$',views.register,name ='register'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^$',views.index,name='Index'),
    url(r'^notifications',views.notification, name='notifications'),
    url(r'^blog',views.blog, name='blog'),
    url(r'^health',views.health, name='health'),
    url(r'^authorities',views.authorities, name='authorities'),
    url(r'^businesses',views.businesses, name='businesses'),
    
    # url(r'^view/blog/(\d+)',views.view_blog,name='view_blog'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)