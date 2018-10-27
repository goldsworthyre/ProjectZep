from django.conf.urls import url

from src.sensor import views

urlpatterns = [
    url(r'^data/$', views.data),
    url(r'^accel/$', views.accel),
    url(r'^sensor_constants/$', views.sensor_constants),
]