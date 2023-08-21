
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from densityAPI import views
from dj_rest_auth.views import PasswordResetConfirmView



urlpatterns = [
    path('api/v1/dj-rest-auth/password/reset/confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('admin/', admin.site.urls),
    path('', include('stockright.urls')),
    path('users/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('densityAPI.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    re_path(r'^api/v1/dj-rest-auth/account-confirm-email/(?P<key>[-:\w]+)/$',
            views.CustomVerifyEmailView.as_view(), name='account_confirm_email'),
    path(
        'api/v1/dj-rest-auth/account-email-verification-sent/', views.CustomEmailConfirmView.as_view(),
        name='account_email_verification_sent')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

