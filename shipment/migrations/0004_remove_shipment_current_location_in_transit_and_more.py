# Generated by Django 5.0.2 on 2024-02-15 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0003_alter_shipmemt_history_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='current_location_in_transit',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='remark',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='status',
        ),
    ]