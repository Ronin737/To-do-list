# Generated by Django 4.0.1 on 2022-01-23 00:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0013_alter_task_task_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 23, 6, 18, 43, 124994), verbose_name='Date and Time'),
        ),
        migrations.AlterField(
            model_name='taskdetail',
            name='task',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='detail', serialize=False, to='Task.task'),
        ),
        migrations.AlterField(
            model_name='taskdetail',
            name='task_percent',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=4),
        ),
    ]