from django.urls import path

from . import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('video/<int:id>/', views.video_detail, name='video_detail'),
]
