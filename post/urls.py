# ./post.urls
# django의 메소드와 blog 앱에서 사용할 모든 views를 불러온다.

from django.urls import path
from . import views

urlpatterns = [
        path('', views.post_list, name='post_list'),
        ]
