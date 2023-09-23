from django.urls import path

from .views import *


urlpatterns = [
    path(
        'latest', 
        LatestShawProcesses.as_view(), 
        name='latest_shaw_processes'
    ),
    path(
        '',
        ShawProcessList.as_view(),
        name='shaw_process_list'
    ),
    path(
        '<slug:shaw_process_slug>/',
        ShawProcessDetail.as_view(),
        name='shaw_process_detail'
    )
]
