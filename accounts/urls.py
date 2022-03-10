from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    #path('login/', views.user_login, name='user_login')    
    path('login/', auth_views.LoginView.as_view(), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='user_logout'),
    path('', views.dashboard, name='user_dashboard'),
]
