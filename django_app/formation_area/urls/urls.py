from django.urls import path, include


urlpatterns = [
    path('', include('formation_area.urls.formation_area_urls')),
    path('', include('formation_area.urls.sub_formation_area_urls')),
    path('', include('formation_area.urls.formation_environment_urls')),
]