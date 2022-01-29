from rest_framework.serializers import ModelSerializer
from .models import Taskdetail,Task

class TaskSerialiser(ModelSerializer):

    class Meta:
        model=Task
        fields='__all__'


class TaskdetailSerialiserwithoutstatus(ModelSerializer):

    class Meta:
        model=Taskdetail
        exclude=['task_status']
    
    task=TaskSerialiser()

class TaskdetailSerialiserwithstatus(ModelSerializer):

    class Meta:
        model=Taskdetail
        fields='__all__'
    
    task=TaskSerialiser()
