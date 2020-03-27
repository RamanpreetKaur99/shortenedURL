from django.conf.urls import url 
from users.views import loginview,logoutview,signupview

urlpatterns=[
    url(r'^signup/$',signupview,name="signup"),
    url(r'^login/$',loginview,name='login'),
    url(r'^logout/$',logoutview,name="logout")

]
