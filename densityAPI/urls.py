from django.urls import path, include, re_path
from densityAPI import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)



app_name = 'densityapi'

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('owners/', views.user_list_create),
    path('owners/<int:pk>/', views.user_detail),
    path('ponds/', views.pond_list_create, name='pond-list-create'), #get all ponds
    path('pond/<int:pondId>/', views.pond_detail), #get a single pond
    path('check-stocks/<int:pondId>/', views.densities_list_create), #lists densities of a pond and check new density
    path('single-stock/<int:densityId>/', views.density_detail), #get a single density
    path('api-token-auth/', obtain_auth_token),
    
]