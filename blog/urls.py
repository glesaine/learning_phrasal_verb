from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
    path('enter_verbs/', views.enter_verbs, name='enter_verbs'),
    path('ask_verbs/<int:number>/<str:meaning>/', views.ask_verbs, name='ask_verbs'),
    path('statistics/', views.statistics, name='statistics')
]
