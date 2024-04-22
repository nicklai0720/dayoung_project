# Generated by Django 4.1 on 2024-04-17 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_formingmachine_actual_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formingmachine',
            name='actual_time',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='formingmachine',
            name='capacity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='formingmachine',
            name='machine_code',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='formingmachine',
            name='output',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='formingmachine',
            name='per_mins',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='formingmachine',
            name='time_zone',
            field=models.CharField(max_length=200),
        ),
    ]