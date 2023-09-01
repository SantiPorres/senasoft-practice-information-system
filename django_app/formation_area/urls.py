from django.urls import path, include

from formation_area import views

urlpatterns = [
    path('formation_areas/', views.FormationAreaList.as_view()),
    #path('sub_formation_areas/', views.SubFormationAreaList.as_view()),
    #path('formation_environments/', views.FormationEnvironmentsList.as_view()),
    #path('<slug:formation_area>/', views.FormationAreaDetail.as_view()),
    #path('<slug:formation_area>/<slug:sub_formation_area>/', views.SubFormationAreaDetail.as_view()),
    #path('<slug:formation_area>/<slug:sub_formation_area>/<slug:formation_environment>', views.FormationEnvironmentDetail.as_view()),
]