
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stockright.urls')),
    path('users/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('densityAPI.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]

