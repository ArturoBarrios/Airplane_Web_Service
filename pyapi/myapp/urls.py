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
    path('airplanecustomers/', views.AirplaneCustomer_list),
]
