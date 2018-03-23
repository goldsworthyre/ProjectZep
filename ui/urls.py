from django.conf.urls import url

from ui import views

urlpatterns = [
    url(r'^control/$', views.control),
]