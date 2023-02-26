# Generated by Django 4.1.7 on 2023-02-25 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('appointment_time', models.DateTimeField()),
                ('reason', models.CharField(max_length=200)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
    ]
