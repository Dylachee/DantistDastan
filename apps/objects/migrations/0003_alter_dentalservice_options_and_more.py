# Generated by Django 4.2.1 on 2023-05-17 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_dentist_options_alter_patient_options'),
        ('objects', '0002_dentalservice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dentalservice',
            options={'verbose_name': 'Стоматологическая услуга', 'verbose_name_plural': 'Стоматологические услуги'},
        ),
        migrations.AlterModelOptions(
            name='medicalhistory',
            options={'verbose_name': 'Медицинская книга', 'verbose_name_plural': 'Медицинские книги'},
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('patient_email', models.EmailField(max_length=254)),
                ('appointment_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('dentist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='users.dentist')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
    ]
