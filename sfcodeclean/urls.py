"""sfcodeclean URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView

from codescanner import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),

    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^auth/callback/$', views.AuthCallbackView.as_view(), name='auth-callback'),
    re_path(r'^logout/$', TemplateView.as_view(template_name="logout.html"), name='logout'),

    re_path(r'^job/scanning/(?P<slug>[-\w]+)/$', views.JobProcessingView.as_view(), name='job-scanning'),
    re_path(r'^job/status/(?P<slug>[-\w]+)/$', views.JobStatusView.as_view(), name='job-status'),
    re_path(r'^job/json/(?P<slug>[-\w]+)/$', views.JobJsonView.as_view(), name='job-json'),
    re_path(r'^job/(?P<slug>[-\w]+)/$', views.JobView.as_view(), name='job'),

    re_path(r'^apexclass/(?P<pk>\d+)/$', views.ApexClassBodyView.as_view(), name='apex-class-body'),

    re_path(r'^api/job/$', views.ApiJobCreateView.as_view(), name='api-job-create'),
    re_path(r'^api/job/status/(?P<slug>[-\w]+)/$', views.JobStatusView.as_view(), name='api-job-status'),
    re_path(r'^api/job/(?P<slug>[-\w]+)/$', views.JobJsonView.as_view(), name='api-job-json'),
]
