# Generated by Django 4.0 on 2021-12-13 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Second_Screen', '0002_parkinglist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parkinglist',
            old_name='number',
            new_name='Number',
        ),
        migrations.AddField(
            model_name='parkinglist',
            name='TimeEnd',
            field=models.CharField(default='00:00', max_length=40, verbose_name='TimeEnd'),
        ),
        migrations.AddField(
            model_name='parkinglist',
            name='TimeStart',
            field=models.CharField(default='00:00', max_length=40, verbose_name='TimeStart'),
        ),
    ]
