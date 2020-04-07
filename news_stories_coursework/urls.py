from django.contrib import admin
from django.urls import path, include
from news_stories import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('news_stories/', include('news_stories.urls')),
    path('admin/', admin.site.urls),
]