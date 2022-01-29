from django.urls import path
from .views import ListFilterTaskAPI,CreateandListTaskAPI,DeleteTaskAPI,RetrieveandUpdateTaskDetailsAPI,FinishtaskAPI,RestartTaskAPI


urlpatterns=[path('',CreateandListTaskAPI.as_view(),name='api-list/createnew'),
            path('<str:filter>/',ListFilterTaskAPI.as_view(),name='api-filtered-list'),
            path('task/<str:pk>',RetrieveandUpdateTaskDetailsAPI.as_view(),name='api-showtask'),
            path('update/<str:pk>',RetrieveandUpdateTaskDetailsAPI.as_view(),name='api-updatetask'),
            path('finish/<str:pk>',FinishtaskAPI.as_view(),name='api-markfinish'),
            path('delete/<str:pk>/',DeleteTaskAPI.as_view(),name='api-deletetask'),
            path('restart/<str:pk>/',RestartTaskAPI.as_view(),name='api-restarttask')
            ]