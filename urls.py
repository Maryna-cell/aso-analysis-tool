from django.contrib import admin
from django.urls import path, include
from aso_analysis.views import home


urlpatterns = [
    path('', home, name='home'),  # Главная страница
    path('admin/', admin.site.urls),
    path('api/', include('aso_analysis.urls')),  # API для поиска
]
