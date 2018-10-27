from django.conf.urls import url

from src.control import views

urlpatterns = [
    url(r'^control/$', views.control),
    url(r'^config', views.control_data),
    url(r'^movement', views.control_movement),
]