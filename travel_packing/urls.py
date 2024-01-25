# travel_packing/urls.py

from django.contrib import admin
from django.urls import include, path
from packinglist import views as packinglist_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', packinglist_views.trip_list, name='root'),  # Root URL
    path('packinglist/', include('packinglist.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]
