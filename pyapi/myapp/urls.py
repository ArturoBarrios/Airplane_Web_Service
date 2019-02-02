from django.urls import path
from myapp import views

urlpatterns = [
    path('airplanes/', views.airplane_list),
    path('airplanes/<int:pk>', views.airplane_detail),
    path('airports/', views.airport_list),
    path('airports/<int:pk>', views.airport_detail),
    path('customers/', views.customer_list),
    path('customers/<int:pk>', views.customer_detail),
    path('flights/', views.flight_list),
    path('flights/<int:pk>', views.flight_detail),
    path('customerairplane/', views.customerairplane_list),
    path('customerairplane/<int:pk>', views.customerairplane_detail),
    path('flightairplane/', views.flightairplane_list),
    path('flightairplane/<int:pk>', views.flightairplane_detail),
    path('flightairport/', views.flightairport_list),
    path('flightairport/<int:pk>', views.flightairport_detail),
]
