# Generated by Django 4.1 on 2024-04-19 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_dailyreport_reasonable_produce'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyreport',
            name='turn_on_speed_per_mins',
            field=models.FloatField(null=True),
        ),
    ]
