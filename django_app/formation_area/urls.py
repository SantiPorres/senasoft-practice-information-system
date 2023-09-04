from django.urls import path, include
from rest_framework import routers

from formation_area import views

"""router=routers.DefaultRouter()
router.register(r'formation_areas', views.FormationAreaViewSet)
router.register(r'sub_formation_areas', views.SubFormationAreaViewSet)
router.register(r'formation_environments', views.FormationEnvironmentViewSet)"""

urlpatterns = [
    #path('', include(router.urls)),
    path('formation_areas/', views.FormationAreaList.as_view(), name='formation_areas_list'),
    path('create_formation_area/', views.FormationAreaDetail.as_view(), name='create_formation_area'),
    path('formation_areas/<slug:formation_area_slug>/', views.FormationAreaDetail.as_view(), name='formation_area_detail'),
    #path('sub_formation_areas/', views.SubFormationAreaList.as_view()),
    #path('formation_environments/', views.FormationEnvironmentsList.as_view()),
    #path('<slug:formation_area>/', views.FormationAreaDetail.as_view()),
    #path('<slug:formation_area>/<slug:sub_formation_area>/', views.SubFormationAreaDetail.as_view()),
    #path('<slug:formation_area>/<slug:sub_formation_area>/<slug:formation_environment>', views.FormationEnvironmentDetail.as_view()),
]