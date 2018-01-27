from django.urls import path
from CamposOcultos import views

urlpatterns = [
    path('', views.index, name='index'),
    path('controlador1/', views.controlador1, name='controller1'),
    path('controlador2/', views.controlador2, name='controller2'),
]
