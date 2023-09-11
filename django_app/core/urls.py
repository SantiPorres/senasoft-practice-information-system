from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
    path('api/formation-area/', include('formation_area.urls'), name='formation-area'),
    path('api/environmental/', include('environmental.urls'), name='formation-area'),
    #path('api/', include('environmental.urls'), name='environmental'),
    #path('api/', include('shaw.urls'), name='shaw'),
    path('api_generate_token/', views.obtain_auth_token),
]
