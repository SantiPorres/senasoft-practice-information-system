from django.urls import path

from formation_area.views.formation_environment_views import *


urlpatterns = [

    #Formation Environment urls
    path(
        '<slug:formation_area_slug>/sub-formation-area/'\
            '<slug:sub_formation_area_slug>/formation-environment', 
        FormationEnvironmentList.as_view(), 
        name='formation_environment_list'
    ),
    path(
        '<slug:formation_area_slug_parameter>/sub-formation-area/'\
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