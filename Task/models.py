from email.policy import default
from django.db import models
from django_extensions.db.models import AutoSlugField
from datetime import datetime

class Task(models.Model):
    task_name=models.CharField('Name',max_length=20)
    task_desciption=models.TextField('Description',default='',blank=True)
    task_datetime=models.DateTimeField('Date and Time',default=datetime.now())
    task_pinned=models.BooleanField('Pin this task?',choices=[(True,'Yes'),(False,'No')],default=False)
    task_id=AutoSlugField(populate_from=['task_name','task_datetime'], unique=True,primary_key=True,default='')

    class Meta:
        ordering=['task_datetime']



class Taskdetail(models.Model):
    task_status=models.CharField('Status',max_length=15,choices=[('Complete','Completed'),('Incomplete','Not completed')], default='Incomplete')
    task_challenge=models.TextField('Challenges in task',default='',blank=True)
    task_eta=models.IntegerField('ET for completion',default=0,help_text='Estimated time to completion in minutes')
    task_percent=models.DecimalField(max_digits=4,decimal_places=1,default=0.0)
    task=models.OneToOneField(Task,on_delete=models.CASCADE,related_name='detail',primary_key=True,blank=True)

    
    class Meta:
        verbose_name='Task Detail'
