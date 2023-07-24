from django.urls import path
from densityAPI import views
from rest_framework.authtoken.views import obtain_auth_token



app_name = 'densityapi'

urlpatterns = [
    path('owners/', views.user_list_create),
    path('owners/<int:pk>', views.user_detail),
    path('ponds/', views.pond_list_create), #get all ponds
    path('ponds/<int:pondId>', views.pond_detail), #get a single pond
    path('check-stocks/<int:pondId>', views.densities_list_create), #lists densities of a pond and check new density
    path('single-stock/<int:densityId>', views.density_detail), #get a single density
    path('api-token-auth/', obtain_auth_token),
]