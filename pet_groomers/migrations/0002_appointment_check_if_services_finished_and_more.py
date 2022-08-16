# Generated by Django 4.1 on 2022-08-16 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_groomers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='check_if_services_finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appointment',
            name='phone_numb',
            field=models.CharField(default='Enter Phone Number', max_length=13),
        ),
        migrations.AddField(
            model_name='appointment',
            name='report',
            field=models.TextField(default='Enter a report after the services'),
        ),
    ]