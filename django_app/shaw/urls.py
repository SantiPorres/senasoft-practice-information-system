from django.urls import path

from .views import LatestShawProcesses


urlpatterns = [
    path('latest', LatestShawProcesses.as_view(), name='latest-shaw-processes')
]
