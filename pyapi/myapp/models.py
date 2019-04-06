# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#testing Jenkins again and again!!!!!!!!!!!!!!!!!!!!!!!
from django.db import models
from django.urls import reverse

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
    cust_id = models.IntegerField(primary_key=True)
    c_first_name = models.CharField('First Name',max_length=30,default="")
    c_last_name = models.CharField('Last Name',max_length=30,default="")
    address = models.CharField('Address',max_length=30,default="")
    city = models.CharField('City',max_length=30,default="")
    postal_code = models.CharField('Postal Code',max_length=30,blank=True, null=True)
    email = models.CharField('Email',max_length=30,default="")
    phone = models.IntegerField('Phone Number',null=False)

    def get_absolute_url(self):
        return reverse('customer', kwargs={})


    class Meta:
        db_table = 'Customer'



class Flight(models.Model):
    flight_id = models.IntegerField(primary_key=True, null=False)
    airplane_id = models.ForeignKey('Airplane',null=True, on_delete=models.CASCADE)
    cust_id = models.ForeignKey('Customer',null=True, on_delete=models.CASCADE)
    date_arriv = models.DateField()
    date_dep = models.DateField()
    scheduled_dep_time = models.TimeField(null=False)
    scheduled_arriv_time = models.TimeField(null=False)
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
