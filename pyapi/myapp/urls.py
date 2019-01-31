from django.urls import path
from myapp import views

urlpatterns = [
    path('airplanes/', views.airplane_list),
    path('airplanes/<int:pk>', views.airplane_detail),
]
