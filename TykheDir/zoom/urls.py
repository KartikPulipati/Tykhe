from django.urls import path
from . import views

urlpatterns = [

    path('', views.listZoom, name='listZoom'),
    path('create/', views.createZoom, name="createZoom"),
    path('<int:zoom_pk>/delete', views.deleteZoom, name="deleteZoom"),

]