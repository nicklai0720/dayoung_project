# Generated by Django 4.1 on 2024-04-17 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_formingmachine_actual_time_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DailyReport',
        ),
    ]
