
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from dj_rest_auth.registration.views import VerifyEmailView, ResendEmailVerificationView
from densityAPI.views import NewEmailConfirmation




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stockright.urls')),
    path('users/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('densityAPI.urls')),
    path('api/v1/auth/',  include('dj_rest_auth.urls')),
    path('api/v1/auth/register/', include('dj_rest_auth.registration.urls')),
    re_path(
        r'^api/v1/auth/register/account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
        name='account_confirm_email'),
    path('accounts/', include('allauth.urls')),
    path('api/v1/auth/resend-email/', NewEmailConfirmation.as_view(), name='resend_email_confirmation'),
    path('password-reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('password/reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm',),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

