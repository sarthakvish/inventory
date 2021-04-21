from django.contrib import admin
from django.urls import path,include,re_path
from inventory_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory_app.urls')),
    path('accounts/', include('allauth.urls')),
]
