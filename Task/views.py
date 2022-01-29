from rest_framework.generics import ListCreateAPIView,ListAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveAPIView
from .serialisers import TaskSerialiser,Taskdetail,Task, TaskdetailSerialiserwithoutstatus,TaskdetailSerialiserwithstatus
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

class CreateandListTaskAPI(ListCreateAPIView):
    serializer_class=TaskSerialiser
    queryset=Task.objects.all()

    def perform_create(self, serializer):
        new_task=Task.objects.create(**serializer.data)
        default_task_details=Taskdetail.objects.create(task=new_task)

class ListFilterTaskAPI(ListAPIView):
    serializer_class=TaskSerialiser

    def get_queryset(self):
        arg=self.kwargs['filter']
        queryset=Task.objects.all()
        if(arg=='pinned'):
            queryset=Task.objects.filter(task_pinned=True)
        elif arg=='incomplete' in arg:
            queryset=Task.objects.filter(detail__task_status='Incomplete')
        else:
            queryset=Task.objects.filter(detail__task_status='Complete')
        
        return queryset

class RetrieveandUpdateTaskDetailsAPI(RetrieveUpdateAPIView):
    
    def get_serializer_class(self):
        if self.request.method=='GET':
            return TaskdetailSerialiserwithstatus
        return TaskdetailSerialiserwithoutstatus
    
    queryset=Taskdetail.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if('task' in request.data):
            taskdata=request.data.pop('task')
            partial=True
            taskpartial=True
            if len(taskdata.keys())==5:
                taskpartial=False
            updated_task=TaskSerialiser(instance.task,taskdata,partial=taskpartial)
            updated_task.is_valid(raise_exception=True)
            updated_task.save()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class FinishtaskAPI(RetrieveAPIView):
    serializer_class=TaskSerialiser
    queryset=Task.objects.all()
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if(not serializer.data['task_pinned']):
            instance.delete()
        else:

            new_details=TaskdetailSerialiserwithstatus(instance.detail,data={"task_eta": 0,
                                                                             "task_percent":100,
                                                                             'task_status':'Complete'},
                                                                             partial=True)
            new_details.is_valid(raise_exception=True)
            new_details.save()
        
        return Response(status=status.HTTP_200_OK)


class DeleteTaskAPI(RetrieveDestroyAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerialiser

class RestartTaskAPI(RetrieveAPIView):
    
    queryset=Task.objects.all()
    serializer_class=TaskSerialiser

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        restarted_task=self.serializer_class(instance,data={'task_datetime':datetime.now()},partial=True)
        restarted_task.is_valid(raise_exception=True)
        restarted_task.save()
        new_details=TaskdetailSerialiserwithstatus(instance.detail,data={"task_eta": 0,
                                                                         "task_percent":0,
                                                                         'task_status':'Incomplete',
                                                                         'task_challenge':''},
                                                                             partial=True)

        new_details.is_valid(raise_exception=True)
        new_details.save()

        return Response(status=status.HTTP_200_OK)


        











    

        



    



    

