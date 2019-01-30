from django.urls import path
from myapp import views

urlpatterns = [
    path('airplanes/', views.airplane_list),
]
