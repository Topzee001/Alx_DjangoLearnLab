from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import signup_view, profile_view, profile_update_view

urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'), 
    path('signup/', signup_view, name='signup'),
    # path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile-update/', profile_update_view, name='profile-updates'),
    path('profile/', profile_view, name='profile'),
]