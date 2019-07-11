from django.urls import path
from . import views

urlpatterns = [
    path('prototype/', views.prototype, name='prototype'),
    path('bars/', views.bars, name='bars'),
    path('', views.index, name='index')
]