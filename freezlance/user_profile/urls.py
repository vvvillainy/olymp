from django.urls import path
from user_profile.views import *

urlpatterns = [
    path('', index),
]