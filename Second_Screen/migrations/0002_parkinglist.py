# Generated by Django 4.0 on 2021-12-13 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Second_Screen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=2, verbose_name='Number')),
                ('Status', models.CharField(max_length=40, verbose_name='Status')),
            ],
        ),
    ]
