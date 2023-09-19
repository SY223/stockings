from django.urls import path, re_path, include
from densityAPI import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)




app_name = 'densityapi'

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('ponds/', views.pond_list_create, name='pond_list_create'), #get all ponds
    path('pond/<int:pondId>/', views.pond_detail, name='pond_detail'), #get a single pond
    path('check-stocks/<int:pondId>/', views.densities_list_create, name='check_densities'), #lists densities of a pond and check new density
    path('single-stock/<int:densityId>/', views.density_detail, name='a_single_density'), #get a single density
    path('owner/profile/', views.profile_list_create, name='my_profile'),
    path('all/breeders/', views.all_breeders, name='all-breeder'), #Admin view
    path('all/breeders/<int:pk>/', views.breeder_detail, name='breeder-detail'), #Admin view
    path('api-token-auth/', obtain_auth_token),
    
]