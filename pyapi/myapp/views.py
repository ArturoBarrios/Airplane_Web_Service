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
# Create your views here.

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
