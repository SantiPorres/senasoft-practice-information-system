from django.urls import path

from formation_area.views.formation_area_views import *


urlpatterns = [

    #Formation Area urls
    path(
        '', FormationAreaList.as_view(), 
        name='formation_areas_list'
    ),
    path(
        '<slug:formation_area_slug>/', 
        FormationAreaDetail.as_view(), 
        name='formation_area_detail'
    ),
    path(
        'create', 
        create_formation_area, 
        name='create_formation_area'
    ),
]
