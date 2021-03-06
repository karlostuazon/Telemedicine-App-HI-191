# Generated by Django 4.0.4 on 2022-06-08 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telemedicine', '0006_alter_doctor_hospital_affliations'),
        ('consultation_record', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultationrecord',
            name='consultation_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consultationrecord',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='telemedicine.doctor'),
        ),
        migrations.AlterField(
            model_name='consultationrecord',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='telemedicine.patient'),
        ),
    ]
