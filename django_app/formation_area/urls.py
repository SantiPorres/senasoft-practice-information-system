from django.urls import path

from formation_area import views


urlpatterns = [
    #path('', include(router.urls)),
    path('', views.FormationAreaList.as_view(), name='formation_areas_list'),
    path('create/', views.create_formation_area, name='create_formation_area'),
    path('<slug:formation_area_slug>/', views.FormationAreaDetail.as_view(), name='formation_area_detail'),
    #path('sub_formation_areas/', views.SubFormationAreaList.as_view()),
    #path('formation_environments/', views.FormationEnvironmentsList.as_view()),
    #path('<slug:formation_area>/', views.FormationAreaDetail.as_view()),
    #path('<slug:formation_area>/<slug:sub_formation_area>/', views.SubFormationAreaDetail.as_view()),
    #path('<slug:formation_area>/<slug:sub_formation_area>/<slug:formation_environment>', views.FormationEnvironmentDetail.as_view()),
]