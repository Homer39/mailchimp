from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, ActivateView, send_activate_mail_view, forget_password_view, \
    recover_password_view

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),

    path('activate/<uidb64>/<token>', ActivateView.as_view(), name='activate'),
    path('confirm_prof/', send_activate_mail_view, name='send_activate_mail'),

    path('random_password_form/', forget_password_view, name='random_password_form'),
    path('recover_password/', recover_password_view, name='recover_password'),
]
