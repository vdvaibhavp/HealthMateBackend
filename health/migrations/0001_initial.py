# Generated by Django 4.2.4 on 2023-09-06 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctor_id', models.AutoField(primary_key=True, serialize=False)),
                ('doctor_name', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('patient_name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Daily_Time_Slots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_date', models.DateTimeField()),
                ('time_slots', models.JSONField()),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.AutoField(primary_key=True, serialize=False)),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField()),
                ('appointment_purpose', models.TextField(blank=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.patient')),
            ],
        ),
    ]
