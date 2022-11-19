from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

# Rest Framework 
from rest_framework import routers

app_name = "blog"

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<slug:slug>', views.article, name="read_article"),
    path('latest-articles/', views.LatestArticlesList.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)