from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

from utils.constants import API_URL


urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{API_URL}/', include('djoser.urls')),
    path(f'{API_URL}/', include('djoser.urls.authtoken')),
    path(f'{API_URL}/formation-area/', include('formation_area.urls'), name='formation-area'),
    path(f'{API_URL}/environmental/', include('environmental.urls'), name='formation-area'),
    #path(f'{API_URL}/', include('environmental.urls'), name='environmental'),
    #path(f'{API_URL}/', include('shaw.urls'), name='shaw'),
    path('api_generate_token/', views.obtain_auth_token),
]
