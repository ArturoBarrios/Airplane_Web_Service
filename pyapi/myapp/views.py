# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework import viewsets, views, status
from django.http import HttpResponse, JsonResponse
from django.views import View
from . import models
from .serializers import *
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from myapp.models import Customer, Flight, Airport, Airplane, Customer_Airplane, Flight_Airplane, Flight_Airport, Flight_Customer
from django.views import generic
from django import forms
from django.views.generic import FormView
from django.views.generic import CreateView
# Create your views here.

class FlightCreateView(CreateView):
    model = Flight
    fields = ('flight_id', 'airplane_id', 'cust_id', 'scheduled_dep_time', 'scheduled_arriv_time', 'departure_airport', 'arrival_airport')
    widgets = {'myDateField': forms.DateInput(attrs={'id': 'datetimepicker12'})}

class airplane_list_new(generic.ListView):
    model = Airplane
class customer_list_new(generic.ListView):
    model = Customer
class flight_list_new(generic.ListView):
    model = Flight
class customer_detail_new(generic.DetailView):
    model = Customer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_cus = Customer.objects.all().count()
    num_airplanes = Airplane.objects.all().count()

    # Available books (status = 'a')
    num_flights = Flight.objects.all().count()

    # The 'all()' is implied by default.
    num_airports = Airport.objects.all().count()

    context = {
        'num_customers': num_cus,
        'num_airplanes': num_airplanes,
        'num_flights': num_flights,
        'num_airports': num_airports,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

@csrf_exempt
def airplane_list(request):
    # list all the airplane, or create a new airplane
    if request.method == 'GET':
        airplanes = Airplane.objects.all()
        serializer = AirplaneSerializer(airplanes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AirplaneSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def airplane_detail(request, pk):
    # Operate on one specific airplane by its id
    try:
        airplane = Airplane.objects.get(pk=pk)
    except Airplane.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AirplaneSerializer(airplane)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AirplaneSerializer(airplane, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        airplane.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def airport_list(request):
    # List all the airport, or create a new airport
    if request.method == 'GET':
        airports = Airport.objects.all()
        serializer = AirportSerializer(airports, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AirportSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def airport_detail(request, pk):
    # Operate on one specific airport by its id
    try:
        airport = Airport.objects.get(pk=pk)
    except Airport.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AirportSerializer(airport)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AirportSerializer(airport, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        airport.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def customer_list(request):
    # list all customers, or create a new customer
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def customer_detail(request, pk):
    # OPerate on one specific customer by its id
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(customer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def flight_list(request):
    # list all flights, or create a new flight
    if request.method == 'GET':
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FlightSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def flight_detail(request, pk):
    # OPerate on one specific flight by its id
    try:
        flight = Flight.objects.get(pk=pk)
    except Flight.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FlightSerializer(flight)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FlightSerializer(flight, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        flight.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def customerairplane_list(request):
    if request.method == 'GET':
        relations = Customer_Airplane.objects.all()
        serializer = CustomerAirplaneSerializer(relations, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomerAirplaneSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def customerairplane_detail(request, pk):
    # OPerate on one specific customer_airplane relation by its id
    try:
        relation = Customer_Airplane.objects.get(pk=pk)
    except Customer_Airplane.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerAirplaneSerializer(relation)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CustomerAirplaneSerializer(relation, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        relation.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def flightairplane_list(request):
    # list all flightairplane relationship, or create a new one
    if request.method == 'GET':
        relations = Flight_Airplane.objects.all()
        serializer = FlightAirplaneSerializer(relations, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FlightAirplaneSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def flightairplane_detail(request, pk):
    # OPerate on one specific flight_airplane relationship by its id
    try:
        relation = Flight_Airplane.objects.get(pk=pk)
    except Flight_Airplane.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FlightAirplaneSerializer(relation)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FlightAirplaneSerializer(relation, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        relation.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def flightairport_list(request):
    # list all flightairport relationship, or create a new one
    if request.method == 'GET':
        relations = Flight_Airport.objects.all()
        serializer = FlightAirportSerializer(relations, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FlightAirportSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def flightairport_detail(request, pk):
    # OPerate on one specific flight_airplort relationship by its id
    try:
        relation = Flight_Airport.objects.get(pk=pk)
    except Flight_Airport.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FlightAirportSerializer(relation)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FlightAirportSerializer(relation, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        relation.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def flightcustomer_list(request):
    # list all flightcustomer relationship, or create a new one
    if request.method == 'GET':
        relations = Flight_Customer.objects.all()
        serializer = FlightCustomerSerializer(relations, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FlightCustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def flightcustomer_detail(request, pk):
    # OPerate on one specific flight_airplort relationship by its id
    try:
        relation = Flight_Customer.objects.get(pk=pk)
    except Flight_Customer.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FlightCustomerSerializer(relation)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FlightCustomerSerializer(relation, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        relation.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
