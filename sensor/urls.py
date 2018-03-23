from django.conf.urls import url

from sensor import views

urlpatterns = [
    url(r'^data/$', views.data),
]