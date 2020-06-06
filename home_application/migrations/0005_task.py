# Generated by Django 2.2.6 on 2020-06-06 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0004_template_updator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=64)),
                ('type', models.CharField(default='', max_length=64)),
                ('template', models.CharField(default='', max_length=64)),
                ('symbol', models.CharField(default='', max_length=64)),
                ('business', models.CharField(default='', max_length=64)),
                ('creator', models.CharField(default='', max_length=64)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]