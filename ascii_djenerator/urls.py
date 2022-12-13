"""
Ascii Djenerator routes
"""

import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="home"),
    path('generator', views.generator, name='generator'),
    path('random', views.random, name='random')
]
