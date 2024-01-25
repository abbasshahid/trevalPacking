from django.urls import path
from . import views

urlpatterns = [
    path('trips/', views.trip_list, name='trip_list'),
   # In your urls.py
    path('packinglist/<int:trip_id>/', views.packinglist, name='packinglist'),  
    path('additem/', views.add_item, name='add_item'),
    path('add_trip/', views.add_trip, name='add_trip'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    
]
