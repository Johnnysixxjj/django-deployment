# Generated by Django 4.1 on 2022-09-13 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesOffered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('prices', models.DecimalField(decimal_places=2, max_digits=10)),
                ('service_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('invoice_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='based.servicesoffered')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=2)),
                ('phone_number', models.CharField(max_length=12)),
                ('home_address', models.CharField(max_length=100)),
                ('pet_name', models.CharField(max_length=50)),
                ('pet_age', models.CharField(max_length=2)),
                ('pet_breed', models.CharField(default='Put Breed Here', max_length=100)),
                ('pet_name2', models.CharField(blank=True, max_length=50, null=True)),
                ('pet_age2', models.CharField(blank=True, max_length=2, null=True)),
                ('pet_breed2', models.CharField(default='Put Breed Here', max_length=100)),
                ('pet_name3', models.CharField(blank=True, max_length=50, null=True)),
                ('pet_age3', models.CharField(blank=True, max_length=2, null=True)),
                ('pet_breed3', models.CharField(default='Put Breed Here', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClientAppointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=11)),
                ('email_adress', models.EmailField(max_length=254)),
                ('appointment_date', models.CharField(default='m/d/y', max_length=9)),
                ('appointment_finished', models.BooleanField(default=False)),
                ('appointment_desc', models.TextField(blank=True, default='Describe how the service went ', null=True)),
                ('service', models.ManyToManyField(to='based.servicesoffered')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]