from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView



urlpatterns=[
    url(r'^index',views.index,name='index'),
    url(r'^$',views.register,name ='register'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^notifications',views.notification, name='notifications'),
    url(r'^blog',views.blog, name='blog'),
    url(r'^health',views.health, name='health'),
    url(r'^authorities',views.authorities, name='authorities'),
    url(r'^businesses',views.businesses, name='businesses'),
    url(r'^my_profile/',views.my_profile, name='my_profile'),
    url(r'^view/blog/(\d+)',views.view_blog,name='view_blog'),
    url(r'^new/blogpost$',views.new_blogpost, name='new-blogpost'),
    url(r'^new/notification$',views.new_notification, name='new-notification'),
    url(r'^new/business$',views.new_business, name='new_business'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)