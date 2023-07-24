
from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stockright.urls')),
    path('users/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('densityAPI.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/vi/dj-rest-auth/password/reset/', PasswordResetView.as_view()),
    path('api/vi/dj-rest-auth/password/reset/confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]

