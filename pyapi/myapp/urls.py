from django.urls import path
from myapp import views

urlpatterns = [
    path('airplanes/', views.airplane_list),
    path('airplanes/<int:pk>', views.airplane_detail),
    path('airports/', views.airport_list),
    path('airports/<int:pk>', views.airport_detail),
]
