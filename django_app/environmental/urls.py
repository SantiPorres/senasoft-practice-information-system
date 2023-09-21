from django.urls import path

from .views import *


urlpatterns = [
    path(
        'latest', 
        LatestEnvironmentalProcesses.as_view(), 
        name='latest_environmental_processes'
    ),
    path(
        '', 
        EnvironmentalProcessList.as_view(), 
        name='environmental_process_list'
    ),
    path(
        '<slug:environmental_process_slug>/', 
        EnvironmentalProcessDetail.as_view(), 
        name='environmental_process_detail'
    ),
    path(
        'create', 
        create_environmental_process, 
        name='create_environmental_process'
    ),
    path(
        '<slug:environmental_process_slug>/delete',
        delete_environmental_proccess,
        name='delete_environmental_process'
    )
]