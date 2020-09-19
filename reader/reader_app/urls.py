from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('annotate', views.annotate, name='annotate')
]
