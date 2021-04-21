from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# For normal app
from .models import Stock
from .forms import StockCreateForm
class StockCreateAdmin(ImportExportModelAdmin):
   list_display = ['category', 'item_name', 'quantity']
   form = StockCreateForm
   list_filter = ['category']
   search_fields = ['category', 'item_name']
admin.site.register(Stock, StockCreateAdmin)

#
#
# from django.contrib.auth.admin import UserAdmin
# from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth import get_user_model
# class CustomUserAdmin(UserAdmin):
#    """Define admin model for custom User model with no username field."""
#    fieldsets = (
#       (None, {'fields': ('phone', 'password')}),
#       (_('Personal info'), {'fields': ('first_name', 'last_name')}),
#       (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
#                                      'groups', 'user_permissions')}),
#       (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#    )
#    add_fieldsets = (
#       (None, {
#          'classes': ('wide',),
#          'fields': ('email', 'password1', 'password2'),
#       }),
#    )
#    list_display = ('email', 'first_name', 'last_name', 'is_staff')
#    search_fields = ('email', 'first_name', 'last_name')
#    ordering = ('email',)
#
#
# admin.site.register(get_user_model(), CustomUserAdmin)