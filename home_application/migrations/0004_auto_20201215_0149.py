# Generated by Django 2.2.6 on 2020-12-15 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0003_auto_20200619_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='hostMonitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(default='', max_length=64)),
                ('cpu', models.CharField(default='', max_length=64)),
                ('disk', models.CharField(default='', max_length=64)),
                ('mem', models.CharField(default='', max_length=64)),
                ('monitor_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.DeleteModel(
            name='Template',
        ),
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
