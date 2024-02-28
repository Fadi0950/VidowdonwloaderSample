from django.urls import path
from .views import download_video_view

urlpatterns = [
    path('download/', download_video_view, name='download_video'),
]
