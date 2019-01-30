# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Airplane(models.Model):
    airplane_id = models.IntegerField(blank=True, primary_key=True, default=0)
    manufacturer = models.TextField(default='')
    max_seats = models.IntegerField(default=0)
    type = models.TextField(default='')

    class Meta:
        db_table = 'Airplane'


class AirplaneAirport(models.Model):
    scheduled_dep_time = models.DateTimeField(blank=True, null=True)
    scheduled_arr_time = models.DateTimeField(blank=True, null=True)
    airplane = models.ForeignKey(Airplane, models.DO_NOTHING)
    airport = models.ForeignKey('Airport', models.DO_NOTHING)

    class Meta:
        db_table = 'Airplane_Airport'


class AirplaneCustomer(models.Model):
    airplane = models.ForeignKey(Airplane, models.DO_NOTHING)
    cust = models.ForeignKey('Customer', models.DO_NOTHING)

    class Meta:
        db_table = 'Airplane_Customer'


class Airport(models.Model):
    airport_id = models.IntegerField(blank=True, null=True)
    airport_name = models.TextField()
    city = models.TextField()
    state = models.TextField()

    class Meta:
        db_table = 'Airport'


class Customer(models.Model):
    cust_id = models.IntegerField(blank=True, null=True)
    c_first_name = models.TextField()
    c_last_name = models.TextField()
    address = models.TextField()
    city = models.TextField()
    postal_code = models.IntegerField(blank=True, null=True)
    email = models.TextField()
    phone = models.IntegerField()

    class Meta:
        db_table = 'Customer'


class CustomerSeat(models.Model):
    cust = models.ForeignKey(Customer, models.DO_NOTHING)
    seat_number = models.ForeignKey('Seat', models.DO_NOTHING, db_column='seat_number')

    class Meta:
        db_table = 'Customer_Seat'


class Seat(models.Model):
    seat_number = models.TextField(unique=True, blank=True, null=True)
    airplane = models.ForeignKey(Airplane, models.DO_NOTHING)

    class Meta:
        db_table = 'Seat'
