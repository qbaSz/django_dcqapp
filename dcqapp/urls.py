from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:commit_id>', views.detail, name='detail'),
    path('<str:commit_id>/details', views.detail, name='detail')
]