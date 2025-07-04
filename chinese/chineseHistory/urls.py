from django.urls import path
import views


urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns = [
    path('reviews/submit/', views.submit_review, name='submit_review'),
    path('reviews/get/', views.get_reviews, name='get_reviews'),
]
