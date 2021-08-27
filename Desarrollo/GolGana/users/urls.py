from django.urls import path
from .views import register, ProfileUpdate, activate
from django.contrib.auth.views import LoginView, LogoutView
from .forms import FormWithCaptcha
post_patterns = ([
    #path('registro/', createUserView.as_view(), name="signup"),
    path('register/', register, name='register'),
    path('activate/<uidb64>/<token>/',activate, name='activate'),

    path('accounts/profile/', ProfileUpdate.as_view(), name='profile'),
    path('login/', LoginView.as_view(redirect_authenticated_user = True, template_name = "registration/login.html",
    extra_context = {'capcha':FormWithCaptcha}), name="login"),
    path('logout/', LogoutView.as_view(), name="logout")
], "user")
