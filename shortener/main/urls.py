from django.conf.urls import url 
from main import views 

urlpatterns=[
    
    url(r'^showURLs/$',views.showURLs,name='showURLs'),
    url(r'',views.home,name='home'),
]