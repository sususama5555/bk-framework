# Generated by Django 2.2.6 on 2020-06-19 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0002_auto_20200619_1106'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FileInfo',
            new_name='BackupLog',
        ),
    ]