"""
Ascii Djenerator routes
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('generator', views.generator, name='generator'),
    path('random', views.random, name='random')
]
