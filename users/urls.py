from django.urls import path,reverse_lazy
from users import views
from django.contrib.auth import views as auth_views



app_name = 'users'

urlpatterns = [    
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("password-change/", 
        auth_views.PasswordChangeView.as_view(success_url='done'),
        name="password_change"),
    path("password-change/done/", 
        auth_views.PasswordChangeDoneView.as_view(), 
        name="password_change_done"),
    path("password-reset/", 
        auth_views.PasswordResetView.as_view(
            template_name='registration/my_password_reset_form.html',
            success_url='done'), 
        name="password_reset"),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy('users:password_reset_complete')),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path('register/', views.register, name='register'),
]