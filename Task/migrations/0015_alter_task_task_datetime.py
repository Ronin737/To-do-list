# Generated by Django 4.0.1 on 2022-01-23 01:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0014_alter_task_task_datetime_alter_taskdetail_task_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 23, 6, 37, 12, 682160), verbose_name='Date and Time'),
        ),
    ]
