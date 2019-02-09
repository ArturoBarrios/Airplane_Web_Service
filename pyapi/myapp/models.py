# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Airplane(models.Model):
    airplane_id = models.IntegerField(primary_key=True, default=0)
    manufacturer = models.TextField(default="")
    max_seats = models.IntegerField(default=0)
    type = models.TextField(default="")

    class Meta:
        db_table = 'Airplane'

class Customer_Airplane(models.Model):
    id = models.IntegerField(primary_key=True)
    airplane_id = models.ForeignKey('Airplane', on_delete=models.CASCADE)
    cust_id = models.ForeignKey('Customer', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Customer_Airplane'

class Airport(models.Model):
    airport_id = models.IntegerField(primary_key=True, default=0)
    airport_name = models.TextField(default="")
    city = models.TextField(default="")
    state = models.TextField(default="")

    class Meta:
        db_table = 'Airport'


class Customer(models.Model):
    cust_id = models.IntegerField(primary_key=True, default=0)
    c_first_name = models.TextField(default="")
    c_last_name = models.TextField(default="")
    address = models.TextField(default="")
    city = models.TextField(default="")
    postal_code = models.TextField(blank=True, null=True)
    email = models.TextField(default="")
    phone = models.IntegerField(default=0)


    class Meta:
        db_table = 'Customer'


class Flight(models.Model):
    flight_id = models.IntegerField(primary_key=True, default=0)
    cust_id = models.ForeignKey('Airplane', on_delete=models.CASCADE, default=0)
    cust_id = models.ForeignKey('Customer', on_delete=models.CASCADE, default=0)
    scheduled_dep_time = models.DateTimeField(null=True, blank=True)
    scheduled_arriv_time = models.DateTimeField(null=True, blank=True)
    departure_airport = models.TextField(blank=True,null=True)  # Field name made lowercase.
    arrival_airport = models.TextField(blank=True,null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Flight'

#not used
class Flight_Airplane(models.Model):
    id = models.IntegerField(primary_key=True)
    flight_id=models.ForeignKey('Flight', on_delete=models.CASCADE)
    airplane_id = models.ForeignKey('Airplane', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Flight_Airplane'

class Flight_Airport(models.Model):
    id = models.IntegerField(primary_key=True)
    flight_id = models.ForeignKey('Flight', on_delete=models.CASCADE)
    airport_id = models.ForeignKey('Airport', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Flight_Airport'

#not used
class Flight_Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    flight_id = models.ForeignKey('Flight', on_delete=models.CASCADE)
    cust_id = models.ForeignKey('Customer', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Flight_Customer'
