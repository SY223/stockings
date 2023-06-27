from django.urls import path
from densityAPI import views


app_name = 'densityapi'

urlpatterns = [
    path('owners', views.user_list),
    path('owners/<int:pk>/', views.user_detail),
    path('ponds/', views.pond_list_create),
    path('ponds/<int:pondId>/', views.pond_detail),
    path('check-stocks/<int:pondId>/', views.densities_list_create),
    path('single-stock/<int:densityId>/', views.density_detail), 
    # path('secret/', views.secret),
    # path('manager-view/', views.manager_view),
]