from django.urls import path
from . import views

# http://logalhost/user
app_name = 'user'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('mypage/', views.mypage, name='mypage'),
    path('mypage/delete/', views.mypage_delete, name='mypage_delete'),
    path('mypage/password', views.password_edit_view, name='password_edit_view'),
]