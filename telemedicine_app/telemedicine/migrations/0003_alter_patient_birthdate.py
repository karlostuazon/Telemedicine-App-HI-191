# Generated by Django 4.0.4 on 2022-06-08 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemedicine', '0002_alter_patient_attending_doctor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]