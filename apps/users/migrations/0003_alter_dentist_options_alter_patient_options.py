# Generated by Django 4.2.1 on 2023-05-17 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_patient'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dentist',
            options={'verbose_name': 'Стоматолог', 'verbose_name_plural': 'Стоматологи'},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name': 'Пациент', 'verbose_name_plural': 'Пациенты'},
        ),
    ]
