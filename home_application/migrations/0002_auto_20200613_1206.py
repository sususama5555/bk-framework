# Generated by Django 2.2.6 on 2020-06-13 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostinfo',
            name='monitor',
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='is_monitor',
            field=models.CharField(default='未监控', max_length=64),
        ),
    ]
