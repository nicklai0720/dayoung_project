# Generated by Django 4.1 on 2024-04-17 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_delete_dailyreport'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FormingMachine',
        ),
        migrations.DeleteModel(
            name='PrintingMachine',
        ),
    ]