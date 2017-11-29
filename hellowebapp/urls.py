from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from collection import views

urlpatterns = [

    url(r'^$', views.index, name='home'),

    url(r'^1modules/$',
        TemplateView.as_view(template_name='1modules.html'),
        name='1modules'),

    url(r'^1courseinfo/$', 
        TemplateView.as_view(template_name='1courseinfo.html'),
        name='1courseinfo'),

    url(r'^1resources/$',
        TemplateView.as_view(template_name='1resources.html'),
        name='1resources'),

    url(r'^2HTMLCSS/$', 
        TemplateView.as_view(template_name='2HTMLCSS.html'),
        name='2HTMLCSS'),

    url(r'^2JAVASCRIPT/$', 
        TemplateView.as_view(template_name='2JAVASCRIPT.html'),
        name='2JAVASCRIPT'),

    url(r'^2PYTHON/$', 
        TemplateView.as_view(template_name='2PYTHON.html'),
        name='2PYTHON'),

    url(r'^2NEW/$',
        TemplateView.as_view(template_name='2NEW.html'),
        name='2NEW'),

    url(r'^admin/', admin.site.urls),
    
]
