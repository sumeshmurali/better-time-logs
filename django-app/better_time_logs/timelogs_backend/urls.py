from django.urls import path

from . import views

urlpatterns = [
    path('helloworld/', views.hello_world),
    path('categories/', views.categories),
    path('timelogs/', views.timelogs)
]
