from django.contrib import admin
from stockright.models import StockingDensity, Pond

# Register your models here.
class PondAmin(admin.ModelAdmin):
    fields = ['owner', 'name', 'date_added']
    list_display = ('owner', 'name', 'date_added')
    list_filter = ['owner']

class StockingDensityAdmin(admin.ModelAdmin):
    fields = ['pond', 'length', 'width', 'height', 'to_stock']
    list_display = ['pond', 'length', 'width', 'height', 'to_stock']


admin.site.register(StockingDensity, StockingDensityAdmin)
admin.site.register(Pond, PondAmin)
