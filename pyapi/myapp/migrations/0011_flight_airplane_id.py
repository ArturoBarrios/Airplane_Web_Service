# Generated by Django 2.1.5 on 2019-02-06 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20190203_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='airplane_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='myapp.Airplane'),
        ),
    ]