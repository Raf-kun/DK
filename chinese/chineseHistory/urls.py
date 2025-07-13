from django.urls import path
import views
from django.contrib import admin
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # ← маршрут главной страницы
    path('', include('chineseHistory.urls')),
]
