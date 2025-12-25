from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("detect/", views.detect),
    path("send_alert/", views.send_alert),
]