# Generated by Django 2.1.5 on 2019-02-11 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20190211_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='c_first_name',
            field=models.CharField(default='', max_length=30, verbose_name='First Name'),
        ),
    ]
