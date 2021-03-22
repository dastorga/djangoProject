from django.urls import path

from . import views
from .views import get_key
from django.conf.urls import url
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', views.index, name='index'),
    path('getKey/<int:key>', views.get_key, name='get_key'),
]



