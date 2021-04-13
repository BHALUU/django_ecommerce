from django.urls import path

from . import views
from .api import views as rest_views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('/api/', views.home, name='home'),
]
