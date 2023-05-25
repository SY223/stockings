from django.urls import path
from stockright import views

app_name = 'stockright'

urlpatterns = [
    path('', views.index, name="index"),
    path('ponds/', views.ponds, name='ponds'),
    path('ponds/<int:pond_id>', views.pond, name='pond'),
    path('new_pond', views.new_pond, name='new_pond'),
    path('check_stock/<int:pond_id>', views.check_stock, name='check_stock'),
    path('edit/<int:stock_id>', views.edit_density, name='edit_density'),
    path('delete/<int:stock_id>', views.delete_density, name='delete_density'),

]