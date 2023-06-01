from django.urls import path, include
from .views import * 

urlpatterns = [
    path('items/', ItemsView),
    path('items/<int:nm>/', ItemView),
    path('packages/', PackagesView),
    path('tourPoints/', TourPointsView),
    path('tourPoints/<int:nm>/', TourPointView),
    path('users/', UsersView),
    path('users/<int:nm>/', UserView),
    path('bookings/', BookingsView),
    path('bookings/<int:nm>/', BookingView),
]
