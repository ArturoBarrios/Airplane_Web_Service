# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from myapp.models import Airplane, Customer_Airplane, Airport, Customer, Flight, Flight_Airplane, Flight_Airport, Flight_Customer

admin.site.register(Airplane)
admin.site.register(Customer_Airplane)
admin.site.register(Airport)
admin.site.register(Customer)
admin.site.register(Flight)
admin.site.register(Flight_Airplane)
admin.site.register(Flight_Airport)
admin.site.register(Flight_Customer)
# Register your models here.
