from django.urls import path
from .views import *

app_name = 'better_templates'

urlpatterns = (
    path('readme/', ReadMeView.as_view(), name='readme'),
)