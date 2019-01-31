# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets, views, status
from django.http import HttpResponse, JsonResponse
from django.views import View
from . import models
from .serializers import *
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def airplane_list(request):
    # list all the airplane, or create a new airplane_id
    if request.method == 'GET':
        airplanes = Airplane.objects.all()
        serializer = AirplaneSerializer(airplanes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AirplaneSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def airplane_detail(request, pk):
    try:
        airplane = Airplane.objects.get(pk=pk)
    except Airplane.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AirplaneSerializer(airplane)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AirplaneSerializer(airplane, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        airplane.delete()
        return HttpResponse(status=204)
