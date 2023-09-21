from django.urls import path

from formation_area.views.sub_formation_area_views import *


urlpatterns = [
    
    #Sub Formation Area urls
    path(
        '<slug:formation_area_slug>/sub-formation-area', 
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
    path(
        '<slug:sub_formation_area_slug>/delete',
        delete_sub_formation_area,
        name='delete_sub_formation_area'
    )
]
