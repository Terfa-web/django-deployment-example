from django.conf.urls import url
from basicApp import views

#tempalte tagging. SET GLOBAL VARIABLE = YOUR APP NAME
app_name = 'basicApp'

urlpatterns = [
    #create url LINKS for the views
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),

]
