from django.urls import path
from news_stories import views

app_name = 'news_stories'

urlpatterns = [
    path('', views.index, name='index'),
]