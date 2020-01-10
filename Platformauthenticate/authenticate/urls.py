from django.urls import path
from django.contrib.auth import views as auth_views
from . import  views

app_name = 'authenticate'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'authenticate/login.html'), name='login'),
    path('',views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.log_out, name='logout')
]