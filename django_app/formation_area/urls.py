from django.urls import path

from formation_area.views.formation_area_views import *
from formation_area.views.sub_formation_area_views import *


urlpatterns = [
    #path('', include(router.urls)),
    path('', FormationAreaList.as_view(), name='formation_areas_list'),
    path('<slug:formation_area_slug>/', FormationAreaDetail.as_view(), name='formation_area_detail'),
    path('create/', create_formation_area, name='create_formation_area'),
    path('<slug:formation_area_slug>/sub_formation_area/', SubFormationAreaList.as_view(), name='sub_formation_areas_list'),
    path('sub-formation-area/create/', create_sub_formation_area, name='sub_formation_areas_list'),
    path('<slug:formation_area_slug>/sub-formation-area/<slug:sub_formation_area_slug>/', SubFormationAreaDetail.as_view(), name='sub_formation_area_detail'),
    #path('formation_environments/', views.FormationEnvironmentsList.as_view()),
    #path('<slug:formation_area>/', views.FormationAreaDetail.as_view()),
    #path('<slug:formation_area>/<slug:sub_formation_area>/', views.SubFormationAreaDetail.as_view()),
    #path('<slug:formation_area>/<slug:sub_formation_area>/<slug:formation_environment>', views.FormationEnvironmentDetail.as_view()),
]