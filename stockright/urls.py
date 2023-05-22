from django.urls import path
from stockright import views

app_name = 'stockright'

urlpatterns = [
    path('', views.index, name="index"),
    path('ponds', views.ponds, name='ponds'),
    path('ponds/<int:pond_id>', views.pond, name='pond'),
    path('check_stock/<int:pond_id>', views.check_stock, name='check_stock'),
    #path('result/', views.resultPage, name="results"),
]