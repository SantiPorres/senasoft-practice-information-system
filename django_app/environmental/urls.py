from django.urls import path

from environmental import views


urlpatterns = [
    path('', views.LatestEnvironmentalProccesses.as_view(), name='formation_areas_list'),
    #path('create-formation-area/', views.FormationAreaDetail.as_view(), name='create_formation_area'),
    #path('formation-areas/<slug:formation-area-slug>/', views.FormationAreaDetail.as_view(), name='formation_area_detail'),
    #path('sub_formation_areas/', views.SubFormationAreaList.as_view()),
    #path('formation_environments/', views.FormationEnvironmentsList.as_view()),
    #path('<slug:formation_area>/', views.FormationAreaDetail.as_view()),
    #path('<slug:formation_area>/<slug:sub_formation_area>/', views.SubFormationAreaDetail.as_view()),
    #path('<slug:formation_area>/<slug:sub_formation_area>/<slug:formation_environment>', views.FormationEnvironmentDetail.as_view()),
]