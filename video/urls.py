from django.urls import path
from .views import CreateVideo, DetailVideo, UpdateVideo, DeleteVideo, index, VideoCategoryList, SearchVideo
from. import views

urlpatterns=[
    path('', index.as_view(), name='index'),
    path('create/', CreateVideo.as_view(), name='video-create'),
    path('<int:pk>/', DetailVideo.as_view(), name='video-detail'),
    path('<int:pk>/update',UpdateVideo.as_view(), name='video-update'),
    path('<int:pk>/delete',DeleteVideo.as_view(),name='video-delete'),
    path('category/<int:pk>', VideoCategoryList.as_view(), name='category-list'),
        path('search/', SearchVideo.as_view(), name='video-search'),

]