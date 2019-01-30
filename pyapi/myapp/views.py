# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets, views, status
from rest_framework.response import Response
from django.views import View
from . import models
from .serializers import *
from rest_framework.views import APIView
# Create your views here.
