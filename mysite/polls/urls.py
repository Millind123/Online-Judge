from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:number>/', views.problem_statement, name='problemStatement'),
]