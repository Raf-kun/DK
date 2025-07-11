from django.urls import path
import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # ← маршрут главной страницы
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chineseHistory.urls')),
]
