from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from stockright.models import CustomUser, Pond, StockingDensity, Profile

# Register your models here.
class PondAmin(admin.ModelAdmin):
    fields = ['owner', 'name', 'date_added']
    list_display = ('owner', 'name', 'date_added')
    list_filter = ['owner']

class StockingDensityAdmin(admin.ModelAdmin):
    fields = ['pond', 'length', 'width', 'height', 'to_stock']
    list_display = ['pond', 'length', 'width', 'height', 'to_stock']

class ProfileAdminInline(admin.StackedInline):
    model = Profile
    verbose_name_plural = "profiles"

class CustomUserAdmin(BaseUserAdmin):
    inlines = [ProfileAdminInline]

admin.site.register(StockingDensity, StockingDensityAdmin)
admin.site.register(Pond, PondAmin)
#admin.site.unregister(CustomUser)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)

