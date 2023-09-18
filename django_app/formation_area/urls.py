from django.urls import path

from formation_area.views.formation_area_views import *
from formation_area.views.sub_formation_area_views import *
from formation_area.views.formation_environment_views import *


urlpatterns = [
    #path('', include(router.urls)),

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


    #Sub Formation Area urls
    path(
        '<slug:formation_area_slug>/sub-formation-area/', 
        SubFormationAreaList.as_view(), 
        name='sub_formation_areas_list'
    ),
    path(
        '<slug:formation_area_slug>/sub-formation-area/create', 
        create_sub_formation_area, 
        name='create_sub_formation_areas'
    ),
    path(
        '<slug:formation_area_slug>/sub-formation-area/'\
            '<slug:sub_formation_area_slug>/',
        SubFormationAreaDetail.as_view(), 
        name='sub_formation_area_detail'
    ),


    #Formation Environment urls
    path(
        '<slug:formation_area_slug>/sub-formation-area/'\
            '<slug:sub_formation_area_slug>/formation-environment/', 
        FormationEnvironmentList.as_view(), 
        name='formation_environment_list'
    ),
    path(
        '<slug:formation_area_slug>/sub-formation-area/'\
            '<slug:sub_formation_area_slug>/formation-environment/create', 
        create_formation_environment, 
        name='create_formation_environment'
    ),
    path(
        '<slug:formation_area_slug>/sub-formation-area/'\
            '<slug:sub_formation_area_slug>/formation-environment/'\
                '<slug:formation_environment_slug>/', 
        FormationEnvironmentDetail.as_view(), 
        name='formation_environment_detail'
    ),
]